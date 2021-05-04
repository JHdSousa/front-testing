import unittest
from selenium import webdriver
from selenium import *
from selenium.webdriver.common.keys import Keys

# inherit TestCase Class and create a new test class
class LoginPageTest(unittest.TestCase):
  
    # initialization of webdriver
    def setUp(self):
        self.driver = webdriver.Firefox() #sets webdriver to firefox
  
    # Test case method. It should always start with test_
    def test_login_details(self):
          
        # get driver
        driver = self.driver
        # get python.org using selenium
        driver.get("http://127.0.0.1/")
  
        # assertion to confirm if title has python keyword in it
        self.assertIn("Login", driver.title)
  
        # locate element using name
        password = driver.find_element_by_id("password")
        username = driver.find_element_by_id('username')
        login = driver.find_element_by_name('submit')
  
        # send data
        username.send_keys("username")
        password.send_keys("password")
        
        login.click()

        # recieve data
        #elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
  
    # cleanup method called after every test performed
    def tearDown(self):
        self.driver.close()
  
# execute the script
if __name__ == "__main__":
    unittest.main()
