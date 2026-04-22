from app import CREATE_APP
from flask import Flask
import os

app = CREATE_APP()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))