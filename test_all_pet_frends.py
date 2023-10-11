# Проверка карточек питомцев ВСЕХ пользователей
#     на наличие фото, имени и описания
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


def test_all_pet_frends(test_my_pets):
    """Проверка карточек питомцев ВСЕХ пользователей
    на наличие фото, имени и описания (порода и возраст)"""

    # Установка неявного ожидания
    pytest.driver.implicitly_wait(10)

    # Установка явного ожидания
    element = WebDriverWait(pytest.driver, 12).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[2]/a[1]')))

    # Нажимаем на кнопку "Все питомцы"
    pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[2]/a[1]').click()

    # Проверяем, что мы оказались на странице "Все питомцы"
    assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/all_pets'

    images = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    assert names[0].text != ''

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ',' in descriptions[i].text
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0