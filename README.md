# pyInfoCrawler
Paraguay Information Crawler

## Setup Development Env
1. Install python libs
```bash
$ py3 -m venv venv
$ source ./venv/bin/activate
$ pip install wheel
$ pip install -r requirements.txt
$ docker-compose up -d db
$ bash shell/migratedb.sh
$ cd crawler
$ scrapy crawl infocasas.com.py
```
2. Modify the following config files
    - docker-compose.example.yml
    - crawler/crawler/config.example.yml
    - db/flyway.conf.example