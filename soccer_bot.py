from subprocess import check_output
import praw
import requests
import urlparse
import json
import os

user_agent = ("Soccer Video 0.1")

r = praw.Reddit(user_agent = user_agent)

subreddit = r.get_subreddit("soccer")

url_list = [];

for submission in subreddit.get_new(limit = 100):
    if "streamable.com" in submission.url:
        url_list.append(submission.url);
        parsed_url = urlparse.urlparse(submission.url);
        down_res = requests.get("https://api.streamable.com/videos"+parsed_url.path);
        json_obj = down_res.json();
        video_url = "https:"+json_obj['files']['mp4']['url'];
        #print video_url;
        #up_res = requests.get("https://api.streamable.com/import?url="+video_url + " \  -u soccer_bot:soccer_bot");
        #print "https://api.streamable.com/import?url="+video_url + " \  -u soccer_bot:soccer_bot";
        os.system("curl https://api.streamable.com/import?url="+video_url + " \  -u soccer_bot:soccer_bot");
