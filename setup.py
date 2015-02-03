from setuptools import setup

setup(name='broken-spec-test',
      version='1.0.0',
      packages=['broken_spec', 'broken_spec.example'],
      namespace_packages=['broken_spec'],
      install_requires=['Flask ==0.10.1'])
