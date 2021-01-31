# import game
import string

from engine import Gallows

print("""Компьютер генерирует слово, а человек побуквенно пытается угадать, что за слово было загадано.
Количество попыток назвать букву ограничено, оно равно 7.
Если игрок открыл всё слово, то он победил.""")

input('press Enter to start')
game = Gallows()

stars = game.symbols_instead_words()  # Вывод звездочек вместо слова
print(stars)
letters_used = []
while game.health > 0:  # Пока кол-во жизней больше 0
	print(f'Attempts Left {game.health}')  # Выводим кол-во жизней

	players_letter = input('Enter your RUSSIAN letter: ')
	if game.search_letter_in_alphabet(players_letter) is True and players_letter != '':
		if players_letter not in letters_used:
			letters_used = game.get_used_letters(players_letter)
			index_letters_in_word = game.search_letter_in_word(players_letter)  # Позиции букв в слове
			letters_index_list = game.stars_list(stars)

			for elem in letters_index_list:
				if elem == ' ':
					letters_index_list.remove(elem)

			for elem in index_letters_in_word:
				letters_index_list[elem - 1] = players_letter

			letters_index_str = str(letters_index_list) \
				.replace(',', '').replace(' ', '').replace("'", "").replace('[', '').replace(']', '').lower()
			print(letters_index_str)
			stars = letters_index_str
			letters_index_str = str(letters_index_str)

			if game.lack_of_letter_in_word(players_letter) is True:
				game.health -= 1

			if game.health == 0:
				print('You Lose!')
				print(f'Hidden word - {game.word}')

				break

			if game.health > 0 and letters_index_str == game.word:
				print('You win!')
				break
			print(f'You used letters {str(letters_used).lower()}')
		else:
			print('You have already used this letter')
			continue
	elif players_letter == '' or players_letter in string.punctuation:
		print('Enter a letter')
		continue
	else:
		print('Enter a RUSSIAN letter')
		continue
input('Press enter to exit')
