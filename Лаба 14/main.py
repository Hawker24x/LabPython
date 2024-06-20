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
