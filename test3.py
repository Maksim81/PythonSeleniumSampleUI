'''
Created on Nov 3, 2018

@author: Maksim Kolodijev
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#binary = FirefoxBinary("C://Users/Gamma Test/eclipse-workspace/IMDB/src/geckodriver.exe")

class ImbdTestSuite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/home/osboxes/uitest/geckodriver')

    def test_verify_film_name_exists(self):
        driver = self.driver
        driver.get("https://www.imdb.com/search/name?gender=male,female&ref_=nv_tp_cel_1")
        elem = driver.find_element_by_xpath("//*[@id='main']/div/div[3]/div[1]/div[2]/p[1]/a").text
        assert elem != "", "Film Name OK"

    def test_verify_subpage_header_exists(self):
        driver = self.driver
        driver.get("https://www.imdb.com/search/name?gender=male,female&ref_=nv_tp_cel_1")
        elem = driver.find_element_by_xpath("//*[@id='main']/div/h1").text
        assert len(elem) > 0, "Header name is empty"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
