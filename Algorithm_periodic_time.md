# Periodic time calculation:
To calculate the periodic time, this formula will be used

$$
T=2*\pi * \sqrt(l/g)
$$

where l is the length of the string in meters, g is the acceleration due to gravity in $$ m/s^2 $$
## The Algorithm:
1- start with defining a function to calculate the periodic time ```python calculate_periodic_timr(l) ```python  with agrument l and g where g is constant of 9.81 m/s^2.
2- use lambda function to calculate the periodic time ```python lambda l: 2* math.pi/ math.sqrt(g / l) ```python. 
3- use a list of length values ```python x = [0.5, 1, 1.5, 2, 2.5] ```python  and use map function to allow calculation of time using each element of the list ```python  periodic_times = map(calculate_periodic_time(l), x) ```python

4- create a list of periodic times using the periodic_times map elements ```python  T=[periodic_time for periodic_time in periodic_times] 

5- print results as to print the periodic time of the element of index 0 in the list of length and its corresponding value in the time list and repeat the same for each index in the list. 
**for example:** the periodic time for the element of index zero in x is the element of index zero in T in "seconds" ```python  print("periodic time for l= ", x[0] , "m is ", T[0],"seconds") ```python

```python 

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

# create a list of periodic times using the map values:
T=[periodic_time for periodic_time in periodic_times]

# Print the periodic times
print("periodic time for l= ", x[0] , "m is ", T[0],"seconds", "\n", "periodic time for l= ", x[1] , "m is ", T[1],"seconds","\n", "periodic time for l= ", x[2] , "m is ", T[2], "seconds", "\n", "periodic time for l= ", x[3] , "m is ", T[3],"seconds","\n", "periodic time for l= ", x[4] , "m is ", T[4],"seconds",)
