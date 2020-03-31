# Youtube MP3 Downloader v0.3
import os
import os.path
import urllib.request
from bs4 import BeautifulSoup



def DL_MP3(search):
    query = urllib.parse.quote(search)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    counter = 0
    for vid in soup.find_all(attrs={"class": "yt-uix-tile-link"}):
        if counter < 1:
            counter = counter + 1
            global final_url
            final_url = str("https://www.youtube.com" + vid["href"])
            os.system(
                "youtube-dl -o 'Musik/%(title)s.%(ext)s' --no-playlist --playlist-items 1 -x --audio-format mp3 "
                + final_url
            )

def DL_MP4(search):
    query = urllib.parse.quote(search)
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
    counter = 0
    for vid in soup.find_all(attrs={"class": "yt-uix-tile-link"}):
        if counter < 1:
            counter = counter + 1
            global final_url
            final_url = str("https://www.youtube.com" + vid["href"])
            os.system(
                "youtube-dl -o 'Video/%(title)s.%(ext)s' --no-playlist --playlist-items 1 --recode-video mp4 "
                + final_url
            )


def main():
    print("1.Audio")
    print("2.Video")

    choice = int(input("Choice: "))

    if (choice == 1):
        songs = open("songs.txt")
        for x in songs:
            DL_MP3(x)
        songs.close

    if (choice == 2):
        videos = open("videos.txt")
        for x in videos:
            DL_MP4(x)
        videos.close
    
if __name__ == "__main__":
    main()