from classes.security import Verification

class VerifiKey(Verification):

    """Внебрачный сын Verification который смотрит за 'temporary_data'"""
  
    
    def add(self, user_id: int):
        """Создаст пару в словаре 'temporary_data' по id"""
        self.temporary_data[user_id] = [None, None, None]


    def kick(self, user_id: int):
        """удалит пару в словаре 'temporary_data' по id"""
        self.temporary_data.pop(user_id)


    def app(self, user_id: int):
        """запишет строку в файл id"""
        res = self.temporary_data.pop(user_id)


    def fill(self, user_id: int, index: int, data: str):
        """Заполнит value в словаре 'temporary_data'
        по указанному индексу (от 0 до 2)"""
        self.temporary_data[user_id][index] = data


    def check(self, user_id):
        """Проверяет вхождение id в 'temporary_data'"""
        return user_id in self.temporary_data