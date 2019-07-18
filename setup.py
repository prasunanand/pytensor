from distutils.core import setup, Extension

module1 = Extension('ctensor',
					define_macros = [('MAJOR_VERSION', '1'),
                                     ('MINOR_VERSION', '0')],
                    include_dirs = ['/usr/local/include'],
                    sources = ['tensor/csrc/tensormodule.c'])

setup (name = 'PyTensor',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])
