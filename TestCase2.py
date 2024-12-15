import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class WebAppTest(unittest.TestCase):

    def setUp(self):
        # Set up Chrome options to avoid potential issues
        options = Options()
        options.add_argument("--start-maximized")  # Maximize the window
        options.add_argument("--disable-infobars")  # Disable info bars
        options.add_argument("--disable-extensions")  # Disable extensions
        
        # Use ChromeDriverManager to get the correct driver version
        service = Service(ChromeDriverManager().install())
        
        # Initialize the WebDriver with options and service
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.get("http://collaborative.ase.ro/Pasul1.0.aspx")  # URL of the page
        self.driver.implicitly_wait(10)  # Wait time for elements to load

    def test_navigation(self):
        driver = self.driver
        
        # Step 3: Check the second radio button (RadioButton2)
        radio_button2 = driver.find_element(By.ID, "RadioButton2")
        radio_button2.click()
        time.sleep(2)  # Wait for 2 seconds
        
        # Step 4: Click the "Pasul urmator" button after selecting RadioButton2
        pasul_urmator_button = driver.find_element(By.ID, "Button1")  # The "Pasul urmator" button
        pasul_urmator_button.click()  # Click the "Pasul urmator" button to move to the next step
        time.sleep(2)  # Wait for 2 seconds
        
        # Step 5: Select CheckBoxList items 1, 5, 10, then select items 1.1, 1.3, 1.10 from ListBox
        checkbox_1 = driver.find_element(By.ID, "CheckBoxList1_0")  # Example: Use the CheckBoxList ID and option
        checkbox_1.click()
          
        checkbox_5 = driver.find_element(By.ID, "CheckBoxList1_4")  # Modify based on your inspection
        checkbox_5.click()
        
        checkbox_10 = driver.find_element(By.ID, "CheckBoxList1_9")  # Modify based on your inspection
        checkbox_10.click()
        time.sleep(2)
        
        # Select ListBox items 1.1, 1.3, 1.10
        listbox_items = driver.find_elements(By.XPATH, "//select[@id='ListBox1']/option")
        listbox_items[0].click()  # Selecting 1.1 (index 0)
        listbox_items[2].click()  # Selecting 1.3 (index 2)
        listbox_items[9].click()  # Selecting 1.10 (index 9)
        time.sleep(2)
        
        # Step 6: Click the "Pasul urmator" button after the selections
        pasul_urmator_button = driver.find_element(By.ID, "Button1")
        pasul_urmator_button.click()  # Click the "Pasul urmator" button
        time.sleep(2)  # Wait for 2 seconds

        # Step 7: Select the second checkbox (CRITERII ECOLOGICE)
        checkbox_criteria = driver.find_element(By.ID, "CheckBoxList1_1")  # This targets the second checkbox (CRITERII ECOLOGICE)
        checkbox_criteria.click()
        time.sleep(2)  # Wait for 5 seconds 

        # Step 8: Select items 2.2, 2.7 from ListBox
        listbox_items = driver.find_elements(By.XPATH, "//select[@id='ListBox1']/option")
        listbox_items[1].click()  # Selecting 2.2 (index 7)
        listbox_items[6].click()  # Selecting 2.7 (index 12)
        time.sleep(2)  # Wait for 5 seconds

        pasul_urmator_button = driver.find_element(By.ID, "Button1")  # The "Pasul urmator" button
        pasul_urmator_button.click()  # Click the "Pasul urmator" button to move to the next step
        time.sleep(2) 

        # Step 9: Fill in the textboxes with values 1, 2, 3, 4, 5, 6
        driver.find_element(By.ID, "TextBox00").send_keys("1")  # For "2.2 Volumul (cantitatea) de DEEE tratate"
        driver.find_element(By.ID, "TextBox01").send_keys("2")  # For "2.7 Consumul de energie pe unitatea de DEEE reciclat"
        driver.find_element(By.ID, "TextBox10").send_keys("3")  # For "1.1 Aparate frigorifice de mari dimensiuni"
        driver.find_element(By.ID, "TextBox11").send_keys("4")  # For "1.3 Aparate frigorifice / Congelatoare"
        driver.find_element(By.ID, "TextBox20").send_keys("5")  # For "1.10 Plite electrice"
        driver.find_element(By.ID, "TextBox21").send_keys("6")  # For the second value related to "2.7 Consumul de energie"
        time.sleep(2)  # Wait for 5 seconds after filling in the textboxes

        # Step 10: Click the "Pasul urmator" button to go to the next page
        pasul_urmator_button = driver.find_element(By.ID, "Button1")
        pasul_urmator_button.click()  # Click the "Pasul urmator" button
        time.sleep(2)  # Wait for 2 seconds
        
        # Step 11: Click the "Pasul urmator" button to go to the next page
        pasul_urmator_button = driver.find_element(By.ID, "Button1")
        pasul_urmator_button.click()  # Click the "Pasul urmator" button
        time.sleep(2)  # Wait for 2 seconds

        # Step 12: Fill in the textbox with value 9 and click the "Completează matrice" button
        # Locate the textbox and input the value 9
        textbox = driver.find_element(By.NAME, "ctl21")
        textbox.clear()
        textbox.send_keys("9")
        time.sleep(2)

        # Locate and click the "Completează matrice" button
        completeaza_matrice_button = driver.find_element(By.NAME, "ctl25")
        completeaza_matrice_button.click()
        time.sleep(2)

        # After completing the matrix, click the "Pasul urmator" button
        pasul_urmator_button = driver.find_element(By.ID, "Button1")
        pasul_urmator_button.click()
        time.sleep(2)

        # Step 13: Navigate to next step, export to Word
        export_button = driver.find_element(By.ID, "Button1")
        export_button.click()  # Assuming there is a button to export to Word
        time.sleep(2)  # Wait for 5 seconds

        # Step 14: Close the browser window
        self.driver.quit()
    
    def tearDown(self):
        # Ensure the browser is closed after each test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
