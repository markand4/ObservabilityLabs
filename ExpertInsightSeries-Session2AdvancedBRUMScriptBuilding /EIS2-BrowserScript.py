# -*- coding: utf-8 -*-
#Date 06/23/2025
#Description: This sample script is a framework and more in depth synthetic script that you can use to help you learn browser synthetics for Splunk AppDynamics
#Author: Mark Kurpiel
#
##############################################################################################################
#Disclaimer
#Cisco (Splunk AppDynamics)/CSS provides this extension script "as is" without warranties, express or implied.
#Use this script at your own risk. Cisco (Splunk AppDynamics)/CSS is not responsible for any errors,
#data loss, system malfunctions, or other consequences. The user assumes full responsibility for verifying
#functionality and ensuring compliance. Under no circumstances shall Cisco (Splunk AppDynamics)/CSS be liable
#for any direct, indirect, or consequential damages arising from the use of this script. By using it, the user
#agrees to these terms and releases Cisco (Splunk AppDynamics)/CSS from any claims or liabilities.
#
##############################################################################################################

# These are all the imports I would use for selenium functionalities please add/remove as needed 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException

# Importing the logging module to generate output for the script when running in AppDynamics.
import logging

# This package is used for managing the WebDriver locally.
# IMPORTANT: Make sure to comment out this import before uploading to AppDynamics!
from chromedriver_py import binary_path  # Provides the path to the ChromeDriver executable.



# This function finds a web element using its ID attribute.
# Parameters:
# - name (string): The ID of the element to locate.
#
# Function behavior:
# 1. It waits for up to 10 seconds (can be changed) for the element to become clickable using Selenium's `WebDriverWait`.
# 2. If the element is not clickable within the timeout period, it falls back to directly locating the element using `find_element` by ID.
# 3. The located element is then returned.
#
# This function ensures the element is ready for interaction, improving stability for elements that may take time to load or become clickable.
def find_elem_by_id(name):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, name))
        )
    except:
        element = driver.find_element(By.ID, name)
 
    return element

# This function finds a web element using its CSS selector.
# Parameters:
# - name (string): The CSS selector used to locate the element.
#
# Function behavior:
# 1. It waits for up to 10 seconds (can be changed) for the element to become clickable using Selenium's `WebDriverWait`.
# 2. If the element is not clickable within the timeout period, it falls back to directly locating the element using `find_element` by CSS selector.
# 3. The located element is then returned.
#
# This function ensures the element is ready for interaction, making it reliable for elements that may take time to load or become interactive.
def find_elem_by_css(name):
    driver.execute_script('var x = document.getElementsByClassName("__acs"); if(typeof x[0] !== "undefined") { x[0].remove() };')
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, name))
        )
    except:
        element = driver.find_element(By.CSS_SELECTOR, name)
 
    return element

# This function finds a web element using its Class.
# Parameters:
# - name (string): The Class is used to locate the element.
#
# Function behavior:
# 1. It waits for up to 10 seconds (can be changed) for the element to become clickable using Selenium's `WebDriverWait`.
# 2. If the element is not clickable within the timeout period, it falls back to directly locating the element using `find_element` by Class.
# 3. The located element is then returned.
#
# This function ensures the element is ready for interaction, making it reliable for elements that may take time to load or become interactive.
def find_elem_by_class(name):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, name))
        )
    except:
        element = driver.find_element(By.CLASS_NAME, name)
 
    return element
 
# This function finds a web element using its XPath.
# Parameters:
# - name (string): The XPath expression used to locate the element.
#
# Function behavior:
# 1. It waits for up to 10 seconds for the element to become clickable using Selenium's `WebDriverWait`.
# 2. If the element is not clickable within the timeout period, it falls back to directly locating the element using `find_element` by XPath.
# 3. The located element is then returned.
#
# This function ensures the element is ready for interaction, improving reliability for elements that may take time to load or become clickable.
def find_elem_by_xpath(name):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, name))
        )
    except:
        element = driver.find_element(By.XPATH, name)
 
    return element
 
# This function finds a web element using its visible link text.
# Parameters:
# - name (string): The exact visible text of the link to locate.
#
# Function behavior:
# 1. It waits for up to 10 seconds (can be changed) for the link to become clickable using Selenium's `WebDriverWait`.
# 2. If the link is not clickable within the timeout period, it falls back to directly locating the link using `find_element` by its link text.
# 3. The located element is then returned.
#
# This function ensures the link is ready for interaction, making it reliable for dynamically loaded or delayed elements.
def find_elem_by_linktext(name):
    driver.execute_script('var x = document.getElementsByClassName("__acs"); if(typeof x[0] !== "undefined") { x[0].remove() };')
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, name))
        )
 
    except:
        element = driver.find_element(By.LINK_TEXT, name)
 
    return element


# This function finds a web element using its visible partial link text.
# Parameters:
# - name (string): The exact visible text of the link to locate.
#
# Function behavior:
# 1. It waits for up to 10 seconds (can be changed) for the link to become clickable using Selenium's `WebDriverWait`.
# 2. If the link is not clickable within the timeout period, it falls back to directly locating the link using `find_element` by its link text.
# 3. The located element is then returned.
#
# This function ensures the link is ready for interaction, making it reliable for dynamically loaded or delayed elements.
def find_elem_by_partiallinktext(name):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, name))
        )
 
    except:
        element = driver.find_element(By.PARTIAL_LINK_TEXT, name)
 
    return element

