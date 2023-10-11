# Тест, проверяет, что в списке нет повторяющихся питомцев

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


def test_duplicate_pets(test_my_pets):
   """В списке нет повторяющихся питомцев"""

   # Установка явного ожидания
   element = WebDriverWait(pytest.driver, 10).until(
   EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))

   # Сохранение данных в переменную "pet_data"
   pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Сортировка данных переменной "pet_data"
   list_data = []
   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
      split_data_pet = data_pet.split(' ')
      list_data.append(split_data_pet)

   # Формирование строки с данными
   line = ''
   for i in list_data:
      line += ''.join(i)
      line += ' '

   # Получение списка из строки "line"
   list_line = line.split(' ')

   # Превращение списка в множество
   set_list_line = set(list_line)

   # Нахождение количества элементов списка и множества
   a = len(list_line)
   b = len(set_list_line)

   # Из количества элементов списка вычитается количество элементов множества
   result = a - b

   # Если количество элементов == 0, то карточки с одинаковыми данными отсутствуют
   assert result == 0