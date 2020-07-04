# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()),
# деление (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух
# клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше
# нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
# метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет
# строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет
# строку: *****\n*****\n*****.

class Cells:
    def __init__(self, num_cells):
        self.num_cells = num_cells

    def __add__(self, other):
        return Cells(self.num_cells + other.num_cells)

    def __sub__(self, other):
        result = self.num_cells - other.num_cells
        if result < 0:
            print("Меньше нуля!!!")
        else:
            return result

    def __mul__(self, other):
        return Cells(round(self.num_cells * other.num_cells))

    def __truediv__(self, other):
        return Cells(round(self.num_cells / other.num_cells))

    def __str__(self):
        return f"{self.num_cells}"

    def make_order(self, n):
        my_list = []
        for i in range(1, self.num_cells + 1):
            my_list.append("*")
            if i % n == 0:
                my_list.append("\n")
        my_list = "".join(my_list)
        return my_list


my_cells_1 = Cells(57)
my_cells_2 = Cells(13)
print(my_cells_1 * my_cells_2)
print(my_cells_1.make_order(12))
