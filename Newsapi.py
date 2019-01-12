import requests


def NewsFromBBC():
    # BBC news api
    news_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=db2d23e3260b4b58b6f77741563c76e4"

    # BBC news json response
    bbc_page_response = requests.get(news_url).json()
    article = bbc_page_response["articles"]

    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])

        # Driver Code
if __name__ == '__main__':

        NewsFromBBC()