from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Data:
    url = "https://www.instagram.com/guviofficial/"

class Suman(Data):

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(3)

    def shutdown(self):
        self.driver.quit()

    # Fetch followers and following count
    def fetch_followers_and_following(self):
        # Assuming you are already logged in or able to bypass the login page
        sleep(5)  # Wait for page to load completely
        
        # XPath for followers and following
        followers_xpath = "//a[contains(@href,'/followers')]/span"
        following_xpath = "//a[contains(@href,'/following')]/span"

        try:
            followers = self.driver.find_element(by=By.XPATH, value=followers_xpath).get_attribute("title")
            following = self.driver.find_element(by=By.XPATH, value=following_xpath).text
        except Exception as e:
            print("Error fetching data:", e)
            return None

        return {"followers": followers, "following": following}

if __name__ == "__main__":
    suman = Suman()
    suman.start()

    # Fetch and print the followers and following count
    followers_and_following = suman.fetch_followers_and_following()
    if followers_and_following:
        print(f"Followers: {followers_and_following['followers']}")
        print(f"Following: {followers_and_following['following']}")
    
    suman.shutdown()