"""zad 1"""

import sys
import numpy as np


def read_data(filename):

    with open(filename, 'r') as file:
        data = file.read().split()
    return list(map(float, data))


def calculate_statistic(data, function_number):

    if function_number == 1:
        return sum(data)
    elif function_number == 2:
        return max(data)
    elif function_number == 3:
        return min(data)
    elif function_number == 4:
        return np.mean(data)
    elif function_number == 5:
        return np.median(data)
    elif function_number == 6:
        return np.std(data, ddof=0)
    elif function_number == 7:
        return np.std(data, ddof=1)
    elif function_number == 8:
        return np.var(data, ddof=0)
    elif function_number == 9:
        return np.var(data, ddof=1)
    else:
        return "Invalid function number."


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py filename function_number")
        sys.exit(1)

    filename = sys.argv[1]
    function_number = int(sys.argv[2])

    data = read_data(filename)
    result = calculate_statistic(data, function_number)
    print(result)

"""zad 2"""
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-10, 10, 400)
y = 2 * np.sin(3 * x) + 3 * np.cos(2 * x)


plt.figure(figsize=(10, 6))
plt.plot(x, y, label='2*sin(3*x) + 3*cos(2*x)')
plt.title('Wykres funkcji 2*sin(3*x) + 3*cos(2*x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

