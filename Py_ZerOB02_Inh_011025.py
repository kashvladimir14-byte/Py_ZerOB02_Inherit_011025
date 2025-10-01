# Задание
# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
#  У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.

class User:
    def __init__(self, user_id, name, access_level):
        self.__user_id = user_id
        self.__name = name
        self.__access_level = access_level
    def get_user_id(self):  # getter для поля user_id
        return self.__user_id
    def get_name(self):  # getter для поля name
        return self.__name

    def get_access_level(self):  # getter для поля access_level
        if self.__access_level == 2:
            return 'Администратор'
        else:
            return 'Пользователь'

    def set_name(self, new_name):  # setter для поля name
        if new_name != '':
            self.__name = new_name
        else:
            print('Имя не может быть пустым')


# class Admin(User):
class Admin(User):
    def __init__(self, user_id, name, access_level, admin_access_level):
        super().__init__(user_id, name, access_level)
        self.__admin_access_level = admin_access_level
        self.__user_list = []

    def get_user_list(self):  # getter для поля user_list
        return self.__user_list

    def add_user(self, user):  # метод для добавления пользователя в список
        if isinstance(self,User):
            self.__user_list.append(user)
        else:
            print('Ошибка: Можно добавить только экземпляр класса User')

    def remove_user(self, user_id):  # метод для удаления пользователя из списка
        for user in self.__user_list:
            if user.get_user_id() == user_id:
                self.__user_list.remove(user)
                print(f"Пользователь с ID {user_id} удален.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

        def list_users(self):
            for user in self.__user_list:
                print('ID:', user.get_user_id())
                print('Имя:', user.get_name())
                print('Уровень доступа:', user.get_access_level())
                print('--------------------------------')

    if __name__ == '__main__':

        user1 = User(1, 'Иван', 1)
        user2 = User(2, 'Петр', 1)
        user3 = User(3, 'Сидор', 1)

       # admin1 = Admin
        admin1=Admin(1, 'Иван', 2, 1)
        admin1.add_user(user1)
        admin1.add_user(user2)
        admin1.add_user(user3)

        admin1.list_users()

        admin1.remove_user(user_id=2)

        admin1.list_users()

