# character_creation_module/main.py

from random import randint

# Новый импорт.
# Из модуля start_game_banner, который расположен в папке graphic_arts,
# импортируем функцию run_screensaver().
from graphic_arts.start_game_banner import run_screensaver

def attack(char_name: str, char_class: str) -> str:
    """Атака героя."""


def defence(char_name: str, char_class: str) -> str:
    """Защита героя."""


def special(char_name: str, char_class: str) -> str:
    """Вид героя."""


def start_training(char_name: str, char_class: str) -> str:
    """Старт тренировки."""


def choice_char_class() -> str:
    """Выбор героя."""


print(attack.__doc__)
print(defence.__doc__)
print(special.__doc__)
print(start_training.__doc__)

if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))

main()
