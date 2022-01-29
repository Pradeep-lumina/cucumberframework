from behave import *
from selenium import webdriver


@given('Browser open')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")
    context.driver.maximize_window()



@when('I Pass the url')
def step_impl(context):
    context.driver.get("https://www.facebook.com/")



@then('valid credentials')
def step_impl(context):
    context.driver.find_element_by_id("email").send_keys("test")
    context.driver.find_element_by_id("pass").send_keys("test123")



@then('I enter the invalid crednetials')
def step_impl(context):
    context.driver.find_element_by_id("email").send_keys("test123")
    context.driver.find_element_by_id("pass").send_keys("test1")

