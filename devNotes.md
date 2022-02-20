# 2022-02-17 Flask in Docker dev notes

Conceptual architecture of what this project is working towards is this ![diagram:](/pier2pier%20v0%20conceptual%20diagram%202022-02-16-001.png)

PK suggested this link <https://medium.com/swlh/flask-docker-the-basics-66a699aa1e7d> as a place to start
and, Yay!, it works!

## 2022-02-19 notes

1. David Duncan led me to this web page:
  <https://medium.com/swlh/alpine-slim-stretch-buster-jessie-bullseye-bookworm-what-are-the-differences-in-docker-62171ed4531d>
  
  This in turn yielded this resource:
  <https://hub.docker.com/_/python/>
  
  And this in turn led me to thinking that our Docker image will *not*
  be using Alpine, but rather one of the latest Python version "slim"
  images based on Debian releases ("buster" is the current stable
  release).
  
## 2022-02-20 notes

1. adding jinja2 code; the following Flask routes work:
```
  localhost:5001/
  localhost:5001/ttest
  localhost:5001/page-news
```

