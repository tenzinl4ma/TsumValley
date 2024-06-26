from flask import Flask, render_template
from werkzeug.urls import url_quote
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/explore.html')
def explore():
    return render_template('explore.html')
@app.route('/travel.html')
def travel():
    return render_template('travel.html')
@app.route('/news.html')
def news():
    return render_template('news.html')

@app.route('/about.html')
def about():
    return render_template('about.html')
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
    
