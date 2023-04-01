# Generated by Selenium IDE
# Registro sin rellenar el campo nombre en TUCÁN - Usuario
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

class TestCP001N():
  def setup_method(self):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_cP001N(self, username, email, password):
    self.driver.get("https://tucan.toolsincloud.net/")
    self.driver.set_window_size(1382, 736)
    self.driver.find_element(By.ID, "auto").click()
    self.driver.find_element(By.NAME, "username").click()
    self.driver.find_element(By.NAME, "username").send_keys(username)
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").click()
    self.driver.find_element(By.CSS_SELECTOR, ".form-group:nth-child(4) > #exampleInputEmail1").send_keys(email)
    self.driver.find_element(By.ID, "exampleInputPassword1").click()
    self.driver.find_element(By.ID, "exampleInputPassword1").send_keys(password)
    self.driver.find_element(By.NAME, "signup").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".text-center:nth-child(1)").text == "name is required"
    
  def exeCP001N(self):
    try:
      self.test001n = TestCP001N()
      with open("registros.csv") as c:
        self.reader = csv.DictReader(c)
        for row in self.reader:
          self.test001n.setup_method()
          self.test001n.test_cP001N(username=row["username"], email=row["email"], password=row["password"])
          self.test001n.teardown_method()
    except:
      print("Algo inesperado ha ocurrido en el CP001N")
      
exe = TestCP001N()
exe.exeCP001N()