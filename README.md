### Documentation for the Streamlit Dashboard Code

 **Streamlit Dashboard**  allows the user to search for a specific term on Google and display the search result URLs in a table format. The program uses **Selenium** (with **Undetected ChromeDriver**) to automate the Google search, collect links from the search results, and display them using **Streamlit**. Here is a step-by-step explanation of how the code works:

---

### **Libraries Required:**
The following libraries are required to run this code:
1. **Streamlit**: For building the web dashboard.
   - `streamlit as st`
2. **Pandas**: For managing and displaying the search results in a table format.
   - `import pandas as pd`
3. **Selenium**: For web scraping, simulating user interaction on Google, and retrieving search results.
   - `import selenium`
4. **Undetected Chromedriver**: For bypassing detection and using Chrome to scrape Google search results.
   - `import undetected_chromedriver as uc`
  

----

### **Library and Arguments Explanation:**


### **Libraries Used:**

#### 1. **`streamlit`**: 
   - **Purpose**: This library is the core of your dashboard. It allows you to build interactive web applications for data science, machine learning, and automation tasks.
   - **Key Functions**:
     - `st.title()`: Used to set the main title of the Streamlit dashboard.
     - `st.subheader()`: Adds a subheading to the app.
     - `st.text_input()`: Creates a text input box for the user to type search terms.
     - `st.button()`: Creates a button for user interaction.
     - `st.write()`: Displays text or data (such as a table, charts, etc.) in the app.

   **Necessity**: This is used to create the user interface (UI) where the user can enter a search term and view the search results. It powers the entire dashboard's layout.

---

#### 2. **`pandas`**:
   - **Purpose**: Pandas is a powerful data manipulation library. It is used to handle and process data in a tabular form (i.e., DataFrames).
   - **Key Functions**:
     - `pd.DataFrame()`: Converts lists (or other data structures) into a tabular format, which is displayed as a table in the Streamlit app.

   **Necessity**: After collecting search result URLs, we need to store and display the URLs in an organized format. Pandas helps convert the list of URLs into a DataFrame, which is then displayed as a table in Streamlit.

---

#### 3. **`selenium`**:
   - **Purpose**: Selenium is a tool for automating web browsers. It interacts with websites, clicks buttons, submits forms, and scrapes data. It is crucial for automating Google search and scraping the links.
   - **Key Classes and Methods**:
     - `webdriver.Chrome()`: Initializes the Chrome browser instance.
     - `driver.get()`: Opens a URL in the browser (Google search in this case).
     - `find_element(By.NAME, "q")`: Locates the search input field on the Google page by its `name` attribute and sends the query.
     - `find_elements(By.CLASS_NAME, 'yuRUbf')`: Finds all elements containing the search results (with the class name `yuRUbf`).

   **Necessity**: Selenium automates the Google search, interacts with the page to type the query, and scrapes the search result links. Without Selenium, this automation would not be possible.

---

#### 4. **`time`**:
   - **Purpose**: This library provides functions to handle time-related tasks such as delays.
   - **Key Functions**:
     - `time.sleep(seconds)`: Pauses the execution for a specified number of seconds. It is used to wait for elements to load and to simulate user-like behavior.
   
   **Necessity**: Since the Google search results take time to load, `time.sleep()` is used to introduce delays and ensure that the page is fully loaded before the next action is performed.

---

#### 5. **`undetected_chromedriver`**:
   - **Purpose**: This library provides an undetected ChromeDriver that bypasses Google's detection mechanisms. Regular ChromeDriver might be blocked or flagged by Google for scraping activity, but this undetected version is designed to avoid detection.
   - **Key Functions**:
     - `uc.Chrome()`: Initializes the undetected Chrome browser.
   
   **Necessity**: Without this, Google could detect the automated scraping and block access. The undetected driver ensures that the scraping goes unnoticed, making the process smoother and less likely to be interrupted.

---

