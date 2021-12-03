# Quantum Computer Simulator(QCS)
## Introduction
The Quantum computing simulator is a python package that simulates qubits and their various operations. This package support pre-defined gates like X, H, CX, and a general u3 and controlled u3 gate, with the additional support of parametric gates and global parameters which allows this to simulate variation quantum algorithms.

## Features

- Simulates N number of qubits (Performance Depends on the Local hardware)
- Supports regularly used gates i.e X, H,CX, and general gates u3 and controller u3
- Supports parametric gates and global parameters.
- Visualisation of the measurements

## Dependencies

QCS uses a couple of open source projects to work properly:

- [Numpy](https://numpy.org/) - Matrix calculations and built-in hardware acceleration.
- [Matplotlib](https://matplotlib.org/) - Histograms of the measurement counts.

## Importing the package

Download the [qsim.py](https://github.com/akshaykale17/quantum_computer_simulator/blob/main/qsim.py) file and import it as shown in the [q_sim.ipynb](https://github.com/akshaykale17/quantum_computer_simulator/blob/main/q_sim.ipynb) or [q_sim.pdf](https://github.com/akshaykale17/quantum_computer_simulator/blob/main/q_sim.pdf).

```python
import qsim
```

## How-to-use 

### Input Format 

The package requires 2 inputs.

- total_qubits - total number of qubits for the operation.
- circuit - A JSON that has qubit operations ***in order***, with gate, target qubits, and parameters.

Circuit Example -

```
[ { "gate": "h", "target": [0] ,"params":0}, 
{ "gate": "cx", "target": [0,2] ,"params":0} ]
```

### Qubit Operations i.e Running the Circuit

We use 2 functions from the package to initialize and run the circuit.

Steps are
- initialize the circuit 
- Run all qubit operations on the Initialised circuit.

Example -

```python
my_qpu = qsim.get_ground_state(total_qubits)   #1st Step
final_state = qsim.run_program(total_qubits,my_qpu, my_circuit) #2nd Step
```
### Measurement and Visualisation

Requires the number of shots

```python
counts = qsim.get_counts(total_qubits,final_state, 1000)  #1000 number of shots
```

And display the histogram using plot_readings function as shown below

```python
qsim.plot_readings(counts)
```
***For more examples please visit [q_sim.ipynb](https://github.com/akshaykale17/quantum_computer_simulator/blob/main/q_sim.ipynb) or [q_sim.pdf](https://github.com/akshaykale17/quantum_computer_simulator/blob/main/q_sim.pdf)***


## Additional feature in works
- Complete Circuit Visualisation
- Support for Open Quantum Assembly Language OpenQASM
