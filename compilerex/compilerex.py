import subprocess
import tempfile
import os

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

def assemble(args):
    if not isinstance(args, list):
        args = [args]
    path = os.path.join(os.path.dirname(__file__), "..", "assemble.sh")
    p = subprocess.Popen(["bash", path] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = p.communicate()
    returncode = p.wait()
    return returncode, res

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
