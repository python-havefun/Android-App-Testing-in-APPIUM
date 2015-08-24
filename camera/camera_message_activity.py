__author__ = 'aditya'

import os, time, unittest
from appium import webdriver
from time import sleep
from subprocess import call
#from selenium.webdriver.common import desired_capabilities

class Camera500Test(unittest.TestCase):

    def setUp(self):
        desired_caps={}

        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='4.4'
        desired_caps['deviceName']='Play_8X_1200'
        desired_caps['appPackage']='com.android.gallery3d'
        desired_caps['appActivity']='com.android.camera.CameraLauncher'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_camera_500_times(self):
        '''checking image details'''
        k=0
        for i in range(0,5):
            self.driver.find_element_by_id("com.android.gallery3d:id/shutter_button_photo").click()
            k+=1
            print(k)

        if k==5:
            print("Script run for 5 times")
        else:
            print("got some error......###  ***")
            #sleep(2)
    def test_message(self):
        self.driver.start_activity('com.android.mms', '.ui.BootActivity')
        self.driver.find_element_by_accessibility_id('New message').click()
        self.driver.find_elements_by_class_name('android.widget.MultiAutoCompleteTextView')[0].send_keys('0000000000')
        #self.driver.send_keys('0000000000')
        self.driver.find_elements_by_class_name('android.widget.EditText')[0].send_keys('hey man this is for testing')
        #self.driver.send_keys('this is for testing only')
        self.driver.back()
        self.driver.back()
        self.driver.press_keycode(82)



if __name__ == "__main__":
    suit= unittest.TestLoader().loadTestsFromTestCase(Camera500Test)
    unittest.TextTestRunner(verbosity=2).run(suit)
