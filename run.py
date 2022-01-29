# sudo pacman -S geckodriver
#
from selenium.webdriver.common.by import By
from time import sleep, ctime
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

import os
url = os.environ["URL"]


opts = Options()
opts.add_argument("--headless")
browser = Firefox(options=opts)

#playlist_id = 'PLQOaTSbfxUtCrKs0nicOg2npJQYSPGO9r'
#playlist_link = 'https://www.youtube.com/playlist?list=' + playlist_id;

browser.get(url)
search_form = browser.find_elements(By.ID, 'video-title')

print(len(search_form))
url_list = []
naim = []
for index in search_form:
    url_list.append(index.get_attribute('href'))
    print(index.get_attribute('href'))
    naim.append(index.get_attribute('aria-label'))
    print(index.get_attribute('aria-label'))

# return url_list, naim




"""
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.headless = True
#assert opts.headless  # без графического интерфейса.

browser = Firefox(options=opts)
#browser.get('https://duckduckgo.com')


"""

"""
from selenium.webdriver.common.by import By
from time import sleep, ctime
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

opts = Options()
opts.add_argument("--headless")

browser = Firefox(options=opts)

playlist_id = 'PLQOaTSbfxUtCrKs0nicOg2npJQYSPGO9r'
playlist_link = 'https://www.youtube.com/playlist?list=' + playlist_id;

browser.get(playlist_link)
#browser.find_element_by_id('search-icon-legacy').send_keys('webdriver')
#sleep(5)
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#sleep(5)
#search_form = browser.find_elements_by_class_name('yt-simple-endpoint style-scope ytd-playlist-video-renderer')

#search_form = browser.find_elements_by_id('contents')
#SAS = search_form.find_element_by_id('video-title')
#browser.implicitly_wait(3)
#browser.page_source()
search_form = browser.find_elements(By.ID, 'video-title')

print(len(search_form))
#print(len(search_form))
linkList = []
for index in search_form:
    print(index.get_attribute('href'))

#results = browser.find_elements_by_class_name('result')
#print(len(tracks))
#print(search_form[0].get_attribute('href'))

"""
