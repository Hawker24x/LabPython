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
