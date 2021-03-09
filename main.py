message = print("""
Regra do negócio
1 - Números múltiplos de 3: fizz
2 - Números múltiplos de 5: buzz
3 - Números múltiplos de 3 e 5: fizzbuzz
4 - Qualquer valor não múltiplo apresenta o númmero
""")
import sys
from functools import partial

multiple_of = lambda base, num: num % base == 0
multiple_of_three = partial(multiple_of, 3)  # verifica se o numero é multiplo de 3
multiple_of_five = partial(multiple_of, 5)  # verifica se o numero é multiplo de 5


def robot(pos):
    say = str(pos)

    if multiple_of_three(pos) and multiple_of_five(pos):
        say = 'FizzBuzz'
    elif multiple_of_three(pos):
        say = 'Fizz'
    elif multiple_of_five(pos):
        say = 'Buzz'

    return say


if __name__ == '__main__':
    print(message)
    var = int(input("Enter a value: "))
    print(robot(var))
