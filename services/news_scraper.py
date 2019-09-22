import praw
from config import (
    NA_API_KEY,
    NA_API_LANGUAGE,
    RA_API_CLIENT_ID,
    RA_API_CLIENT_SECRET,
    RA_API_USERNAME,
    RA_API_PASSWORD,
    RA_API_USER_AGENT
)
from newsapi import NewsApiClient


class NewsScrapers:
    def __init__(self):
        # News API settings
        self.news_api_key = NA_API_KEY
        self.news_api_language = NA_API_LANGUAGE
        # Reddit API settings
        self.reddit_client_id = RA_API_CLIENT_ID
        self.reddit_client_secret = RA_API_CLIENT_SECRET
        self.reddit_username = RA_API_USERNAME
        self.reddit_password = RA_API_PASSWORD
        self.reddit_user_agent = RA_API_USER_AGENT
        self.validate_settings_values()

    def validate_settings_values(self):
        """
        desciption: This function validates that third party api settings are not empty.
        """
        members = [attr for attr in dir(self) if
                   not callable(getattr(self, attr)) and not attr.startswith("__")]
        for member in members:
            member_value = getattr(self, member)
            member_key = " ".join([word.title() for word in member.split('_')])
            if not member_value:
                raise Exception("{} value is missing".format(member_key))

    def newsapi_scraper(self, query: str = None):
        """

        :param query: used for search query (optional)
        :return: List of newsapi top headlines within custom format
        """
        format_newsapi_object = lambda _object: {
            'headline': _object['title'],
            'link': _object['url'],
            'source': 'newsapi',
        }

        newsapi = NewsApiClient(api_key=self.news_api_key)
        top_headlines = newsapi.get_top_headlines(language=self.news_api_language, q=query)
        formatted_data = map(format_newsapi_object, top_headlines['articles'])
        return list(formatted_data)

    def redditapi_scraper(self, query: str = None):
        """

        :param query: used for search query (optional)
        :return: List of redditapi top subreddits within custom format
        """
        if not query:
            query = 'all'
        format_redditapi_object = lambda _object: {
            'headline': _object.title,
            'link': 'https://www.reddit.com' + _object.permalink,
            'source': 'reddit',
        }

        reddit = praw.Reddit(client_id=self.reddit_client_id,
                             client_secret=self.reddit_client_secret,
                             user_agent=self.reddit_user_agent,
                             username=self.reddit_username,
                             password=self.reddit_password)
        top_subreddits = reddit.subreddit(query).top(limit=20)
        formatted_data = map(format_redditapi_object, top_subreddits)
        return list(formatted_data)

    def combined_news_data(self, query: str = None):
        """

        :param query: used for search query (optional)
        :return: List of redditapi top subreddits + newsapi top headlines within custom format
        """
        combined_data = list()
        newsapi_data = self.newsapi_scraper(query)
        redditapi_data = self.redditapi_scraper(query)
        combined_data.extend(newsapi_data)
        combined_data.extend(redditapi_data)
        return combined_data
