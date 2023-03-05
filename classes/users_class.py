class File:

    """Родительский класс для работы с файлами"""

    users_id = {} # ключ это id пользователя, значение это лист с состоянием пользователя(вкл\выкл(bool) и флаг(int))
    users_data = {} # словарь для работы с данными юзера
    temporary_data = {} # Промежуточное хранение/заполнение строки


    def open(self):

        """Стартовая функция, открывает файл user_id, и заполняет словарь user_id, 
        вызывается при старте"""

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
        with open(f'data\setup\{user_id}', 'w') as file1:
            file1.write('1')
        with open(r'data\users_id.txt', 'a') as file2:
            file2.write(f'{str(user_id)}\n')


    def app_str(self, user_id: int):
        
        """Добавит строку в конец файла"""

        with open(f'data\data\{user_id}', 'a',encoding='UTF-8') as file1:
            file1.write(f'{self.temporary_data[user_id][1]} →  {self.temporary_data[user_id][0]} →  {self.temporary_data[user_id][2]}\n')


    def extract_data(self, user_id: int):

        """Считает файл пользователя заполнит 'users_data'"""

        with open(f'data\data\{user_id}', 'r', encoding='UTF-8') as file:
            data = file.readlines()
            data = [data[i].strip().split(' →  ') for i in range(len(data))]
            self.users_data[user_id] = data

