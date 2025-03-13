from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Configure Selenium to connect to the existing Edge session
options = webdriver.EdgeOptions()
options.debugger_address = "127.0.0.1:9222"  # Connect to existing Edge session

# Start WebDriver
driver = webdriver.Edge(options=options)

# Open ChatGPT (if not already open)
driver.get("https://chat.openai.com")

# Function to send messages to ChatGPT
def send_chatgpt_message(message):
    try:
        # Find the ChatGPT input field
        input_box = driver.find_element(By.TAG_NAME, "textarea")
        
        # Send message
        input_box.send_keys(message)
        input_box.send_keys(Keys.ENTER)

        time.sleep(2)  # Wait for response to load

        # Get latest ChatGPT response
        responses = driver.find_elements(By.CLASS_NAME, "message")  # Adjust class name if needed
        last_response = responses[-1].text if responses else "No response found."

        return last_response

    except Exception as e:
        return f"Error: {str(e)}"

# Example usage:
response = send_chatgpt_message("Hello, how are you?")
print("ChatGPT response:", response)
