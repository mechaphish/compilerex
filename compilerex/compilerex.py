import subprocess
import os


def compile(args):
    if not isinstance(args, list):
        args = [args]
    path = os.path.join(os.path.dirname(__file__), "..", "compile.sh")
    p = subprocess.Popen(["bash", path] + args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = p.communicate()
    return res
