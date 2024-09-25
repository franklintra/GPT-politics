from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException
import time
from askgpt import GPTResponseParser
from config import Config

class PolitiscalesQuiz:
    def __init__(self):
        self.config = Config()
        self.driver = None
        self.gpt_parser = GPTResponseParser()

    def run(self):
        if not self._initialize_driver():
            print("Failed to initialize the WebDriver. Exiting.")
            return
        self._open_website()
        self._answer_questions()
        self._save_results()
        self._close_browser()

    def _initialize_driver(self):
        try:
            service = FirefoxService(GeckoDriverManager().install())
            self.driver = webdriver.Firefox(service=service)
            return True
        except WebDriverException as e:
            print(f"Failed to initialize Firefox WebDriver: {e}")
            return False

    def _open_website(self):
        self.driver.get("https://politiscales.fr/quiz")
        if self.config.debug:
            print("Opened the website")
        time.sleep(1)
        self.driver.refresh()
        if self.config.debug:
            print("Reloaded the page")

    def _get_question_text(self):
        question_element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "question-text"))
        )
        if self.config.debug:
            print(f"Got question: {question_element.text}")
        return question_element.text

    def _click_button(self, response):
        if self.config.debug:
            print(f"Trying to click button: {response}")
        button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f"button.{response}"))
        )
        button.click()

    def _answer_questions(self):
        try:
            while True:
                if self.config.debug:
                    print("Starting new question")
                question = self._get_question_text()
                response = self.gpt_parser.parse_gpt_response(question)
                self._click_button(response)
                time.sleep(0.01)
        except Exception as e:
            if self.config.debug:
                print(f"Exception occurred: {str(e)}")
            print("Quiz completed")
    def _save_qa_history(self):
        try:
            if self.config.save_response:
                self.gpt_parser.save_qa_history()
        except Exception as e:
            if self.config.debug:
                print(f"Error saving responses: {str(e)}")
            print("Failed to save responses")
    
    def _save_html(self):
        pass
    
    def _save_results(self):
        self._save_qa_history()
        self._save_html()
        
    def _close_browser(self):
        if self.driver:
            input("Press Enter to close the browser...")
            self.driver.quit()
            if self.config.debug:
                print("Browser closed")
        else:
            print("No browser instance to close.")

if __name__ == "__main__":
    quiz = PolitiscalesQuiz()
    quiz.run()
