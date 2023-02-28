from classes.users_class import File

class User_data(File):

    def fill_list(self, user_id: int, index: int, value: str):
        """Заполняет вложенный лист по индексу для последующей записи в файл"""
        self.users_id[user_id][3][index] = value
        print(self.users_id[user_id])

        
    def check_flag(self, user_id: int) -> int:
        """Вернет список с флагами пользователя по id"""
        return self.users_id[user_id]


    def change_flag(self, user_id: int, flag: int, index: int ):
        """изменяет флаг с указанным индексом в словаре user_id"""
        self.users_id[user_id][index] = flag  

    def check_id(self, user_id: int) -> bool:
        """Проверка на наличие id в словаре"""
        return user_id in self.users_id


    def finish_processing(self, user_id: int):
        """Удаляет id из словаря"""
        self.users_data.pop(user_id)


