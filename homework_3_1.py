"""ДЗ 3.1. Робота з типами даних."""


def length_of_string(user_str: str) -> int:
    """1.1. Рядки (Strings):
    функція, яка приймає рядок і повертає його довжину.
    """
    return len(user_str)


TEST_STR = "This is a test"
str_length = length_of_string(TEST_STR)
print(f"\nThis is the length of our string: {str_length} characters.")


def concatenation_two_strings(user_str_1: str, user_str_2: str) -> str:
    """1.2. Рядки (Strings): функція, яка приймає два рядки
    і повертає об'єднаний рядок.
    """
    return user_str_1 + user_str_2


STR_1 = "Conan Doyle is the father "
STR_2 = "of Sherlock Holmes."
print(concatenation_two_strings(STR_1, STR_2))


def square_of_number(numb: int | float) -> int | float:
    """2.1. Числа (Int/float):
    функція, яка приймає число і повертає його квадрат.
    """
    return numb * numb  # or numb ** 2


print(f"\nThis is the square of our number: {square_of_number(25)}.")


def sum_of_two_numbers(num_1: int | float, num_2: int | float) -> int | float:
    """2.2. Числа (Int/float):
    функція, яка приймає два числа і повертає їхню суму.
    """
    return num_1 + num_2


print(f"This is the sum of our numbers: {sum_of_two_numbers(13, 24.8)}.")


def integer_division(numb_1: int, numb_2: int) -> tuple[int, int]:
    """2.3. Числа (Int/float):
    функція, яка приймає 2 числа типу int, виконує операцію ділення
    та повертає цілу частину і залишок.
    """
    return divmod(numb_1, numb_2)
    # or return numb_1 // numb_2, numb_1 % numb_2


print(f"This is the quotient: {integer_division(26, 5)[0]} "
      f"and the remainder: {integer_division(26, 5)[1]}.\n")


def average_of_list_of_numbers(lst_of_numbers: list[int | float]) -> float:
    """3.1. Списки (Lists):
    функція обчислення середнього значення списку чисел.
    """
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


user_list_1 = [35.5, 87, 112.56, 17]
user_list_2 = [35.5, 187, 12.56, 17]
print(f"This is the intersection of our two lists: "
      f"{intersection_of_two_lists(user_list_1, user_list_2)}.\n")


def dict_keys(my_dict):
    """4.1. Словники (Dictionaries): функція, яка приймає словник
    і виводить всі ключі цього словника.
    """
    return my_dict.keys()


user_dict = {"apple": 35, "kiwi": 9, "plum": 27, "cherry": 30}
print(f"This is the keys of our dictionary: {list(dict_keys(user_dict))}.")


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


user_dict_1 = {"apple": 35, "kiwi": 9, "plum": 27, "cherry": 30}
user_dict_2 = {"apple": 45, "peach": 9, "plum": 27, "melon": 30}
print(f"This is the merging of our dictionaries: "
      f"{merging_dictionaries(user_dict_1, user_dict_2)}.\n")


def merging_sets(set_1: set, set_2: set) -> set:
    """5.1. Множини (Sets):
    функція, яка приймає дві множини і повертає їхнє об'єднання.
    """
    merging_set = set_1
    for item in set_2:
        if item not in set_1:  # можна без цієї умови
            merging_set.add(item)
    return merging_set  # return set_1 | set_2 замінює весь цей блок


user_set_1 = {"apple", 35, "kiwi", 9, "plum", 27, "cherry", 30}
user_set_2 = {"apple", 45, "peach", 9, "plum", 27, "melon", 30}
print(f"This is the merging of our sets: "
      f"{merging_sets(user_set_1, user_set_2)}.")


def subset_or_not(set_1: set, set_2: set) -> bool:
    """5.2. Множини (Sets):
    функція, яка перевіряє, чи є одна множина підмножиною іншої.
    """
    for item in set_2:
        if item not in set_1:
            return False
    return True  # return set_2 <= set_1 замінює весь цей блок


users_set_1 = {"apple", 35, "kiwi", 9, "plum", 27, "cherry", 30}
users_set_2 = {"apple", 9, "plum", 27, 30}
print(f"Is the {users_set_2} subset of the {users_set_1}? "
      f"{subset_or_not(users_set_1, users_set_2)}.\n")


def even_or_odd(number: int) -> str:
    """6.1. Умовні вирази та цикли: функція, яка приймає число
    і виводить "Парне", якщо число парне,
    і "Непарне", якщо непарне.
    """
    return "Even" if number % 2 == 0 else "Odd"


print(f"The number 5 is {even_or_odd(5)}, 18 is {even_or_odd(18)}.")


def list_of_even(list_of_numbers: list[int]) -> list[int]:
    """6.2. Умовні вирази та цикли: функція, яка приймає список чисел
    і повертає новий список, що містить тільки парні числа.
    """
    list_of_even_numbers = []
    for item in list_of_numbers:
        if item % 2 == 0:
            list_of_even_numbers.append(item)
    return list_of_even_numbers
    # Замінює весь блок:
    # return [item for item in list_of_numbers if item % 2 == 0]


print(f"Only even numbers of our list of numbers: "
      f"{list_of_even([35, 88, 112, 17, 88, 187, 12, 17])}.\n")


# 7. Лямбда-функція, яка визначає парне/непарне.
# Функція приймає параметр (число) і,
# якщо парне, видає слово “парне”, якщо ні, то “непарне”.
NUM_1 = 5
print(
    f"The number {NUM_1} is "
    f"{(lambda number: 'Even' if number % 2 == 0 else 'Odd')(NUM_1)}."
)
