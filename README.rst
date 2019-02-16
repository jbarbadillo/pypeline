========
pypeline
========

A functional tool for managing pipelines of methods with error handling. 

The library provides a decorator for converting Python methods into **Either** objects. Either objetcs can be
composed to form pipelines of methods in order to *transform* data. 

Either objects can be of type **Success** or **Failure**.
If the input type is Success then the method will be applied, otherwise the method is bypassed to return the same Failure 
object. 


* Free software: MIT license
* Documentation: https://pypeline.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage