#!/usr/bin/env python

import os
import sys
from distutils.core import setup

version_file = os.path.join('lib','__version__.py')
if 1 or not os.path.exists(version_file):
    major_version = 0
    minor_version = 4
    execfile(os.path.join('tools','get_revision.py'))
    __version__='%d.%d.%d'%(major_version,minor_version,revision_version)
    for l in ['lib','lib152']:
        f = open(os.path.join(l,'__version__.py'),'w')
        f.write('__version__ = "%s"\n'%(__version__))
        f.close()
execfile(version_file)


setup (name = "PyVTK",
       version = __version__,
       description = "PyVTK - tools for manipulating VTK files in Python",
       author = "Pearu Peterson",
       author_email = "pearu@cens.ioc.ee",
       license = "LGPL",
       long_description= """
       PyVTK provides tools for manipulating VTK (Visualization Toolkit)
       files in Python:

       VtkData - create VTK files from Python / read VTK files to Python.
       """,
       url = "http://cens.ioc.ee/projects/pyvtk/",
       packages = ['pyvtk'],
       package_dir = {'pyvtk':{'2':'lib','1':'lib152'}[sys.version[0]]}
       )

print "PyVTK Version",__version__
