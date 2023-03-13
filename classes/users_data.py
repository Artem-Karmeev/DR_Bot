from classes.users_class import File

class UserData(File):

    """Унаследован от File. Работа с словарями."""

    def check_id(self, user_id: int) -> bool:
        """Проверка на наличие id в словаре users_id"""
        return user_id in self.users_id


    def return_data(self, user_id: int) -> str:
        """Вернет события пользователя"""
        new_str = ''
        for i in range(len(self.users_data[user_id])):
            new_str += f'🆔: {i}   📆: {self.users_data[user_id][i][0]}   📝: {self.users_data[user_id][i][1]}\n'
        return new_str


    def kick_data(self, user_id: int):
        """Удалит из словаря 'users_data' пару по id если он там есть """
        if user_id in self.users_data:
            self.users_data.pop(user_id)


    def search(self, user_id: int, search: str, flag: bool = True) -> str:
        
        """Вернет все вхождения в value словаря user_data
        если передать флаг True, вернет значения включая индексы"""
        
        result_search = ''
        if flag:
            for i in range(len(self.users_data[user_id])):
                if search in self.users_data[user_id][i][0] or search in self.users_data[user_id][i][1]:
                    result_search += f'🆔: {i}   📆: {self.users_data[user_id][i][0]}   📝: {self.users_data[user_id][i][1]}\n'
            return result_search
        else:
            for i in range(len(self.users_data[user_id])):
                if search in self.users_data[user_id][i][0] or search in self.users_data[user_id][i][1]:
                    result_search += f'📆: {self.users_data[user_id][i][0]}   📝: {self.users_data[user_id][i][1]}\n'
            return result_search


    def return_len(self, user_id: int) -> int:
        """Вернет длину value из словаря users_data"""
        return len(self.users_data[user_id])
    

    def del_event(self, user_id: int, index: int):
        """Удалит событие из value пользователя"""
        self.users_data[user_id].pop(index)
        print(self.users_data)