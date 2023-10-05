# Periodic time calculation:
To calculate the periodic time, this formula will be used

$$
T=2*\pi * \sqrt(l/g)
$$

where l is the length of the string in meters, g is the acceleration due to gravity in $m/s^2$
## The Algorithm:
1- start with defining a function to calculate the periodic time ``` calculate_periodic_timr(l) ```  with agrument l and g where g is constant of 9.81 m/s^2.
2- use lambda function to calculate the periodic time ``` lambda l: 2* math.pi/ math.sqrt(g / l) ```. 
3- Ask the user to enter the list of lengths separated by comma and use map function to calculate the periodic time for each value in the list

```
lengths_list = input("Enter a list of length, separated by commas: ")

lengths_list = lengths_list.split(",")

integer_list = []
for element in lengths_list:
  integer_list.append(int(element))

print("your list of lengths is: ", "\n", integer_list)
```

and use map function to allow calculation of time using each element of the list ```  periodic_times = map(calculate_periodic_time(integer_list), integer_list) ```.

4- create a list of periodic times using the periodic_times map elements ```  T=[periodic_time for periodic_time in periodic_times] ```

5- round the elements of the times list to 2 sig figs ``` round_time=[round(element,2) for element in T]``` 
6- print results ``` print("periodic times corresporing to the lengths are ", round_time)```
7- make the .py file callable module  ``` __all__=["calculate_periodic_time"] ```



## python code:

# This is Python code


```

#algorithm.py
import math

def calculate_periodic_time(l):
  """Calculates the periodic time of a simple pendulum.

  Args:
    l: The length of the pendulum in meters.

  Returns:
    The periodic time of the pendulum in seconds.
  """
# Acceleration due to gravity in meters per second squared.
  g = 9.81
# use lambda function calculate the periodic time where l is the length of the string and return the value calculated
  calculate_periodic_time= (lambda l: 2* math.pi/ math.sqrt(g / l))
  return calculate_periodic_time
  #-----------------------------------------------------------#
# Prompt the user for a list input.

lengths_list = input("Enter a list of length, separated by commas: ")

# Split the user input string into a list.
lengths_list = lengths_list.split(",")

# Convert the elements of the list to integers.
integer_list = []
for element in lengths_list:
  integer_list.append(int(element))

# Print the integer list.
print("your list of lengths is: ", "\n", integer_list)

#--------------------------------------------------------------#

# Use map to apply the lambda function to each length in the list
periodic_times = map(calculate_periodic_time(integer_list), integer_list)

# Print the periodic times and round them to 2 sig digits
T=[periodic_time for periodic_time in periodic_times]
round_time=[round(element,2) for element in T]
print("periodic times corresporing t0 the lengths are ", round_time)


__all__=["calculate_periodic_time"]

```

#USE The Algorithm.py file as a module. 

** import algorithm **

then the code will ask for the input and run automatically untill it prints the results.
