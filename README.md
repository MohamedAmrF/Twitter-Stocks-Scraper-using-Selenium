# Stock Ticker Mention Scraper

This Python script allows users to track the mention of a specific stock ticker on Twitter within a defined time interval. The script uses Selenium to automate the web browser and scrape the data from Twitter. 

## Prerequisites

- Python 3.x
- Selenium
- BeautifulSoup
- Chrome WebDriver

## Installation

1. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

2. Download and install the Chrome WebDriver from [here](https://developer.chrome.com/docs/chromedriver/downloads) in the following path.
> C:\Program Files (x86)\chromedriver.exe

## Configuration
Update the USERNAME and PASSWORD variables in the script with your Twitter login credentials.

## Script Usage
Before running the script add the username and password of your twitter account in lines 14 and 15.
1. Run the script:

```bash
python ticker_scraper.py
```

2. Follow the prompts to input:
- The number of Twitter URLs to scrape.
- Each Twitter URL.
- The stock ticker you want to track.
- The time interval (in minutes) for tracking mentions of the ticker.

## Example
```bash
How many URLs do you want to enter? 2
Enter URL 1: https://twitter.com/someuser
Enter URL 2: https://twitter.com/anotheruser
Enter a stock ticker (3 or 4 uppercase characters only): $AAPL
You entered: $AAPL
Enter a time interval in minutes: 60
You entered: 60 minutes
```
## Output

The script will output the number of times the specified stock ticker was mentioned in the tweets from the provided URLs within the given time interval. For example:
```
$AAPL was mentioned 5 times in the last 60 minutes.
```

## Detailed Script Explanation
1. Global Variables:
- cnt: Counter for the number of mentions.
- scroll: Amount to scroll down in pixels.
- scroll_delay: Delay between each scroll action.
- USERNAME and PASSWORD: Twitter login credentials.
- found: Dictionary to map the date of the tweet to whether the ticker was found.
- breaker_limit: Number of times to scroll to the bottom of the page before stopping if tweets are out of the interval.

2. User Input:

The script prompts the user to input the number of URLs, the URLs themselves, the stock ticker, and the time interval in minutes.

3. Twitter Login:

The script uses Selenium to log into Twitter with the provided credentials.

4. Scraping Tweets:

The script navigates to each URL and scrolls down the page, extracting tweets and their timestamps. It stops scrolling after reaching a set limit of tweets outside the time interval.

5. Ticker Mention Check:

For each tweet, the script checks if the specified ticker is mentioned and if the tweet is within the given time interval. If both conditions are met, it records the mention.

6. Output the Result:

Finally, the script counts and prints the number of times the ticker was mentioned in the specified time interval.

## Notes
- The script uses hardcoded values for scrolling and delays, which may need adjustment based on the user's internet speed and Twitter's response time.
- Ensure the Chrome WebDriver version matches the installed Chrome browser version.
- Handle Twitter's rate limiting and login protection mechanisms appropriately.

This README provides a comprehensive guide on setting up and using the Twitter stock ticker mention scraper. Happy tracking!