**Framework**: FastAPI

**Pre-requisites:**
* Python 3.6+
* Update settings for NewsAPI and RedditAPI in config.py file.

**Command to install App related Dependicies:**
* pip install -r requirements.txt

**Commad to run app:**
* uvicorn main:app

**Commad to run app tests:**
* pytest tests/test_*.py

**Description:**
This API contains following endpoints for serving data:
* **/r/news** (return list of redditapi related data)
* **/n/news** (return list of newsapi related data)
* **/news**   (return list of newsapi+redditapi related data)

All above endpoints support query search feature just as follow:
* `/news?query=abc`
* `/r/news?query=abc`
* `/n/news?query=abc`

This API also has a swagger based UI where you can execute the APIs directly. This UI will be accessible on following URL:
* `http(s)://ip:port/api-doc`