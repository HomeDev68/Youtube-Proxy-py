Youtube-Proxy
=============

Made in Ruby with Sinatra-rb, this Youtube-Proxy was made in less than a week, so that I could go on youtube in school.
Hosted on my own Computer (turn it on when I go to school).

How it Works
------------

When the user visits the site, a basic html version of Youtube will be displayed.
Then when a user clicks on a video, the url will look like this: "http://youtubeproxy.com/watch?v=dQw4w9WgXcQ".
The program will then take the url parameters (/watch?v=dQw4w9WgXcQ) and then add it to the youtube url (http://youtube.com)
and create the full url(http://youtube.com/watch?v=dQw4w9WgXcQ). That's the easy part. Then the program uses an API (viddl-rb) to download the chosen youtube video to my computer, then after the video has downloaded, the video will be streamed from my computer to the user.

This means that all the video data is being sent from my computer to the school, instead of from youtube to the school. And because my ip is not blocked by the school, the video streams nicely!

Python Implementation
=====================

This project has been re-implemented in Python using Flask. The Python version provides the same functionality as the original Ruby version.

How it Works
------------

When the user visits the site, a basic html version of Youtube will be displayed.
Then when a user clicks on a video, the url will look like this: "http://youtubeproxy.com/watch?v=dQw4w9WgXcQ".
The program will then take the url parameters (/watch?v=dQw4w9WgXcQ) and then add it to the youtube url (http://youtube.com)
and create the full url(http://youtube.com/watch?v=dQw4w9WgXcQ). That's the easy part. Then the program uses `pytube` to download the chosen youtube video to my computer, then after the video has downloaded, the video will be streamed from my computer to the user.

This means that all the video data is being sent from my computer to the school, instead of from youtube to the school. And because my ip is not blocked by the school, the video streams nicely!

Setup and Running the Python Implementation
-------------------------------------------

1. Install the required dependencies:
   ```
   pip install Flask pytube youtube_dl
   ```

2. Run the Flask app:
   ```
   python proxy.py
   ```

Dependencies
------------

* Flask
* pytube
* youtube_dl
