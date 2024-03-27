from faker import Faker
from colorama import init
from termcolor import cprint
from levels import levels
from user_score import UserScore


def get_popitka(word: str, level: str) -> int:
    return len(word) + levels[level]


def get_word() -> str:
    f = Faker("ru_RU")
    word = f.word().lower()
    return word


def print_intro(popitka):
    cprint(
        f"Добро пожаловать в игру угадай слово у выс есть {popitka} попыток!",
        color="blue",
    )


def get_hidden_word(word: str) -> str:
    return len(word) * "X"


def user_guess(word, hidden_word, letters):
    oshibka = False
    l = input("Введите букву: ")
    if l in letters:
        cprint("Вы уже использовали эту букву!", color="red")
        return hidden_word, letters, oshibka
    if l in word:
        cprint("Вы угадали букву!", color="green")
        for i, x in enumerate(word):
            if x == l:
                hidden_word = hidden_word[0:i] + l + hidden_word[i + 1 :]
    else:
        cprint("Вы не угадали!", color="red")
        oshibka = True
    letters.append(l)
    return hidden_word, letters, oshibka


if __name__ == "__main__":
    init(autoreset=True)
    score=UserScore(lose=0,win=0)
    cprint("Сколько вы хотите сыграть игр?", color="yellow")
    games = int(input())
    for i in range(games):
        word = get_word()
        cprint("Введите уровень сложности: легкий, средний, сложный!", color="yellow")
        level = input()
        popitka = get_popitka(word, level)
        print_intro(popitka)
        hidden_word = get_hidden_word(word)
        # print(word)
        letters = []
        while True:
            hidden_word, letters, oshibka = user_guess(word, hidden_word, letters)
            cprint(f"Текущее слово = {hidden_word}", color="yellow")
            if oshibka == True:
                popitka -= 1
                cprint(f"Теперь у вас  осталось {popitka} попыток", color="magenta")
            if popitka == 0:
                cprint(f"Вы проиграли ваше слово было {word}!!!!", color="red")
                score.lose+=1
                break
            if hidden_word == word:
                cprint("Вы победили!", color="light_green")
                score.win+=1
                break
        cprint(f"Вы закончили игру ваши победы {score.win} и ваши поражения {score.lose}")