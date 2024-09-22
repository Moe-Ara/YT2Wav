import yt_dlp
import sys
import os

def download_youtube_audio(url):
    try:
        output_folder = "."
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_folder}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '0',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download and conversion complete!")

    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <YouTube_URL>")
    else:
        video_url = sys.argv[1]
        download_youtube_audio(video_url)
