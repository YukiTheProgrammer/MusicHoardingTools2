from Z_SeleniumHelper import MakeDriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pprint
import time
"""
Album - disco_type_s
Live Album - disco_type_l
EP - disco_type_e
Single - disco_type_i
Music Video - disco_type_o
Appears On - disco_type_a
Compilation - disco_type_c
VA Compilation - disco_type_v
Bootleg - disco_type_b
Video - disco_tye_d
Additional Release - disco_type_x
"""
def GetAllReleases(artistUrl):
    driver = MakeDriver()
    driver.get(artistUrl)
    time.sleep(3)
    adButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ad-close-button")))
    adButton.click()
    time.sleep(1)
    expandButtons = driver.find_elements(By.CLASS_NAME, "disco_expand_section_btn")
    for button in expandButtons:
        notClickable = True
        while notClickable:
            driver.execute_script("window.scrollBy(0, 10);")
            notClickable = False
            try:
                WebDriverWait(driver, 0.1).until(EC.element_to_be_clickable(button))
            except:
               notClickable = True
        button.click()
        try:
            element = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, "loading_disco")))
        except:
            stillLoading = False
        stillLoading = True
        while stillLoading:
            try:
                element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CLASS_NAME, "loading_disco")))
            except:
                stillLoading = False
    pageSource = driver.page_source
    driver.close()
    rymPageSoup = BeautifulSoup(pageSource,'lxml')
    discography = {
                    "Albums":[],
                    "Live Albums":[],
                    "EPs":[],
                    "Singles":[],
                    "Music Videos":[],
                    "Appears Ons":[],
                    "Compilations":[],
                    "VA Compilations":[],
                    "Bootlegs":[],
                    "Videos":[],
                    "Additoinal Releases":[]
                  }
    discographyKeys = list(discography.keys())
    sections = ['disco_type_s','disco_type_l','disco_type_e','disco_type_i','disco_type_o','disco_type_a','disco_type_c','disco_type_v','disco_type_b','disco_type_d','disco_type_x']
    for i in range(len(discographyKeys)):
        section = sections[i]
        section = rymPageSoup.find(id=section)
        if section:
            releases = section.find_all(class_="disco_release")
            for release in releases:    
                discography[discographyKeys[i]].append(release.find(class_="disco_info").find("a").get('title'))
    return(discography)
