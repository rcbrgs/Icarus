Development
-----------

Instructions on how to recreate the dev environment, to fallback onto in case installation instructions have a problem:

$ virtualenv --python=$(which python3) vIcarus
$ cd vIcarus
$ source bin/activate
$ git clone git@github.com:rcbrgs/Icarus.git
$ ln -s ~/vIcarus/Icarus bin/python3.4/site-packages/Icarus

I'm sure there is a more pythonic way of doing the last step above, but after numerous hours spent struggling with setuptools, distutils, setup.py, esky, and trying to copy "best practices" solutions, I find the above hack simple, clear and reliable.