#### 6. **`selenium.webdriver.common.by.By`**:
   - **Purpose**: This module helps in locating elements on a webpage by different attributes (like `name`, `class`, `id`, etc.).
   - **Key Functions**:
     - `By.NAME`: Locates an element using its `name` attribute.
     - `By.CLASS_NAME`: Locates an element by its `class` name.
     - `By.XPATH`: Locates an element using its XPath (a query language for selecting nodes in XML documents).
   
   **Necessity**: These locators are essential for identifying elements on the webpage to interact with them. In your case, you're locating the search box and search result links using these locators.

---

#### 7. **`selenium.webdriver.common.keys.Keys`**:
   - **Purpose**: This module provides keyboard keys that can be used for sending keyboard inputs programmatically.
   - **Key Functions**:
     - `Keys.RETURN`: Simulates pressing the "Enter" key.
   
   **Necessity**: After typing the search query into the search box, `Keys.RETURN` is used to simulate pressing the "Enter" key, submitting the search.

---

#### 8. **`selenium.webdriver.common.action_chains.ActionChains`**:
   - **Purpose**: This class is used to perform complex user interactions like mouse movements, clicks, and key presses in a sequence.
   - **Necessity**: This could be used to simulate mouse actions or automate scrolling behavior (if needed).

---

#### 9. **`selenium.webdriver.support.ui.WebDriverWait` and `selenium.webdriver.support.expected_conditions`**:
   - **Purpose**: These modules are used to wait for elements to appear or become interactable before interacting with them.
   - **Key Functions**:
     - `WebDriverWait(driver, 10)`: Waits for up to 10 seconds until an element is located or becomes interactable.
     - `EC.presence_of_element_located`: Used to check if an element is present in the DOM.

   **Necessity**: Google search results may take time to load. These waits ensure that the program doesn't try to interact with elements before they are ready, thus avoiding errors.

---

### **Explanation of Key Arguments Used in the Code:**

1. **`"--no-sandbox"`**:
   - **Purpose**: This argument disables the sandbox security feature in Chrome. This is useful when running Chrome in certain environments (like Docker or virtual machines) where sandboxing causes issues.

2. **`"--disable-dev-shm-usage"`**:
   - **Purpose**: This argument disables the usage of the `/dev/shm` file system for shared memory. It is useful in environments with limited shared memory, preventing certain errors related to memory allocation.

3. **`"start-maximized"`**:
   - **Purpose**: This argument starts the Chrome browser in a maximized window. It ensures the browser is large enough to view all the elements and that they load correctly.

4. **`options.add_argument("--headless")`**:
   - **Purpose**: When uncommented, this option runs Chrome in headless mode, which means no browser window will open. This is typically used for automation tasks and when you don’t need to see the UI.

5. **`time.sleep(3)`**:
   - **Purpose**: Pauses the script for 3 seconds to ensure elements are loaded on the page before interacting with them. Without this, the script might attempt actions before the page finishes loading, resulting in errors.

---

### **How the Code Works:**
1. **User Input**: The user enters a search query in the input box and clicks the "Search" button.
2. **Automated Google Search**: The `perform_google_search()` function is called to search for the query on Google using **Undetected ChromeDriver** and **Selenium**.
3. **Scroll and Collect Results**: The program automatically scrolls through the search results and collects URLs from the first three pages.
4. **Displaying Results**: The collected links are stored in a Pandas DataFrame and displayed as a table in the Streamlit dashboard.

### **Execution Flow:**
1. Streamlit loads the UI and waits for the user to enter a search term.
2. When the user clicks "Search," the code automates the Google search and scrapes the results.
3. The results (URLs) are displayed in a table format using **Pandas** and **Streamlit**.

---

This detailed breakdown explains the libraries, arguments, and overall workflow of the Streamlit Dashboard, making it clear how each part contributes to the overall functionality of the project.


----


### **Step-by-Step Code Explanation:**

#### 1. **Title and Dashboard Setup:**

```python
# Title of the Dashboard
st.title('Streamlit Dashboard for Google search result')

# Text input for search functionality
st.subheader("Search for data")
search_query = st.text_input("Enter search term:")
```
- `st.title` sets the main title of the Streamlit dashboard.
- `st.subheader` adds a subtitle.
- `st.text_input` creates an input field where the user can type a search term.

#### 2. **Submit Button:**

