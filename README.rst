========
pypeline
========

A functional tool for managing pipelines of methods with error handling. 

The library provides a decorator for converting Python methods into **Either** objects. Either objetcs can be
composed to form pipelines of methods in order to *transform* data. 

Either objects can be of type **Success** or **Failure**.
If the input type is Success then the method will be applied, otherwise the method is bypassed to return the same Failure 
object. 

This tool provides an approach for pipelines of operations on data that handle exceptions without breaking the pipeline, in 
a functional style.

License
-------

* Free software: MIT license

Features
--------

Description
-----------

This library is based in railway-oriented programming from Haskell, specially in 
`Either <https://hackage.haskell.org/package/base-4.12.0.0/docs/Data-Either.html>`_ monad. 

A good tutorial on railway-oriented programming can be found at 
`F# for fun and profit <https://fsharpforfunandprofit.com/rop/>`_.

It is also inspired in the code developed by *jruiz* the master craftsman software and *shokunin* from Eastern Navarre. 

The purpose of this tool is merely didactic, although it is completely usable.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage