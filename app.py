from flask import Flask, render_template, request, jsonify
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)

def ask_chatgpt(question):
    """ Opens ChatGPT in Edge, sends a question, and retrieves the response. """
    try:
        print("Assistant: Opening ChatGPT...")

        options = webdriver.EdgeOptions()
        options.add_experimental_option("detach", True)  # Keeps browser open

        driver = webdriver.Edge(options=options)
        driver.get("https://chat.openai.com/")

        wait = WebDriverWait(driver, 15)

        print("Assistant: Waiting for input box...")
        input_box = wait.until(EC.element_to_be_clickable((By.TAG_NAME, "textarea")))

        input_box.click()
        input_box.send_keys(question)
        input_box.send_keys(Keys.RETURN)

        print("Assistant: Waiting for ChatGPT response...")
        time.sleep(10)  # Allow ChatGPT to respond

        messages = driver.find_elements(By.CLASS_NAME, "message-text")
        response = messages[-1].text if messages else "No response from ChatGPT."

        print("Assistant: Response received!")
        driver.quit()  # Close the browser
        return response

    except Exception as e:
        return f"Error with ChatGPT: {e}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data.get('message', '')

    # Send query to ChatGPT
    response = ask_chatgpt(user_message)
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
