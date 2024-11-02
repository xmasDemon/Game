import random

def guess_the_number():

    number_to_guess = random.randint(1, 10)
    attempts = 3

    print("Добро пожаловать в игру 'Угадай число'!")
    print("Я загадал число от 1 до 10. У вас есть 3 попытки, чтобы его угадать.")

    for attempt in range(1, attempts + 1):
        try:

            user_guess = int(input(f"Попытка {attempt}: Введите ваше число: "))


            if user_guess < 1 or user_guess > 10:
                print("Пожалуйста, введите число в диапазоне от 1 до 10.")
                continue

            if user_guess == number_to_guess:
                print(f"Поздравляем! Вы угадали число {number_to_guess} за {attempt} попыток!")
                break
            else:
                print("Неправильно. Попробуйте еще раз.")
        except ValueError:
            print("Это не число! Пожалуйста, введите целое число.")

    else:
        print(f"Вы проиграли. Загаданное число было {number_to_guess}.")


if __name__ == "__main__":
    guess_the_number()