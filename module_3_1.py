calls = 0
# Создаём функцию count_calls и изменять в ней значение переменной calls.
def count_calls ():
    global calls
    calls+=1
    #Создать функцию count_calls и изменять в ней значение переменной calls.
    # Эта функция должна вызываться в остальных двух функциях.
    #Метод string.lower() в Python преобразует все символы верхнего регистра в строке в символы нижнего регистра
    #len() в Python — это встроенная функция, которая принимает объект в качестве аргумента и возвращает его длину
def  string_info (string ):
    count_calls()
    return (len(string), string.upper(), string.lower())


# Создаём функцию is_contains с двумя параметрами string и list_to_search
#string.upper - преобразует все символы нижнего регистра в строке в символы верхнего регистра
#Return — это ключевое слово в программировании, которое используется
#в функциях для предоставления результата выполнения этой функции или завершения её работы
def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]


# Вывод результата
print(string_info('Капибара'))
print(string_info('Армагеддон'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic']))  # No matches
print(calls)