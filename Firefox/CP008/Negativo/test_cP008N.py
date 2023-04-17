# Generated by Selenium IDE
# Cambiar el nombre de usuario de TUCAN por uno ya existente - Usuario
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

class TestCP008N():
  def setup_method(self):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_cP008N(self, email, password, ready):
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
    self.driver.find_element(By.ID, "exampleInputPassword1").send_keys(ready)
    self.driver.find_element(By.NAME, "submit").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".alert > .text-center").text == "This username is already use"
  
  def exeCP008N(self):
    try:
      self.test009n=TestCP008N()
      with open("registros.csv") as c:
        self.reader=csv.DictReader(c)
        for row in self.reader:
          self.test009n.setup_method()
          self.test009n.test_cP008N(email=row["email"], password=row["password"], ready=row["ready_name"])
          self.test009n.teardown_method()
          print("Cambio de nombre por uno ya existente",row["id"],"hecho correctamente.")
    except:
      print("Algo inesperado ha ocurrido en el CP008N")
      
exe = TestCP008N()
exe.exeCP008N()