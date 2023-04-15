# Generated by Selenium IDE
# Cambiar la contraseña actual de la cuenta de TUCAN - Usuario
import pytest
import time
import json
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestCP010P():
  def __init__(self):
    pass
  
  def setup_method(self):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_cP010P(self, name, email, password, change_password):
    self.driver.get("https://tucan.toolsincloud.net/index.php")
    self.driver.set_window_size(1382, 736)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(email)
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys(password)
    self.driver.find_element(By.NAME, "login").click()
    self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(9) > .wrapper-left-elements").click()
    self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(9) strong").click()
    self.driver.find_element(By.ID, "v-pills-profile-tab").click()
    self.driver.find_element(By.NAME, "old_password").click()
    self.driver.find_element(By.NAME, "old_password").send_keys(password)
    self.driver.find_element(By.NAME, "new_password").click()
    self.driver.find_element(By.NAME, "new_password").send_keys(change_password)
    self.driver.find_element(By.NAME, "ver_password").click()
    self.driver.find_element(By.NAME, "ver_password").send_keys(change_password)
    self.driver.find_element(By.CSS_SELECTOR, ".text-center:nth-child(5) > .btn").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".home-name").text == name
  
  def exeCP010P(self):
    try:
      self.test010p = TestCP010P()
      with open("registros.csv") as c:
        self.reader = csv.DictReader(c)
        for row in self.reader:
          self.test010p.setup_method()
          self.test010p.test_cP010P(name=row["name"], email=row["email"], password=row["password"], change_password=row["change_password"])
          self.test010p.teardown_method()
          print("Cambio de contraseña actual",row["id"],"hecho correctamente.")
    except:
      print("Algo inesperado ha ocurrido en el CP010P")
      
exe = TestCP010P()
exe.exeCP010P()