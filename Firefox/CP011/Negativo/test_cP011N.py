# Generated by Selenium IDE
# Ingreso a TUCAN con contraseña errónea - Usuario
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

class TestCP011N():
  def __init__(self):
    pass
  
  def setup_method(self):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_cP011N(self, email, username):
    self.driver.get("https://tucan.toolsincloud.net/index.php")
    self.driver.set_window_size(1382, 736)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(email)
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys(username)
    self.driver.find_element(By.NAME, "login").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".span-fp-error").text == "the email or password is not correct"
  
  def exeCP011N(self):
    try:
      self.test011n=TestCP011N()
      with open("registros.csv") as c:
        self.reader = csv.DictReader(c)
        for row in self.reader:
          self.test011n.setup_method()
          self.test011n.test_cP011N(email=row["email"], username=row["username"])
          self.test011n.teardown_method()
    except:
      print("Algo inesperado ha ocurrido en el CP011N")
      
exe = TestCP011N()
exe.exeCP011N()