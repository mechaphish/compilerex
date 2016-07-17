from distutils.core import setup
from distutils.command.build import build as _build
import os

BIN_PATH = "bin"


class build(_build):
    def run(self):
        for f in os.listdir(BIN_PATH):
            os.chmod(os.path.join("bin", f), 0777)


setup(
    name='compilerex',
    version='0.1',
    packages=['compilerex'],
    install_requires=[
    ],
    cmdclass={'build': build}
)
