import time
import json
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tools import prnt, progress
from sel import *
from message import synonym
  
# Reading from file
iterations=9
############## SCRIPT ##############
def init():
  f = open ('config.json', "r")
  config = json.loads(f.read())
  f.close()

  prnt("Initializing Reward Maker")
  driver = webdriver.Chrome()
  driver.get(config['urls']['signin'])
  find(driver, "email", by='id').send_keys(config['credentials']['user'])
  find(driver, "adornment-password", by='id').send_keys(config['credentials']['password'])
  find(driver, config['xpaths']['signin_button']).click()
  prnt(f"Logging into account: {config['credentials']['user']}")
  for i in range(iterations):
    progress(i, iterations)
    neo=random.choice(config['team'])
    prnt(f"[ GENERATING REWARD 🏆 ]: => {neo}")
    find(driver, config['xpaths']['reward_trigger']).click()
    time.sleep(3)
    Key(driver,value=[Keys.TAB, Keys.TAB], type_speed=small_wait)
    Key(driver,value=f"{synonym('great')} {synonym('work', pos='NOUN')} @{neo}", type_speed=small_wait)
    Key(driver,value=[Keys.DOWN, Keys.ENTER], type_speed=small_wait)
    # PICK AWARD TYPE
    award_type_int=random.randint(1,3)
    Key(driver,value=Keys.TAB, type_speed=small_wait, repeat=award_type_int)
    Key(driver,value=Keys.ENTER, type_speed=small_wait)
    
    # SUBMIT
    Key(driver,value=Keys.TAB, type_speed=small_wait, repeat=(award_type_int*-1)+5)
    Key(driver,value=Keys.ENTER, type_speed=small_wait)
    # find(driver, config['xpaths']['reward_submit']).click()
    prnt(f"[ SENDING REWARD 🏆 ]: => {neo}")
    time.sleep(5)
  driver.quit()

if __name__ == "__main__":
  init()