import re


def extract_video_id(url):
    # Regular expression pattern to match the video ID
    pattern = r'^.*((youtu.be\/)|(v\/)|(\/u\/\w\/)|(embed\/)|(watch\?))\??v?=?([^#&?]*).*'
    match = re.match(pattern, url)

    if match:
        return match.group(7)
    else:
        return None


