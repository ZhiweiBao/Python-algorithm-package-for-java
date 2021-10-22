import os
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize


# extensions = [Extension("detect_calculated", ["detect_calculated.py"],
#                         include_dirs=["/home/bao/WorkSpace/Python3/hello"],
#                         libraries=["/home/bao/anaconda3/lib/python3.8/site-packages/scipy/stats/_stats.cpython-38-x86_64-linux-gnu.so", 
#                                    ""],
#                         library_dirs=["/home/bao/anaconda3/lib/python3.8/site-packages/scipy/stats",
#                                       ""]
#                         )]


path = os.path.abspath(os.path.dirname(__file__))
setup(
    name='Add Lib',
    ext_modules=cythonize(path+"/test_add.py"),
)