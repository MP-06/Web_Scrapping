# Import Packages
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bs

def get_trend():

    # URL of website
    url = "https://github.com/trending"
    response = requests.get(url)


    content = response.text

    soup = bs(content, "html.parser")
    # Get values of all block i.e. article tag
    block = soup.find_all("article", {"class": "Box-row"})

    # Create list of different details
    author = []
    repo = []
    lang = []
    star = []
    fork = []

    # Iterate through each block of article tag
    for i in range(len(block)):
        # Get the values title text that is in h1 tag
        title = block[i].find_all("h1", {"class": "h3 lh-condensed"})[0].text
        # Remove extra spaceses from the text values
        title = title.strip().replace(" ", "")
        # Split on the basis of /
        value_list = title.split("/")
        # Append the values of author and repo 
        author.append(value_list[0])
        repo.append(value_list[1][2:])

        # Get the values language that is in span tag
        lang_list = block[i].find_all("span", {"itemprop": "programmingLanguage"})
        # print(lang)
        if (lang_list):
            lang.append(lang_list[0].text)
        else:
            lang.append(np.nan)


        # Get the values star that is in a tag
        star_list = block[i].find_all("a", {"class": "Link--muted d-inline-block mr-3"})
        # Check if star list availabel
        if (star_list):
            # Remove extra spaceses from the text values
            star.append(star_list[0].text.strip())
        else:
            star.append(np.nan)

        
        # Get the values fork that is in a tag
        fork_list = block[i].find_all("a", {"class": "Link--muted d-inline-block mr-3"})
        # Check if star list availabel
        if (fork_list):
            # Remove extra spaceses from the text values
            fork.append(star_list[1].text.strip())
        else:
            fork.append(np.nan)

    # Create dict of trend values
    trend_dict = {
        "Author": author,
        "Repo": repo,
        "Lang": lang,
        "Star": star,
        "Fork": fork,
    }

    # Create dataframe of trend values
    trend_df = pd.DataFrame(trend_dict)
    # print(trend_df.head())

    # Create Csv of the DataFrame
    # trend_df.to_csv("Trending Repos on GitHub")
    return trend_df
