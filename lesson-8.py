#Задание 1
'''
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
В рамках класса реализовать два метода. Первый, с декоратором @classmethod. 
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». 
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). 
Проверить работу полученной структуры на реальных данных.

'''
print('Задание 1')
class Data:
    def __init__(self, date_string):
        self.date_string = str(date_string)

    @classmethod
    def extract(cls, date_string):
        my_date = []

        for i in date_string.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2021 >= year >= 0:
                    return f'Верная дата'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.date_string)}'


today = Data('17 - 10 - 2021')
print(today)

print(Data.valid(17, 10, 2022))
print(today.valid(17, 16, 2021))
print(Data.valid(32, 10, 2021))
print(Data.valid(17, 10, 2021))

print(Data.extract('17 - 10 - 2021'))
print(today.extract('17 - 10 - 2022'))



#Задание 2
'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. 
Проверьте его работу на данных, вводимых пользователем. 
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
'''
print('Задание 2')
class MyError(Exception):
    def __init__(self, text):
	    self.text = text
		
def my_calc(a, b):
    try:
        if b == 0:
            raise MyError('Деление на ноль!')
        print(a/b)
    except MyError as e:
        print('Деление на ноль запрещено!')

a = float(input())
b = float(input())
my_calc(a, b)


#Задание 3
'''
Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. 
Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо только числами. 
Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. 
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду «stop». 
При этом скрипт завершается, сформированный список с числами выводится на экран.

Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. 
Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента. 
Вносить его в список, только если введено число. 
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. 
При этом работа скрипта не должна завершаться.


'''
print('Задание 3')
class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f'Недопустимое значение!')
                q = input(f'Попробовать еще раз? Y/N ')

                if q == 'Y':
                    print(try_except.my_input())
                elif q == 'N':
                    return f'Вы закончили!'
                else:
                    return f'Вы закончили!'

try_except = Error(1)
print(try_except.my_input())


#Задание 4, 5, 6
'''
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. 
А также класс «Оргтехника», который будет базовым для классов-наследников. 
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). 
В базовом классе определите параметры, общие для приведённых типов. 
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

Продолжить работу над заданием. 
Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое подразделение компании. 
Для хранения данных о наименовании и количестве единиц оргтехники, 
а также других данных, можно использовать любую подходящую структуру (например, словарь).


Продолжить работу над заданием. 
Реализуйте механизм валидации вводимых пользователем данных. 
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

'''
print('Задание 4, 5, 6')
class Store:
	def __init__(self):
		self.store = {}
	def __str__(self):
		return f'{self.store}'
	def to_accept(self, el_store):
		print(f'Введите кол-во {el_store.name}, которое хотите сдать: ')
		count = int(input())
		if el_store.name in self.store:
			self.store[el_store.name] += count
		else:
			self.store[el_store.name] = count
	def to_give(self, el_store):
		print(f'Введите кол-во {el_store.name}, которое хотите взять: ')
		count = int(input())
		if (el_store.name in self.store) and (self.store[el_store.name] - count >= 0):
			self.store[el_store.name] -= count
		else:
			print('Техники на складе недостаточно!')


class Equipment:
	def __init__(self, name, price, color):
		self.price = price
		if color not in ['Черно-белый', 'Цветной']:
			raise ValueError('Неверное значение параметра')
		else:
			self.color = color
		self.name = name


class Printer(Equipment):
	def __init__(self, name, price, color):
		super().__init__(name, price, color)
	def to_print(self):
		return f'Это принтер - {self.name}'
		
class Scanner(Equipment):
	def __init__(self, name, price, color):
		super().__init__(name, price, color)
	def to_scan(self):
		return f'Это сканнер - {self.name}'
		
class Xerox(Equipment):
	def __init__(self, name, price, color):
		super().__init__(name, price, color)
	def to_copy(self):
		return f'Это ксерокс - {self.name}'

my_store = Store()
m = Printer('HP', 2000, 'Цветной')
n = Scanner('Canon', 8000, 'Черно-белый')
s = Scanner('Epson', 13000, 'Цветной')
k = Xerox('Xerox', 7500, 'Черно-белый')

my_store.to_accept(m)
my_store.to_accept(n)
my_store.to_give(s)
my_store.to_accept(s)
my_store.to_give(s)
my_store.to_accept(k)

print(m.to_print())
print(n.to_scan())
print(k.to_copy())

print()
print(my_store)


#Задание 7
'''
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». 
Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта. 
Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.

'''
print('Задание 7')
class ComplexNumber:
    def __init__(self, x, y, *args):
        self.x = x
        self.y = y
        self.z = 'x + i * y'

    def __add__(self, other):
        print(f'Сумма z1 и z2: ')
        return f'z = {self.x + other.x} + {self.y + other.y} * i'

    def __mul__(self, other):
        print(f'Умножение z1 и z2: ')
        return f'z = {self.x * other.x - self.y * other.y} + {self.x * other.y + self.y * other.x} * i' #(a1*a2 - b1*b2) + (a1*b2+b1*a2)*i

    def __str__(self):
        return f'z = {self.x} + i * {self.y}'


z_1 = ComplexNumber(2, 3)
z_2 = ComplexNumber(5, 2)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)


g = input('Нажмите чтобы закрыть') 