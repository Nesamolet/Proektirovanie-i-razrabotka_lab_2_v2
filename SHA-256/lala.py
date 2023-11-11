import hashlib
import string
import time

class ExitRecursion(Exception):
    pass

def calculate_hash(password):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode('utf-8'))
    return sha256_hash.hexdigest()

def generate_nested_loops(depth, alphabet, exclude_starting_letter, SHA_256, current_combination=None):
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
            # Исключаем символы, начинающиеся с заданной буквы
            if alphabet[a] >= exclude_starting_letter:
                generate_nested_loops(depth - 1, alphabet, exclude_starting_letter, SHA_256, current_combination + [alphabet[a]])

# Пример использования
start_time = time.time()
# Алфавит, включающий буквы и цифры
alphabet = string.ascii_lowercase + "".join(list(map(str, range(0, 10))))
letters = 4
SHA = "7d4f2b7830aa1fc028065ffb2349cbadd427ddd21b844b204a0e9ed53690aeb0"
starting_letter_to_exclude = 'h'

try:
    generate_nested_loops(letters, alphabet, starting_letter_to_exclude, SHA)
except ExitRecursion:
    pass

end_time = time.time()
execution_time = end_time - start_time
print(f"Пароль найден за {execution_time} секунд.")
