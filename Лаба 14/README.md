Лабораторна робота №14: Boolean Expressions and Conditional
Statements
___
Мета роботи:
In this lab, you will write a script to analyze Boolean expressions and use
conditional statements to solve various problems. Each task will require you to
manipulate and evaluate Boolean conditions in different contexts.
___
Опис завдання:
```Python
Task 1: Basic Boolean Operations
Write a function check_truth that takes three boolean parameters ( a , b , c )
and returns the result of the expression (a and b) or c .
Example of function usage:
Task 2: Logical Equivalence
Write a function logical_equivalence that takes two boolean parameters and
returns True if they are logically equivalent, otherwise False .
Example of function usage:
Task 3: Exclusive Or (XOR)
Write a function xor that takes two boolean arguments and returns True if
exactly one of the arguments is True .
Example of function usage:
print(check_truth(True, False, True)) # True
print(logical_equivalence(True, True)) # True
print(logical_equivalence(True, False)) # False
Task 4: Conditional Greeting
Write a function greet that takes a boolean value. If True , the function should
return "Hello, World!", otherwise it should return "Goodbye, World!".
Example of function usage:
Task 5: Nested Conditions
Write a function nested_condition that takes three integers ( x , y , z ). The
function should return "All same" if all three are equal, "All different" if they are all
different, and "Neither" otherwise.
Example of function usage:
Task 6: Conditional Counting
Write a function count_true that accepts a list of boolean values and returns the
count of how many are True .
Example of function usage:
print(xor(True, False)) # True
print(xor(True, True)) # False
print(greet(True)) # Hello, World!
print(greet(False)) # Goodbye, World!
print(nested_condition(3, 3, 3)) # All same
print(nested_condition(3, 4, 5)) # All different
Task 7: Boolean Parity
Write a function parity that accepts an integer and returns True if the number
of 1 s in the binary representation of the number is even, otherwise False .
Example of function usage:
Task 8: Majority Vote
Write a function majority_vote that takes three boolean inputs and returns
True if more than half of them are True , otherwise False .
Example of function usage:
Task 9: Boolean Switch
Write a function switch that takes a boolean value and returns its opposite.
Example of function usage:
Task 10: Ternary Operator Simulation
Write a function ternary_check that simulates a ternary operator. It takes three
parameters: a boolean condition, a result if true, and a result if false. It returns the
print(count_true([True, False, True, False, True])) # 3
print(parity(3)) # False (binary 11)
print(majority_vote(True, True, False)) # True
print(switch(True)) # False
corresponding result based on the condition.
Example of function usage:
Task 11: Validate Combination
Write a function validate that takes three booleans ( x , y , z ) and returns
True if x is True or both y and z are True , otherwise False .
Example of function usage:
Task 12: Condition Chain
Write a function chain_check that evaluates a sequence of conditions. It takes
three integers and returns "Increasing" if they are in strictly increasing order,
"Decreasing" if in strictly decreasing order, or "Neither" otherwise.
Example of function usage:
Task 13: Boolean Filter
Write a function filter_true that takes a list of boolean values and returns a
new list containing only the True values.
Example of function usage:
print(ternary_check(True, "Yes", "No")) # Yes
print(validate(True, False, True)) # True
print(chain_check(1, 2, 3)) # Increasing
print(chain_check(3, 2, 1)) # Decreasing
Task 14: Conditional Multiplexer
Write a function multiplexer that takes four parameters: three boolean inputs
and one integer. If the first boolean is True , return double the integer. If the
second is True , return triple the integer. If the third is True , return the integer
minus five. If none are True , return the integer unchanged.
Example of function usage:
print
 
(filter_true([True, False, True, False])) # [True, True]
print(multiplexer(False, False, True, 10)) # 5
```
___
Виконання роботи:
```Python
def check_truth(a, b, c):
    return (a and b) or c

def logical_equivalence(a, b):
    return a == b

def xor(a, b):
    return (a and not b) or (not a and b)

def greet(is_hello):
    if is_hello:
        return "Hello, World!"
    else:
        return "Goodbye, World!"

def nested_condition(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y and y != z and x != z:
        return "All different"
    else:
        return "Neither"

def count_true(bool_list):
    count = 0
    for item in bool_list:
        if item:
            count += 1
    return count


def parity(number):
    binary_representation = bin(number)[2:]
    count_ones = binary_representation.count('1')

    return count_ones % 2 == 0

def majority_vote(a, b, c):
    count_true = sum([a, b, c])
    return count_true > 1

def switch(boolean_value):
    return not boolean_value

def ternary_check(condition, result_true, result_false):
    return result_true if condition else result_false

def validate(x, y, z):
    return x or (y and z)

def chain_check(a, b, c):
    if a < b < c:
        return "Increasing"
    elif a > b > c:
        return "Decreasing"
    else:
        return "Neither"

def filter_true(bool_list):
    return [value for value in bool_list if value]

def multiplexer(bool1, bool2, bool3, integer):
    if bool1:
        return integer * 2
    elif bool2:
        return integer * 3
    elif bool3:
        return integer - 5
    else:
        return integer

# Task 1: check_truth
print(check_truth(True, False, True))  # Output: True
print(check_truth(False, False, True))  # Output: True

# Task 2: logical_equivalence
print(logical_equivalence(True, True))  # Output: True
print(logical_equivalence(True, False))  # Output: False

# Task 3: xor
print(xor(True, False))  # Output: True
print(xor(True, True))  # Output: False

# Task 4: greet
print(greet(True))  # Output: Hello, World!
print(greet(False))  # Output: Goodbye, World!

# Task 5: nested_condition
print(nested_condition(1, 1, 1))  # Output: All same
print(nested_condition(1, 2, 3))  # Output: All different
print(nested_condition(1, 1, 2))  # Output: Neither

# Task 6: count_true
print(count_true([True, False, True]))  # Output: 2
print(count_true([False, False, False]))  # Output: 0

# Task 7: parity
print(parity(3))  # Output: False (binary 11 has two 1s)
print(parity(4))  # Output: True (binary 100 has one 1)

# Task 8: majority_vote
print(majority_vote(True, False, True))  # Output: True
print(majority_vote(False, False, True))  # Output: False

# Task 9: switch
print(switch(True))  # Output: False
print(switch(False))  # Output: True

# Task 10: ternary_check
print(ternary_check(True, "Yes", "No"))  # Output: Yes
print(ternary_check(False, "Yes", "No"))  # Output: No

# Task 11: validate
print(validate(True, False, False))  # Output: True
print(validate(False, True, False))  # Output: False

# Task 12: chain_check
print(chain_check(1, 2, 3))  # Output: Increasing
print(chain_check(3, 2, 1))  # Output: Decreasing
print(chain_check(1, 3, 2))  # Output: Neither

# Task 13: filter_true
print(filter_true([True, False, True, False]))  # Output: [True, True]
print(filter_true([False, False, False]))  # Output: []

# Task 14: multiplexer
print(multiplexer(True, False, False, 5))  # Output: 10
print(multiplexer(False, True, False, 5))  # Output: 15
print(multiplexer(False, False, True, 5))  # Output: 0
print(multiplexer(False, False, False, 5))  # Output: 5
```
___
Результати:
```Python
True
True
True
False
True
False
Hello, World!
Goodbye, World!
All same
All different
Neither
2
0
True
False
True
False
False
True
Yes
No
True
False
Increasing
Decreasing
Neither
[True, True]
[]
10
15
0
5
```
___
Висновки: Ці функції демонструють різні аспекти роботи з логічними виразами, умовами та маніпуляціями зі списками в Python. Вони є корисними прикладами для розуміння основних принципів програмування на Python, включаючи умовні оператори, цикли, операції з булевими значеннями та основи роботи з бінарними числами.
___