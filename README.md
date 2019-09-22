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

This API also has an swagger based ui where you can execute 
the apis directly.This ui will be accessible on following url:
* `http(s)://ip:port/api-doc`