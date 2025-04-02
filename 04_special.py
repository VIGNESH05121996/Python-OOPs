
# lambda arguments: expression
add = lambda x, y: x + y  
print(add(3, 5))  # Output: 8

"""
above lambda expression is same as below
def add(x, y):
    return x + y
"""

#enumurate
testList = [1,2,3,4,5]
for index,value in enumerate(testList):
    if(value % 2 == 0):
        print(index)

#keywargs - keyword arguments - allows to pass a variable number of named arguments to a function.
def details(*args, **kwargs):  
    print("Args:", args) # * - means single input which added to tuple
    print("Kwargs:", kwargs) # ** - means dictionary

details(1, 2, 3, name="Alice", age=30) #dynamic arguments can be passed.

"""
import random

random module in python
    random.random()	Random float between 0 and 1
    random.uniform(a, b)	Random float between a and b
    random.randint(a, b)	Random integer between a and b
    random.randrange(start, stop, step)	Random integer in range
    random.choice(seq)	Pick one random item
    random.choices(seq, k=n)	Pick n items (with replacement)
    random.sample(seq, k=n)	Pick n items (without replacement)
    random.shuffle(seq)	Shuffle a list
    random.seed(n)	Set seed for reproducibility
"""
print(__name__)
