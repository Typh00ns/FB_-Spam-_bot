import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

def spam_bot():
    print('Facbook Messenger spam_bot is executing')
    # Use webdriver-manager to automatically handle driver installation
    service = Service(ChromeDriverManager().install())

    options = Options()
    options.add_argument("--headless=new")  # Run Chrome in headless mode
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--enable-logging")
    options.add_argument("--v=1")

    driver = webdriver.Chrome(service=service, options=options)

    email = input("Enter your email or phone number: ")
    password = input("Enter your password : ")

    print('Logging in...Please wait')

    url = 'https://www.facebook.com'
    driver.get(url)

    element_login_id = 'email'
    element_login_pw = 'pass'

    wait = WebDriverWait(driver, 10)
    time.sleep(random.uniform(2, 5))  
    
    text_field_id = wait.until(EC.presence_of_element_located((By.ID, element_login_id)))
    text_field_pw = wait.until(EC.presence_of_element_located((By.ID, element_login_pw)))
    
    id_text = email.strip()
    pw_text = password.strip()
    
    time.sleep(random.uniform(2, 5)) 
    text_field_id.send_keys(id_text)
    
    time.sleep(random.uniform(2, 5)) 
    text_field_pw.send_keys(pw_text)
    
    time.sleep(random.uniform(2, 5)) 
    connect_button_css = 'button[type="submit"]'
    connect_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, connect_button_css)))
    connect_button.click()

    if driver.current_url.startswith("https://www.facebook.com/two_step_verification"):
        print('Please re-run the script')
        driver.quit()

    timeout = 60
    print('__________________________________________________________________________________')
    print(f"Please confirm the connection on your phone or pc. You have {timeout} seconds.")
    print("Press Enter once you've approved the connection.")
    print('If your 2fa connection is not activated press enter')
    print('If the bot was caught by a capthca, just re-run')
    print('__________________________________________________________________________________')
    start_time = time.time()

    while True:
        # Check if the timer has run out
        elapsed_time = time.time() - start_time
        remaining_time = timeout - int(elapsed_time)

        if remaining_time <= 0:
            print("Time's up! Re-run the script and make sure to confirm your login within the time frame .")
            break

        print(f"Time remaining: {remaining_time}s", end="\r", flush=True)

        # Check for user input
        if input() == "":
            print("Connection approved. Proceeding...")
            break

        time.sleep(1)  # Avoid excessive CPU usage

    print('Navigate to the person\'s messenger url and copy it')
    url = input('Please paste the person\'s messenger url: ')
    driver.get(url)
    print('Navigating...')

    text_field_css_selector = '.x14wi4xw'
    wait = WebDriverWait(driver, 10)
    text_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, text_field_css_selector)))

    print('Enter the spamable message')
    message_text = input('Message text: ')
    print('Enter the how many times you want the message to be spammed')
    spam_it = int(input('Spam time : '))
    print(f'You entered: "{message_text}" to be spammed {spam_it} times.')
    print('Sending messages...Please wait')

    for i in range(spam_it):
        for char in message_text:
            text_field.send_keys(char)
            time.sleep(0.0001)
        text_field.send_keys(Keys.ENTER)
    time.sleep(0.5 * spam_it)

    print('Messages sent successfully')
    print('Re-run the script for another spam')
    driver.quit()

if __name__ == "__main__":
    spam_bot()
