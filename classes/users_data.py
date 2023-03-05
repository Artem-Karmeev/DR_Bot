from classes.users_class import File

class UserData(File):


    """Унаследован от File. Работа с словарями."""

    def check_flag(self, user_id: int) -> list:
        """Вернет список с флагами"""
        return self.users_id[user_id]


    def change_head_flag(self, user_id: int, flag: int):
        """изменяет флаг с индексом 1"""
        self.users_id[user_id][1] = flag 


    def change_support_flag(self, user_id: int, flag: int):
        """изменяет флаг с индексом 2"""
        self.users_id[user_id][2] = flag


    def check_id(self, user_id: int) -> bool:
        """Проверка на наличие id в словаре"""
        return user_id in self.users_id


    def finish(self, user_id: int):
        """Удаляет id из словаря"""
        self.users_data.pop(user_id)

    def return_data(self, user_id: int) -> str:
        """Покажет список имен"""
        data = self.users_data[user_id]
        new_str = ''
        for i in range(len(data)):
            new_str += f'{i}. {data[i][1]} {data[i][0]} {data[i][2]}\n'
        return new_str
    

    def kick_data(self, user_id: int):
        """Удалит из словаря 'users_data' пару по id"""
        self.users_data.pop(user_id)

