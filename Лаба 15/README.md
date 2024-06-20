Лабораторна робота №15: Overview of Big Data Technologies
___
Мета роботи:
Метою цієї роботи є навчитися використовувати регулярні вирази, маніпулювати рядками та списками в Python для виконання різних завдань з обробки даних
___
Опис завдання:
```Python
Overview of Big Data Technologies
Task 1: Clean Data
Write a function clean_data() that takes a long string of data points separated
by commas, and uses map() to return a list of data points where each is stripped
of whitespace and converted to lowercase.
Example of function usage:
Task 2: Filter Emails
Create a function filter_emails() that takes a long string containing emails,
and uses filter() to return a list containing only valid email addresses. An
email is valid if it contains exactly one '@' symbol.
Example of function usage:
Task 3: Extract Keywords
Write a function extract_keywords() that takes a long string of words, and uses
filter() to return a list containing words that are longer than a specified length.
Example of function usage:
data = " Apple, Banana , orange "
cleaned = clean_data(data)
print(cleaned) # ['apple', 'banana', 'orange']
emails = "mail us test@example.com and invalid-email.com.djwd
with example@test.co"
valid_emails = filter_emails(emails)
print(valid_emails) # ['test@example.com', 'example@test.co']
words = "apple pear banana kiwi"
filtered_words = extract_keywords(words, 4)
print(filtered_words) # ['apple', 'banana']
Task 4: Process Text Data
Write a function process_text() that takes a long string of text data, uses
map() to strip whitespace, remove special characters, and convert to lowercase,
then uses filter() to return a list excluding any empty or very short entries.
Example of function usage:
Task 5: Normalize Data
Write a function normalize_data() that takes a long string of numeric values
separated by commas and normalizes them to a range between 0 and 1 based on
the maximum value.
Example of function usage:
Task 6: Concatenate Strings
Develop a function concatenate_strings() that takes multiple strings separated
by a special character and concatenates them into a single string without the
separator.
Example of function usage:
Task 7: Sum Numeric Strings
Create a function sum_numeric_strings() that takes a string containing
numbers separated by commas and calculates their total sum.
texts = " Hello! , Yes? , No. , "
processed_texts = process_text(texts)
print(processed_texts) # ['hello', 'yes', 'no']
numbers = "10, 20,30"
normalized_numbers = normalize_data(numbers)
print(normalized_numbers) # [0.333, 0.667, 1.0]
data = "hello*world*again"
concatenated = concatenate_strings(data, '*')
print(concatenated) # 'helloworldagain'
Example of function usage:
Task 8: Filter Numbers
Write a function filter_numbers() that filters out numbers from a string that are
above a specified threshold.
Example of function usage:
Task 9: Map to Squares
Create a function map_to_squares() that takes a string of numbers, converts
them to their squares, and returns them as a list.
Example of function usage:
Task 10: Reverse Strings
Develop a function reverse_strings() that takes a string of words separated by
commas and reverses each word.
Example of function usage:
numbers = "1, 2, test, 3, 4"
total_sum = sum_numeric_strings(numbers)
print(total_sum) # 10
numbers = "10 test30 40"
filtered = filter_numbers(numbers, 25)
print(filtered) # [30, 40]
numbers = "1, 2, 3, 4"
squared_numbers = map_to_squares(numbers)
print(squared_numbers) # [1, 4, 9, 16]
words = "apple,banana,carrot"
reversed_words = reverse_strings(words)
print(reversed_words) # ['elppa', 'ananab', 'torrac']
```
___
Виконання роботи:
```Python
import re

def clean_data(data):
    if isinstance(data, str):
        data = data.split(',')
    cleaned = [item.strip().lower() for item in data]
    return cleaned

def filter_emails(emails_string):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    valid_emails = re.findall(pattern, emails_string)
    valid_emails_list = [email for email in valid_emails if email.count('@') == 1]
    return valid_emails_list

def extract_keywords(words, length):
    filtered_words = [word for word in words.split() if len(word) > length]
    return filtered_words

def process_text(text):
    processed = [re.sub(r'[^\w\s]', '', item.strip().lower()) for item in text.split(',')]
    processed = [item for item in processed if item]
    return processed

def normalize_data(numbers):
    numbers_list = [float(num) for num in numbers.split(',')]
    max_value = max(numbers_list)
    normalized = [round(num / max_value, 3) for num in numbers_list]
    return normalized

def concatenate_strings(data, separator):
    concatenated = ''.join(data.split(separator))
    return concatenated

def sum_numeric_strings(numbers):
    total_sum = sum(map(int, re.findall(r'\d+', numbers)))
    return total_sum

def filter_numbers(input_string, threshold):
    numbers_list = [int(num) for num in re.findall(r'\d+', input_string)]
    filtered_numbers = [num for num in numbers_list if num > threshold]
    return filtered_numbers

def map_to_squares(numbers):
    squared_numbers = [int(num) ** 2 for num in numbers.split(',')]
    return squared_numbers

def reverse_strings(words):
    reversed_words = [word[::-1] for word in words.split(',')]
    return reversed_words

# Test the functions
data = " Apple,  Banana , orange "
cleaned_data = clean_data(data)
print("Cleaned Data:", cleaned_data)  # Output: ['apple', 'banana', 'orange']

emails = "mail us test@example.com and invalid-email.com.djwd with example@test.co"
valid_emails = filter_emails(emails)
print("Valid Emails:", valid_emails)  # Output: ['test@example.com', 'example@test.co']

words = "apple pear banana kiwi"
filtered_words = extract_keywords(words, 4)
print("Filtered Words:", filtered_words)  # Output: ['apple', 'banana']

texts = "Hello! , Yes? , No. , "
processed_texts = process_text(texts)
print("Processed Texts:", processed_texts)  # Output: ['hello', 'yes', 'no']

numbers = "10, 20, 30, 40, 50"
normalized_numbers = normalize_data(numbers)
print("Normalized Numbers:", normalized_numbers)  # Output: [0.2, 0.4, 0.6, 0.8, 1.0]

data_to_concatenate = "Hello, World!, How, are, you?"
separator = ","
concatenated_data = concatenate_strings(data_to_concatenate, separator)
print("Concatenated Data:", concatenated_data)  # Output: "Hello World! How are you?"

numeric_strings = "10, 20, abc, 30, def, 40"
sum_of_numeric_strings = sum_numeric_strings(numeric_strings)
print("Sum of Numeric Strings:", sum_of_numeric_strings)  # Output: 100

numbers_to_filter = "10, 20, abc, 30, def, 40"
threshold = 25
filtered_numbers = filter_numbers(numbers_to_filter, threshold)
print("Filtered Numbers:", filtered_numbers)  # Output: [30, 40]

numbers_to_square = "1, 2, 3, 4, 5"
squared_numbers = map_to_squares(numbers_to_square)
print("Squared Numbers:", squared_numbers)  # Output: [1, 4, 9, 16, 25]

strings_to_reverse = "apple, banana, orange, PEAR, kiwi"
reversed_strings = reverse_strings(strings_to_reverse)
print("Reversed Strings:", reversed_strings)  # Output: ['elppa', 'ananab', 'egnaro', 'RAEP', 'iwik']

```
___
Результати:
```Python
Cleaned Data: ['apple', 'banana', 'orange']
Valid Emails: ['test@example.com', 'example@test.co']
Filtered Words: ['apple', 'banana']
Processed Texts: ['hello', 'yes', 'no']
Normalized Numbers: [0.2, 0.4, 0.6, 0.8, 1.0]
Concatenated Data: Hello World! How are you?
Sum of Numeric Strings: 100
Filtered Numbers: [30, 40]
Squared Numbers: [1, 4, 9, 16, 25]
Reversed Strings: ['elppa', 'ananab ', 'egnaro ', 'RAEP ', 'iwik ']

```
___
Висновки: Ця робота поглибила розуміння основних операцій обробки та маніпуляції рядковими даними і списками в Python. Реалізація функцій для очищення даних, фільтрації електронних адрес, виділення ключових слів, обробки тексту, нормалізації числових значень, конкатенації рядків, сумування чисел у рядку, фільтрації чисел за порогом, зведення чисел у квадрат та реверсування рядків.
___