class Email_Components_Name_Domain_Suffix:
    
    "Класс для разделения емейла на Имя, Домен и Суффикс"   
    
    @classmethod
    def __validate_email(cls, email):
        return type(email) is str and "@" in email and "." in email
        # Возвращается Тру или Фолс, для проверки if в __Init__!!!

    def __init__(self, email):
        if not self.__validate_email(email):
            raise ValueError('Unknown address, make sure is correct')  # Значение для Исключения
        self.__email = email.split('@')
        self.name = self.__get_name()
        self.domain = self.__get_domain()
        self.suffix = self.__get_suffix()


    def __get_name(self):
        return str(self.__email[0])
                
    
    def __get_domain(self):
        return str(self.__email[1]).split('.')[0]
        
    
    def __get_suffix(self):
        return str(self.__email[1]).split('.')[1]
        

em = Email_Components_Name_Domain_Suffix('1@ED.R')
print(em.name, em.domain, em.suffix)

print(dir(em))


# def test_validate(a=1):
#     print(type(a))
#     if (type(a) == str) and ("@" in a) and ("." in a): return True
#
#     else:
#         return False  # Возвращается Тру или Фолс, для проверки if в __Init__!!!
#
# print(test_validate())
