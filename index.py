from flask import Flask, render_template
import os


app = Flask(__name__)

def env_override(value, key):
  return os.getenv(key, value)

@app.route('/')
def home():
    return render_template('index.html', a_variable=os.getenv('VERCEL_ENV', 'VERCEL_ENV not found'))

@app.route('/about')
def about():
    return 'About'