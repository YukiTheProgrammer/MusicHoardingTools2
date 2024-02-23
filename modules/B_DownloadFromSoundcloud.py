import os
import subprocess
from Z_MultiThreading import MultiThreader,PackForMultiThread
from Z_SeleniumHelper import MakeDriver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from mutagen.easyid3 import EasyID3
import time

#DOWNLOAD ALL TRACKS FROM A PLAYLIST/TRACK
def BaseSoundcloudDownloader(soundcloudUrl, path = r'E:\SoundCloud Downloads'):
    os.chdir(path)
    downloadCommand = f'scdl -l {soundcloudUrl} -c'
    os.system(downloadCommand)

#DOWNLOAD AN ALBUM
def AlbumSoundcloudDownloader(albumUrl, path = r'E:\SoundCloud Downloads'):
    driver = MakeDriver()
    driver.get(albumUrl)
    bottomReached = False
    while not bottomReached:
        driver.execute_script("window.scrollBy(0, 1000);")
        bottomReached = True
        try:
            WebDriverWait(driver,0.02).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".paging-eof")))
        except TimeoutException:
            bottomReached = False
    time.sleep(1.5)
    page_source = driver.page_source
    albumPageSoup = BeautifulSoup(page_source,'lxml')
    driver.close()
    albumTitle = albumPageSoup.find(class_='soundTitle__title').get_text().replace('\n','')
    allAs = albumPageSoup.find_all(class_='sc-link-primary')
    allSongLinks = []
    for a in allAs:
        if "?" in a.get("href"):
            allSongLinks.append("https://soundcloud.com" + a.get("href"))
    path = path + "\\" + albumTitle
    os.mkdir(path)
    MultiThreader(BaseSoundcloudDownloader,[allSongLinks,path])
    print (f'Album {albumTitle} Downloaded')
    
def MassBaseSoundcloudDownloader(soundcloudUrls, path = r'E:\SoundCloud Downloads'):
    MultiThreader(BaseSoundcloudDownloader,[soundcloudUrls,path])
    print('List of playlists/tracks downloaded')



#DOWNLOAD ALL TRACKS FOR AN ARIST
def AllArtistTracksSoundcloudDownloader(artistUrl, path = r'E:\SoundCloud Downloads'):
    artistName = artistUrl[23:]
    driver = MakeDriver()
    driver.get(artistUrl)
    bottomReached = False
    while not bottomReached:
        driver.execute_script("window.scrollBy(0, 1000);")
        bottomReached = True
        try:
            WebDriverWait(driver,0.02).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".paging-eof")))
        except TimeoutException:
            bottomReached = False
    page_source = driver.page_source
    albumPageSoup = BeautifulSoup(page_source,'lxml')
    driver.close()
    allAs = albumPageSoup.find_all(class_='sc-link-primary')
    allSongLinks = []
    for a in allAs:
        if artistName in a.get("href"):
            if not "sets" in a.get("href"): 
                allSongLinks.append("https://soundcloud.com" + a.get("href"))

    allSongLinks = allSongLinks[:-5]
    THREADING_SIZE = len(allSongLinks)
    for songLink in allSongLinks:
        songLink = [songLink,path]
    allSongLinks = [allSongLinks[i:i+THREADING_SIZE] for i in range(0, len(allSongLinks), THREADING_SIZE)]
    for batch in allSongLinks:
        MultiThreader(BaseSoundcloudDownloader, [batch,path])
    print(f'{artistUrl} Tracks Downloaded')

def MassAllArtistTracksSoundcloudDownloader(soundcloudUrls, path = r'E:\SoundCloud Downloads'):
    MuliThreader(AllArtistTracksSoundcloudDownloader,[soundcloudUrls,path])

    print('List of artists tracks downloaded')
