"""
Модуль для работы с базой данных
"""
import time

users = {}


def add_user(login: str, password: str) -> bool:
    """
    Функция добавляет пользователя в базу данных с проверкой уникальности пользователя

    :param login: Логин
    :param password: Пароль
    :return: True, если добавлен успешно, иначе False
    """
    if login not in users:
        users[login] = password
        print(f"{time.ctime()} - Пользователь {login} добавлен")
        return True
    else:
        print(f'{time.ctime()} - Пользователь {login} уже существует')
        return False



# def remove_user(login: str) -> bool:
#     """
#     Функция удаляет пользователя из базы данных
#
#     :param login: Логин
#     :return: True, если удален успешно, иначе False
#     """
#
#     a = input("Введите логин пользователя, которого необходимо удалить из системы: ")
#     if a in users