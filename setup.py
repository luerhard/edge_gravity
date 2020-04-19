from distutils.core import Extension, setup
from Cython.Build import cythonize


USE_CYTHON = True

ext = '.pyx' if USE_CYTHON else '.c'

# define an extension that will be cythonized and compiled
extensions = Extension(name="edge_gravity.edge_gravity",
                       sources=["edge_gravity/edge_gravity" + ext])

setup(
    name="edge_gravity",
    version="0.0.1",
    author="Lukas Erhard",
    author_email="luerhard@googlemail.com",
    include_package_data=True,
    description="Calculates Edge Gravity for a given networkx DiGraph",
    packages=["edge_gravity"],
    ext_modules=cythonize(extensions)
)
