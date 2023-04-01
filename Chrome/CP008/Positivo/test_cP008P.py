# Generated by Selenium IDE
# Cambiar el nombre de usuario de TUCAN - Usuario
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

class TestCP008P():
  def setup_method(self):
    self.options = webdriver.ChromeOptions()
    self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
    self.driver = webdriver.Chrome(executable_path='<path-to-chrome>', options=self.options)
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_cP008P(self, email, password, replace):
    self.driver.get("https://tucan.toolsincloud.net/index.php")
    self.driver.set_window_size(1382, 736)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(email)
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys(password)
    self.driver.find_element(By.NAME, "login").click()
    self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(9) strong").click()
    self.driver.find_element(By.ID, "exampleInputPassword1").clear()
    self.driver.find_element(By.ID, "exampleInputPassword1").click()
    self.driver.find_element(By.ID, "exampleInputPassword1").send_keys(replace)
    self.driver.find_element(By.NAME, "submit").click()
  
  def exeCP008P(self):
    try:
      self.test009p=TestCP008P()
      with open("registros.csv") as c:
        self.reader=csv.DictReader(c)
        for row in self.reader:
          self.test009p.setup_method()
          self.test009p.test_cP008P(email=row["email"], password=row["password"], replace=row["replace"])
          self.test009p.teardown_method()
    except:
      print("Algo inesperado ha ocurrido en el CP008P")
      
exe = TestCP008P()
exe.exeCP008P()