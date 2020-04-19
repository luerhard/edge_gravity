from distutils.core import Extension, setup
from Cython.Build import cythonize

# define an extension that will be cythonized and compiled
ext = Extension(name="edge_gravity", sources=["edge_gravity/edge_gravity.pyx"])
setup(ext_modules=cythonize(ext))