# Import Packages
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs

# URL of website
url = "https://github.com/topics"
response = requests.get(url)
# print(response.status_code)
content = response.text
soup = bs(content, "html.parser")
# print(soup)

block = soup.find_all("div", {"class": "py-4 border-bottom"})
# print(block)

title = []
description = []

for i in range(len(block)):
    # Get the values title text that is in h1 tag
    title_1 = block[i].find_all("p", {"class": "f3 lh-condensed mb-0 mt-1 Link--primary"})[0].text
    # Remove extra spaceses from the text values
    title_1 = title_1.strip().replace(" ", "")
    # Append the values of author and repo 
    title.append(title_1)

    description_1 = block[i].find_all("p", {"class": "f5 color-text-secondary mb-0 mt-1"})
    # Check if description available
    if (description_1):
        description_1 = description_1[0].text.replace("\n", "").strip()
        description.append(description_1)
    else:
        description.append(np.nan)

    # for i in range(len(title)):
    #     print("title ===>", title[i])
    #     print("title ===>", description[i])

topic_dict = {
    "Title": title,
    "Description": description
}

# Create dataframe of trend values
topic_df = pd.DataFrame(topic_dict)
# print(trend_df.head())

# Create Csv of the DataFrame
topic_df.to_csv("Featured Topics on Github")
