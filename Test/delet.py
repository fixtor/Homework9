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


