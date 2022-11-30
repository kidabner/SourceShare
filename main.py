from flask import Flask, Response,send_from_directory
from flask import render_template
import os
app = Flask(__name__)

@app.route('/')
def home():
    fileList = os.listdir('static')
    return render_template('home.html',fileList=fileList)

@app.route("/download/<path:filename>")
def downloader(filename):
    dirpath = os.path.join(app.root_path, 'static')  # 这里是下在目录，从工程的根目录写起，比如你要下载static/js里面的js文件，这里就要写“static/js”
    return send_from_directory(dirpath, filename, as_attachment=True)  # as_attachment=True 一定要写，不然会变成打开，而不是下载
app.run('0.0.0.0',5000)
