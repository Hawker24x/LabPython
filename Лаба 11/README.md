Лабораторна робота №11: Advanced Working with Arrays of Numbers in Python
___
Мета роботи:
Ці завдання мають на меті розширити та поглибити навички роботи з масивами чисел у Python. Кожне завдання охоплює різні аспекти обробки даних, алгоритмів та маніпуляцій з масивами.
___
Опис завдання:
```Python
Task 1: Sum of Squares
Create a function sum_of_squares that accepts an array of numbers and returns the sum of the squares of each number.
Example of function usage:
print(sum_of_squares([1, 2, 3])) # Output: 14 

Task 2: Filter and Sum
Create a function filter_and_sum that accepts an array of numbers and returns the sum of all the elements that are greater or equal than the average of the array.
Example of function usage:
print(filter_and_sum([1, 2, 3, 4, 10])) # Output: 14 

Task 3: Sort by Frequency
Create a function sort_by_frequency that sorts an array of numbers based on the frequency of each element from highest to lowest. If two numbers have the same frequency, the smaller number should come first.
Example of function usage:
print(sort_by_frequency([4, 6, 2, 6, 4, 4, 6])) # Output: [4, 4, 4, 6, 6, 6, 2] 

Task 4: Find Missing Number
Create a function find_missing_number that finds the missing number in an array containing all integers from 1 to n except one. Assume the array has no duplicates.
Example of function usage:
print(find_missing_number([1, 2, 4, 5])) # Output: 3 

Task 5: Longest Consecutive Sequence
Create a function longest_consecutive that finds the length of the longest consecutive elements sequence in an unsorted array.
Example of function usage:
print(longest_consecutive([100, 4, 200, 1, 3, 2])) # Output: 4 
Task 6: Rotate Array

Create a function rotate_array that rotates the array to the right by k steps, where k is non-negative.
Example of function usage:
print(rotate_array([1, 2, 3, 4, 5], 2)) # Output: [4, 5, 1, 2, 3] 
Task 7: Array of Products
Create a function array_of_products that calculates an array of products of all numbers except the one at the current index without using division.
Example of function usage:
print(array_of_products([1, 2, 3, 4])) # Output: [24, 12, 8, 6]
 
Task 8: Maximum Subarray Sum
Create a function max_subarray_sum that finds the maximum sum of a contiguous subarray within a one-dimensional array of numbers.
Example of function usage:
print(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4])) # Output: 6 

Task 9: Spiral Order Matrix
Create a function spiral_order that returns all elements of a 2D matrix in spiral order.
Example of function usage:
print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5] 

Task 10: K Closest Points to Origin
Create a function k_closest_points that finds the k closest points to the origin (0, 0) in a 2D plane, given an array of coordinate points.
Example of function usage:
print(k_closest_points([(1, 2), (1, 1), (3, 4)], 2)) # Output: [(1, 1), (1, 2)] :
```
___
Виконання роботи:
```Python
def task1(numbers):

    return sum(i ** 2 for i in numbers)

def task2(numbers):
    average = sum(numbers) / len(numbers)

    return sum(i for i in numbers if i >= average)

def task3(arr):
    frequency_dict = {}
    for num in arr:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    sorted_arr = sorted(arr, key=lambda x: (-frequency_dict[x], x))

    return sorted_arr

def task4(numbers):
    n = len(numbers) + 1
    total_sum = n * (n + 1) // 2

    return total_sum - sum(numbers)

def task5(nums):
    if not nums:
        return 0

    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

def task6(arr, k):
    k = k % len(arr)

    return arr[-k:] + arr[:-k]

def task7(arr):
    n = len(arr)
    products_before = [1] * n
    products_after = [1] * n

    for i in range(1, n):
        products_before[i] = products_before[i - 1] * arr[i - 1]

    for i in range(n - 2, -1, -1):
        products_after[i] = products_after[i + 1] * arr[i + 1]

    return [products_before[i] * products_after[i] for i in range(n)]

def task8(arr):
    current_sum = max_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

def task9(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result

def task10(points, k):
    distances = [(x**2 + y**2, (x, y)) for x, y in points]
    distances.sort()

    return [point for _, point in distances[:k]]

# Примеры использования и вывод результатов для каждой функции:

# Пример для task1
numbers1 = [1, 2, 3, 4]
print(f"task1({numbers1}) = {task1(numbers1)}")

# Пример для task2
numbers2 = [1, 2, 3, 4, 5]
print(f"task2({numbers2}) = {task2(numbers2)}")

# Пример для task3
arr3 = [4, 5, 6, 5, 4, 3]
print(f"task3({arr3}) = {task3(arr3)}")

# Пример для task4
numbers4 = [1, 2, 4, 5]
print(f"task4({numbers4}) = {task4(numbers4)}")

# Пример для task5
nums5 = [100, 4, 200, 1, 3, 2]
print(f"task5({nums5}) = {task5(nums5)}")

# Пример для task6
arr6 = [1, 2, 3, 4, 5, 6, 7]
k6 = 3
print(f"task6({arr6}, {k6}) = {task6(arr6, k6)}")

# Пример для task7
arr7 = [1, 2, 3, 4]
print(f"task7({arr7}) = {task7(arr7)}")

# Пример для task8
arr8 = [-2,1,-3,4,-1,2,1,-5,4]
print(f"task8({arr8}) = {task8(arr8)}")

# Пример для task9
matrix9 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"task9({matrix9}) = {task9(matrix9)}")

# Пример для task10
points10 = [(1, 3), (3, 4), (2, -1)]
k10 = 2
print(f"task10({points10}, {k10}) = {task10(points10, k10)}")

```
___
Результати:
```Python
task1([1, 2, 3, 4]) = 30
task2([1, 2, 3, 4, 5]) = 12
task3([4, 5, 6, 5, 4, 3]) = [4, 4, 5, 5, 3, 6]
task4([1, 2, 4, 5]) = 3
task5([100, 4, 200, 1, 3, 2]) = 4
task6([1, 2, 3, 4, 5, 6, 7], 3) = [5, 6, 7, 1, 2, 3, 4]
task7([1, 2, 3, 4]) = [24, 12, 8, 6]
task8([-2, 1, -3, 4, -1, 2, 1, -5, 4]) = 6
task9([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) = [1, 2, 3, 6, 9, 8, 7, 4, 5]
task10([(1, 3), (3, 4), (2, -1)], 2) = [(2, -1), (1, 3)]
```
___
Висновки: Ці функції демонструють різні алгоритми та структури даних, що використовуються в програмуванні для розв'язання різних задач.
___