# pqrng
Psuedo Quantum Random Number Generator (PQRNG) built by python and Google CirQ.

https://marcomattiucci.it/informatica_quantum_computing_pqrng.php

This is a Psuedo Quantum Random Number Generator (PQRNG) based on LFSR+XOR algorithm. It builds a quantum circuit in Google CirQ that implements the PQRNG over n qbits.
The code acts both as a quantum circuit builder and as a hybrid (classical+quantum) processing pipeline.

Warning: It's strongly discouraged to install complex Python packages like CirQ system-wide. 
Create an isolated environment:

Create the directory:

$ mkdir mycirq

Create the virtual environment (venv):

$ python3 -m venv .venv

Activate the venv:
$ source .venv/bin/activate

Upgrade pip and install CirQ:

$ pip install --upgrade pip

$ pip install cirq
