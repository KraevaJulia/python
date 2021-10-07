#Задание 1
'''
 Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. 
 Об окончании ввода данных свидетельствует пустая строка.
'''
print('Задание 1')
my_f = open('my_f1.txt', 'w')
line = input('Введите данные \n')
while True:
	my_f.writelines(line) #writelines - запись построчно
	line = input('Введите данные \n')
	if not line:
		break

my_f.close()
my_f = open('my_f1.txt', 'r')
content = my_f.readlines() #Просматриваем получившийся файл
print(content)
my_f.close()

#Задание 2
'''
 Создать текстовый файл (не программно), сохранить в нем несколько строк, 
 выполнить подсчет количества строк, количества слов в каждой строке.
'''
print('Задание 2')
my_f2 = open('text2.txt', 'r')
content = my_f2.read()
print(f'Записано в файле: \n{content}')
my_f2.close()

my_f2 = open('text2.txt', 'r')
content = my_f2.readlines()
l = len(content)
print(f'Строк в файле: {l}')
my_f2.close()

my_f2 = open('text2.txt', 'r')
for line in my_f2:
	word = 0
	content = line.split(' ')
	word += len(content)
	print(f'Слов в строке: {word}')	
my_f2.close()



#Задание 3
'''
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
'''
print('Задание 3')
with open('text3.txt', 'r') as f_obj:
	name = []
	salary = []
	my_list = f_obj.read().split('\n') 
	for line in my_list:
		line = line.split(' ')
		if int(line[1]) < 20000:
			name.append(line[0])
		salary.append(line[1])
a = sum(map(int, salary)) #map - преобразуем исходный элемент в новый. 
a = a/len(salary) #Средняя величина: Сумма всех окладов к количеству людей.
print(f'Оклад меньше 20.000:\n{name}')
print(f'Средняя величина дохода всех сотрудников: {a}')

#Задание 4
'''
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. 
Новый блок строк должен записываться в новый текстовый файл.
'''
print('Задание 4')
my_dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
new_f = []
with open('text4.txt', 'r') as f_obj4:
	for line in f_obj4:
		line = line.split(' ', 1)
		new_f.append(my_dict[line[0]] + '  ' + line[1])

new_f4 = open('my_f4.txt', 'w') #Записываем в файл
new_f4.writelines(new_f)
new_f4.close()

new_f4 = open('my_f4.txt', 'r') #Читаем файл
content = new_f4.read()
print(content)
new_f4.close()

#Задание 5
'''
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
print('Задание 5')
def my_sum():
	with open('my_f5.txt', 'w+') as f_obj5:
		n = input('Вводите числа через пробел \n')
		f_obj5.writelines(n)
		c = n.split(' ')
		c_sum = sum(map(float, c))
		print(f'Сумма чисел в файле: {c_sum:.3f}')

my_sum()

#Задание 6
'''
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран.
'''
print('Задание 6')
def my_calc(file_path):
	result = {}
	try:
		with open(file_path, 'r') as f_obj6:
			for line in f_obj6:
				subject, hours = line.split(':')
				hours_sum = sum(
					int(s) for i in hours.split() for s in i.split('(') if s.isdigit()
				)
				result[subject] = hours_sum
	except IOError as e:
		print(e)
	except ValueError:
		print('Неправильные данные')
	return result
	
my_hours = my_calc('text6.txt')
print(my_hours)

#Задание 7
'''
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
'''
print('Задание 7')
import json
profit = {}
pr = {}
prof = 0
s_prof = 0
i = 0
with open('text7.txt', 'r') as f_obj7:
	for line in f_obj7:
		name, firm, d, e = line.split(' ')
		profit[name] = int(d) - int(e) #Прибыль/убыток
		if profit.setdefault(name) > 0: #Фирма работает с прибылью? (выручка минус издержки - больше 0)
			prof += profit.setdefault(name)
			i += 1
	if i != 0: #Если кол-во фирм работающих с прибылью не ноль, то
		s_prof = prof/i #Средняя прибыль
		print(f'Средняя прибыль - {s_prof:.3f}')
	else:
		print(f'Все фирмы работают в убыток')
	pr = {'Средняя прибыль': round(s_prof)}
	profit.update(pr)
	print(f'Прибыль каждой компании - {profit}')
	
with open('my_f7.json', 'w') as my_obj7:
	json.dump(profit, my_obj7)
	js_str = json.dumps(profit)
	print(f'Файл с расширением json: \n{js_str}')

g = input('Нажмите чтобы закрыть') 