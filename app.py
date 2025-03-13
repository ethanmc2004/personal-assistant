import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re

def ask_chatgpt(question):
    """Sends a question to an existing ChatGPT session and retrieves structured response."""
    try:
        print("Assistant: Connecting to ChatGPT...")

        # Connect to existing Edge session
        edge_options = webdriver.EdgeOptions()
        edge_options.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Edge(options=edge_options)

        # Ensure ChatGPT tab is active
        driver.get("https://chat.openai.com/")
        time.sleep(3)

        # Locate and send the question
        input_box = driver.find_element(By.TAG_NAME, "textarea")
        input_box.send_keys(question)
        input_box.send_keys(Keys.RETURN)

        print("Assistant: Waiting for ChatGPT response...")
        time.sleep(10)

        # Extract latest response
        messages = driver.find_elements(By.CLASS_NAME, "message-text")
        response = messages[-1].text if messages else "NO_ACTION"

        print(f"ChatGPT Response: {response}")

        # Process response
        return handle_chatgpt_response(response)

    except Exception as e:
        return f"Error: {e}"

def handle_chatgpt_response(response):
    """Checks if the response contains an action trigger and executes it."""
    if response.startswith("SET_TIMER|"):
        _, time_value, reason = response.split("|")
        return set_timer(time_value, reason)

    elif response.startswith("ADD_EVENT|"):
        _, event_details = response.split("|", 1)
        return add_calendar_event(event_details)

    elif response.startswith("SET_REMINDER|"):
        _, time_value, message = response.split("|")
        return set_reminder(time_value, message)

    elif response.startswith("SEARCH_WEB|"):
        _, query = response.split("|", 1)
        return search_web(query)

    elif response.startswith("OPEN_APP|"):
        _, app_name = response.split("|", 1)
        return open_application(app_name)

    return response  # If no action, return ChatGPT’s original response

def set_timer(time_value, reason):
    """Sets a timer for a given time and reason."""
    print(f"🔔 Timer set for {time_value} - {reason}")
    return f"Timer set for {time_value} - {reason}"

def add_calendar_event(event_details):
    """Adds an event to the calendar (to be implemented with iOS shortcuts)."""
    print(f"📅 Calendar event added: {event_details}")
    return f"Calendar event added: {event_details}"

def set_reminder(time_value, message):
    """Creates a reminder (to be implemented with iOS Shortcuts or notifications)."""
    print(f"🔔 Reminder set at {time_value}: {message}")
    return f"Reminder set for {time_value}: {message}"

def search_web(query):
    """Opens a Google search in the browser."""
    print(f"🌍 Searching web for: {query}")
    return f"Searching the web for: {query}"

def open_application(app_name):
    """Attempts to open a specified application (placeholder)."""
    print(f"🚀 Opening {app_name}...")
    return f"Opening {app_name}..."

# Example usage
if __name__ == "__main__":
    user_input = "Remind me to call Kate at 7 PM"
    result = ask_chatgpt(user_input)
    print(f"Result: {result}")
