import subprocess
def compile(args):
    p = subprocess.popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = p.communicate()
    return res
