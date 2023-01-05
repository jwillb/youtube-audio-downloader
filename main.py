from youtube_search import YoutubeSearch as yt_search

from downloader import Downloader

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
            "preferredcodec": "mp3"
        }
    ]
}

yt_download = Downloader(download_dir, options)

proxy_choice = input("Use a proxy? [y/N]: ")
if proxy_choice.lower() == 'y':
    Downloader.setProxy(input("Enter proxy URL: "))
else:
    pass

if input("Batch Download? [y/N]: ").lower() == 'y':
    downloads = []
    
    for line in open(input("File Name: "), 'r').readlines():
        term = line.strip('\n')
        print(f"Search term: {term}")
        results = yt_search(term, max_results=10).to_dict()
        
        for i in range(len(results)):
            print(f"{i + 1}. " + results[i]["title"] + "\t(Uploaded by " + results[i]["channel"] + ")")
        
        choice = input("Which one would you like to choose? [1]: ")
        
        if choice == "":
            choice = 1
            
        url = "https://youtube.com" + results[int(choice) - 1]["url_suffix"]
        title = input("Enter title: ")
        artist = input("Enter artist: ")

        downloads.append([url, title, artist])

    for i in range(len(downloads)):
        yt_download.downloadFile(downloads[i][0], downloads[i][1], downloads[i][2])
else:
    again = 'y'
    while again.lower() == 'y':
        term = input("Search term: ")
        results = yt_search(term, max_results=10).to_dict()
        
        for i in range(len(results)):
            print(f"{i + 1}. " + results[i]["title"] + "\t(Uploaded by " + results[i]["channel"] + ")")
        
        choice = input("Which one would you like to choose? [1]: ")
        
        if choice == "":
            choice = 1
                
        url = "https://youtube.com" + results[int(choice) - 1]["url_suffix"]
        title = input("Enter title: ")
        artist = input("Enter artist: ")
            
        yt_download.downloadFile(url, title, artist)
        again = input("Continue? [y/N]: ")
