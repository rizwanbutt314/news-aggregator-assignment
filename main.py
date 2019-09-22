from fastapi import FastAPI, Depends
from services.news_scraper import NewsScrapers

# Intializing FastAPI app
app = FastAPI(
    title="News Aggregator App",
    description="This is just an coding assignment app.",
    version="1.0.0",
    docs_url="/api-doc",
    redoc_url=None,
)
# Intializing NewsScrapers instance
news_source = NewsScrapers()


@app.get("/n/news")
def newsapi_headlines(query: str = None):
    """

    :param query: used for search query (optional)
    :return: List of newsapi top headlines
    """
    news_data = news_source.newsapi_scraper(query)
    return news_data


@app.get("/r/news")
def redditapi_headlines(query: str = None):
    """

    :param query: used for search query (optional)
    :return: List of redditapi top subreddits
    """
    news_data = news_source.redditapi_scraper(query)
    return news_data


@app.get("/news")
def combined_headlines(query: str = None):
    """

    :param query: used for search query (optional)
    :return: List of newsapi top headlines + redditapi top subreddits
    """
    news_data = news_source.combined_news_data(query)
    return news_data
