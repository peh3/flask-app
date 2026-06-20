import threading
# Simple web application using Flask framework
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, TK!</p>"

@app.route("/home")
def home():
    return "<p>Welcome Home!</p>"

@app.route("/thread-check")
def thread_check():
    # Returns the name of the thread handling this specific request
    current_thread = threading.current_thread().name
    return f"<p>Active Request Thread Name: {current_thread}</p>"

#if __name__ == '__main__':
#    app.run(host="0.0.0.0", port=8080)

if __name__ == '__main__':
    # Force single-threaded execution (requests will block sequentially)
    app.run(host="0.0.0.0", port=8080, threaded=False)
    
    # Force multi-threaded execution explicitly
    # app.run(host="0.0.0.0", port=8080, threaded=True)