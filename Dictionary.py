"""Real-Time searching for the meaning of a word suggested by the user and looking at the results.
    Displays the 'Part of Speech' and  'Meaning' of the word"""

import bs4, requests, textwrap, json


def word_meaning():
    x = 'y'
    while x == 'y':
        # Taking input from the user and checking if it's a valid word
        word_to_search = input("Please enter the word you want to search")
        with open('Dictionary_Words.json') as f:
            data = json.load(f)
            if word_to_search not in data:
                print("Please enter a valid word")
                continue

        # Generating the URL and getting the data from the page
        url = "https://www.google.com/search?q=" + word_to_search + "+meaning"
        request_result = requests.get(url)
        soup = bs4.BeautifulSoup(request_result.text, "lxml")

        # Looking for the div class which has the part_of_speech meaning.
        toc = soup.find("div", class_='BNeawe s3v9rd AP7Wnd')

        # Converting to a list for better slicing of result
        ss = toc.text.split()
        pos = ss[0]
        mean = " ".join(ss[1:])
        para_mean = textwrap.fill(textwrap.dedent(mean), subsequent_indent='   ' * 3, width=150)

        # Displaying the results to the user
        print("The part of speech is --", pos.capitalize())
        print(f"The meaning of *{word_to_search}* is --", para_mean)
        print("Click on the link for more information --", url)

        x = input("Press y to search again or n to exit")
        print('\n')


word_meaning()
