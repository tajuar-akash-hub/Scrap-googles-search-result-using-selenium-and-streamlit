#libraries to instal 
import streamlit as st
import pandas as pd
import numpy as np


from selenium import webdriver
import time
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
#setup undetected web driver
import time
import undetected_chromedriver as uc 








# Title of the Dashboard
st.title('Streamlit Dashboard for Google search results')



# Text input for search functionality
st.subheader("Search for data")
search_query = st.text_input("Enter search term:")

# Submit button
submit_button = st.button("Search")





#function for google search start --------------------------------------------

def perform_google_search(search_query):
    # Setup Undetected ChromeDriver
    options = uc.ChromeOptions()
    # options.add_argument("--headless")  # Optional: Run in headless mode (without GUI)

    options.add_argument("--no-sandbox")  #security feature 
    options.add_argument("--disable-dev-shm-usage")  #  shared memory file system d to create a sandbox error caused by inadequate shared memory.
    options.add_argument("start-maximized")  # This option starts Chrome with a maximized window.

    # Initialize the undetected driver
    driver = uc.Chrome(options=options)

    # Open Google Search
    driver.get("https://www.google.com")

    # Search for the query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)  # Press Enter to submit the search

    # Wait for the search results to load
    time.sleep(3)


    # Wait for the search box to load
    time.sleep(2)


    link_collection = []
    for i in range(3):
        time.sleep(2)
        #scroll 
        height = driver.execute_script('return document.body.scrollHeight') 
        # print(height)
        #scroll
        for i in range(0,height,30):
            driver.execute_script(f'window.scrollTo(0,{i});')

        time.sleep(2)
        # Collect the elements that contain the search results
        collect = driver.find_elements(By.CLASS_NAME, 'yuRUbf')

        time.sleep(2)

        # Extract the URLs from the 'href' attribute of each element and print them
        for item in collect:
            link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')  # Get the href attribute
            # print(link)
            link_collection.append(link)
    
    #click on the next button 

        next_xpath = '//*[@id="pnnext"]/span[2]'
        next_button = driver.find_element(By.XPATH,next_xpath)
        time.sleep(2)
        next_button.click()

    driver.quit()

    return link_collection

#function for google search end --------------------------------------------



# When the submit button is pressed, perform the Google search
if submit_button and search_query:
    st.write(f"Searching for: {search_query}")

    # Perform the search and get results
    links = perform_google_search(search_query)

    # Display the search results (links)

    # st.write(f"Found {len(links)} results:")
    # for link in links:
    #     st.write(link)

    if links:
        df = pd.DataFrame(links,columns=['Search results'])
        st.write("Search result",df)   #dispaying as a table 

else:
    st.write("Start by entering a search term and click 'Search'!")









