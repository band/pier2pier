from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return 'Flask with docker!'
#
@app.route('/page-news')
def page_news():
    return 'page-news has no new pages yet.'
#
@app.route('/ttest')
def template_test():
    return render_template('template.html', my_string="Tap, tap  ...  hello?")
