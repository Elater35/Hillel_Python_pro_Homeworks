# ДЗ 3.1. Робота з типами даних


def length_of_string(str_of_user: str) -> int:
    """1.1. Рядки (Strings): функція, яка приймає рядок і повертає його довжину."""
    return len(str_of_user)

print(f"\nThis is the length of our string: {length_of_string("This is a test")} characters.")

def concatenation_of_two_strings(str_of_user_1: str, str_of_user_2: str) -> str:
    """1.2. Рядки (Strings): функція, яка приймає два рядки і повертає об'єднаний рядок."""
    return str_of_user_1 + str_of_user_2

print(concatenation_of_two_strings("Conan Doyle is the father",
                                   " of Sherlock Holmes.\n"))


def square_of_number(number: int | float) -> int | float:
    """2.1. Числа (Int/float): функція, яка приймає число і повертає його квадрат."""
    return number * number  # or number ** 2

print(f"This is the square of our number: {square_of_number(25)}.")

def sum_of_two_numbers(number_1: int | float, number_2: int | float) -> int | float:
    """2.2. Числа (Int/float): функція, яка приймає два числа і повертає їхню суму."""
    return number_1 + number_2

print(f"This is the sum of our numbers: {sum_of_two_numbers(13, 24.8)}.")

def integer_division_and_remainder(number_1: int, number_2: int) -> tuple[int, int]:
    """2.3. Числа (Int/float): функція, яка приймає 2 числа типу int, виконує операцію
    ділення та повертає цілу частину і залишок.
    """
    return divmod(number_1, number_2)  # or return number_1 // number_2, number_1 % number_2

print(f"This is the quotient: {integer_division_and_remainder(26, 5)[0]} "
      f"and the remainder: {integer_division_and_remainder(26, 5)[1]}.\n")


def average_of_list_of_numbers(lst_of_numbers: list[int | float]) -> float:
    """3.1. Списки (Lists): функція обчислення середнього значення списку чисел."""
    return sum(lst_of_numbers) / len(lst_of_numbers)

print(f"This is the average of our list of the numbers: "
      f"{average_of_list_of_numbers([35.5, 87, 112.56, 17])}.")

def intersection_of_two_lists(list_1: list, list_2: list) -> list:
    """3.2. Списки (Lists): функція, яка приймає два списки і повертає список,
    який містить спільні елементи обох списків.
    """
    intersection_list = []
    for item in list_1:
        if item in list_2:
            intersection_list.append(item)
    # або ліпше через генератор списків:
    # intersection_list = [item for item in list_1 if item in list_2]
    return intersection_list

print(f"This is the intersection of our two lists: "
      f"{intersection_of_two_lists([35.5, 87, 112.56, 17], [35.5, 187, 12.56, 17])}.\n")


def dictionary_keys(my_dict):
    """4.1. Словники (Dictionaries): функція, яка приймає словник
    і виводить всі ключі цього словника.
    """
    return my_dict.keys()

print(f"This is the keys of our dictionary: "
      f"{list(dictionary_keys({"apple": 35, "kiwi": 9, "plum": 27, "cherry": 30}))}.")

def merging_dictionaries(dict_1: dict, dict_2: dict) -> dict:
    """4.2. Словники (Dictionaries): функція, яка приймає два словники
    і повертає новий словник, який є об'єднанням обох словників.
    """
    merging_list = list(dict_1.items())
    dict_1_list = list(dict_1.items())
    dict_2_list = list(dict_2.items())
    for item in dict_2_list:
        if item not in dict_1_list:
            merging_list.append(item)
    return dict(merging_list)  # return dict_1 | dict_2 замінює весь цей блок

print(f"This is the merging of our dictionaries: "
      f"{merging_dictionaries({"apple": 35, "kiwi": 9, "plum": 27, "cherry": 30},
                              {"apple": 45, "peach": 9, "plum": 27, "melon": 30})}.\n")


def merging_sets(set_1: set, set_2: set) -> set:
    """5.1. Множини (Sets): функція, яка приймає дві множини і повертає їхнє об'єднання."""
    merging_set = set_1
    for item in set_2:
        if item not in set_1:  # можна без цієї умови, бо добавляться лише унікальні елементи
            merging_set.add(item)
    return merging_set  # return set_1 | set_2 замінює весь цей блок

print(f"This is the merging of our sets: "
      f"{merging_sets({"apple", 35, "kiwi", 9, "plum", 27, "cherry", 30}, 
                      {"apple", 45, "peach", 9, "plum", 27, "melon", 30})}.")

def subset_or_not(set_1: set, set_2: set) -> bool:
    """5.2. Множини (Sets): функція, яка перевіряє, чи є одна множина підмножиною іншої."""
    for item in set_2:
        if item not in set_1:
            return False
    return True  # return set_2 <= set_1 замінює весь цей блок

print(f"Is the set_2 subset of the set_1? "
      f"{subset_or_not({"apple", 35, "kiwi", 9, "plum", 27, "cherry", 30}, 
                       {"apple", 9, "plum", 27, 30})}.\n")


def even_or_odd(number: int) -> str:
    """6.1. Умовні вирази та цикли: функція, яка приймає число
    і виводить "Парне", якщо число парне,
    і "Непарне", якщо непарне.
    """
    return "Even" if number % 2 == 0 else "Odd"

print(f"The number 5 is {even_or_odd(5)}, 18 is {even_or_odd(18)} and 0 is {even_or_odd(0)}.")

def list_of_even(list_of_numbers: list[int]) -> list[int]:
    """6.2. Умовні вирази та цикли: функція, яка приймає список чисел
    і повертає новий список, що містить тільки парні числа.
    """
    list_of_even_numbers = []
    for item in list_of_numbers:
        if item % 2 == 0:
            list_of_even_numbers.append(item)
    return list_of_even_numbers
    # return [item for item in list_of_numbers if item % 2 == 0] замість всього блоку

print(f"Only even numbers of our list of numbers: "
      f"{list_of_even([35, 88, 112, 17, 88, 187, 12, 17])}.\n")


# 7. Лямбда-функція, яка визначає парне/непарне.
#    Функція приймає параметр (число) і, якщо парне, видає слово “парне”, якщо ні, то “непарне”.
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"

print(f"The number 5 is {even_or_odd(5)}, 18 is {even_or_odd(18)} and 0 is {even_or_odd(0)}.")
