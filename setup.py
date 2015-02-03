from setuptools import find_packages, setup

setup(name='broken-spec-test',
      version='1.0.0',
      packages=find_packages(),
      namespace_packages=['broken_spec', 'broken_spec.example'],
      zip_safe=True,
      install_requires=['Flask ==0.10.1'])
