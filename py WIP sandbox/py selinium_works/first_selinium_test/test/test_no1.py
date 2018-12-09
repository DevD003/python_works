from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome (
    "E:\Pycharm Py proj\python_works\py WIP sandbox\py selinium_works\/first_selinium_test\/test\drivers\chromedriver.exe" )
# driver = webdriver.Firefox()
# driver = webdriver.Ie()

driver.set_page_load_timeout ( "10" )

# go to google url
driver.get ( "https://www.google.com/" )
# find the search bar and enter the given search word
driver.find_element_by_name ( "q" ).send_keys ( "Adithya Sai Krishna Kesineni" )
driver.find_element_by_name ( "btnK" ).send_keys(Keys.ENTER)
time.sleep ( 4 )
driver.quit ( )
