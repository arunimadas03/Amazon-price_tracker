import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from faker import Faker
import time
from datetime import datetime
from os import system
import pandas as pd

# Insert the product url HERE
url="https://www.amazon.in/Airdopes-141-Playtime-Resistance-Bluetooth/dp/B09N3ZNHTY/"

# function to bypass bot detection 
def get_soup_retry(url):
      fake = Faker()
      uag_random = fake.user_agent()

      header = {
        'User-Agent': uag_random,
        'Accept-Language': 'en-US,en;q=0.9'
      }
      isCaptcha = True
      while isCaptcha:
        page = requests.get(url, headers=header)
        assert page.status_code == 200
        soup = BeautifulSoup(page.content, 'html.parser')
        if 'captcha' in str(soup):
            uag_random = fake.user_agent()
            print(f'\rBot has been detected... retrying ... use new identity: {uag_random} ', end='', flush=True)
            continue
        else:
            print('Bot bypassed')
            return soup
        

# To view the html from the url in a text file 
#with open('output.txt', 'w', encoding='utf-8') as f:   
     # with redirect_stdout(f):
      #  print(get_soup_retry(url))


# To extract the price from the html 
price_element = get_soup_retry(url).select_one('span.a-offscreen')
price= (price_element.text.replace('₹', '').replace(',', ''))
print("The current price:", price)
timestamp = time.strftime('%Y-%m-%d %H:%M:%S')


# function to take values from a text file and plot a graph
# Replace 'your_data.txt' with the actual filename
df = pd.read_csv('price_history.txt', names=['timestamp', 'price'])

# Convert the 'timestamp' column to datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d %H:%M:%S')

plt.figure(figsize=(7, 5))
plt.plot(df['timestamp'], df['price'])
plt.xlabel('Timestamp')
plt.ylabel('Price')
plt.title('Price History')
plt.grid(True)
plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjusts plot to fit labels

plt.savefig('price_history.png') # Saves the plot for viewing in future
plt.show()


# function to track the price at a fixed interval and save the output in a text file
def track_price(url, filename='price_history.txt', interval=3600):
      while True:
        price1 = price 
        if price1:
          with open(filename, 'a') as f:
            f.write(f"{timestamp},{price}\n")
          print(f"Price at {timestamp}: {price1}")
        else:
         print(f"Price not found at {timestamp}")

        time.sleep(interval)  
track_price(url)        
    



