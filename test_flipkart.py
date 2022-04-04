from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
import pytest

@pytest.fixture
def setUp():
    global driver,product
    product = input("Enter the product to be searched :")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()
    print("Tested Successfully")

def test_search_product(setUp):
    driver.get("https://www.google.com/")
    time.sleep(1)
    driver.find_element_by_name("q").send_keys("Flipkart")
    time.sleep(1)
    driver.find_element_by_name("btnK").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[7]/div/div[10]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div[1]/a/h3").click()
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
    time.sleep(1)
    driver.find_element_by_name("q").send_keys(product)
    time.sleep(1)
    driver.find_element_by_class_name("L0Z3Pu").click()
    time.sleep(8)
    driver.execute_script("window.scrollTo(0,window.scrollY+3500)")
    time.sleep(8)
    driver.close()
