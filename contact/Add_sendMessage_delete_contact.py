'''
Created on Aug 13, 2015

@author: aditya
'''
import unittest, os, time
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.webdriver.common import desired_capabilities

class Contact_test(unittest.TestCase):
    
    def setUp(self):
        desired_caps={}
        
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='4.4'
        desired_caps['deviceName']='Play_8X_1200'
        desired_caps['appPackage']='com.android.contacts'
        desired_caps['appActivity']='.activities.PeopleActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)   

    def tearDown(self):
        self.driver.quit()


    def test_add_contacts(self):
        '''Add contact will open add contact option in contacts app'''
        el=self.driver.find_element_by_accessibility_id("Add Contact")
        el.click()
        '''contact will select phone_contacts to store your contacts'''
        m1=self.driver.find_element_by_name('Phone contact')
        m1.click()
        '''this will return EditText options as list So that you can write your name phone number and ohter'''
        textfields = self.driver.find_elements_by_class_name("android.widget.EditText")
        '''textfields[0] gives Name to enter'''
        textfields[0].send_keys("Test Number")
        '''add number to user'''
        textfields[1].send_keys("999999999999")
        #'''textfields[2] gives email address to add'''
        #textfields[2].send_keys("appium_Node@xolo.in")
        '''this will click on contact photo to add'''
        self.driver.find_element_by_accessibility_id("contact photo").click()
#        time.sleep(2)
        '''This will choose take_photo option from avai'''
        self.driver.find_elements_by_class_name("android.widget.TextView")[0].click()
        #time.sleep(2)
        '''This will tap on take poto for you contact'''
        self.driver.find_elements_by_class_name("android.widget.ImageView")[1].click()
        #time.sleep(2)
        '''this will tap on take_photo'''
        self.driver.find_elements_by_class_name("android.widget.ImageView")[1].click()
        #time.sleep(2)
        '''this will capture photo for your contact'''
        self.driver.find_element_by_id("com.android.gallery3d:id/shutter_button_photo").click()
       # time.sleep(2)
        '''this will tap on done OK button'''
        self.driver.find_element_by_id("com.android.gallery3d:id/btn_done").click()
        #time.sleep(2)
        '''this will tap on just one_time button'''
        self.driver.find_element_by_id("android:id/button_once").click()
        #time.sleep(2)
        '''this will save your croped image'''
        self.driver.find_element_by_id("com.android.gallery3d:id/filtershow_done").click()
        #time.sleep(2)
        self.driver.find_elements_by_class_name("android.widget.ImageView")[0].click()
        time.sleep(10)
        
        self.driver.find_element_by_id("com.android.contacts:id/secondary_action_view_container").click()
        self.driver.find_element_by_id("com.android.mms:id/embedded_text_editor").send_keys("hey man how are you")
        self.driver.back()
        self.driver.back()
        self.driver.press_keycode(82)
        self.driver.find_elements_by_class_name("android.widget.LinearLayout")[2].click()
        self.driver.find_element_by_name("OK").click()
        
        
        
       
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    suit= unittest.TestLoader().loadTestsFromTestCase(Contact_test)
    unittest.TextTestRunner(verbosity=2).run(suit)