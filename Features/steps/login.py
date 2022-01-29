from lib2to3.pgen2 import driver

import behave

from behave import *
from selenium import webdriver



@given('I open the browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")
    context.driver.maximize_window()


@when('I open the url')
def step_impl(context):
    context.driver.get("https://www.facebook.com/")



@then('I enter the valid credentials')
def step_impl(context):
    context.driver.find_element_by_id("email").send_keys("test")
    context.driver.find_element_by_id("pass").send_keys("test123")



@then('I close the browser')
def step_impl(context):
    context.driver.close()

