# IMPORT SELENIUM, TIME, CSV AND THREADING
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import csv
import threading

# INITIATE BROWSER FOR SCRAPPING
browser = webdriver.Chrome()
action = ActionChains(browser)

# NAVIGATE TO MUSIC GENRE HOMEPAGE
browser.get('https://www.di.fm/deephouse')

def fiveminloop():
  # SETUP 5MIN TIMER
  threading.Timer(300.0, fiveminloop).start()
  time.sleep(5)

  track = browser.find_elements_by_css_selector('#content-wrap > div > div > div.content-area > div > div > section:nth-child(1) > div > div > div > div.now-playing-component__info > a')
  artist = browser.find_elements_by_css_selector('#content-wrap > div > div > div.content-area > div > div > section:nth-child(1) > div > div > div > div.now-playing-component__info > div.now-playing-component__artist') 
  
  #LIKE COUNTS HIDDEN UNDER LIKE BUTTON, FIRST HOVER OVER BUTTON THEN EXTRACT VALUE
  like_button = browser.find_element_by_css_selector('#content-wrap > div > div > div.content-area > div > div > section:nth-child(1) > div > div > div > div.now-playing-component__info > div.now-playing-component__votes-region > ul > li.track-voting-component__vote-btn.track-voting-component__up > i.track-voting-component__icon.track-voting-component__icon--inactive.icon-thumbs-up-outline')
  action.move_to_element(like_button).perform()
  like_count = browser.find_element_by_css_selector('#content-wrap > div > div > div.content-area > div > div > section:nth-child(1) > div > div > div > div.now-playing-component__info > div.now-playing-component__votes-region > ul > li.track-voting-component__vote-btn.track-voting-component__up > div > div > div > span')
  
  time.sleep(5)

  # WRITE SCRAPPED DATA TO CSV FILE
  with open('tracks.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([track[0].text, artist[0].text, like_count.text]) 

#LOOP EVER 5 MINUTES
fiveminloop()
