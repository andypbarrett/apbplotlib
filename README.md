# apbplotlib
A collection of plotting routines

## Description
There are three modules
* `myplot`, which contains plotting routines
* `utilities` containing helper functions
* `maps` containing CRS definitions of EASE Grid projections
* `colors` containing a color table for plotting reanalysis data

## Install
Currently, the package is only on github.  Installing the package so that it can be used
in an environment can be done by cloning the repo and then using `setuptools` to install.

Clone or download repository
```
$ git clone git@github.com:andypbarrett/apbplotlib.git
```
Change directory to `apbplotlib`
```
$ cd apbplotlib
```
Use `setup.py` to install package
```
$ python setup.py install
```

If changes have been made to the github repo, or if you have made changes to your local
repo.  The package installation can be "updated" by doing the following:
```
$ python setup.py install --force
```
This will force installed files to be overwritten

Andy P. Barrett  
<apbarret@nsidc.org>  
https://github.com/andypbarrett  