```python
# Submit button
submit_button = st.button("Search")
```
- `st.button` generates a button labeled "Search". When clicked, the action triggers the search functionality.

#### 3. **Google Search Functionality:**

The main function, `perform_google_search(search_query)`, is where the Google search is automated using **Selenium** and **Undetected ChromeDriver**.

```python
def perform_google_search(search_query):
    # Setup Undetected ChromeDriver
    options = uc.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("start-maximized")

    # Initialize the undetected driver
    driver = uc.Chrome(options=options)
```
- **Undetected ChromeDriver** is used to avoid detection when accessing Google.
- The `options.add_argument()` lines configure Chrome to run without sandbox restrictions and in a maximized window.

```python
    # Open Google Search
    driver.get("https://www.google.com")

    # Search for the query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)  # Press Enter to submit the search
```
- This part opens **Google** using `driver.get()` and enters the search term (`search_query`) into the search box (`By.NAME, "q"`).

```python
    # Wait for the search results to load
    time.sleep(3)
```
- A `sleep(3)` is used to wait for the results to load before scraping the page.

#### 4. **Scrolling and Collecting Links:**

```python
    link_collection = []
    for i in range(3):  # Loop to iterate through the first 3 pages
        time.sleep(2)
        height = driver.execute_script('return document.body.scrollHeight')  # Get page height
        for i in range(0, height, 30):  # Scroll the page in increments of 30px
            driver.execute_script(f'window.scrollTo(0,{i});')
        time.sleep(2)
        
        # Collect the elements that contain the search results
        collect = driver.find_elements(By.CLASS_NAME, 'yuRUbf')  # These contain the links
        
        # Extract URLs from the 'href' attribute and add to list
        for item in collect:
            link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
            link_collection.append(link)
        
        # Click on the "Next" button to move to the next page
        next_xpath = '//*[@id="pnnext"]/span[2]'
        next_button = driver.find_element(By.XPATH, next_xpath)
        time.sleep(2)
        next_button.click()
```
- This part scrolls the page to load more results (if necessary) and collects the links from the search results (`By.CLASS_NAME, 'yuRUbf'`).
- The loop `for i in range(3)` allows the script to scrape the first three pages of results, collecting the links on each page.
- The script also clicks the **Next** button (`//*[@id="pnnext"]/span[2]`) to load the next page of results.

#### 5. **Return Collected Links:**

```python
    return link_collection
```
- The function returns the list `link_collection` containing the URLs of the search results.

#### 6. **Streamlit Output:**

```python
if submit_button and search_query:
    st.write(f"Searching for: {search_query}")

    # Perform the search and get results
    links = perform_google_search(search_query)

    if links:
        df = pd.DataFrame(links, columns=['Search results'])
        st.write("Search result", df)  # Displaying as a table
```
- When the user clicks the submit button (`submit_button`) and enters a search query, the script runs the `perform_google_search()` function to get the search result links.
- The search results are then displayed in a **pandas DataFrame** using `st.write(df)`. This renders the results in a table format.

#### 7. **Else Condition (Initial State):**

```python
else:
    st.write("Start by entering a search term and click 'Search'!")
```
- This part ensures that the message "Start by entering a search term and click 'Search'!" is displayed when the user hasn't entered a search term or clicked the "Search" button.

---

### **Flow of the Application:**

1. **User Input:**
   - The user enters a search term in the input box and clicks the "Search" button.
   
2. **Search Function:**
   - The program uses **Undetected ChromeDriver** and **Selenium** to search Google for the entered term.
   - The program collects links from the first three pages of Google search results.

3. **Display Results:**
   - The search results (URLs) are displayed in a table format using **pandas** and **Streamlit**.

4. **Output:**
   - The search results are presented as a table in the Streamlit dashboard for the user to view.

---

### **How to Run:**
1. Install the necessary libraries:
   ```bash
   pip install streamlit pandas selenium undetected-chromedriver
   ```
   
2. Save the code into a `.py` file (e.g., `google_search_dashboard.py`).

3. Run the Streamlit app:
   ```bash
   streamlit run google_search_dashboard.py
   ```

---




