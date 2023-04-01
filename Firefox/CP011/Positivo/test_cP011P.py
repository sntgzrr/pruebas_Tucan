# Generated by Selenium IDE
# Ingreso a TUCAN - Usuario
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

class TestCP011P():
  def __init__(self):
    pass
  
  def setup_method(self):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_cP011P(self, email, password, name):
    self.driver.get("https://tucan.toolsincloud.net/index.php")
    self.driver.set_window_size(1382, 736)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(email)
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys(password)
    self.driver.find_element(By.NAME, "login").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".name > strong").text == name
    
  def exeCP011P(self):
    try:
      self.test011p=TestCP011P()
      with open("registros.csv") as c:
        self.reader = csv.DictReader(c)
        for row in self.reader:
          self.test011p.setup_method()
          self.test011p.test_cP011P(email=row["email"], password=row["password"], name=row["name"])
          self.test011p.teardown_method()
    except:
      print("Algo inesperado ha ocurrido en el CP011P")
      
exe = TestCP011P()
exe.exeCP011P()