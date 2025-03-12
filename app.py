import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

def ask_chatgpt(question):
    """Attaches to an existing Edge window, sends a question, and retrieves the response."""
    try:
        print("Assistant: Attaching to existing Edge ChatGPT session...")

        # Set up Edge options to connect to the running instance
        edge_options = webdriver.EdgeOptions()
        edge_options.debugger_address = "127.0.0.1:9222"  # Connect to the open Edge session

        # Attach to the existing Edge window
        driver = webdriver.Edge(options=edge_options)

        print("Assistant: Connected to existing Edge session.")

        # Ensure ChatGPT is loaded
        driver.get("https://chat.openai.com/")  # Make sure the tab is correct

        # Wait for the chat input box to be interactable
        time.sleep(3)  # Small delay to ensure loading
        input_box = driver.find_element(By.TAG_NAME, "textarea")

        # Send the question
        input_box.send_keys(question)
        input_box.send_keys(Keys.RETURN)

        print("Assistant: Waiting for ChatGPT response...")
        time.sleep(10)  # Wait for response

        # Extract response
        messages = driver.find_elements(By.CLASS_NAME, "message-text")
        response = messages[-1].text if messages else "No response from ChatGPT."

        print("Assistant: ChatGPT Response Retrieved!")

        return response

    except Exception as e:
        return f"Error interacting with ChatGPT: {e}"
