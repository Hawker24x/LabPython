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
