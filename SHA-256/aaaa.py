from concurrent.futures import ThreadPoolExecutor

def factorial(n, m):
    if n == 0 or n == 1:
        return 1
    else:
        print("подсчет - ", m, "faf - ", n)
        return n * factorial(n - 1, m)

# Пример использования

with ThreadPoolExecutor() as executor:
    future1 = executor.submit(factorial, 5, 5)
    future2 = executor.submit(factorial, 6, 6)
