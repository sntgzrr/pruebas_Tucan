# Generated by Selenium IDE
# Comentar una publicación en TUCAN utilizando letras mayúsculas
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import csv

class TestCP005N():
  def setup_method(self):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test_cP005N(self, email, password):
    self.driver.get("https://tucan.toolsincloud.net/index.php")
    self.driver.set_window_size(1382, 736)
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys(email)
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys(password)
    self.driver.find_element(By.NAME, "login").click()
    self.driver.get("https://tucan.toolsincloud.net/profile.php?username=Santiago")
    self.driver.find_element(By.CSS_SELECTOR, ".box-tweet:nth-child(25) .grid-box-reaction:nth-child(1) .far").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".box-tweet:nth-child(25) > a > span")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".popupComment:nth-child(27) .retweet-msg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".popupComment:nth-child(27) .retweet-msg").send_keys("MUY BUENA PUBLICACIÓN")
    self.driver.find_element(By.CSS_SELECTOR, ".popupComment:nth-child(27) .comment-it").click()
    
  def exeCP005N(self):
    try:
      self.test005n=TestCP005N()
      with open("registros.csv") as c:
        self.reader = csv.DictReader(c)
        for row in self.reader:
          self.test005n.setup_method()
          self.test005n.test_cP005N(email=row["email"], password=row["password"])
          self.test005n.teardown_method()
          print("Comentario de publicación en mayúsculas",row["id"],"hecho correctamente.")
    except:
      print("Algo inesperado ha ocurrido en el CP005N")
        
exe = TestCP005N()
exe.exeCP005N()