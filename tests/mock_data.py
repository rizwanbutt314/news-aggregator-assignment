class MockData:
    """
    description: This class contains the mock data which is being used by tests to avoid direct api hitting.
    """
    @staticmethod
    def newsapi_data(_input=None):
        """
        :param _input: optional
        :return: List of newsapi mocked data objects
        """
        return [
            {"headline": "Test1", "link": "http://abc1.com", "source": "newsapi"},
            {"headline": "Test2", "link": "http://abc2.com", "source": "newsapi"},
            {"headline": "Test3", "link": "http://abc3.com", "source": "newsapi"},
        ]

    @staticmethod
    def redditapi_data(_input=None):
        """
        :param _input: optional
        :return: List of redditapi mocked data objects
        """
        return [
            {"headline": "Test4", "link": "http://abc4.com", "source": "reddit"},
            {"headline": "Test5", "link": "http://abc5.com", "source": "reddit"},
            {"headline": "Test6", "link": "http://abc6.com", "source": "reddit"},
        ]

    @staticmethod
    def combined_data(_input=None):
        """
        :param _input: optional
        :return: List of newsapi + redditapi mocked data objects
        """
        combined_data = list()
        newsapi_data = MockData.newsapi_data()
        redditapi_data = MockData.redditapi_data()
        combined_data.extend(newsapi_data)
        combined_data.extend(redditapi_data)

        return combined_data
