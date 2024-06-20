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