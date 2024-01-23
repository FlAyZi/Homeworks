'''Write a python function, which create a dictionary
for given number N, where keys are numbers from
1 to N, and values are cubs of that numbers'''


def new_dict(N):
    result = {}
    for i in range(1, N + 1):
        result[i] = i**3
    return result
