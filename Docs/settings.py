class settings:
    __first_name = ""
    __inn = ""
    __chet = ""
    __corr_chet = ""
    __bik = ""
    __sobs = ""
    
    # Наименование
    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")
        
        self.__first_name = value.strip()

    # ИНН
    @property
    def inn(self):
        return self.__inn
    
    @inn.setter
    def inn(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")
        if len(value) != 12:
            raise Exception("Некорректная длина!")
        
        self.__inn = value.strip()

    # Счет
    @property
    def chet(self):
        return self.__chet
    
    @chet.setter
    def chet(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")
        if len(value) != 11:
            raise Exception("Некорректная длина!")
        
        self.__chet = value.strip()

    # Корреспондентский счет
    @property
    def corr_chet(self):
        return self.__corr_chet
    
    @corr_chet.setter
    def corr_chet(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")
        if len(value) != 11:
            raise Exception("Некорректная длина!")
        
        self.__corr_chet = value.strip()
    
    # БИК
    @property
    def bik(self):
        return self.__bik
    
    @bik.setter
    def bik(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")
        if len(value) != 9:
            raise Exception("Некорректная длина!")
        
        self.__bik = value.strip()

    # Вид собственности
    @property
    def sobs(self):
        return self.__sobs
    
    @sobs.setter
    def sobs(self, value: str):
        if not isinstance(value, str):
            raise Exception("Некорректный аргумент!")
        if len(value) != 5:
            raise Exception("Некорректная длина!")
        
        self.__sobs = value.strip()