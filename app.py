from app import CREATE_APP
from flask import Flask

app = CREATE_APP()

if __name__ == '__main__':
    app.run(debug=True)