import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


class WebAppTest(unittest.TestCase):

    def setUp(self):
        # Set up Chrome options
        options = Options()
        options.add_argument("--start-maximized")  # Maximize the window
        options.add_argument("--disable-infobars")  # Disable info bars
        options.add_argument("--disable-extensions")  # Disable extensions

        # Use ChromeDriverManager to get the correct driver version
        service = Service(ChromeDriverManager().install())

        # Initialize the WebDriver with options and service
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get("http://collaborative.ase.ro/Pasul1.0.aspx")
        self.driver.implicitly_wait(10)  # Wait time for elements to load

    def test_navigation(self):
        driver = self.driver

        # Step 3: Check the second radio button (RadioButton2)
        radio_button2 = driver.find_element(By.ID, "RadioButton2")
        radio_button2.click()
            # Wait for 5 seconds
        time.sleep(5)
            # navigate to the next step
        next_button = driver.find_element(By.ID, "Button1")
        next_button.click()
        time.sleep(2)

        # Step 4: Select CheckBoxList items 1, 5, 10, then select items 1.1, 1.3, 1.10 from ListBox
            #find the checkboxes
        checkbox_1 = driver.find_element(By.ID, "CheckBoxList1_0")
        checkbox_1.click()

        checkbox_5 = driver.find_element(By.ID, "CheckBoxList1_4")
        checkbox_5.click()

        checkbox_10 = driver.find_element(By.ID, "CheckBoxList1_9")
        checkbox_10.click()
            #wait 5 seconds
        time.sleep(5)

        # Select ListBox items 1.1, 1.3, 1.10
            #find the list
        listbox_items = driver.find_elements(By.XPATH, "//select[@id='ListBox1']/option")
            #select the elements from the ListBox
        listbox_items[0].click()  # Selecting 1.1
        listbox_items[2].click()  # Selecting 1.3
        listbox_items[9].click()  # Selecting 1.10
            #wait 5 seconds
        time.sleep(5)
            # navigate to the next step
        next_button = driver.find_element(By.ID, "Button1")
        next_button.click()
        time.sleep(2)

        # Step 5: Check the second element from CheckBoxList (CRITERII ECOLOGICE)
        checkbox_criteria = driver.find_element(By.ID,
                                                "CheckBoxList1_1")
        checkbox_criteria.click()
            # Wait for 5 seconds
        time.sleep(5)

            #Select items 2.2, 2.7 from ListBox
        listbox_items = driver.find_elements(By.XPATH, "//select[@id='ListBox1']/option")
        listbox_items[1].click()
        listbox_items[6].click()
            # Wait for 5 seconds
        time.sleep(5)
            #navigate to the next step
        next_button = driver.find_element(By.ID, "Button1")
        next_button.click()
        time.sleep(2)

        # Step 6: Fill in the textboxes with values 1, 2, 3, 4, 5, 6
        driver.find_element(By.ID, "TextBox00").send_keys("1")
        driver.find_element(By.ID, "TextBox01").send_keys("2")
        driver.find_element(By.ID, "TextBox10").send_keys("3")
        driver.find_element(By.ID, "TextBox11").send_keys("4")
        driver.find_element(By.ID, "TextBox20").send_keys("5")
        driver.find_element(By.ID, "TextBox21").send_keys("6")
            #wait 5 seconds
        time.sleep(5)

            #navigate to the next step
        next_button = driver.find_element(By.ID, "Button1")
        next_button.click()
        time.sleep(5)

        #Step7: Navigate to the next step
            #navigate to the next step
        next_button = driver.find_element(By.ID, "Button1")
        next_button.click()
            #Wait for 5 seconds
        time.sleep(5)

            #Fill in the textbox with value 9
        driver.find_element(By.NAME, "ctl21").send_keys("9")
        time.sleep(5)
            #click the button "Completeaza matricea"
        complete_matrix_button = driver.find_element(By.NAME, "ctl25")
        complete_matrix_button.click()
        #wait 2 seconds afte click
        time.sleep(2)

        # Step 8: Navigate to next step, export to Word
        next_button = driver.find_element(By.ID, "Button1")
        next_button.click()
            # Wait for 5 seconds
        time.sleep(5)
            # Button ID for exporting to Word
        export_button = driver.find_element(By.ID, "Button1")
        export_button.click()
        time.sleep(2)  # Wait for 2 seconds

        # Step 9: Close the browser window
        self.driver.quit()

    def tearDown(self):
        # Ensure the browser is closed after each test
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)