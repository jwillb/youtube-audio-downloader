from youtube_search import YoutubeSearch as yt_search
from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from music_tag import load_file as load_music_file

category_list = ("sponsor", "music_offtopic", "selfpromo")

download_dir = input("Enter Download Directory (Leave blank or enter . for current working directory): ")
if download_dir == "":
    download_dir = "."

options = {
    "format": "bestaudio",
    "postprocessors": [{
            "key": "SponsorBlock",
            "categories": category_list
        },
        {
            "key": "ModifyChapters",
            "remove_sponsor_segments": category_list
        },
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav"
        }
    ]
}

proxy_choice = input("Use a proxy? [y/N]: ")
if proxy_choice.lower() == 'y':
    options["proxy"] = input("Enter proxy URL: ")
else:
    pass

while True:
    query = input("Search YouTube: ")

    results = yt_search(query, max_results = 10).to_dict()

    for i in range(len(results)):
        print(f"{i + 1}. " + results[i]["title"] + "\t(Uploaded by " + results[i]["channel"] + ")")

    choice = input("Which one would you like to choose? [1]: ")
    if choice == "":
        choice = 1

    suffix = results[int(choice) - 1]["url_suffix"]
    
    title = input("Enter title: ")
    artist = input("Enter artist: ")

    options["outtmpl"] = f"{download_dir}/{title}.%(ext)s"
    
    while True:
        try:
            with YoutubeDL(options) as yt_dl:
                yt_dl.download(["https://youtube.com" + suffix])
            break
        except DownloadError:
            pass

    song_file = load_music_file(f"{download_dir}/{title}.wav")

    song_file["title"] = title
    song_file["artist"] = artist
    song_file.save()

    again = input("Continue? [Y/n]: ")
    if again.lower() == "n":
        exit()
    else:
        pass
