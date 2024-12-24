from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    sum1='Octopus\t'
    sum2='likes water'
    sum= sum1+sum2  
    return sum

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Make sure to listen on all interfaces