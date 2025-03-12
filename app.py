from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def ask_chatgpt(question, session_url):
    """
    Opens Microsoft Edge to the specified ChatGPT session URL,
    sends a question, and retrieves the response.
    """
    try:
        print("Assistant: Opening Edge to your specified ChatGPT session...")
        # Set up Edge options
        options = webdriver.EdgeOptions()
        # (Do not use debugger_address here so it opens a new session)
        # You can add other options if needed
        
        # Initialize the Edge WebDriver (ensure msedgedriver is in PATH or specify full path)
        driver = webdriver.Edge(options=options)
        
        # Navigate to your specific ChatGPT session URL
        driver.get(session_url)
        time.sleep(5)  # Wait for the page to load

        # Attempt to locate the chat input box
        print("Assistant: Locating the chat input box...")
        input_box = driver.find_element(By.TAG_NAME, "textarea")
        input_box.click()
        input_box.send_keys(question)
        input_box.send_keys(Keys.RETURN)

        print("Assistant: Waiting for ChatGPT response...")
        time.sleep(10)  # Wait for ChatGPT to process and respond

        # Get the latest response
        messages = driver.find_elements(By.CLASS_NAME, "message-text")
        response = messages[-1].text if messages else "No response from ChatGPT."
        print("Assistant: ChatGPT Response Retrieved!")
        
        driver.quit()  # Close the browser window
        return response

    except Exception as e:
        return f"Error interacting with ChatGPT: {e}"

if __name__ == "__main__":
    # Replace with your dedicated ChatGPT session URL.
    SESSION_URL = "https://chat.openai.com/chat"  # Example URL; update as needed.
    
    question = "What is the capital of Canada?"
    answer = ask_chatgpt(question, SESSION_URL)
    print("Final Answer:", answer)

