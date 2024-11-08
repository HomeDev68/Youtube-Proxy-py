from flask import Flask, request, send_file, render_template_string
import requests
import os
import time
import yt_dlp

app = Flask(__name__)
app.config['PORT'] = 4567
app.config['PUBLIC_FOLDER'] = 'public'

url = "http://youtube.com"
last_link = "/youtube"
param = None
error = None

@app.route('/')
def home():
    return send_file('public/home.html')

@app.route('/youtube')
def youtube():
    response = requests.get(url)
    return response.content, response.headers['Content-Type']

@app.route('/error')
def error_page():
    return error

@app.route('/clear')
def clear():
    correct_pswrd = "linux123"
    pswrd = request.args.get('auth')
    delCount = 0
    file_count = 0
    oldest_file_date = 0.0

    if pswrd == correct_pswrd:
        for f in os.listdir('public'):
            if f.endswith('.mp4'):
                file_count += 1
                file_path = os.path.join('public', f)
                file_age = (time.time() - os.path.getmtime(file_path)) / 86400.0
                if file_age > oldest_file_date:
                    oldest_file_date = file_age
                if file_age >= 1.0:
                    os.remove(file_path)
                    delCount += 1
        return f"{delCount} File(s) deleted out of {file_count} total files. Oldest file is now {oldest_file_date} days old!"
    else:
        return "Authentication failed."

@app.route('/watch')
def watch():
    v = request.args.get('v')
    watchurl = f"{url}/watch?v={v}"
    ydl_opts = {
        'format': 'best[height<=360][ext=mp4]',
        'outtmpl': 'public/%(title)s.%(ext)s',
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(watchurl, download=True)
        video_title = info_dict.get('title', None)
        video_description = info_dict.get('description', None)
        filename = ydl.prepare_filename(info_dict)
        newname = os.path.basename(filename).replace('[', '(').replace(']', ')').replace("'", "").replace('_', '').replace('#', '')

        if not os.path.exists(f"public/{newname}.mp4"):
            os.rename(filename, f"public/{newname}.mp4")

    return render_template_string("""
    <html>
    <body>
    <h1>{{ video_title }}</h1>
    <form action="{{ last_link }}">
    <input type='submit' value='Go back to Youtube'/>
    </form>
    
    <div>
    <center>
    <embed src='{{ newname }}.mp4' width='720' height='480' scale='tofit' autoplay='false'>

    <object data='{{ newname }}.mp4' width='720' height='480'>
    </object></center>
    </div>

    <h2><u>Description</u><h2>
    <small>{{ video_description }}</small>
    </body>
    </html>
    """, video_title=video_title, newname=newname, last_link=last_link, video_description=video_description)

@app.errorhandler(404)
def not_found(error):
    param = request.path + "?" + request.query_string.decode('utf-8')
    response = requests.get(url + param)
    return response.content, response.headers['Content-Type']

if __name__ == '__main__':
    app.run(port=app.config['PORT'])
