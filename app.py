from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from CI/CD pipeline!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