# This function finds a web element using its "name" attribute.
# Parameters:
# - name (string): The value of the "name" attribute of the element to locate.
#
# Function behavior:
# 1. It waits for up to 10 seconds (can be changed) for the element to become clickable using Selenium's `WebDriverWait`.
# 2. If the element is not clickable within the timeout period, it falls back to directly locating the element using `find_element` by name.
# 3. The located element is then returned.
#
# This function ensures that the element is ready for interaction, improving stability in cases where elements may take time to load or become clickable.
def find_elem_by_name(name):
    try:
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, name))
        )
 
    except:
        element = driver.find_element(By.NAME, name)
 
    return element
 
# This function attempts to click a Selenium element with a fallback mechanism.
# Parameters:
# - element: The Selenium WebElement to be clicked.
# - is_javascript_first (boolean): If True, the function will first attempt to click the element using JavaScript.
#
# Function behavior:
# 1. If `is_javascript_first` is True, it clicks the element using JavaScript (`execute_script`).
# 2. It then attempts to click the element using Selenium's `ActionChains` to simulate a user interaction.
# 3. If both methods fail, it tries a direct `element.click()` call.
# 4. As a final fallback, it clicks the element again using JavaScript.
#
# This ensures robustness when interacting with elements that may be difficult to click due to overlapping elements, scrolling issues, or other browser-specific behavior.
def click_element(element, is_javascript_first):
    try:
        if(is_javascript_first):
            driver.execute_script('arguments[0].click()', element)
 
        webdriver.ActionChains(driver).move_to_element(element).click(element).perform()
    except:
        try:
            element.click()
        except:
            driver.execute_script('arguments[0].click()', element)

#Optional chrome options helps deal with annoying popups
chrome_opt = webdriver.ChromeOptions()
prefs = {"credentials_enable_service": False,
         "profile.password_manager_enabled": False,
         "enablePopups": False,
         "profile.password_manager_leak_detection" : False}
chrome_opt.add_experimental_option("prefs", prefs)
# Comment out the following lines when running in AppDynamics.
svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(options=chrome_opt, service=svc)


# Set the timeout for asynchronous JavaScript execution to 50 seconds.
driver.set_script_timeout(50)

# Configure the logging module to display log messages.
# - level=logging.INFO: Sets the logging level to INFO.
# - format='%(asctime)s - %(levelname)s - %(message)s': Specifies the format of log messages, including the timestamp, log level, and message.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create a logger instance with the name of the current module.
logger = logging.getLogger(__name__)



try:
    # Maximize the browser window to ensure all elements are visible.
    driver.maximize_window()
    # Start editing the script here.
    logger.info("Navigating to https://www.saucedemo.com/?ref=hackernoon.com")
    driver.get("https://www.saucedemo.com/?ref=hackernoon.com")

    logging.info("Log into site using failed username, password, and then hit login")
    find_elem_by_id("user-name").send_keys("locked_out_user")
    find_elem_by_id("password").send_keys("secret_sauce")
    click_element(find_elem_by_id("login-button"), False)

    logging.info("Verifying error message is displayed")
    find_elem_by_xpath("//*[@id='login_button_container']/div/form/div[3]/h3")
    assert find_elem_by_xpath("//*[@id='login_button_container']/div/form/div[3]/h3").text  == "Epic sadface: Sorry, this user has been locked out."
    # Take a screenshot of the page and save it as "error.png".
    driver.get_screenshot_as_file("UserLoginError.png")

    logging.info("Log into site using username, password, and then hit login")
    driver.refresh()
    find_elem_by_id("user-name").send_keys("standard_user")
    find_elem_by_id("password").send_keys("secret_sauce")
    click_element(find_elem_by_id("login-button"), False)

    logging.info("Adding backpack to cart")
    click_element(find_elem_by_id("add-to-cart-sauce-labs-backpack"), False)
    assert find_elem_by_id("remove-sauce-labs-backpack").text == "Remove"

    logging.info("Clicking on Fleece Jacket")
    click_element(find_elem_by_linktext("Sauce Labs Fleece Jacket"), False)

    logging.info("Verifying Price of Fleece Jacket is $49.99")
    assert find_elem_by_class("inventory_details_price").text == "$49.99"

    logging.info("Adding Fleece Jacket to cart")
    click_element(find_elem_by_id("add-to-cart"), False)
    
    logging.info("Clicking on cart")
    click_element(find_elem_by_class("shopping_cart_badge"), False)

    logging.info("Clicking checkout")
    click_element(find_elem_by_id("checkout"),False)

    logging.info("Entering first, lastname, and zipcode")
    find_elem_by_id("first-name").send_keys("Test")
    find_elem_by_id("last-name").send_keys("Test")
    find_elem_by_id("postal-code").send_keys("00000")
    click_element(find_elem_by_id("continue"),False)

    logging.info("CLicking on Finish Button")
    click_element(find_elem_by_id("finish"),False)

    logging.info("Verfying Order Completion")
    find_elem_by_id("checkout_complete_container")

    # Take a screenshot of the final page and save it as "success.png".
    driver.get_screenshot_as_file("success.png")

# Handle a TimeoutException (occurs when an operation exceeds the set time limit).
except TimeoutException as ex:
    # Print the exception details to the console.
    logging.ERROR("Timeout Exception: " + str(ex))
    # Take a screenshot of the page and save it as "timeout.png".
    driver.get_screenshot_as_file("timeout.png")
                                      
    # Raise a new exception with a custom message to indicate the failure.
    raise Exception("Failed with a TimeoutException")
        

# Handle any other generic exception that may occur.
except Exception as e:
    logging.ERROR("Exception: " + str(e))
    # Take a screenshot of the page and save it as "error.png".
    driver.get_screenshot_as_file("error.png")
    # Re-raise the exception to propagate it further.
    raise
        