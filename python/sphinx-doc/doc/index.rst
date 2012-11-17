.. Awesome  documentation master file, created by
   sphinx-quickstart on Fri Nov 16 13:32:53 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Awesome 's documentation!
====================================

This is the most awesome project awesome. It containts cool and ultracool code. 

.. toctree::
	:maxdepth: 2

	code

Additional Documentation
========================
There is so much goodness coming up such as in `Tables n'at`_.


General paragraph text
----------------------
This text is going to be *italized*. This is going to be **bold**. 
I feel like defining a lambda function that does not take an argument. I can do this like ``lambda : 1``. 
I even feel like referencing Para2_ cuz I can. I think I will get tired of singing praises of Python_. So I am going to define a shortcut link for it.

.. _Para2:

Welcome to para2. I have so much to say here. I am going to import an image here. I am *soooo* happy |happy|. 
I think this happiness [1]_ can be often be attributed to coding. Let me cite another happiness [HAP2012]_  and let me do it once again [HAP2012]_. 

.. comments .. |happy| image:: happy.gif

A List of things I like : 

* Food
* Running - Such as in running_
	(1) 5K
	(2) Marathon
* Climbing
* Wine

But, how can I be clear, without defining some important stuff:

running
	The act of spontaneous craziness, where your two feet take you far far away 

climbing
	The act of equal madness, where you don't know how to get down after climbing up
	
Code Blocks
-----------
I think might be a code block ::

	I can do whatever I want here

And here I can put in some python code ::

	>>> def f() : 
	... 	return 1
	...
	>>> f()
	1 

How about this doctest block ::

	>>> print("This is so cool")
	This is so cool

Wonder if I can put in c++ code. This is possible using ``.. code-block:: cpp`` 

.. code-block:: cpp
	
	#include<iostream>
	using namespace std;
	
	int main() {
		cout<<"Hello World"<<endl;
		return 0;
	}

And just a plain code section ::
	
	#include<iostream>
	using namespace std;
	
	int main() {
		cout<<"Hello World"<<endl;
		return 0;
	}


Tables n'at
***********

A simple table. Not sure how these things work. 

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

.. 
	This comment is going to be lost

..	This comment will not be shown but may appear in HTML comments

Figures
+++++++
This is my figure sub-sub sectiokn

.. _running:
.. figure::	images/running.jpg
	:align:	center
	:width:	300
	:height: 200

	The freedom of running

You can even download this image like :download:`Running image<images/running.jpg>`

Text Related
------------

A module is defined as :mod:`awesome` and a class is defined as :class:`awesome.Cool`. I did this by ``:class:`awesome.Cool```.
. Sometimes writing this out again and again can get boring, so you use the ``::replace`` method, to get the |awesome| module. 

.. |awesome| replace:: :mod:`awesome`

Functions and Classes 
*********************

.. function:: Lasso(X, Y, lambda[, nCV=1])
	
	Solve the Lasso regression problem
	
	:param X: The regressors
	:param Y: The predicted value
	:param lambda: The regularization term
	:param nCV: The number of cross validation runs
	:type nCV: integer
	:type lambda: float > 0 
	:rtype: SolutionObject or None


.. include:: blasec.rst

Math
----

Now for some math. I think I like :math:`\alpha * \beta` . How about I write down some DEE conditions : 

.. math::
	
	E(r) = \sum_{i=1}^{N}E_i(r_i) + \sum_{i<j}E_{ij}(r_i,r_j)

Some definitions
----------------

:Authors: Subhodeep Moitra1
:Email: smoitra@cs.cmu.edu
:Version: 0.0.0.0
:Webpage: `Subhodeep Moitra <http://www.cs.cmu.edu/~subhodee>`_

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _Python: http://python.org

Draw a horizontal lines for the references

-------------------------------

.. [1] Comes from python http://python.org
.. [HAP2012] A deep sense of happiness http://readthedocs.org
