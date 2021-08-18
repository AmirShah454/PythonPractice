# basket = ' '.join(['hi', 'my', 'name', 'is', 'amir'])
# print('Basket **************** '+ basket)
# #Dictionary
# dictionary = {
# 	'a': 'amir', 'b': 'Shah', 'c': 'bacha'
# }
# print('dictionary **************** ' + dictionary['a'])

# user = {
# 	'weapon': [1,2,3,4,5],
# 	'age': 27,
# 	'greet': 'hello'
# }
# print('user dictionary ****************  ' + user.get('first_name', 'Syed'))
# print('age' in user.keys())

# is_old = True
# is_licensed = False

# if is_old and is_licensed:
# 	print('your are old enough and has a license to drive! ')
# else:
# 	print('''Yor are not old enough or you don't have a licence''' )
# print('end of if statements')

# Ternary Operator
# is_old = False
# drive = "You can drive" if is_old else '''You can't drive'''
# print(drive + "\n")

# is_magician = True
# is_expert = False

# if is_magician and is_expert:
# 	print("You are a master magician \n")

# elif is_magician and not is_expert:
# 	print("Atleast you are getting closer \n")

# elif not is_magician and is_expert:
# 	print("You need magic powers \n")

# elif not is_magician and not is_expert:
# 	print("You are noting \n")

# user = {
# 	'name': 'Amir Shah',
# 	'age': 23,
# 	'can_swim': False
# }

# for k,v in user.items():
# 	print(k, v)

# my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# counter = 0

# for item in my_list:
# 	counter = counter + item

# print(counter)

# for numbers in range(3):
# 	print(list(range(11)))

# for i, char in enumerate(list(range(20))):
# 	print(i, char)
# 	if char == 15:
# 		print(f'index of {char} is {i}')
# i = 0
# while i < 20:
# 	print(i)
# 	i += 1

# picture = [
# 	[0,0,0,1,0,0,0],
# 	[0,0,1,1,1,0,0],
# 	[0,1,1,1,1,1,0],
# 	[1,1,1,1,1,1,1],
# 	[0,0,0,1,0,0,0],
# 	[0,0,0,1,0,0,0]
# ]

# def show_tree():
# 	for row in picture:
# 		for pixel in row:
# 			if (pixel == 1):
# 				print("*" , end='')
# 			else:
# 				print(" " , end='')
# 		print("")

# show_tree()
# 	
# some_list = ['a', 'b', 'c', 'b', 'd', 'e', 'n', 'm', 'n']
# duplicates = []

# for value in some_list:
# 	if some_list.count(value) > 1:
# 		if value not in duplicates:
# 			duplicates.append(value)

# print(duplicates)

# default parameters
# def some_fucntion(id = 1 , name = 'Rehmat'):
# 	print(f'Your id {id} and name is {name}')

# #Positional Arguments
# some_fucntion(2,'amir')

# #Keyword Arguments
# some_fucntion(id = 3, name = 'Israr') 

# some_fucntion(name='manzoor')

# Clean Code
# def is_even(num):
# 	return num % 2 == 0

# print(is_even(24))

# def super_func(*args):
# 	return sum(args)

# print(super_func(2,4,6,8,10))

# Highest Evens
# def highest_even(li):
# 	evens = []
# 	for items in li:
# 		if items % 2 == 0:
# 			evens.append(items)
# 	return max(evens)

# print(highest_even([1,16,3,11,14,2,4,6,10,12,8,7]))

# class AgricultureUniversity:
# 	def __init__(self, id, name, gpa):
# 		self.id = id
# 		self.name = name
# 		self.gpa = gpa

# 	def marks(self):
# 		print ('Marks')
# 		return 'marks'

# std1 = AgricultureUniversity(164, 'amir', 3.72)

# print(std1.name)	
# class GreenTuitionAcademy:
# 	def __init__(self, num1, num2):
# 		self.num1 = num1
# 		self.num2 = num2
# 		print("Constructor Function")
# 		add = num1 + num2
# 		print(f'Addition of {num1} and {num2} is = ', add)
# 	def quiz(self):
# 		print(f' You have got marks')

