# Тест вход на страницу пользователя с валидными данными

from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Firefox()

   # Переход на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()

@pytest.fixture()
def test_my_pets():
   """ Авторизация на сайте, переход на страницу "Мои питомцы". """

   #Установка явного ожидания
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, 'email')))

   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys('ххххх3@gmail.com')

   # Установка явного ожидания
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.ID, 'pass')))

   # Вводим пароль
   pytest.driver.find_element(By.ID, 'pass').send_keys('7jfezyzKq6эжлJxj')

   # Установка явного ожидания
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))

   # Нажимается кнопка входа
   pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

   # Установка явного ожидания
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[1]/a[1]')))

   # Нажимается кнопка "Мои питомцы"
   pytest.driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul[1]/li[1]/a[1]').click()

# Проверка открытия страницы "Мои питомцы"
   assert pytest.driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

