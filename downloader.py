from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from music_tag import load_file

class Downloader:
    def __init__(self, directory, options):
        self.__directory = directory
        self.__options = options
    
    def setProxy(self, proxy_url):
        self.__options["proxy"] = proxy_url

    def downloadFile(self, video_url, title, artist):
        self.__options["outtmpl"] = f"{self.__directory}/{title}.%(ext)s"
        while True:
            try:
                with YoutubeDL(self.__options) as yt_dl:
                    yt_dl.download(video_url)
                break
            except DownloadError:
                print("Retrying...")
            pass
        
        song_file = load_file(f"{self.__directory}/{title}.mp3")

        song_file["title"] = title
        song_file["artist"] = artist

        song_file.save()

