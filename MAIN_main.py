import hashlib
import string
import threading
import time

class ExitRecursion(Exception):
    pass

def calculate_hash(password):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode('utf-8'))
    return sha256_hash.hexdigest()

def generate_nested_loops(letter, depth, alphabet, SHA_256, current_combination=None):
    if current_combination is None:
        current_combination = []

    global stop
    if stop != 0:
        raise SystemExit
    else:
        if depth == 0:
            # Базовый случай: достигнута максимальная глубина
            if calculate_hash("".join(current_combination)) == SHA_256:
                print("Пароль найден:", "".join(current_combination))
                stop = 1
                raise SystemExit
            else:
                return
        else:
            # Рекурсивно создаем вложенные циклы
            for a in range(len(alphabet)):

                if len(current_combination) == 0 and alphabet[a] < str(letter):
                    continue  # Пропускаем буквы до 'h' на первом месте

                generate_nested_loops("a", depth - 1, alphabet, SHA_256, current_combination + list(alphabet[a]))

# Пример использования
start_time = time.time()
alphabet = string.ascii_lowercase + "".join(list(map(str, range(0, 10))))
letters = 4
SHA = "5f2d5d6090830b8e3398d2bfb586d64a01aff9c45cc4c147c8c10fc176384ff8"

#количество потоков
count = 4

def split_and_return_first(lst, n):
    # Проверяем, что длина списка делится нацело на N

    # Разбиваем список на N частей
    splitted_list = [lst[i:i + len(lst)//n] for i in range(0, len(lst), len(lst)//n)]

    # Возвращаем номера первых элементов каждой части
    return [part[0] for part in splitted_list]

# Пример использования

result = split_and_return_first(alphabet, 4)

global stop
stop = 0
threads = []
print(result)
try:
    for i in range(len(result)):
        letter = result[i]
        exit_flag = threading.Event()
        thread = threading.Thread(target=generate_nested_loops, args=(letter, letters, alphabet, SHA))
        threads.append(thread)
        thread.start()
except ExitRecursion:
    pass

for i in range(len(threads)):
    threads[i].join()

end_time = time.time()
execution_time = end_time - start_time
print(f"Пароль найден за {execution_time} секунд.")
