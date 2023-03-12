class File:

    """Родительский класс для работы с файлами"""

    users_id = {} # ключ это id пользователя, значение это лист с состоянием пользователя(вкл\выкл(int), флаг(int) и вспомогательный флаг(int) )
    users_data = {} # словарь для работы с данными юзера
    temporary_data = {} # Промежуточное хранение/заполнение строки


    def __init__(self) -> None:

        with open(r'data\users_id.txt', 'r', encoding='UTF-8') as file:
            users_id = file.readlines()
            for item in users_id:
                id = item.strip()
                with open(f'data\setup\{id}', 'r') as data:
                    flag = data.read()
                    self.users_id[int(id)] = [int(flag.strip()), 0, 0]


    def add_user(self, user_id: int):

        """добавляет id в словарь, в файл users_id и создает файл для юзера"""

        self.users_id[user_id] = [1, 0, 0]

        with open(f'data\data\{user_id}', 'w') as file1:
            file1.write('')
        with open(f'data\setup\{user_id}', 'w') as file2:
            file2.write('1')
        with open(r'data\users_id.txt', 'a') as file3:
            file3.write(f'{str(user_id)}\n')


    def app_str(self, user_id: int):
        
        """Добавит строку в конец файла с датами"""

        with open(f'data\data\{user_id}', 'a',encoding='UTF-8') as file1:
            file1.write(f'{self.temporary_data[user_id][0]} →  {self.temporary_data[user_id][1]}\n')


    def extract_data(self, user_id: int):

        """Считает файл пользователя, отсортирует и заполнит пару в 'users_data'"""

        with open(f'data\data\{user_id}', 'r', encoding='UTF-8') as file:
            data = file.readlines()
            data = [data[i].strip().split(' →  ') for i in range(len(data))]
            data = sorted(data, key=lambda x: (int(x[0].split('.')[1]), int(x[0].split('.')[0]))) 
            self.users_data[user_id] = data
            print(self.users_data)


    def switch(self,user_id: int, status: bool):

        """Изменит значение в файле setup"""
       
        stat = lambda x: '1' if x else '0' 
        with open(f'data\setup\{user_id}', 'w', encoding='UTF-8') as file:
            file.write(stat(status))
        self.users_id[user_id][0] = int(stat(status))


    def overwrite_data(self, user_id):
        
        """Перезапишет файл в data"""

        result_str = ''
        temp_data = self.users_data[user_id]

        for i in range(len(temp_data)):
            result_str += f'{temp_data[i][0]} →  {temp_data[i][1]}\n'

        with open(f'data\data\{user_id}', 'w', encoding='UTF-8') as file:
            file.write(result_str)






