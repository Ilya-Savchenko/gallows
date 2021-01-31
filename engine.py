import random


str_letter = list()


class Gallows:
	health: int = 7  # Количество ошибок
	russian_alphabet: tuple = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

	def __init__(self):
		self.word = self.wordgenerator()
		self.used_letters = []

	def wordgenerator(self):  # Генерирует слово из файла
		with open('WordsStockRus.txt', encoding="utf-8") as ws:
			words = ws.read().split('\n')
			word = words[random.randint(0, len(words) - 1)]
		return word

	def symbols_instead_words(self):  # Выводим символы вместо слова
		underline = '*' * len(self.word)
		return underline

	def get_used_letters(self, letter: str):  # Использованные буквы
		if self.search_letter_in_alphabet(letter):
			self.used_letters.append(letter)
			set_letter = set(self.used_letters)
			return set_letter

	def search_letter_in_alphabet(self, letter: str):  # Поиск введенной буквы в алфавите
		letter = letter.lower()
		if letter in self.russian_alphabet:
			return True
		return False

	def search_letter_in_word(self, letter):  # Поиск буквы в загаданном слове
		mass = list()
		letter = letter.lower()
		for let in range(len(self.word)):
			if self.word[let] == letter:
				mass.append(len(self.word[0:let]) + 1)
		return mass

	def stars_list(self, string):  # Преобразование строки со звездами с список для добавленния элементов
		letter_index_list = list()
		for elem in string:
			letter_index_list.append(elem)
		return letter_index_list

	def lack_of_letter_in_word(self, letter):  # Проверяет отсутстывие буквы в слове
		if letter not in self.word:
			return True
		return False
