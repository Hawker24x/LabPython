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
