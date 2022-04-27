from rich.prompt import Prompt
from rich.console import Console
from random import choice

SQUARES = {
    'cp': '✅',
    'cl': '⭕',
    'il': '❌'
}

my_file = open("a.txt", "r")
data = my_file.read()
dl = data.split("\n")
# print(dl)
my_file.close()


ag = 1

def cp(ltr):
    return f'[black on green]{ltr}[/]'


def cl(ltr):
    return f'[black on yellow]{ltr}[/]'


def il(ltr):
    return f'[black on white]{ltr}[/]'


def check_guess(guess, answer):
    guessed = []
    wordle_pattern = []
    for i, ltr in enumerate(guess):
        if answer[i] == guess[i]:
            guessed += cp(ltr)
            wordle_pattern.append(SQUARES['cp'])
        elif ltr in answer:
            guessed += cl(ltr)
            wordle_pattern.append(SQUARES['cl'])
        else:
            guessed += il(ltr)
            wordle_pattern.append(SQUARES['il'])
    return ''.join(guessed), ''.join(wordle_pattern)


def game(console, chosen_word):
    end_of_game = False
    already_guessed = []
    full_wordle_pattern = []
    all_words_guessed = []

    while not end_of_game:
        guess = Prompt.ask(g)
        while len(guess) != 5 or guess in already_guessed:
            if guess in already_guessed:
                console.print("[red]You've already guessed this word!!\n[/]")
            else:
                console.print('[red]Please enter a 5-letter word!!\n[/]')
            guess = Prompt.ask(g)
        already_guessed.append(guess)
        guessed, pattern = check_guess(guess, chosen_word)
        all_words_guessed.append(guessed)
        full_wordle_pattern.append(pattern)

        console.print(*all_words_guessed, sep="\n")
        if guess == chosen_word or len(already_guessed) == ag:
            end_of_game = True
    if len(already_guessed) == ag and guess != chosen_word:
        console.print(f"\n[red]WORDLE X/{ag}[/]")
        console.print(f'\n[green]Correct Word: {chosen_word}[/]')
    else:
        console.print(f"\n[green]WORDLE {len(already_guessed)}/{ag}[/]\n")
    console.print(*full_wordle_pattern, sep="\n")

Wwm = f'\n[green on black]               **********CODITATION**********                  [/]\n'
pi = f'\n[black on yellow] Please select the correct word so that i get selected for job 🙏  \n'
g = "\nEnter your guess"

if __name__ == '__main__':
    console = Console()
    chosen_word = choice(dl)
    console.print(Wwm)
    console.print(pi)
    # print(chosen_word)
    game(console, chosen_word)