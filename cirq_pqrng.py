###################################################################
# Program: cirq_pqrng.py
# Goal: This is a Psuedo Quantum Random Number Generator (PQRNG) 
#       based on LFSR+XOR algorithm. It builds a quantum circuit 
#       in Google CirQ that implements the PQRNG over n qbits.
#       The code acts both as a quantum circuit builder and as a
#       hybrid (classical+quantum) processing pipeline.
# Date: 29th of January 2026  
# Ver: 1.2
# Author: Marco Mattiucci
#
# Warning:
# It's strongly discouraged to install complex Python packages 
# like CirQ system-wide. Create an isolated environment:
# Create the directory:
# $ mkdir mycirq
# Create the virtual environment (venv):
# $ python3 -m venv .venv
# Activate the venv:
# $ source .venv/bin/activate
# Upgrade pip and install CirQ:
# $ pip install --upgrade pip
# $ pip install cirq
###################################################################



import cirq     # Import CirQ library (quantum emulator)


seed = [0,1,1,0,1,0,1,1]  # Set the seed of the sequence
rnd_bit_number = len(seed)  # Calculate the number of bits for the seed

while True:

    # Initialization of the quantum register (one quantum bit for each seed bit):
    qrnd = [cirq.LineQubit(i) for i in range(0,rnd_bit_number)]

    # Quantum circuit initialization:
    circuit = cirq.Circuit()    # Create an empty quantum circuit

    # BLOCK 1: ##################################################################
    # For each seed bit, set the corresponding quantum bit.
    # (NOT is the quantum NOT or X gate and I is the quantum identity gate)
    # Note that each quantum bit is set to |0> initially.
    i = 0
    for b in seed:
        if b == 1:
            circuit.append(cirq.X(qrnd[i])) # NOT for |1>
        else:
            circuit.append(cirq.I(qrnd[i])) # I for |0>
        i += 1
    
    # BLOCK 2: ##############################################################################
    # Build the Pseudo Quantum Random Number Generator (XOR)
    circuit.append(cirq.CNOT(qrnd[rnd_bit_number-2],qrnd[0]))   # XOR via CNOT quantum gate

    # BLOCK 3: ##############################################################################
    # Build the Pseudo Quantum Random Number Generator (LFSR)    
    for i in range(rnd_bit_number-1):
        circuit.append(cirq.SWAP(qrnd[i],qrnd[i+1]))    # Shift via SWAP quantum gates
    
    # MEASURE GATES: ########################################################################
    # Measurements (set the collapse of quantum bits to read their final values):
    for i in range(rnd_bit_number):
        circuit.append(cirq.measure(qrnd[i], key='q'+str(i)))

    # Show the constructed quantum circuit:
    print(circuit)

    # QUANTUM PROCESSING: ###################################################################
    # Execute the quantum processing simulation of the circuit:
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1)

    # Show results (measured values):
    print("Number of random bits:",rnd_bit_number)
    print("Seed:",seed,int("".join(map(str,seed)),2))

    # PYTHON CONTROLLER: ###################################################################
    # Set the new seed based on the calculated output value:
    seed = result.data.iloc[0].tolist()     
    print("Output value:",seed,int("".join(map(str,seed)),2))

    # Continue or not the sequence using the new seed:
    a = input("Continue sequence? [n to stop]")
    if a == 'n': quit()

