import requests
import json

def get_channel_videos(channel_id, api_key):
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    video_ids = []
    url = first_url
    while True:
        response = requests.get(url)
        data = json.loads(response.text)
        for video in data['items']:
            if video['id']['kind'] == "youtube#video":
                video_ids.append(video['id']['videoId'])

        try:
            next_page_token = data['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except KeyError:
            break

    with open('video_ids.json', 'w') as f:
        json.dump(video_ids, f)

    return video_ids

api_key = "AIzaSyABMX2X1iL_r3at-5Z4esLybqJ-QMFe9j8"
channel_id = "UCAq50jQvH-8bD-3IJ-HcIfQ"
video_ids = get_channel_videos(channel_id, api_key)
