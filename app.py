from flask import Flask, render_template, request, send_file, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)