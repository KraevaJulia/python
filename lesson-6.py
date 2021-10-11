#Задание 1
'''
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
Продолжительность первого состояния (красный) составляет 7 секунд, 
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
Проверить работу примера, создав экземпляр и вызвав описанный метод.
'''
print('Задание 1')
from time import sleep #time.sleep() - позволяет отсрочить выполнение вызываемого потока на указанное количество секунд.

class TrafficLight:
	__color = ['Красный', 'Желтый', 'Зеленый'] #__color - приватный атрибут
	def running(self):
		k = 0
		while k < 3:
			print(f'Режим светофора: {TrafficLight.__color[k]}')
			if k == 0:
				sleep(7)
			elif k == 1:
				sleep(2)
			elif k == 2:
				sleep(4)
			k += 1

TrafficLight = TrafficLight()
TrafficLight.running()

#Задание 2
'''
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
Значения данных атрибутов должны передаваться при создании экземпляра класса. 
Атрибуты сделать защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, 
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
'''
print('Задание 2')
class Road:
	def __init__(self, _length, _width):
		if (_length <= 0) or (_width <= 0):
			raise ValueError('Длина и ширина дороги должна быть положительной', _length, _width)
		self._length = _length #_length - защищенный атрибут
		self._width = _width
		
	def calc_mass(self, c, l): #c - масса асфальта для покрытия 1 кв метра, l - толщина полотна
		if (c <= 0) or (l <= 0):
			raise ValueError('Длина и ширина дороги должна быть положительной', c, l)
		return self._length * self._width * c * l
	

a = Road(20, 5000)
result = a.calc_mass(25, 5)
print(f'Масса асфальта, необходимая для покрытия всего дорожного полотна: {result} кг')

#Задание 3
'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). 
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: 
оклад и премия, например, {"wage": wage, "bonus": bonus}. 
Создать класс Position (должность) на базе класса Worker. 
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''
print('Задание 3')
class Worker:
	def __init__(self, name, surname, position, wage, bonus):
		self.name = name
		self.surname = surname
		self.position = position
		self._income = {"wage": wage, "bonus": bonus} # _income - защищенный атрибут, ссылающийся на словарь
	
class Position(Worker): # дочерний класс от класса Worker
	def __init__(self, name, surname, position, wage, bonus):
		super().__init__(name, surname, position, wage, bonus)
	def get_full_name(self):
		return self.name + ' ' + self.surname
	def get_total_income(self):
		return sum(self._income.values()) #возвращаем сумму всех значений словаря _income
	
b = Position('Julia', 'Kraeva', 'Bookkeeper', 20000, 5000)
print(f'Полное имя: {b.get_full_name()}')
print(f'Должность: {b.position}')
print(f'Доход: {b.get_total_income()}')	

#Задание 4
'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
Для классов TownCar и WorkCar переопределите метод show_speed. 
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. 
Выполните доступ к атрибутам, выведите результат. 
Выполните вызов методов и также покажите результат.
'''
print('Задание 4')
class Car:
	def __init__(self, speed, color, name, is_police):
		self.speed = speed
		self.color = color
		self.name = name
		self.is_police = is_police
	
	def go(self):
		if self.speed > 0:
			return f'Текущая скорость {self.name} {self.speed} - машина уже движется!'
		else:
			print('Машина сейчас стоит. Введите скорость машины: ')
			self.speed = int(input())
			return f'{self.name} поехал со скоростью - {self.speed}!'
	def stop(self):
		if self.speed == 0:
			return f'Текущая скорость {self.name} {self.speed} - машина уже стоит!'
		else:
			self.speed = 0
			return self.name + ' остановился!'
	def turn_right(self):
		if self.speed == 0:
			return f'Текущая скорость {self.name} {self.speed} - машина не может повернуть направо!'
		else:
			return self.name + ' повернул направо!'
	def turn_left(self):
		if self.speed == 0:
			return f'Текущая скорость {self.name} {self.speed} - машина не может повернуть налево!'
		else:
			return self.name + ' повернул налево!'
	def show_speed(self):
		return f'Текущая скорость {self.name} {self.speed}!'
	def police(self):
		if self.is_police:
			return self.name + ' полицейская машина!'
		else:
			return self.name + ' не является полицейской машиной!'
	
	
class TownCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)
	def show_speed(self):
		if self.speed == 0:
			return f'Текущая скорость {self.name} {self.speed} - машина стоит!'
		elif self.speed > 60:
			return f'Текущая скорость {self.name} {self.speed} - превышение скорости!'
		else:
			return f'Текущая скорость {self.name} {self.speed} - нормальная скорость!'
			
class SportCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)

class WorkCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)
	def show_speed(self):
		if self.speed == 0:
			return f'Текущая скорость {self.name} {self.speed} - машина стоит!'
		elif self.speed > 40:
			return f'Текущая скорость {self.name} {self.speed} - превышение скорости!'
		else:
			return f'Текущая скорость {self.name} {self.speed} - нормальная скорость!'
			
class PoliceCar(Car):
	def __init__(self, speed, color, name, is_police):
		super().__init__(speed, color, name, is_police)
		


kia = TownCar(0, 'Черный', 'Kia', False)
nissan = SportCar(140, 'Желтый', 'Nissan', False)
skoda = WorkCar(50, 'Синий', 'Skoda', True)
ford = PoliceCar(80, 'Белый',  'Ford', True)

print(kia.go())
print(kia.show_speed())
print()

print(f'{nissan.name} {nissan.color}')
print(nissan.turn_right())
print(nissan.police())
print()

print(skoda.show_speed())
print(skoda.turn_left())
print(skoda.stop())
print(skoda.show_speed())
print(skoda.turn_left())
print()

print(ford.go())
print(ford.police())
print(f'{ford.name} является полицейской машиной? - {ford.is_police}')
print()


#Задание 5
'''
Реализовать класс Stationery (канцелярская принадлежность). 
Определить в нем атрибут title (название) и метод draw (отрисовка). 
Метод выводит сообщение “Запуск отрисовки.” 
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
В каждом из классов реализовать переопределение метода draw. 
Для каждого из классов методы должен выводить уникальное сообщение. 
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''
print('Задание 5')
class Stationery:
	title = 'Stationery'
	def draw(self):
		print('Запуск отрисовки')

		
class Pen(Stationery):
	title = 'Ручка'
	def draw(self):
		print(f'Вы взяли {self.title}. Рисуем ручкой!')
class Pencil(Stationery):
	title = 'Карандаш'
	def draw(self):
		print(f'Вы взяли {self.title}. Рисуем карандашом!')
class Handle(Stationery):
	title = 'Маркер'
	def draw(self):
		print(f'Вы взяли {self.title}. Рисуем маркером!')		
		
pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()


g = input('Нажмите чтобы закрыть') 