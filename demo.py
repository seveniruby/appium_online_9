# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "android"
caps["deviceName"] = "hogwarts"
caps["appPackage"] = "com.xueqiu.android"
caps["appActivity"] = ".view.WelcomeActivityAlias"
caps["autoGrantPermissions"] = "true"

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(10)

el1 = driver.find_element_by_id("com.xueqiu.android:id/user_profile_icon")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/tv_login")
el2.click()
el3 = driver.find_element_by_id("com.xueqiu.android:id/tv_login_by_phone_or_others")
el3.click()

driver.quit()