from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def ask_chatgpt(question):
    """Sends a question to an open ChatGPT tab in Edge and retrieves the response."""
    try:
        print("Checking for an open ChatGPT tab...")

        # Use an existing Edge session
        options = webdriver.EdgeOptions()
        options.debugger_address = "localhost:9222"  # Connect to Edge debugging

        service = EdgeService(executable_path="C:\\WebDriver\\msedgedriver.exe")  # Adjust path if needed
        driver = webdriver.Edge(service=service, options=options)

        # Check if ChatGPT is open
        if "chat.openai.com" not in driver.current_url:
            return "Error: ChatGPT is not open. Please open it and try again."

        print("Found ChatGPT. Sending query...")

        # Locate the input box
        wait = WebDriverWait(driver, 10)
        input_box = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))

        # Send question
        input_box.send_keys(question)
        input_box.send_keys(Keys.RETURN)

        print("Waiting for response...")
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "message-text")))

        # Get latest response
        messages = driver.find_elements(By.CLASS_NAME, "message-text")
        response = messages[-1].text if messages else "No response received."

        print("ChatGPT Response:", response)
        return response

    except Exception as e:
        return f"Error: {e}"

# **TESTING THE FUNCTION**
if __name__ == "__main__":
    user_question = "What is the capital of Canada?"
    print(ask_chatgpt(user_question))
