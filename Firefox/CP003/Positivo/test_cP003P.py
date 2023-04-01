# Generated by Selenium IDE
# Realizar una publicación - Usuario
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

class TestCP003P():
  def setup_method(self):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_cP003P(self, email, password, name):
    self.driver.get("https://tucan.toolsincloud.net/index.php")
    self.driver.set_window_size(1382, 736)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(email)
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys(password)
    self.driver.find_element(By.NAME, "login").click()
    self.driver.find_element(By.NAME, "status").click()
    self.driver.find_element(By.NAME, "status").send_keys("estoy realizando pruebas en tucan")
    self.driver.find_element(By.ID, "tweet-input").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".box-tweet:nth-child(3) strong").text == name
    
  def exeCP003P(self):
    try:
      self.test003p=TestCP003P()
      with open("registros.csv") as c:
        self.reader=csv.DictReader(c)
        for row in self.reader:
          self.test003p.setup_method()
          self.test003p.test_cP003P(email=row["email"], password=row["password"], name=row["name"])
          self.test003p.teardown_method()
    except:
      print("Algo inesperado ha ocurrido en el CP003P")
      
exe = TestCP003P()
exe.exeCP003P()