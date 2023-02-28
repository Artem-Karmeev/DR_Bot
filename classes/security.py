class Verification:

    alphabet = tuple()

    # def __init__(self) -> None:
    #     with open(r'technical_data\alphadet.txt', 'a', encoding='UTF-8') as file:
    #         temp_list = file.writelines()
    #         temp_list


    def verifi_date(self, user_date: str) -> tuple:

        """Если утверждение верное вернет кортеж с строкой содержащий дату пользователя дд мм гггг,
        иначе вернет кортеж который содержит False"""

        if len(user_date) == 10:
            date = list(user_date)
            date[2], date[5] = ".", "."
            date = "".join(date)
            date = date.split(".")

            if date[0].isdigit() and date[1].isdigit() and date[2].isdigit():

                if 0 < int(date[1]) < 13:

                    if int(date[1]) == 4 or int(date[1]) == 6 or int(date[1]) == 9 or int(date[1]) == 11:

                        if 0 < int(date[0]) < 31:
                                ('.'.join(date),)

                        else:
                            return (False,)
                        
                    elif int(date[1]) == 2:
                        if int(date[2]) % 4:
                            if 0 < int(date[0]) < 29:
                                return ('.'.join(date),)
                            
                            else:
                                return (False,)
                            
                        else:
                            if 0 < int(date[0]) < 30:
                                return ('.'.join(date),)
                            
                            else:
                                return (False,)
                            
                    else:
                        if 0 < int(date[0]) < 32:

                                return ('.'.join(date),)
                        
                        else:
                            return (False,)
                else:
                    return (False,)
                
            else:
                return (False,)
            
        else:
            return (False,)


    def name(self, name: str) -> tuple:

        """Делает первые буквы слов заглавными"""

