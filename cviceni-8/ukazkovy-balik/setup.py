from setuptools import setup, find_packages

setup(name='mypythonpackage',
      version='0.0.1',
      description='Small lightweight personal library for Python.',
      author='Já Autor',
      author_email='',
      license='MIT',
      packages=find_packages(exclude="tests"),
      install_requires=['numpy']
      )

