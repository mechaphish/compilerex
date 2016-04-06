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
    return res

def compile_from_string(c_str, filename=None):
    '''
    Compile a CGC binary from a C string.
    Removes output file and original C file after compilation.
    '''
    c_file = tempfile.mktemp(dir='/tmp/', prefix="c_file_", suffix=".c")

    with open(c_file, "wb") as f:
        f.write(c_str)

    outfile = filename
    if filename is None:
        outfile = tempfile.mktemp(dir='/tmp/', prefix="compiled_")
    res = compile([c_file, "-o", outfile])

    if res[1] != "":
        raise CompileError(res[1])

    with open(outfile, "rb") as f:
        result = f.read()


    os.remove(c_file)
    os.remove(outfile)

    return result
