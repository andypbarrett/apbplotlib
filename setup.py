from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='apbplotlib',
    url='',
    author='Andy Barrett',
    author_email='andypbarrett@gmail.com',
    # Needed to actually package something
    packages=['apbplotlib'],
    # Needed for dependencies
    install_requires=['numpy','matplotlib','pandas'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='A set of plotting tools',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
