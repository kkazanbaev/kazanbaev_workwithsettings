from settings import settings
from settings_manager import settings_manager
import unittest
import os

class test_settings(unittest.TestCase):
    
    def test_check_create_manager(self):
        # Подготовка
        manager1 = settings_manager()
        manager2 = settings_manager()
        
        # Действие
        
        # Проверки
        print(str(manager1.number))
        print(str(manager2.number))
    
        assert manager1.number == manager2.number
    
    #
    # Проверить корректность заполнения поля first_name
    #
    def test_check_first_name(self):
        # Подготовка
        item = settings()
        
        # Действие
        item.first_name = "a  "
        
        # Проверка
        assert item.first_name == "a"
        
    def test_check_manager_convert(self):
        # Подготовка
        manager = settings_manager()
        manager.open("settings.json")
         
        # Действие
        manager.convert()  
        
    def test_check_open_settings(self):
        # Подготовка
        manager = settings_manager()
        
        # Действие
        result = manager.open("settings.json")
        
        # Проверка
        print(manager.data)
        assert manager.__first_name is not None
        assert manager.__inn is not None
        assert manager.__chet is not None
        assert manager.__corr_chet is not None
        assert manager.__bik is not None
        assert manager.__sobs is not None
    
    def test_check_test_catalog(self):
        # Подготовка
        manager = settings_manager()
        result = manager.open("test/filesett.json")
         
        # Действие
        assert result == True

    def test_check_load(self):
        # Подготовка
        manager = settings_manager()
        
        # Действие
        manager.open("test/filesett.json")
        
        # Проверка
        print(manager.data)
        assert manager.__first_name is not None
        assert manager.__inn is not None
        assert manager.__chet is not None
        assert manager.__corr_chet is not None
        assert manager.__bik is not None
        assert manager.__sobs is not None