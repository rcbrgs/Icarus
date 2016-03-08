Development
-----------

Instructions on how to recreate the dev environment, to fallback onto in case installation instructions have a problem:

$ virtualenv --python=$(which python3) vIcarus

$ cd vIcarus

$ source bin/activate

$ git clone git@github.com:rcbrgs/Icarus.git

$ ln -s ~/vIcarus/Icarus bin/python3.4/site-packages/Icarus

I'm sure there is a more pythonic way of doing the last step above, but after numerous hours spent struggling with setuptools, distutils, setup.py, esky, and trying to copy "best practices" solutions, I find the above hack simple, clear and reliable.

I _highly_ recommend installing ipython, since it barfs errors with colors and tracebacks automatically, autocompletes on the interpreter and other niceties, specially useful when bug hunting. Remember to do so inside your virtualenv.

$ pip install ipython

Now install required packages for the project:

$ pip install -r Icarus/pip_requirements.txt

Coding style
------------

Snake case throughout, except on class names, and since file names should track closely class names, file names should also have first letter uppercase. Example:

$ head Log.py

# -*- coding: utf-8 -*-

class Log ( object ):
  def look_what_a_cool_and_descriptive_function_name ( wow_you_type_really_long_parameter_names ):
    you_are_insane_to_use_long_descriptive_variable_names_on_local_scope = "ALL names should be humanly readable, no exceptions."
