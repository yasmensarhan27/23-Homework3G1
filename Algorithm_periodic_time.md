# Periodic time calculation:
To calculate the periodic time, this formula will be used

$$
T=2*\pi * \sqrt(l/g)
$$

## python code:

# This is Python code
```python
{python}
import math
def calculate_periodic_time(l):
  """Calculates the angular frequency of a simple pendulum.

  Args:
    l: The length of the pendulum in meters.

  Returns:
    The angular frequency of the pendulum in radians per second.
  """

  g = 9.81  # Acceleration due to gravity in meters per second squared.

  #use lambda function to calculate the periodic time of the simple pendulum where l is the length of the string.
  calculate_periodic_time=(lambda l: 2* math.pi/ math.sqrt(g / l))
  return calculate_periodic_time

# Define a list of lengths of pendulums
x = [0.5, 1, 1.5, 2, 2.5]

# Use map to apply the lambda function to each length in the list
periodic_times = map(calculate_periodic_time(l), x)

# Print the periodic times

T=[periodic_time for periodic_time in periodic_times]
print("periodic time for l= ", x[0] , "m is ", T[0],"seconds", "\n", "periodic time for l= ", x[1] , "m is ", T[1],"seconds","\n", "periodic time for l= ", x[2] , "m is ", T[2], "seconds", "\n", "periodic time for l= ", x[3] , "m is ", T[3],"seconds","\n", "periodic time for l= ", x[4] , "m is ", T[4],"seconds",)
