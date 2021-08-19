# required Imports
import math
import cmath
import numpy as np
from numpy.random import choice
import matplotlib.pyplot as plt

##all functions
def get_ground_state(num_qubits):
    # return vector of size 2**num_qubits with all zeroes except first element which is 1
    # validating Inputs by user
    assert type(num_qubits) == int , 'Input Must be a integer'
    assert num_qubits > 0 , 'Input must be greater than 0'

    q1 = np.zeros((2**num_qubits))
    q1[0]=1
    return q1

def get_operator(total_qubits, gate_unitary, target_qubits,params):
    # return unitary operator of size 2**n x 2**n for given gate and target qubits
    # validating Inputs by user
    assert gate_unitary=='u3'or gate_unitary=='x'or gate_unitary=='h'or gate_unitary=='cx', 'Input Gate Undefiend'
    if gate_unitary=='cx':
        assert len(target_qubits)==2,'2 Target Qubits required'
    else:
        assert len(target_qubits)==1,'1 Target Qubits required'
    if gate_unitary=='u3':
        assert len(params)==3,'3 parameters required'
    for i in range(len(target_qubits)):
        assert target_qubits[i]>=0 and target_qubits[i]<total_qubits , 'Target Qubits Out of Bound'

    #Cached Reqularly used gates
    cached_gates = {
        'h': np.array([
        [1/np.sqrt(2), 1/np.sqrt(2)],
        [1/np.sqrt(2), -1/np.sqrt(2)]
        ]),
        'x': np.array([
        [0, 1],
        [1, 0]
        ])
        }
    if(gate_unitary=='u3'):
        theta = params['theta']
        phi = params['phi']
        lamb = params['lamb']
        i = complex(0+1j)
        a1 = math.cos(theta/2)
        a2 = -1*cmath.exp(i*lamb)*math.sin(theta/2)
        a3 = cmath.exp(i*phi)*math.sin(theta/2)
        a4 = cmath.exp(i*lamb+i*phi)*math.sin(theta/2)

        cached_gates['u3'] = np.array([
        [a1, a2],
        [a3, a4]
        ])

    I = np.identity(2)

    #calcualte the operator
    if(len(target_qubits)==1):
        gate = cached_gates[gate_unitary]
        if(total_qubits==1):
            return gate


        if(target_qubits[0]==0):
            O = np.kron(gate,I)
        elif(target_qubits[0]==1):
            O = np.kron(I,gate)
        else:
            O = np.kron(I,I)
        for i in range(2,total_qubits):
            if(i==target_qubits[0]):
                O = np.kron(O,gate)
            else:
                O = np.kron(O,I)

        return O
    else:
        P0x0 = np.array([
        [1, 0],
        [0, 0]
        ])
        P1x1 = np.array([
        [0, 0],
        [0, 1]
        ])
        X = cached_gates['x']
        if(target_qubits[0]==0):
            O = np.kron(P0x0,I)
        elif(target_qubits[0]==1):
            O = np.kron(I,P0x0)
        else:
            O = np.kron(I,I)
        for i in range(2,total_qubits):
            if(i==target_qubits[0]):
                O = np.kron(O,P0x0)
            else:
                O = np.kron(O,I)

        o_control = O
        if(target_qubits[0]==0):
            O = P1x1
        elif(target_qubits[1]==0):
            O = X
        else:
            O = I
        for i in range(1,total_qubits):
            if(target_qubits[0]==i):
                O = np.kron(O,P1x1)
            elif(target_qubits[1]==i):
                O = np.kron(O,X)
            else:
                O = np.kron(O,I)
        o_target = O
        O = o_control + o_target

        return O

def run_program(total_qubits,initial_state, program):

    for i in range(len(program)):
        initial_state = np.dot(initial_state,get_operator(total_qubits,program[i]['gate'],program[i]['target'],program[i]['params']))

    return initial_state

def get_counts(total_qubit,state_vector, num_shots):

    state = np.abs(state_vector)**2
    sample_List = []
    for i in range(len(state_vector)):
        sample_List.append(bin(i)[2:].zfill(total_qubit))

    randomNumberList = choice(
      sample_List, num_shots, p=state)

    unique, counts = np.unique(randomNumberList, return_counts=True)
    count = dict(zip(unique, counts))
    return count

def plot_readings(counts):
    fig = plt.figure(figsize = (10, 5))
    plt.bar(counts.keys(), counts.values(),width = 0.4)
    plt.xlabel("Qubits")
    plt.ylabel("Counts")
    plt.title("Circuit Measurement")
    plt.show()
