Лабораторна робота №17: Generators and Data structures
___
Мета роботи:
Розробити різні генератори на Python для виконання завдань, таких як ітерація через списки, генерація чисел, обхід дерев та графів, робота зі словниками та файлами, ітерація через рядки та обчислення математичних послідовностей.
___
Опис завдання:
```Python
Task 1: Create a generator to iterate over a list of
numbers.
Create a generator function named number_generator that takes a list of
numbers and yields each number one by one.
Example of function usage:
Task 2: Develop a generator that yields even numbers
from a given range.
Create a generator function named even_number_generator that takes two
integers, start and end , and yields even numbers within that range.
Example of function usage:
Task 3: Implement a generator to yield odd numbers
within a specified range.
Create a generator function named odd_number_generator that takes two
integers, start and end , and yields odd numbers within that range.
Example of function usage:
gen = number_generator([1, 2, 3, 4, 5])
print(next(gen)) # 1
print(next(gen)) # 2
gen = even_number_generator(1, 10)
print(next(gen)) # 2
print(next(gen)) # 4
gen = odd_number_generator(1, 10)
print(next(gen)) # 1
print(next(gen)) # 3
Task 4: Write a generator that produces Fibonacci
numbers.
Create a generator function named fibonacci_generator that produces
Fibonacci numbers indefinitely.
Example of function usage:
Task 5: Create a generator that yields prime numbers
up to a given limit.
Create a generator function named prime_number_generator that takes an
integer limit and yields prime numbers up to that limit.
Example of function usage:
Task 6: Develop a generator to traverse a binary tree in
pre-order.
Create a generator function named pre_order_traversal that takes the root of
a binary tree and yields its nodes in pre-order.
Example of function usage:
gen = fibonacci_generator()
print(next(gen)) # 0
print(next(gen)) # 1
print(next(gen)) # 1
print(next(gen)) # 2
gen = prime_number_generator(10)
print(next(gen)) # 2
print(next(gen)) # 3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
gen = pre_order_traversal(root)
print(next(gen)) # 1
print(next(gen)) # 2
Task 7: Implement a generator for in-order traversal of
a binary tree.
Create a generator function named in_order_traversal that takes the root of a
binary tree and yields its nodes in in-order.
Example of function usage:
Task 8: Write a generator for post-order traversal of a
binary tree.
Create a generator function named post_order_traversal that takes the root of
a binary tree and yields its nodes in post-order.
Example of function usage:
Task 9: Create a generator to traverse a graph using
depth-first search (DFS).
Create a generator function named dfs_traversal that takes an adjacency list
representation of a graph and a starting node, and yields nodes in DFS order.
Example of function usage:
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
gen = in_order_traversal(root)
print(next(gen)) # 2
print(next(gen)) # 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
gen = post_order_traversal(root)
print(next(gen)) # 2
print(next(gen)) # 3
graph = {
 1: [2, 3],
 2: [4],
Task 10: Develop a generator for breadth-first search
(BFS) traversal of a graph.
Create a generator function named bfs_traversal that takes an adjacency list
representation of a graph and a starting node, and yields nodes in BFS order.
Example of function usage:
Task 11: Implement a generator that yields the keys of a
dictionary.
Create a generator function named dict_keys_generator that takes a dictionary
and yields its keys one by one.
Example of function usage:
Task 12: Write a generator that yields the values of a
dictionary.
 3: [5],
 4: [],
 5: []
}
gen = dfs_traversal(graph, 1)
print(next(gen)) # 1
print(next(gen)) # 2
graph = {
 1: [2, 3],
 2: [4],
 3: [5],
 4: [],
 5: []
}
gen = bfs_traversal(graph, 1)
print(next(gen)) # 1
print(next(gen)) # 2
gen = dict_keys_generator({'a': 1, 'b': 2, 'c': 3})
print(next(gen)) # 'a'
print(next(gen)) # 'b'
Create a generator function named dict_values_generator that takes a
dictionary and yields its values one by one.
Example of function usage:
Task 13: Create a generator to iterate over key-value
pairs of a dictionary.
Create a generator function named dict_items_generator that takes a
dictionary and yields its key-value pairs as tuples one by one.
Example of function usage:
Task 14: Develop a generator that yields lines from a
file one by one.
Create a generator function named file_lines_generator that takes a file path
and yields its lines one by one.
Example of function usage:
Task 15: Implement a generator to iterate over words in
a text file.
Create a generator function named file_words_generator that takes a file path
and yields its words one by one.
Example of function usage:
gen = dict_values_generator({'a': 1, 'b': 2, 'c': 3})
print(next(gen)) # 1
print(next(gen)) # 2
gen = dict_items_generator({'a': 1, 'b': 2, 'c': 3})
print(next(gen)) # ('a', 1)
print(next(gen)) # ('b', 2)
gen = file_lines_generator('example.txt')
print(next(gen)) # 'First line'
print(next(gen)) # 'Second line'
Task 16: Write a generator that yields characters from a
string one by one.
Create a generator function named string_chars_generator that takes a string
and yields its characters one by one.
Example of function usage:
Task 17: Create a generator to yield unique elements
from a list.
Create a generator function named unique_elements_generator that takes a list
and yields its unique elements one by one.
Example of function usage:
Task 18: Develop a generator that yields elements of a
list in reverse order.
Create a generator function named reverse_list_generator that takes a list
and yields its elements in reverse order.
Example of function usage:
gen = file_words_generator('example.txt')
print(next(gen)) # 'First'
print(next(gen)) # 'line'
gen = string_chars_generator('Hello')
print(next(gen)) # 'H'
print(next(gen)) # 'e'
gen = unique_elements_generator([1, 2, 2, 3, 3, 3])
print(next(gen)) # 1
print(next(gen)) # 2
gen = reverse_list_generator([1, 2, 3, 4, 5])
print(next(gen)) # 5
print(next(gen)) # 4
Task 19: Implement a generator to yield the Cartesian
product of two lists.
Create a generator function named cartesian_product_generator that takes
two lists and yields the Cartesian product of the two lists as tuples.
Example of function usage:
Task 20: Write a generator that yields permutations of a
list.
Create a generator function named permutations_generator that takes a list
and yields all possible permutations of the list.
Example of function usage:
Task 21: Create a generator to yield combinations of a
list of elements.
Create a generator function named combinations_generator that takes a list of
elements and yields all possible combinations of the elements.
Example of function usage:
Task 22: Develop a generator to iterate over a list of
tuples.
gen = cartesian_product_generator([1, 2], ['a', 'b'])
print(next(gen)) # (1, 'a')
print(next(gen)) # (1, 'b')
gen = permutations_generator([1, 2, 3])
print(next(gen)) # (1, 2, 3)
print(next(gen)) # (1, 3, 2)
gen = combinations_generator([1, 2, 3])
print(next(gen)) # (1,)
print(next(gen)) # (2,)
Create a generator function named tuple_list_generator that takes a list of
tuples and yields each tuple one by one.
Example of function usage:
Task 23: Implement a generator that yields elements
from multiple lists in parallel.
Create a generator function named parallel_lists_generator that takes
multiple lists and yields elements from each list in parallel.
Example of function usage:
Task 24: Write a generator that yields elements from a
nested list (flattening the list).
Create a generator function named flatten_list_generator that takes a
nested list and yields each element in a flat sequence.
Example of function usage:
Task 25: Create a generator to yield elements from a
nested dictionary.
Create a generator function named nested_dict_generator that takes a nested
dictionary and yields its elements.
Example of function usage:
gen = tuple_list_generator([(1, 2), (3, 4), (5, 6)])
print(next(gen)) # (1, 2)
print(next(gen)) # (3, 4)
gen = parallel_lists_generator([1, 2, 3], ['a', 'b', 'c'])
print(next(gen)) # (1, 'a')
print(next(gen)) # (2, 'b')
gen = flatten_list_generator([1, [2, [3, 4], 5], 6])
print(next(gen)) # 1
print(next(gen)) # 2
Task 26: Develop a generator to yield powers of 2 up to
a given number.
Create a generator function named powers_of_two_generator that takes an
integer n and yields powers of 2 up to 2^n .
Example of function usage:
Task 27: Implement a generator that yields powers of a
given base up to a specified limit.
Create a generator function named powers_of_base_generator that takes a
base and a limit, and yields powers of the base up to the specified limit.
Example of function usage:
Task 28: Write a generator to yield the squares of
numbers in a given range.
Create a generator function named squares_generator that takes a range of
numbers and yields their squares.
Example of function usage:
gen = nested_dict_generator({'a': {'b': 1, 'c': 2}, 'd': 3})
print(next(gen)) # ('b', 1)
print(next(gen)) # ('c', 2)
gen = powers_of_two_generator(4)
print(next(gen)) # 1
print(next(gen)) # 2
gen = powers_of_base_generator(3, 81)
print(next(gen)) # 1
print(next(gen)) # 3
gen = squares_generator(1, 5)
print(next(gen)) # 1
print(next(gen)) # 4
Task 29: Create a generator to yield cubes of numbers
in a specified range.
Create a generator function named cubes_generator that takes a range of
numbers and yields their cubes.
Example of function usage:
Task 30: Develop a generator that yields factorials of
numbers up to a given limit.
Create a generator function named factorials_generator that takes an integer
n and yields factorials of numbers from 0 up to n .
Example of function usage:
Task 31: Implement a generator to yield numbers in the
Collatz sequence.
Create a generator function named collatz_sequence_generator that takes an
integer and yields numbers in the Collatz sequence.
Example of function usage:
Task 32: Write a generator that yields numbers in a
geometric progression.
gen = cubes_generator(1, 4)
print(next(gen)) # 1
print(next(gen)) # 8
gen = factorials_generator(4)
print(next(gen)) # 1
print(next(gen)) # 1
gen = collatz_sequence_generator(6)
print(next(gen)) # 6
print(next(gen)) # 3
Create a generator function named geometric_progression_generator that
takes an initial term, a common ratio, and a limit, and yields numbers in the
geometric progression.
Example of function usage:
Task 33: Create a generator to yield numbers in an
arithmetic progression.
Create a generator function named arithmetic_progression_generator that
takes an initial term, a common difference, and a limit, and yields numbers in the
arithmetic progression.
Example of function usage:
Task 34: Develop a generator that yields the running
sum of a list of numbers.
Create a generator function named running_sum_generator that takes a list of
numbers and yields their running sum.
Example of function usage:
Task 35: Implement a generator to yield the running
product of a list of numbers.
Create a generator function named running_product_generator that takes a list
of numbers and yields their running product.
gen = geometric_progression_generator(2, 3, 20)
print(next(gen)) # 2
print(next(gen)) # 6
gen = arithmetic_progression_generator(2, 3, 20)
print(next(gen)) # 2
print(next(gen)) # 5
gen = running_sum_generator([1, 2, 3, 4])
print(next(gen)) # 1
print(next(gen)) # 3
Example of function usage:
gen = running_product_generator([1, 2, 3, 4])
print(next(gen)) # 1
print(next(gen)) # 2
```
___
Виконання роботи:
```Python
import itertools
import math

# Define all generator functions and classes
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def number_generator(numbers):
    for number in numbers:
        yield number

def even_number_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 == 0:
            yield number

def odd_number_generator(start, end):
    for number in range(start, end + 1):
        if number % 2 != 0:
            yield number

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def prime_number_generator(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for number in range(2, limit + 1):
        if is_prime(number):
            yield number

def pre_order_traversal(root):
    if root:
        yield root.value
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)

def in_order_traversal(root):
    if root:
        yield from in_order_traversal(root.left)
        yield root.value
        yield from in_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.value

def dfs_traversal(graph, start):
    stack = [start]
    visited = set()
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            yield vertex
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))

def bfs_traversal(graph, start):
    from collections import deque
    queue = deque([start])
    visited = set()
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            yield vertex
            visited.add(vertex)
            queue.extend(graph[vertex])

def dict_keys_generator(dictionary):
    for key in dictionary:
        yield key

def dict_values_generator(dictionary):
    for value in dictionary.values():
        yield value

def dict_items_generator(dictionary):
    for item in dictionary.items():
        yield item

def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word

def string_chars_generator(string):
    for char in string:
        yield char

def unique_elements_generator(elements):
    seen = set()
    for element in elements:
        if element not in seen:
            yield element
            seen.add(element)

def reverse_list_generator(elements):
    for element in reversed(elements):
        yield element

def cartesian_product_generator(list1, list2):
    for product in itertools.product(list1, list2):
        yield product

def permutations_generator(elements):
    for permutation in itertools.permutations(elements):
        yield permutation

def combinations_generator(elements):
    for length in range(1, len(elements) + 1):
        for combination in itertools.combinations(elements, length):
            yield combination

def tuple_list_generator(tuples):
    for tup in tuples:
        yield tup

def parallel_lists_generator(*lists):
    for values in zip(*lists):
        yield values

def flatten_list_generator(nested_list):
    for element in nested_list:
        if isinstance(element, list):
            yield from flatten_list_generator(element)
        else:
            yield element

def nested_dict_generator(nested_dict):
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            yield from nested_dict_generator(value)
        else:
            yield (key, value)

def powers_of_two_generator(n):
    for i in range(n + 1):
        yield 2 ** i

def powers_of_base_generator(base, limit):
    power = 1
    while power <= limit:
        yield power
        power *= base

def squares_generator(start, end):
    for number in range(start, end + 1):
        yield number ** 2

def cubes_generator(start, end):
    for number in range(start, end + 1):
        yield number ** 3

def factorials_generator(n):
    for i in range(n + 1):
        yield math.factorial(i)

def collatz_sequence_generator(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield 1

def geometric_progression_generator(a, r, limit):
    term = a
    while term <= limit:
        yield term
        term *= r

def arithmetic_progression_generator(a, d, limit):
    term = a
    while term <= limit:
        yield term
        term += d

def running_sum_generator(numbers):
    total = 0
    for number in numbers:
        total += number
        yield total

def running_product_generator(numbers):
    total = 1
    for number in numbers:
        total *= number
        yield total

# Usage examples
def print_generators():
    print("Number Generator:")
    gen = number_generator([1, 2, 3])
    print(next(gen))  # 1
    print(next(gen))  # 2
    print(next(gen))  # 3

    print("\nEven Number Generator:")
    gen = even_number_generator(1, 10)
    print(next(gen))  # 2
    print(next(gen))  # 4

    print("\nOdd Number Generator:")
    gen = odd_number_generator(1, 10)
    print(next(gen))  # 1
    print(next(gen))  # 3

    print("\nFibonacci Generator:")
    gen = fibonacci_generator()
    print(next(gen))  # 0
    print(next(gen))  # 1
    print(next(gen))  # 1

    print("\nPrime Number Generator:")
    gen = prime_number_generator(10)
    print(next(gen))  # 2
    print(next(gen))  # 3

    print("\nPre-order Traversal:")
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    gen = pre_order_traversal(root)
    print(next(gen))  # 1
    print(next(gen))  # 2

    print("\nIn-order Traversal:")
    gen = in_order_traversal(root)
    print(next(gen))  # 2
    print(next(gen))  # 1

    print("\nPost-order Traversal:")
    gen = post_order_traversal(root)
    print(next(gen))  # 2
    print(next(gen))  # 3

    print("\nDFS Traversal:")
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    gen = dfs_traversal(graph, 0)
    print(next(gen))  # 0
    print(next(gen))  # 2

    print("\nBFS Traversal:")
    gen = bfs_traversal(graph, 0)
    print(next(gen))  # 0
    print(next(gen))  # 1

    print("\nDictionary Keys Generator:")
    dictionary = {"a": 1, "b": 2}
    gen = dict_keys_generator(dictionary)
    print(next(gen))  # "a"
    print(next(gen))  # "b"

    print("\nDictionary Values Generator:")
    gen = dict_values_generator(dictionary)
    print(next(gen))  # 1
    print(next(gen))  # 2

    print("\nDictionary Items Generator:")
    gen = dict_items_generator(dictionary)
    print(next(gen))  # ("a", 1)
    print(next(gen))  # ("b", 2)

    print("\nString Characters Generator:")
    gen = string_chars_generator("abc")
    print(next(gen))  # "a"
    print(next(gen))  # "b"

    print("\nUnique Elements Generator:")
    gen = unique_elements_generator([1, 2, 2, 3])
    print(next(gen))  # 1
    print(next(gen))  # 2

    print("\nReverse List Generator:")
    gen = reverse_list_generator([1, 2, 3])
    print(next(gen))  # 3
    print(next(gen))  # 2

    print("\nCartesian Product Generator:")
    gen = cartesian_product_generator([1, 2], [3, 4])
    print(next(gen))  # (1, 3)
    print(next(gen))  # (1, 4)

    print("\nPermutations Generator:")
    gen = permutations_generator([1, 2])
    print(next(gen))  # (1, 2)
    print(next(gen))  # (2, 1)

    print("\nCombinations Generator:")
    gen = combinations_generator([1, 2])
    print(next(gen))  # (1,)
    print(next(gen))  # (2,)

    print("\nTuple List Generator:")
    gen = tuple_list_generator([(1, 2), (3, 4)])
    print(next(gen))  # (1, 2)
    print(next(gen))  # (3, 4)

    print("\nParallel Lists Generator:")
    gen = parallel_lists_generator([1, 2], [3, 4])
    print(next(gen))  # (1, 3)
    print(next(gen))  # (2, 4)

    print("\nFlatten List Generator:")
    gen = flatten_list_generator([1, [2, [3, 4], 5]])
    print(next(gen))  # 1
    print(next(gen))  # 2

    print("\nNested Dictionary Generator:")
    nested_dict = {"a": {"b": 1}, "c": 2}
    gen = nested_dict_generator(nested_dict)
    print(next(gen))  # ("b", 1)
    print(next(gen))  # ("c", 2)

    print("\nPowers of Two Generator:")
    gen = powers_of_two_generator(3)
    print(next(gen))  # 1
    print(next(gen))  # 2

    print("\nPowers of Base Generator:")
    gen = powers_of_base_generator(3, 10)
    print(next(gen))  # 1
    print(next(gen))  # 3

    print("\nSquares Generator:")
    gen = squares_generator(1, 3)
    print(next(gen))  # 1
    print(next(gen))  # 4

    print("\nCubes Generator:")
    gen = cubes_generator(1, 3)
    print(next(gen))  # 1
    print(next(gen))  # 8

    print("\nFactorials Generator:")
    gen = factorials_generator(3)
    print(next(gen))  # 1
    print(next(gen))  # 1

    print("\nCollatz Sequence Generator:")
    gen = collatz_sequence_generator(6)
    print(next(gen))  # 6
    print(next(gen))  # 3

    print("\nGeometric Progression Generator:")
    gen = geometric_progression_generator(2, 2, 8)
    print(next(gen))  # 2
    print(next(gen))  # 4

    print("\nArithmetic Progression Generator:")
    gen = arithmetic_progression_generator(1, 2, 5)
    print(next(gen))  # 1
    print(next(gen))  # 3

    print("\nRunning Sum Generator:")
    gen = running_sum_generator([1, 2, 3])
    print(next(gen))  # 1
    print(next(gen))  # 3

    print("\nRunning Product Generator:")
    gen = running_product_generator([1, 2, 3])
    print(next(gen))  # 1
    print(next(gen))  # 2

print_generators()

```
___
Результати:
```Python
Number Generator:
1
2
3

Even Number Generator:
2
4

Odd Number Generator:
1
3

Fibonacci Generator:
0
1
1

Prime Number Generator:
2
3

Pre-order Traversal:
1
2

In-order Traversal:
2
1

Post-order Traversal:
2
3

DFS Traversal:
0
1

BFS Traversal:
0
1

Dictionary Keys Generator:
a
b

Dictionary Values Generator:
1
2

Dictionary Items Generator:
('a', 1)
('b', 2)

String Characters Generator:
a
b

Unique Elements Generator:
1
2

Reverse List Generator:
3
2

Cartesian Product Generator:
(1, 3)
(1, 4)

Permutations Generator:
(1, 2)
(2, 1)

Combinations Generator:
(1,)
(2,)

Tuple List Generator:
(1, 2)
(3, 4)

Parallel Lists Generator:
(1, 3)
(2, 4)

Flatten List Generator:
1
2

Nested Dictionary Generator:
('b', 1)
('c', 2)

Powers of Two Generator:
1
2

Powers of Base Generator:
1
3

Squares Generator:
1
4

Cubes Generator:
1
8

Factorials Generator:
1
1

Collatz Sequence Generator:
6
3

Geometric Progression Generator:
2
4

Arithmetic Progression Generator:
1
3

Running Sum Generator:
1
3

Running Product Generator:
1
2
```
___
Висновки: У цій роботі розроблено 35 генераторних функцій на Python для різних завдань. Генератори ефективно обробляють великі дані, поступово генеруючи значення без завантаження всього набору в пам'ять. Вони охоплюють ітерацію числових послідовностей, обхід структур даних, роботу зі словниками та файлами, а також обчислення математичних послідовностей, надаючи корисні інструменти для щоденних завдань з обробки даних.
___