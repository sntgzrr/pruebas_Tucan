# Generated by Selenium IDE
# Cambiar la dirección de email por una ya registrada en TUCAN - Usuario
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

class TestCP009N():
  def __init__(self):
    pass
  
  def setup_method(self):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_cP009N(self, email, password, ready_email):
    self.driver.get("https://tucan.toolsincloud.net/index.php")
    self.driver.set_window_size(1382, 736)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(email)
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys(password)
    self.driver.find_element(By.NAME, "login").click()
    self.driver.find_element(By.CSS_SELECTOR, ".grid-sidebar:nth-child(9) strong").click()
    self.driver.find_element(By.ID, "exampleInputEmail1").clear()
    self.driver.find_element(By.ID, "exampleInputEmail1").click()
    self.driver.find_element(By.ID, "exampleInputEmail1").send_keys(ready_email)
    self.driver.find_element(By.NAME, "submit").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".alert > .text-center").text == "This email is already use"
    
  def exeCP009N(self):
    try:
      self.test009n = TestCP009N()
      with open("registros.csv") as c:
        self.reader = csv.DictReader(c)
        for row in self.reader:
          self.test009n.setup_method()
          self.test009n.test_cP009N(email=row["email"], password=row["password"], ready_email=row["ready_email"])
          self.test009n.teardown_method()
          print("Cambio de email actual del perfil por uno ya registrado",row["id"],"hecho correctamente.")
    except:
      print("Algo inesperado ha ocurrido en el CP009N")
      
exe = TestCP009N()
exe.exeCP009N()