import pytest
from main import app, news_source
from .mock_data import MockData
from starlette.testclient import TestClient

# Initializing test client
client = TestClient(app)


@pytest.fixture(autouse=True)
def map_mock_data(monkeypatch):
    """
    description: This function map the mock data with pytest session
    """
    monkeypatch.setattr(news_source, 'newsapi_scraper', MockData.newsapi_data)
    monkeypatch.setattr(news_source, 'redditapi_scraper', MockData.redditapi_data)
    monkeypatch.setattr(news_source, 'combined_news_data', MockData.combined_data)


def test_newsapi_headlines():
    """
    description: It is to test the newsapi related endpoint of api
    """
    response = client.get("/n/news")
    response_data = response.json()
    assert response.status_code == 200
    assert len(response_data) == 3
    assert response_data[0]['source'] == 'newsapi'
    assert response_data[1]['source'] == 'newsapi'
    assert response_data[2]['source'] == 'newsapi'
    assert response_data[0]['headline'] == 'Test1'
    assert response_data[1]['headline'] == 'Test2'
    assert response_data[2]['headline'] == 'Test3'


def test_redditapi_headlines():
    """
    description: It is to test the redditapi related endpoint of api
    """
    response = client.get("/r/news")
    response_data = response.json()
    assert response.status_code == 200
    assert len(response_data) == 3
    assert response_data[0]['source'] == 'reddit'
    assert response_data[1]['source'] == 'reddit'
    assert response_data[2]['source'] == 'reddit'
    assert response_data[0]['headline'] == 'Test4'
    assert response_data[1]['headline'] == 'Test5'
    assert response_data[2]['headline'] == 'Test6'


def test_combined_headlines():
    """
    description: It is to test the combined news related endpoint of api
    """
    response = client.get("/news")
    response_data = response.json()
    assert response.status_code == 200
    assert len(response_data) == 6
    assert response_data[0]['source'] == 'newsapi'
    assert response_data[1]['source'] == 'newsapi'
    assert response_data[2]['source'] == 'newsapi'
    assert response_data[3]['source'] == 'reddit'
    assert response_data[4]['source'] == 'reddit'
    assert response_data[5]['source'] == 'reddit'
