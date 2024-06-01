from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta, date
from urllib.parse import urlparse
from utilities.utils import * 
import time
import os

# Global Variables
cnt = 0             # Final Answer (counts number of tickers)
scroll = 100        # Amount of scroll
scroll_delay = 0.25 # Delay between each scroll and the other
USERNAME = ''
PASSWORD = ''
found = {}          # Maps date to if the ticker is found in the post
breaker_limit = 30  # Number of times to scroll to the bottom of the page while detecting tweets out of interval
twitter_login = "https://twitter.com/i/flow/login"


# update the path to the location of the chromedriver.exe file
os.environ['PATH'] += r"C:\Program Files (x86)\chromedriver.exe"


# Input of user
############################################################################################################
# Ask the user for the number of URLs
num_urls = int(input("How many URLs do you want to enter? "))

# Initialize an empty list to store the URLs
urls = []

# Get the URLs from the user
for i in range(num_urls):
    while True:
        url = input(f"Enter URL {i+1}: ")
        # Validate the URL
        try:
            result = urlparse(url)
            # Check if the URL has a network location (netloc) and a scheme (http or https)
            if all([result.scheme, result.netloc]):
                urls.append(url)
                break
            else:
                print("Invalid URL. Please enter a valid URL.")
        except ValueError:
            print("Invalid URL. Please enter a valid URL.")

# Ask the user for a stock ticker
ticker = input("Enter a stock ticker (3 or 4 uppercase characters only): $")

# Check if the ticker is 3 or 4 characters long
while len(ticker) < 3 or len(ticker) > 4 or not ticker.isupper():
    print("Invalid ticker. Please enter a ticker that is 3 or 4 characters long.")
    ticker = input("Enter a stock ticker (3 or 4 uppercase characters only): $")


ticker = '$' + ticker
print(f"You entered: {ticker}")
# Ask the user for a time interval in minutes
time_interval = int(input("Enter a time interval in minutes: "))

print(f"You entered: {time_interval} minutes")


# Open twitter login page
driver = webdriver.Chrome()
driver.get(twitter_login)
time.sleep(10)

# Enter username
username = driver.find_element(By.TAG_NAME, "input")
username.send_keys(USERNAME)

# Click next
all_buttons = driver.find_elements(By.XPATH, "//button[@role='button']")
next_button = all_buttons[-3]
next_button.click()

time.sleep(5)
# Enter password
secret = driver.find_element(By.XPATH, "//input[@type='password']")
secret.send_keys(PASSWORD)

# Click login
all_buttons = driver.find_elements(By.XPATH, "//button[@role='button']")
login_button = all_buttons[-2]
login_button.click()
time.sleep(5)

today = datetime.today()

# Calculate the start date for scraping
today_minutes = convert_date_to_minutes(today)
scrape_start = today_minutes - time_interval
scrape_start = convert_minutes_to_date(scrape_start)
scrape_start = scrape_start.strftime("%Y-%m-%d")
print(f"Scrape start: {scrape_start}")


for url in urls:
    driver.get(url)
    time.sleep(5)
    breaker = 0
    while True:
        driver.execute_script("window.scrollBy(0, " + str(scroll) + ")", "")
        time.sleep(scroll_delay)
        tweet = driver.find_element(By.XPATH, "//div[@class='css-175oi2r r-1iusvr4 r-16y2uox r-1777fci r-kzbkwu']")
        tweet_date = driver.find_element(By.XPATH, ".//time")
        tweet_date = tweet_date.get_attribute("datetime")
        tweet_date = datetime.strptime(tweet_date, '%Y-%m-%dT%H:%M:%S.%fZ')

        try:
            tweet_text = tweet.find_element(By.XPATH, ".//div[@class='css-146c3p1 r-8akbws r-krxsd3 r-dnmrzs r-1udh08x r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-bnwqim']").text
        except:
            tweet_text = ""

        difference = today - tweet_date
        difference = difference.total_seconds() / 60

        if difference > time_interval:
            breaker += 1
        if breaker == 30:
            break

        if ticker in tweet_text and difference < time_interval:
            found[tweet_date] = 1

for val in found:
    cnt += 1

print(f"{ticker} was mentioned {cnt} times in the last {time_interval} minutes.")
