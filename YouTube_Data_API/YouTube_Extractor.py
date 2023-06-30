import requests
import json

def get_video_info(video_id, api_key):
    search_url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part=snippet,contentDetails,statistics,status"
    response = requests.get(search_url)
    data = json.loads(response.text)
    video_data = {}
    for video in data['items']:
        title = video['snippet']['title']
        description = video['snippet']['description']
        tags = video['snippet'].get('tags', [])  # Use an empty list if 'tags' is not present
        views = video['statistics']['viewCount']
        video_data = {"Title": title, "Description": description, "Tags": tags, "Views": views}
    return video_data


api_key = "API"

# Load video IDs from the JSON file
with open('video_ids.json', 'r') as f:
    video_ids = json.load(f)

# Extract data for each video and store it in a dictionary
all_video_data = {}
for video_id in video_ids:
    all_video_data[video_id] = get_video_info(video_id, api_key)

# Save the data to a JSON file
with open('video_data.json', 'w') as f:
    json.dump(all_video_data, f)