# 	@classmethod
# 	def multiply(cls, marks, rollno):
# 		pass


# obj = GreenTuitionAcademy(4,6)
# obj2 = GreenTuitionAcademy.quiz(' ')

# class Encapsulation:

# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# 	def run(self):
# 		print('This is run funtion')

# 	def speak(self):
# 		print(f"This is Speak funtion having {self.name} and {self.age} year old")

# obj = Encapsulation('amir', 23)
# obj.speak()
# class Parent():
# 	def sign_in(self):
# 		print("You are logged_In")

# class Child1(Parent):
# 	def __init__(self, name, dob):
# 		self.name = name
# 		self.dob = dob
# 	def details(self):
# 		print(f'{self.name} your date of birth is {self.dob}')

# class Child2(Parent):
# 	def __init__(self, name, dob):
# 		self.name = name
# 		self.dob = dob

# 	def details2(self):
# 		print(f'{self.name} your date of birth is {self.dob}')

# obj = Child1('asfandyar', '22-06-2000')
# obj.details()
# def multiply_by2(item):
# 	return item

# dictionary = {
# 	'name': 'amir',
# 	'DOB': '2-3-1998'
# }
# output = list(map(multiply_by2, dictionary))
# print(output)
# my_list = [1,2,3,4]
# your_list = ('a','b','c','d')
# their_list = {10, 20, 30, 40}

# output = list(zip(my_list, your_list, their_list))
# print(output)

# my_list = [1,2,3,4,5]
# your_list = {'a', 'b', 'c', 'd', 'e'}

# output = list(map(lambda item: item*2, my_list))
# print(output)

# output2 = list(filter(lambda item: item % 2 != 0,my_list))
# print(output2)

# my_list = [5,3,4]

# ot = list(map(lambda item: item**2, my_list))
# print(ot)

# #List sorting
# a = [(2,4,1), (9,6,3), (0,1,2), (9,5,8)]
# a.sort(key = lambda x: x[2])
# print(a)
# my_list = [char for char in 'hello']
# print(my_list)

# my_list2 = [num for num in range(0,20)]
# print(my_list2)

# my_list3 = [num**2 for num in range(0,20)]
# print(my_list3)

# my_list4 = [num**2 for num in range(0,20) if num % 2 == 0]
# print(my_list4)

# some_list = ['a', 'b', 'c', 'b', 'd', 'e', 'n', 'm', 'n']
# duplicates = []

# for value in some_list:
# 	if some_list.count(value) > 1:
# 		if value not in duplicates:
# 			duplicates.append(value)

# print(duplicates)

# some_list = ['a', 'b', 'c', 'b', 'd', 'e', 'n', 'm', 'n']

# duplicates = list(set([x for x in some_list if some_list.count(x) > 1]))
# print(duplicates)
# age = int(input('Please enter your age? '))
# print(age)
# import pdb
# def add(num1, num2):
#     pdb.set_trace()
#
#     return num1 + num2
#
# print(add(5,6))
# my_file = open('message.txt')
#
# print(my_file.read())
# my_file.close()

# with open('message.txt', mode = 'a') as my_file:
#     text = my_file.write('\n Welcome \n Welcome')
#     print(text)
# from translate import Translator
# translator= Translator(to_lang="ur")
# try:
#     with open('message.txt', mode='r') as my_file:
#         text = my_file.read()
#         translation_text = translator.translate(text)
#         with open('translated_text.txt', mode='w') as my_file2:
#             my_file2.write(translation_text)
# except FileNotFoundError as err:
#     print('Check your path ')

# from translate import Translator
#
# select_language = Translator(to_lang = "ur")
# text = 'My name is Syed Amir Ali Shah'
# translated_text = select_language.translate(text)
#
# print(translated_text)
# import re
# pattern = re.compile(r"[A-Za-z@%&#*0-9]{7,}\d")
# password = 'Sair@344'
#
# check = pattern.fullmatch(password)
# print(check)
