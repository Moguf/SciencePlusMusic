SciencePlusMusic
================

We can understand amazing sciences results through music. SciencePlusMusic helps you to understand Science.


Requirements
------------

* mpg123  > 1.23.6 ::

    Mpg123 witch can convet .mp3 file to .wav file is an open source program. You can get that through your browser.
  
* Python  >  3.5.1
* Scipy   >  0.18.0
* Numpy   >  1.11.1

Set Up
------

Install virtualenv. (for protecting your Home environment.)

.. code-block:: bash
   
   python3 -m pip install -U pip setuptools
   python3 -m pip install virtualenv
   # or
   pip3 install virtualenv

activate virtualenv

.. code-block:: bash
   
   virtualenv -p python3 venv
   source venv/bin/activate
   # Removing virtual environment
   # (venv) deactivate
   
build & install
---------------

.. code-block:: bash
   
   pip install git+https://github.com/Moguf/SciencePlusMusic.git
   # or 
   git clone https://github.com/Moguf/SciencePlusMusic.git
   cd enet_network
   python setup.py build
   python setup.py install



Sound Source
============

`DOVA-SYNDROME`_

.. _DOVA-SYNDROME: http://dova-s.jp

