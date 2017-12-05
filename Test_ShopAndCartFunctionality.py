import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class test_EmployeeLogin(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome("C:\\chromedriver.exe")

   def test_EmployeeLogin(self):
       user = "instructor"
       pwd = "test1234"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://gs-food-pantry.herokuapp.com/portfolio/login/?next=/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div/form/p[3]/input").click()
       driver.find_element_by_link_text("Shop").click()
       driver.find_element_by_link_text("Bagel").click()
       driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/div/form/input[3]").click()
       driver.find_element_by_link_text("Checkout").click()
       visit = "1"
       first_name = "Pooja"
       last_name = "Yalala"
       email = "pyalala@unomaha.edu"
       address = "1110 S 67th st"
       postal_code = "68022"
       city = "Omaha"
       elem = driver.find_element_by_id("id_visit")
       elem.send_keys(visit)
       time.sleep(2)
       elem = driver.find_element_by_id("id_first_name")
       elem.send_keys(first_name)
       time.sleep(2)
       elem = driver.find_element_by_id("id_last_name")
       elem.send_keys(last_name)
       time.sleep(2)
       elem = driver.find_element_by_id("id_email")
       elem.send_keys(email)
       time.sleep(2)
       elem = driver.find_element_by_id("id_address")
       elem.send_keys(address)
       time.sleep(2)
       elem = driver.find_element_by_id("id_postal_code")
       elem.send_keys(postal_code)
       time.sleep(2)
       elem = driver.find_element_by_id("id_city")
       elem.send_keys(city)
       time.sleep(2)
       elem = driver.find_element_by_xpath("//*[@id='app-layout']/div/div/div/form/p[8]/input").click()
       time.sleep(2)
       assert "order placed"
       time.sleep(5)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
