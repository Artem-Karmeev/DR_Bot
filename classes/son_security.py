from classes.security import Verification

class VerifiKey(Verification):

    """Внебрачный сын Verification который смотрит за 'temporary_data и флаги'"""
  
    
    def add(self, user_id: int):
        """Создаст пару в словаре 'temporary_data' по id"""
        self.temporary_data[user_id] = [None, None]


    def kick_tmp_data(self, user_id: int):
        """удалит пару в словаре 'temporary_data' по id если есть вхождение"""
        if user_id in self.temporary_data:
            self.temporary_data.pop(user_id)


    def fill(self, user_id: int, index: int, data: str):
        """Заполнит value в словаре 'temporary_data'
        по указанному индексу (от 0 до 1)"""
        self.temporary_data[user_id][index] = data


    def check_flag(self, user_id: int) -> list:
        """Вернет список с флагами"""
        return self.users_id[user_id]


    def change_head_flag(self, user_id: int, flag: int):
        """изменяет флаг с индексом 1"""
        self.users_id[user_id][1] = flag 


    def change_support_flag(self, user_id: int, flag: int):
        """изменяет флаг с индексом 2"""
        self.users_id[user_id][2] = flag
