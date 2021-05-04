##probably wont use
from needle.cases import NeedleTestCase
from needle.driver import NeedleChrome, NeedleSafari
from selenium import webdriver

class loginPageTest (NeedleTestCase):
    engine_class = 'needle.engines.perceptualdiff_engine.Engine'
    def testLoginContainerDefaultViewport(self):
        self.driver.get('http://127.0.0.1/Login') #default driver is firefox gonna write seperate classes for different web drivers
        self.assertScreenshot('login-container', 'loginContainerTestShot')
      

        ###selecting a webdriver just need to oevrrride the system preset
        @classmethod
        def get_web_driver(cls):
            return NeedleChrome()


       ####setting viewport size
    def test12(self):
           self.set_viewport_size(width=1024, height=768)
