from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

geoAllowed = webdriver.FirefoxOptions()
geoAllowed.set_preference('geo.prompt.testing', True)
geoAllowed.set_preference('geo.prompt.testing.allow', True)
geoAllowed.set_preference('geo.provider.network.url',
    'data:application/json,{"location": {"lat": 51.47, "lng": 0.0}, "accuracy": 100.0}')
driver = webdriver.Firefox(options=geoAllowed)
driver.maximize_window()
THRESHHOLD = 0.54
WAITTIME_BETWEEN_CLICKS = 3
driver.get("https://leaked.cx/login/")
