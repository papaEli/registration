import re
import string


class Registration:

    def __init__(self, login, password):
        self.login = login
        self.password = password

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @staticmethod
    def check_email(email):
        expression = re.compile(
            r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$')
        result = expression.search(email)
        return bool(result)

    @login.setter
    def login(self, n_l):
        if not isinstance(n_l, str):
            raise TypeError(
                "the entered value type does not match the string type")

        if not Registration.check_email(n_l):
            raise ValueError(
                "Login must include atleast one @ and . email")

        self.__login = n_l

    @staticmethod
    def is_include_digit(pattern):
        expression = re.compile(r'\d')

        result = expression.search(pattern)

        return bool(result)

    @staticmethod
    def is_include_all_register(str_p):
        i = 0

        for letter in str_p:

            if letter.isupper():
                i += 1

        return True if i >= 2 else False

    @staticmethod
    def include_only_latin(word):
        flg = True
        i = 0

        for p in word:

            if p not in string.ascii_letters + string.digits + string.punctuation:
                flg = False

        return flg

    @staticmethod
    def easy_password(password):
        flg = True

        with open('easy_passwords.txt', encoding='utf-8') as file_obj:
            for s in file_obj.readlines():

                if password == s.rstrip('\n'):
                    flg = False

        return flg

    @password.setter
    def password(self, n_p):
        if not isinstance(n_p, str):

            raise TypeError("Пароль должен быть строкой")

        if 5 > len(n_p) or len(n_p) > 11:

            raise ValueError(
                "Пароль должен быть длинее 4 и меньше 12 символов")

        if not Registration.is_include_digit(n_p):

            raise ValueError("Пароль должен  содержать хотя бы одну цифру")

        if not Registration.is_include_all_register(n_p):

            raise ValueError(
                "Пароль должен содержать хотя бы 2 заглавные буквы")

        if not Registration.include_only_latin(n_p):

            raise ValueError(
                "Пароль должен содержать только латинский алфавит")

        if not Registration.easy_password(n_p):

            raise ValueError(
                'Ваш пароль содержится в списке самых легких паролей')

        self.__password = n_p


login = 'bukashka@mailru'
password = 'VdbdGfbdg1&'

user = Registration(login, password)

print(user.login)
