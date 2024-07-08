# youtube-audio-downloader

A little console app I made to download songs and podcasts from YouTube via yt-dlp's Python implementation that automatically removes sponsors and silence using SponsorBlock (in the case of music videos). 

## Installation / Quick Start
1. Download both the `downloader.py` file and the `main.py` file and place them in the same directory.
2. Ensure that Python 3 is installed, and install it if it isn't.
3. Install the required package with Pip by running `pip install yt_dlp youtube_search music_tag`
4. Run the program with `python main.py` (NOTE: May need to use `python3` instead of `python` on some systems such as stable Linux distros, though many no longer include Python 2 by default)
