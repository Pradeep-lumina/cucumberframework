

from behave import *
from selenium import webdriver


@given('Open the browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="D:\chromedriver_win32 (8)\chromedriver.exe")
    context.driver.maximize_window()



@when('Enter the url')
def step_impl(context):
    context.driver.get("https://www.facebook.com/")



@then('Enter the username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element_by_id("email").send_keys(user)
    context.driver.find_element_by_id("pass").send_keys(pwd)



@then('Close the browser')
def step_impl(context):
    context.driver.close()


