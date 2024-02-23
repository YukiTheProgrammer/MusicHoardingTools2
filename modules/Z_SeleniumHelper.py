from selenium import webdriver

def MakeDriver():
    geoAllowed = webdriver.FirefoxOptions()
    geoAllowed.set_preference('geo.prompt.testing', True)
    geoAllowed.set_preference('geo.prompt.testing.allow', True)
    geoAllowed.set_preference('geo.provider.network.url',
        'data:application/json,{"location": {"lat": 51.47, "lng": 0.0}, "accuracy": 100.0}')
    driver = webdriver.Firefox(options=geoAllowed)
    driver.maximize_window()
    return(driver)
