Лабораторна робота №13: Tasks for data processing.
___
Мета роботи:
Functions with different parameter types for solving data processing tasks.
___
Опис завдання:
```Python
lab13
Tasks for data processing. Functions with different
parameter types for solving data processing tasks.
Task 1: Interpolate Missing Values
Create a function interpolate_missing that takes a list of numbers, which may
include None as a placeholder for missing values. The function should interpolate
missing values using the average of the nearest non- None neighbors.
Example of function usage:
Task 2: Fibonacci Series Generator
Write a generator function fibonacci that yields the Fibonacci series up to n
terms.
Example of function usage:
Task 3: Batch Data Processing
Define a function process_batches that takes a list of numbers and a batch size,
then processes each batch to return their maximum values.
Example of function usage:
Task 4: Encode and Decode Strings
print(interpolate_missing([1, None, None, 4])) # Output: [1, 2,
3, 4]
for num in fibonacci(5):
 print(num) # Output: 0, 1, 1, 2, 3
print(process_batches([1, 2, 3, 4, 5, 6], 2)) # Output: [2, 4,
6]
Create two functions encode_string and decode_string . encode_string
should convert the string into a run-length encoded format, and decode_string
should revert it back to the original string.
Example of function usage:
Task 5: Matrix Rotation
Write a function rotate_matrix that rotates a given n x n matrix 90 degrees
clockwise.
Example of function usage:
Task 6: Regular Expression Search
Define a function regex_search that takes a list of strings and a regular
expression pattern, returning a list of all strings that match the pattern.
Example of function usage:
Task 7: Merge Sorted Arrays
Create a function merge_sorted_arrays that merges two sorted arrays into a
single sorted array.
Example of function usage:
encoded = encode_string("aaabbc")
print(encoded) # Output: "3a2bc"
print(decode_string(encoded)) # Output: "aaabbc"
matrix = [
 [1, 2],
 [3, 4]
]
print(rotate_matrix(matrix)) # Output: [[3, 1], [4, 2]]
print(regex_search(["test", "test123", "none"], "test\d+")) #
Output: ["test123"]
Task 8: Prime Number Checker
Write a function is_prime that takes a number and returns True if it is a prime
number, otherwise False .
Example of function usage:
Task 9: Group by Key
Define a function group_by_key that takes a list of dictionaries and groups them
by a specified key.
Example of function usage:
Task 10: Remove Outliers
Create a function remove_outliers that removes elements from a list that are
more than two standard deviations away from the mean.
Example of function usage:
print(merge_sorted_arrays([1, 3, 5], [2, 4, 6])) # Output: [1,
2, 3, 4, 5, 6]
print(is_prime(11)) # Output: True
data = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2},
{'key': 'a', 'value': 3}]
print(group_by_key(data, 'key')) # Output: {'a': [1, 3], 'b':
[2]}
print(remove_outliers([10, 100, 200, 300, 400, 500, 600])) #
Output: [100, 200, 300, 400, 500]
```
___
Виконання роботи:
```Python
import numpy as np

def interpolate_missing(numbers):
    none_indexes = [i for i, x in enumerate(numbers) if x is None]

    for index in none_indexes:
        left_neighbor = next((i for i in range(index, -1, -1) if numbers[i] is not None), None)
        right_neighbor = next((i for i in range(index, len(numbers)) if numbers[i] is not None), None)

        if left_neighbor is not None and right_neighbor is not None:
            numbers[index] = (numbers[left_neighbor] + numbers[right_neighbor]) / 2

    return numbers


def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def process_batches(numbers, batch_size):
    max_values = []
    for i in range(0, len(numbers), batch_size):
        batch = numbers[i:i + batch_size]
        max_values.append(max(batch))
    return max_values


def encode_string(s):
    encoded = ''
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded += str(count) + s[i - 1]
            count = 1
    encoded += str(count) + s[-1]
    return encoded


def decode_string(encoded):
    decoded = ''
    i = 0
    while i < len(encoded):
        count = int(encoded[i])
        decoded += encoded[i + 1] * count
        i += 2
    return decoded


def rotate_matrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix


import re


def regex_search(strings, pattern):
    matched_strings = []
    regex = re.compile(pattern)
    for string in strings:
        if regex.search(string):
            matched_strings.append(string)
    return matched_strings


def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def group_by_key(data, key):
    grouped = {}
    for item in data:
        k = item[key]
        if k in grouped:
            grouped[k].append(item['value'])
        else:
            grouped[k] = [item['value']]
    return grouped

def remove_outliers(arr):
    mean = np.mean(arr)
    sd = np.std(arr)
    final_list = [x for x in arr if (x > mean - 2 * sd)]
    final_list = [x for x in final_list if (x < mean + 2 * sd)]
    return final_list

# Примеры использования и вывод результатов для каждой функции:

import numpy as np

# Пример для interpolate_missing
numbers1 = [1, None, 3, None, 5]
print(f"interpolate_missing({numbers1}) = {interpolate_missing(numbers1)}")

# Пример для fibonacci
n2 = 10
fibonacci_sequence = list(fibonacci(n2))
print(f"fibonacci({n2}) = {fibonacci_sequence}")

# Пример для process_batches
numbers3 = [1, 3, 5, 2, 8, 7, 4, 6]
batch_size3 = 3
print(f"process_batches({numbers3}, {batch_size3}) = {process_batches(numbers3, batch_size3)}")

# Пример для encode_string
s4 = "aaabbcccc"
encoded_string = encode_string(s4)
print(f"encode_string('{s4}') = {encoded_string}")

# Пример для decode_string
encoded_string5 = "3a2b4c"
decoded_string = decode_string(encoded_string5)
print(f"decode_string('{encoded_string5}') = {decoded_string}")

# Пример для rotate_matrix
matrix6 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotated_matrix = rotate_matrix(matrix6)
print(f"rotate_matrix({matrix6}) = {rotated_matrix}")

# Пример для regex_search
strings7 = ["apple", "banana", "cherry", "date"]
pattern7 = "a"
matched_strings = regex_search(strings7, pattern7)
print(f"regex_search({strings7}, '{pattern7}') = {matched_strings}")

# Пример для merge_sorted_arrays
arr1_8 = [1, 3, 5]
arr2_8 = [2, 4, 6]
merged_array = merge_sorted_arrays(arr1_8, arr2_8)
print(f"merge_sorted_arrays({arr1_8}, {arr2_8}) = {merged_array}")

# Пример для is_prime
n9 = 29
print(f"is_prime({n9}) = {is_prime(n9)}")

# Пример для group_by_key
data10 = [
    {"key": "a", "value": 1},
    {"key": "b", "value": 2},
    {"key": "a", "value": 3}
]
grouped_data = group_by_key(data10, "key")
print(f"group_by_key({data10}, 'key') = {grouped_data}")

# Пример для remove_outliers
arr11 = [10, 12, 12, 12, 13, 13, 14, 14, 15, 100]
filtered_arr = remove_outliers(arr11)
print(f"remove_outliers({arr11}) = {filtered_arr}")

```
___
Результати:
```Python
interpolate_missing([1, None, 3, None, 5]) = [1, 2.0, 3, 4.0, 5]
fibonacci(10) = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
process_batches([1, 3, 5, 2, 8, 7, 4, 6], 3) = [5, 8, 6]
encode_string('aaabbcccc') = 3a2b4c
decode_string('3a2b4c') = aaabbcccc
rotate_matrix([[7, 4, 1], [8, 5, 2], [9, 6, 3]]) = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
regex_search(['apple', 'banana', 'cherry', 'date'], 'a') = ['apple', 'banana', 'date']
merge_sorted_arrays([1, 3, 5], [2, 4, 6]) = [1, 2, 3, 4, 5, 6]
is_prime(29) = True
group_by_key([{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2}, {'key': 'a', 'value': 3}], 'key') = {'a': [1, 3], 'b': [2]}
remove_outliers([10, 12, 12, 12, 13, 13, 14, 14, 15, 100]) = [10, 12, 12, 12, 13, 13, 14, 14, 15]

```
___
Висновки: Ці приклади демонструють використання різних функцій, їхній виклик та вивід результатів. Вони охоплюють широкий спектр задач, від роботи з масивами та рядками до використання математичних та статистичних методів.
___