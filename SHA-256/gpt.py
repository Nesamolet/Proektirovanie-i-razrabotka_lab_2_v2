import threading
import itertools
import string

# Задайте исходное слово
target_word = "emp23"

# Задайте длину слова N
N = len(target_word)

# Создайте генератор слов из букв английского алфавита и цифр
alphabet_and_digits = string.ascii_letters + string.digits
word_generator = itertools.product(alphabet_and_digits, repeat=N)

# Флаг для сигнала о завершении
found_flag = threading.Event()

# Функция для генерации слов и проверки на совпадение с исходным словом
def generate_words():
    global found_flag
    for word_tuple in word_generator:
        generated_word = ''.join(word_tuple)
        if generated_word == target_word:
            found_flag.set()
            print(f"Слово найдено: {generated_word}")
            break

# Запустите несколько потоков
num_threads = 10
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=generate_words)
    thread.start()
    threads.append(thread)

# Ждем, пока хотя бы один поток не найдет исходное слово
found_flag.wait()

# Завершаем все потоки
for thread in threads:
    thread.join()

print("Работа всех потоков завершена.")
