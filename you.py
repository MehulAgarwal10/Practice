from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

movie = input('Enter name of the movie : ')


driver.get('https://www.youtube.com/')

search = driver.find_element_by_xpath('//*[@id="masthead-search-term"]')
search.clear()
search.send_keys(movie+' trailer')
search.send_keys(Keys.RETURN)

video = driver.find_element_by_xpath('//*[@id="results"]/ol/li[2]/ol/li[1]/div/div/div[2]/h3/a')

video.click()

url = driver.current_url
# print('Current url : '+url)

new_url = url[:12] + 'ss' + url[12:]
# print('New url : ' + new_url)

driver.get(new_url)
time.sleep(4)
dl_link = driver.find_element_by_xpath('//*[@id="sf_result"]/div/div[1]/div[2]/div[2]/div[1]/a')
dl_link.click()