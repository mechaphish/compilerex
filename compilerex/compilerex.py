import subprocess
import tempfile
import os
import magic

class CompileError(Exception):
    pass

def compile(args):
    if not isinstance(args, list):
        args = [args]
    path = os.path.join(os.path.dirname(__file__), "..", "compile.sh")
    p = subprocess.Popen(["bash", path] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = p.communicate()
    returncode = p.wait()
    return returncode, res

def clang_assemble(args):
    if not isinstance(args, list):
        args = [args]
    path = os.path.join(os.path.dirname(__file__), "..", "assemble.sh")
    p = subprocess.Popen(["bash", path] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = p.communicate()
    returncode = p.wait()
    return returncode, res

def gcc_assemble(args):
    if not isinstance(args, list):
        args = [args]
    p = subprocess.Popen(["gcc"] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = p.communicate()
    returncode = p.wait()
    return returncode, res

#obsolete
def get_clang_args(filename):
    magic_string = magic.from_file(filename)
    with open(filename, "rb") as f:
        start_bytes = f.read(0x100)
    if magic_string.startswith("ELF"):
        if "x86-64" in magic_string:
            return ["-target", "x86", "-nostdlib", "-static", "-Wl,-m64"]
        elif "Intel 80386" in magic_string:
            return ["-nostdlib", "-static", "-Wl,-m32"]
    elif start_bytes.startswith("\x7fCGC"):
        return ["-nostdlib", "-static", "-Wl,-mcgc_i386"]
    raise Exception("Unsupported file type (magic: '%s')" % (magic_string))

def auto_assemble(input_filename, asm_filename, output_filename, extra_opts=None):
    extra_opts = [] if extra_opts is None else extra_opts
    magic_string = magic.from_file(input_filename)
    with open(input_filename, "rb") as f:
        start_bytes = f.read(0x100)
    if magic_string.startswith("ELF"):
        if "x86-64" in magic_string:
            return gcc_assemble(["-m64", asm_filename, "-o", output_filename] + extra_opts)
        elif "Intel 80386" in magic_string:
            return gcc_assemble(["-m32", asm_filename, "-o", output_filename] + extra_opts)
    elif start_bytes.startswith("\x7fCGC"):
        return clang_assemble(["-nostdlib", "-static", "-Wl,-mcgc_i386", asm_filename, "-o", output_filename]
                              + extra_opts)
    raise Exception("Unsupported file type (magic: '%s')" % (magic_string))

def get_preferred_syntax(filename):
    magic_string = magic.from_file(filename)
    with open(filename, "rb") as f:
        start_bytes = f.read(0x100)
    if start_bytes.startswith("\x7fCGC"):
        return "at&t"
    else:
        return "intel"

def compile_from_string(c_str, filename=None):
    '''
    Compile a CGC binary from a C string.
    Removes output file and original C file after compilation.

    :param str c_str:   The source code to compile
    :returns bytes:     The compiled binary
    '''
    c_file = tempfile.mktemp(dir='/tmp/', prefix="c_file_", suffix=".c")

    with open(c_file, "w") as f:
        f.write(c_str)

    outfile = filename
    if filename is None:
        outfile = tempfile.mktemp(dir='/tmp/', prefix="compiled_")
    retcode, res = compile([c_file, "-o", outfile])

    if retcode != 0:
        raise CompileError(res[1])

    with open(outfile, "rb") as f:
        result = f.read()


    os.remove(c_file)
    if filename is None:
        os.remove(outfile)

    return result
