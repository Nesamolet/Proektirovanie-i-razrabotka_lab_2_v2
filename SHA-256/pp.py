import hashlib
import string
import time

class ExitRecursion(Exception):
    pass

def calculate_hash(password):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode('utf-8'))
    return sha256_hash.hexdigest()

def generate_nested_loops(depth, alphabet, SHA_256, current_combination=None):
    if current_combination is None:
        current_combination = []

    if depth == 0:
        # Базовый случай: достигнута максимальная глубина
        if calculate_hash("".join(current_combination)) == SHA_256:
            print("Пароль найден:", "".join(current_combination))
            raise ExitRecursion
        else:
            return
    else:
        # Рекурсивно создаем вложенные циклы
        for a in range(len(alphabet)):
            generate_nested_loops(depth - 1, alphabet, SHA_256, current_combination + list(alphabet[a]))

# Пример использования
start_time = time.time()
alphabet = string.ascii_lowercase + "".join(list(map(str, range(0, 10))))
letters = 4
SHA = "7d4f2b7830aa1fc028065ffb2349cbadd427ddd21b844b204a0e9ed53690aeb0"

try:
    generate_nested_loops(letters, alphabet, SHA)
except ExitRecursion:
    pass

end_time = time.time()
execution_time = end_time - start_time

num_threads = 4

print(f"Пароль найден за {execution_time} секунд.")

def split_and_return_first(lst, n):
    # Проверяем, что длина списка делится нацело на N


    # Разбиваем список на N частей
    splitted_list = [lst[i:i + len(lst)//n] for i in range(0, len(lst), len(lst)//n)]

    # Возвращаем номера первых элементов каждой части
    return [part[0] for part in splitted_list]

# Пример использования

result = split_and_return_first(alphabet, num_threads)

print(result)

