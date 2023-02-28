class File:

    users_id = {} # ключ это id пользователя, значение это лист с состоянием пользователя(вкл\выкл(bool) и флаг(int))
    users_data = {} # словарь для работы с данными юзера

    def open(self):

        """Стартовая функция, открывает файл user_id, и заполняет словарь user_id, 
        вызывается при старте"""

        with open(r'data\users_id.txt', 'r', encoding='UTF-8') as file:
            users_id = file.readlines()
            users_id = [int(item.strip()) for item in users_id]
            for item in users_id:
                self.users_id[item] = [True, 0, 0, ["", "", ""]]


    def extract_user_data(self, user_id: int):

        """откроет файл по id и заполнит значение в словаре """
        
        self.users_data[user_id] = 0 ########### ваш парсинг мог быть тут 


    def add_user(self, user_id: int):

        """добавляет id в словарь, в файл users_id и создает файл для юзера"""

        self.users_id[user_id] = [True, 0, 0, ["", "", ""]]

        with open(f'data\{user_id}', 'w') as file1:
            file1.write('')

        with open(r'data\users_id.txt', 'a') as file2:
            file2.write(f'{str(user_id)}\n')



    

