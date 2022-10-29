<<<<<<< HEAD
class Email:
    
    "Класс для разделения емейла на Имя, Домен и Суффикс"   
    
    @classmethod
    def __validate_email(cls, email):
        if type(email) is str and "@" in email and "." in email: return True
        else: return False       #Возвращается Тру или Фолс, для проверки if в __Init__!!!


    def __init__(self, email):
        if self.__validate_email(email):
            self.__email = email
            self.__temp = self.__email.split('@')
        else:
            self.__email = 'None@None.None' #Значение для Исключения
            self.__temp = self.__email.split('@')

    def get_name(self):
        return str(self.__temp[0])
                
    
    def get_domain(self):
        return str(self.__temp[1]).split('.')[0]
        
    
    def get_suffix(self):
        return str(self.__temp[1]).split('.')[1]
        

em = Email('igor@yandex.ru')
print(em.get_domain(), em.get_name())

print(em.__dict__)


# def test_validate(a=1):
#     print(type(a))
#     if (type(a) == str) and ("@" in a) and ("." in a): return True
#
#     else:
#         return False  # Возвращается Тру или Фолс, для проверки if в __Init__!!!
#
# print(test_validate())
=======
from webbrowser import get


class Email:

    def __init__(self, email):
        self.__email = email
        self.__tmp = None
        
        
    def get_name(self):
        self.__tmp = self.__email.split('@')
        return str(self.__tmp[0])
                
    
    def get_domain(self):
        return str(self.__tmp[1]).split('.')[0]
        
    
    def get_suffix(self):
        return str(self.__tmp[1]).split('.')[1]
        

p = Email('igor@yandex.ru')
p1 = Email('nata.ladanova@mail.ru')

print(p.get_name())
print(p.get_domain())
print(p.get_suffix())


print(p1.get_name(), p1.get_domain(), p1.get_suffix())


>>>>>>> dbd501062327b31eade20e610f14ebc3cac04974
