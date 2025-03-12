from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ** Connect to an Already Open Microsoft Edge Browser **
options = webdriver.EdgeOptions()
options.debugger_address = "localhost:9222"  # Connect to running Edge instance

try:
    driver = webdriver.Edge(options=options)
    print("✅ Connected to existing Edge browser.")

    # ** Ensure ChatGPT is Open **
    chatgpt_url = "https://chat.openai.com/"
    if chatgpt_url not in driver.current_url:
        driver.get(chatgpt_url)
        print("🔄 Navigating to ChatGPT...")
        time.sleep(5)  # Wait for it to load

    # ** Wait for ChatGPT Input Box **
    wait = WebDriverWait(driver, 10)
    input_box = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))
    print("✅ ChatGPT is ready!")

    # ** Function to Ask ChatGPT a Question **
    def ask_chatgpt(question):
        """ Sends a question to ChatGPT and retrieves the response. """
        try:
            print(f"💬 Asking: {question}")
            input_box.click()
            input_box.send_keys(question)
            input_box.send_keys(Keys.RETURN)

            # ** Wait for response to appear **
            print("⏳ Waiting for ChatGPT response...")
            time.sleep(8)  # Adjust if response takes longer

            # ** Get the latest response **
            messages = driver.find_elements(By.CLASS_NAME, "message-text")
            response = messages[-1].text if messages else "No response from ChatGPT."

            print(f"🤖 ChatGPT Response: {response}")
            return response

        except Exception as e:
            return f"⚠️ Error interacting with ChatGPT: {e}"

    # ** Test the function **
    user_question = "What is the capital of Canada?"
    chatgpt_answer = ask_chatgpt(user_question)
    print(f"Final Answer: {chatgpt_answer}")

except Exception as e:
    print(f"❌ Failed to connect to Edge browser: {e}")

