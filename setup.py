# vim: set fileencoding=utf-8:
import sys
from setuptools import setup, Extension

def ext_modules(build=False):
  if build:
    sources = ['fontconfig.pyx']
  else:
    sources = ['fontconfig.c']
  ext = [Extension('fontconfig', sources, libraries=["fontconfig"])]
  return ext

args = dict(
  name='Python-fontconfig',
  version='0.6.0',
  author='Vayn a.k.a. VT',
  author_email='vayn@vayn.de',
  url='https://github.com/Vayn/python-fontconfig',
  license='LICENSE.txt',
  description='Python bindings for Fontconfig library',
  long_description=open('README.rst').read(),

  classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Intended Audience :: System Administrators',
      'License :: OSI Approved :: GNU General Public License (GPL)',
      'Operating System :: POSIX',
      'Operating System :: MacOS :: MacOS X',
      'Topic :: Text Processing :: Fonts',
      'Topic :: Utilities',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 2.7',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.2',
      'Programming Language :: Python :: 3.3',
      'Programming Language :: Cython',
  ]
)


if __name__ == '__main__':
  if sys.argv[1] == 'build_ext':
    from Cython.Distutils import build_ext

    args.update(cmdclass={'build_ext': build_ext})
    args.update(ext_modules=ext_modules(True))
    setup(**args)
  else:
    args.update(ext_modules=ext_modules())
    setup(**args)
