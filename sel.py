import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from tools import prnt
explicit=10
small_wait=random.uniform(0, 0.3)
def Key(driver, value='', type_speed=small_wait, repeat=1):
  actions = ActionChains(driver)
  for r in range(repeat):
    for v in value:
      actions.send_keys(v).perform()
      time.sleep(type_speed)

  return True

def wait(driver, data, by="xpath"):
    try:
      if by == 'xpath':WebDriverWait(driver, explicit).until(EC.presence_of_element_located((By.XPATH, data)))
      if by == 'id':WebDriverWait(driver, explicit).until(EC.presence_of_element_located((By.ID, data)))
    except TimeoutException:
      if by == 'xpath':WebDriverWait(driver, explicit).until(EC.presence_of_element_located((By.XPATH, data)))
      if by == 'id':WebDriverWait(driver, explicit).until(EC.presence_of_element_located((By.ID, data)))

def find(driver, data, by='xpath'):
  wait(driver, data, by=by)
  if by == 'xpath':
    prnt(f"[ Finding Element By XPATH ]: {data}")
    find=driver.find_element(By.XPATH, data)
  if by == 'id':
    prnt(f"[ Finding Element By ID ]: {data}")
    find=driver.find_element(By.ID, data)
  return find


def finds(driver, data, by='xpath'):
  wait(driver, data, by=by)
  if by == 'xpath':find=driver.find_elements(By.XPATH, data)
  if by == 'id':find=driver.find_elements(By.ID, data)
  return find