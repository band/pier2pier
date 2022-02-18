from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return 'Flask with docker!'
#
@app.route('/page-news')
def page_news():
    return 'page-news has no new pages yet.'
