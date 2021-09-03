from selenium import webdriver
import time
url = 'http://hlpdesk.ftst3.fttb.corbina.net/ptn/ng_ptn#/hd_auth/lo..'
driver = webdriver.Chrome('C:\\webdrivers\\chromedriver.exe')

try:
  driver.get(url=url)
  time.sleep(5)
  login = driver.find_element_by_xpath('//*[@id="inputLogin"]')
  time.sleep(3)
  login.send_keys('AVBusyrev')
  time.sleep(3)
  password = driver.find_element_by_xpath('//*[@id="inputPassword"]')
  time.sleep(3)
  password.send_keys('r0fwjFTS')
  time.sleep(3)
  button = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/form/div/div[3]/div[2]/div/div[1]/button')
  button.click()
  time.sleep(3)
except Exception as ex:
  print(ex)
finally:
  driver.close()
  driver.quit()