#DOWNLOAD ALL PLAYLISTS FOR AN ARTIST
def AllArtistPlaylistsSoundcloudDownloader(artistUrl, path = r'E:\SoundCloud Downloads'):
    driver = MakeDriver()
    driver.get(artistUrl+"/sets")
    bottomReached = False
    while not bottomReached:
        driver.execute_script("window.scrollBy(0, 1000);")
        bottomReached = True
        try:
            WebDriverWait(driver,0.1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".paging-eof")))
        except TimeoutException:
            bottomReached = False
    page_source = driver.page_source
    albumPageSoup = BeautifulSoup(page_source,'lxml')
    driver.close()
    allAs = albumPageSoup.find_all(class_='sc-link-primary')
    allAlbumLinks = []
    allNewAs = []
    for a in allAs:
        if "sets" in a.get("href"):
            allAlbumLinks.append("https://soundcloud.com" + a.get("href"))
    MultiThreader(AlbumSoundcloudDownloader,[allAlbumLinks,path])
    print("All Playlists Downloaded For Aritst")

def MassAllArtistPlaylistSoundcloudDownloader(soundcloudUrls, path = r'E:\SoundCloud Downloads'):
    MultiThreader(AllArtistPlaylistsSoundcloudDownloader,[soundcloudUrls,path])
    print('List of artists tracks downloaded')

    
#DOWNLOAD ALL ALBUMS FOR AN ARIST
def AllArtistAlbumsSoundloucdDownloader(artistUrl, path = r'E:\SoundCloud Downloads'):
    geoAllowed = webdriver.FirefoxOptions()
    geoAllowed.set_preference('geo.prompt.testing', True)
    geoAllowed.set_preference('geo.prompt.testing.allow', True)
    geoAllowed.set_preference('geo.provider.network.url',
        'data:application/json,{"location": {"lat": 51.47, "lng": 0.0}, "accuracy": 100.0}')
    driver = webdriver.Firefox(options=geoAllowed)
    driver.maximize_window()
    driver.get(artistUrl+"/albums")
    bottomReached = False
    while not bottomReached:
        driver.execute_script("window.scrollBy(0, 1000);")
        bottomReached = True
        try:
            WebDriverWait(driver,0.1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".paging-eof")))
        except TimeoutException:
            bottomReached = False
    page_source = driver.page_source
    albumPageSoup = BeautifulSoup(page_source,'lxml')
    driver.close()
    allAs = albumPageSoup.find_all(class_='sc-link-primary')
    allAlbumLinks = []
    allNewAs = []
    for a in allAs:
        if "sets" in a.get("href"):
            allAlbumLinks.append("https://soundcloud.com" + a.get("href"))
    MultiThreader(AlbumSoundcloudDownloader,[allAlbumLinks,path])
    
    print("All Albums Downloaded For Aritst")


#DOWNLOAD EVERYTHIGN FOR AN ARTIST
def AllAritstSoundcloudDownloader(artistUrl, path = r'E:\SoundCloud Downloads'):
    print(artistUrl)
    artistName = artistUrl[23:]
    path = path + "\\" + artistName
    os.mkdir(path)
    AllArtistAlbumsSoundloucdDownloader(artistUrl,path)
    AllArtistPlaylistsSoundcloudDownloader(artistUrl,path)
    AllArtistTracksSoundcloudDownloader(artistUrl,path)
    RemoveDuplicates(path)
    print(f"Everything From {artistName} Downloaded")

def MassAllArtistSoundcloudDownloader(artistUrls, path =r'E:\SoundCloud Downloads'):
    MultiThreader(AllAritstSoundcloudDownloader,[artistUrls,path])   

def RemoveDuplicates(path = r'E:\SoundCloud Downloads'):
    albums = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    loosies = [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
    tracksToKeep = []
    for album in albums:
        files = os.listdir(path+"\\"+album)
        for file in files:
            tracksToKeep.append(EasyID3(path+"\\"+album+"\\"+file)['title'][0])
    tracksToLose = []
    x=0
    for loosie in loosies:
        tags = EasyID3(path+"\\"+loosie)
        if "title" in tags:
            if tags['title'][0] in tracksToKeep:
                os.remove(path+"\\"+loosie)
                x += 1
    print(f"{x} Duplicates Removed")

startTime = int(time.time())
artistUrls = ['https://soundcloud.com/richamiri','https://soundcloud.com/sk8star','https://soundcloud.com/untiljapan']
AllAritstSoundcloudDownloader('https://soundcloud.com/untiljapan')
print(time.time()-startTime)
