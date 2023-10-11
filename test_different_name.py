# Поверка, что на странице "Мои питомцы" у питомцев разные имена
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def test_different_name(test_my_pets):
    """Поверка, что на странице "Мои питомцы" у питомцев разные имена"""

    # Явное ожидание
    element = WebDriverWait(pytest.driver, 12).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.table.table-hover tbody tr')))

    # Сохранение эданных в переменную "pet_data"
    pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Формируются данные из переменной "pet_data"
    # Выбираются имена и добавляются в список "pets_name"
    pets_name = []
    for i in range(len(pet_data)):
        data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        pets_name.append(split_data_pet[0])

    # Если имя повторяется срабатывает счетчик
    # Если r == 0, то повторяющихся имен нет
    r = 0
    for i in range(len(pets_name)):
        if pets_name.count(pets_name[i]) > 1:
            r += 1
    assert r == 0
    print(r)
    print(pets_name)