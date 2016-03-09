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
    c_file = tempfile.mktemp(dir='/tmp/', prefix="c_file_", suffix=".c")

    with open(c_file, "wb") as f:
        f.write(c_str)

    if filename is None:
        filename = tempfile.mktemp(dir='/tmp/', prefix="compiled_")
    res = compile([c_file, "-o", filename])

    if res[1] != "":
        raise CompileError(res[1])

    with open(filename, "rb") as f:
        result = f.read()

    return result
