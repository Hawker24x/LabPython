Лабораторна робота №12: Using nested lists to create and manipulate twodimensional data structures
___
Мета роботи:
Метою роботи (lab12) є навчитися створювати та маніпулювати двовимірними структурами даних у Python через клас Matrix, що включає операції додавання елементів, сумування рядків, транспонування, множення, обертання, "сплющення" та витяг діагоналі.
___
Опис завдання:
```Python
lab12
Using nested lists to create and manipulate twodimensional data structures.
Task 1: Create a Matrix
Create a Python class Matrix that initializes a two-dimensional list with zeros.
The constructor should accept two parameters: rows and columns, indicating the
dimensions of the matrix.
Example of class usage:
Task 2: Add Elements to Matrix
Extend the Matrix class by adding a method add_element that adds an element
at a specific position (row, column).
Example of class usage:
Task 3: Sum of Rows
Add a method sum_of_rows to the Matrix class that returns a list of sums of
each row in the matrix.
Example of class usage:
matrix = Matrix(2, 3)
print(matrix.data) # [[0, 0, 0], [0, 0, 0]]
matrix = Matrix(2, 3)
matrix.add_element(1, 2, 10)
print(matrix.data) # [[0, 0, 10], [0, 0, 0]]
matrix = Matrix(2, 3)
matrix.add_element(0, 0, 5)
matrix.add_element(0, 1, 10)
Task 4: Matrix Transposition
Create a method transpose in the Matrix class that returns a new Matrix
object, which is the transpose of the original matrix.
Example of class usage:
Task 5: Multiply Matrices
Implement a method multiply_by in the Matrix class that accepts another
Matrix object and returns a new Matrix object that is the result of the multiplication
of the two matrices.
Example of class usage:
Task 6: Check Symmetric Matrix
Add a method is_symmetric to the Matrix class that checks if the matrix is
symmetric (i.e., the matrix is equal to its transpose).
Example of class usage:
matrix.add_element(1, 2, 20)
print(matrix.sum_of_rows()) # [15, 20]
matrix = Matrix(2, 3)
matrix.add_element(0, 1, 1)
matrix.add_element(1, 2, 2)
transposed = matrix.transpose()
print(transposed.data) # [[0, 0], [1, 0], [0, 2]]
matrix1 = Matrix(2, 3)
matrix1.add_element(0, 0, 1)
matrix1.add_element(0, 1, 2)
matrix1.add_element(0, 2, 3)
matrix2 = Matrix(3, 2)
matrix2.add_element(0, 0, 1)
matrix2.add_element(1, 0, 2)
matrix2.add_element(2, 0, 3)
result = matrix1.multiply_by(matrix2)
print(result.data) # [[14, 0], [0, 0]]
Task 7: Rotate Matrix
Implement a method rotate_right in the Matrix class that rotates the matrix
90 degrees to the right.
Example of class usage:
Task 8: Flatten Matrix
Create a method flatten in the Matrix class that returns a single list containing
all elements of the matrix.
Example of class usage:
Task 9: Matrix from List
Add a static method from_list to the Matrix class that creates a matrix object
from a given list of lists.
Example of class usage:
matrix = Matrix(2, 2)
matrix.add_element(0, 1, 5)
matrix.add_element(1, 0, 5)
print(matrix.is_symmetric()) # True
matrix = Matrix(2, 2)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
matrix.rotate_right()
print(matrix.data) # [[3, 1], [4, 2]]
matrix = Matrix(2, 2)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
print(matrix.flatten()) # [1, 2, 3, 4]
Task 10: Extract Diagonal
Create a method diagonal in the Matrix class that extracts the diagonal of a
square matrix as a list.
Example of class usage:
python
list_of_lists = [[1, 2], [3, 4]]
matrix = Matrix.from_list(list_of_lists)
print(matrix.data) # [[1, 2], [3, 4]]
matrix = Matrix(3, 3)
matrix.add_element(0, 0, 1)
matrix.add_element(1, 1, 2)
matrix.add_element(2, 2, 3)
print(matrix.diagonal()) # [1, 2, 3]
```
___
Виконання роботи:
```Python
class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def add_element(self, row, column, value):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.data[row][column] = value

    def sum_of_rows(self):
        sums = []
        for row in self.data:
            row_sum = sum(row)
            sums.append(row_sum)
        return sums

    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
        transposed_matrix = Matrix(self.columns, self.rows)
        transposed_matrix.data = transposed_data
        return transposed_matrix

    def multiply_by(self, other):
        if self.columns != other.rows:
            return None

        result_rows = self.rows
        result_columns = other.columns
        result_matrix = Matrix(result_rows, result_columns)

        for i in range(result_rows):
            for j in range(result_columns):
                dot_product = sum(self.data[i][k] * other.data[k][j] for k in range(self.columns))
                result_matrix.data[i][j] = dot_product

        return result_matrix

    def is_symmetric(self):
        transpose_matrix = self.transpose()
        return self.data == transpose_matrix.data

    def rotate_right(self):
        self.data = self.transpose().data[::-1]

    def flatten(self):
        flattened_list = []
        for row in self.data:
            flattened_list.extend(row)
        return flattened_list

    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        columns = len(list_of_lists[0])
        matrix = Matrix(rows, columns)
        matrix.data = list_of_lists
        return matrix

    def diagonal(self):
        if self.rows != self.columns:
            return None

        return [self.data[i][i] for i in range(self.rows)]

# Примеры использования и вывод результатов для класса Matrix

# Создание матрицы 3x3 и добавление элементов
matrix1 = Matrix(3, 3)
matrix1.add_element(0, 0, 1)
matrix1.add_element(0, 1, 2)
matrix1.add_element(0, 2, 3)
matrix1.add_element(1, 0, 4)
matrix1.add_element(1, 1, 5)
matrix1.add_element(1, 2, 6)
matrix1.add_element(2, 0, 7)
matrix1.add_element(2, 1, 8)
matrix1.add_element(2, 2, 9)
print(f"Matrix1 data: {matrix1.data}")

# Сумма строк матрицы
print(f"Sum of rows: {matrix1.sum_of_rows()}")

# Транспонирование матрицы
transposed_matrix1 = matrix1.transpose()
print(f"Transposed matrix data: {transposed_matrix1.data}")

# Умножение матриц
matrix2 = Matrix(3, 2)
matrix2.add_element(0, 0, 1)
matrix2.add_element(0, 1, 2)
matrix2.add_element(1, 0, 3)
matrix2.add_element(1, 1, 4)
matrix2.add_element(2, 0, 5)
matrix2.add_element(2, 1, 6)
print(f"Matrix2 data: {matrix2.data}")

result_matrix = matrix1.multiply_by(matrix2)
print(f"Result of multiplication: {result_matrix.data if result_matrix else 'None'}")

# Проверка на симметричность
matrix3 = Matrix.from_list([[1, 2, 3], [2, 1, 4], [3, 4, 1]])
print(f"Matrix3 is symmetric: {matrix3.is_symmetric()}")

# Поворот матрицы вправо
matrix4 = Matrix.from_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix4.rotate_right()
print(f"Matrix4 rotated right: {matrix4.data}")

# Преобразование матрицы в одномерный список
flattened_matrix1 = matrix1.flatten()
print(f"Flattened matrix1: {flattened_matrix1}")

# Создание матрицы из списка списков
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix5 = Matrix.from_list(list_of_lists)
print(f"Matrix5 from list: {matrix5.data}")

# Получение диагонали матрицы
diagonal_matrix5 = matrix5.diagonal()
print(f"Diagonal of matrix5: {diagonal_matrix5}")

```
___
Результати:
```Python
Matrix1 data: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Sum of rows: [6, 15, 24]
Transposed matrix data: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
Matrix2 data: [[1, 2], [3, 4], [5, 6]]
Result of multiplication: [[22, 28], [49, 64], [76, 100]]
Matrix3 is symmetric: True
Matrix4 rotated right: [[3, 6, 9], [2, 5, 8], [1, 4, 7]]
Flattened matrix1: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Matrix5 from list: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Diagonal of matrix5: [1, 5, 9]
```
___
Висновки: Ці приклади демонструють використання класу Matrix. Кожен блок коду створює матрицю, виконує різні операції та друкує результати цих операцій.
___