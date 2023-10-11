#Проверка, что на странице пользователя хотя бы у половины питомцев есть фото.
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def test_have_poto(test_my_pets):
    """Поверка что на странице пользователя хотя бы у половины питомцев есть фото."""

    # Установка явного ожидания
    element = WebDriverWait(pytest.driver, 12).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.\\.col-sm-4.left')))

    # Сохранение статистики в переменную "statistic"
    statistic = pytest.driver.find_elements(By.CSS_SELECTOR, '.\\.col-sm-4.left')

    # Сохранение элементов "img" в переменную "images"
    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

    # Количество объектов из статистики
    number = statistic[0].text.split('\n')
    number = number[1].split(' ')
    number = int(number[1])

    # Половина от количества
    half = number // 2

    # Поиск объектов с фотографией
    number_of_photos = 0
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            number_of_photos += 1

    # Проверка того, что количество объектов с фотографией >= половине общего количества
    assert number_of_photos >= half
    print(f'Количество фото: {number_of_photos}')
    print(f'Половина от числа питомцев: {half}')