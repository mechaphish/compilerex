from distutils.core import setup
from distutils.command.build import build as _build
import os




class build(_build):
    def run(self):
        for f in os.listdir("compilerex/bin/"):
            os.chmod(os.path.join("compilerex/bin/", f), 0o777)
        for f in os.listdir("compilerex/scripts/"):
            os.chmod(os.path.join("compilerex/scripts/", f), 0o777)


setup(
    name='compilerex',
    version='0.1',
    packages=['compilerex'],
    install_requires=[
        'python-magic'
    ],
    package_data={'compilerex': ['scripts/*', 'bin/*', 'lib/*']},
    cmdclass={'build': build}
)
