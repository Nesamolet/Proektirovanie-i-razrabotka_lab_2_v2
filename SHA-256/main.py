import hashlib
import multiprocessing
import os
import string
import threading
import time

class ExitRecursion(Exception):
    pass

def calculate_hash(password):
    # Создаем объект хэша SHA-256


    sha256_hash = hashlib.sha256()

    # Кодируем пароль в байты (UTF-8) и обновляем хэш
    sha256_hash.update(password.encode('utf-8'))

    # Получаем и возвращаем шестнадцатеричное представление хэша
    return sha256_hash.hexdigest()

def generate_nested_loops(depth, alphabet, number_letter, SHA_256 , current_combination=None) :

        global stop
        process_id = os.getpid()
        print(f"Идентификатор процесса внутри функции: {process_id}")
        print("stop = " , stop)
        if stop == 0:
            print(current_combination)
            if current_combination is None:
                current_combination = []
            if depth == 0:
                # Базовый случай: достигнута максимальная глубина
                if calculate_hash("".join(current_combination)) == SHA_256:
                    print("".join(current_combination))
                    stop = 1
                    end_time = time.time()
                    execution_time = end_time - start_time
                    print(f"Пароль подобран за {execution_time} секунд.")

                    d = input('Если Вы хотите закончить ввод введите "0" : ')


                    raise ExitRecursion


                else:

                    return
            else:

                if len(current_combination) == 0:
                    a = alphabet[number_letter]
                    pass

                # Рекурсивно создаем вложенные циклы
                for a in range(len(alphabet)):
                    generate_nested_loops(depth - 1, alphabet, 0, SHA_256, current_combination + list(alphabet[a]))







# Пример использования
start_time = time.time()
alphabet = string.ascii_lowercase + "".join(list(map(str, range(0, 10))))

global stop
stop = 0

threads = []
num_threads = int(input("Введите количество потоков : "))
letters = 4

def split_and_return_first(lst, n):
    # Проверяем, что длина списка делится нацело на N


    # Разбиваем список на N частей
    splitted_list = [lst[i:i + len(lst)//n] for i in range(0, len(lst), len(lst)//n)]

    # Возвращаем номера первых элементов каждой части
    return [part[0] for part in splitted_list]

# Пример использования

result = split_and_return_first(alphabet, num_threads)

d = 0
while d == 0:


    SHA = input("Введите hash пароля : ")
    start_time = time.time()
    for i in range(num_threads):

        process = multiprocessing.Process(target=generate_nested_loops(letters, alphabet, [i for i, char in enumerate(alphabet) if char == result[1]][i], SHA))
        threads.append(process)

        process.start()
        stop = stop + 1

        if i == 1:
            d = input()



