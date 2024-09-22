# YouTube Audio Downloader

This Python script allows you to download audio from a YouTube video and automatically convert it to a `.wav` file using `yt-dlp` and `FFmpeg`.

## Features
- Downloads the best available audio format from YouTube.
- Converts the audio to `.wav` format using `FFmpeg`.
- Saves the audio in the current directory.

## Requirements

Make sure you have the following installed on your system:

- [Python 3.x](https://www.python.org/downloads/)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/download.html)

## Installation

1. Clone this repository or download the script directly.
2. Install the required packages using `pip`:

   ```bash
   pip install yt-dlp
   ```
   
3. Ensure that FFmpeg is installed and available in your system's PATH. You can verify the installation by running:

    ```bash
    ffmpeg -version
    ```
## Usage
1. Open a terminal/command prompt in the directory where the script is located.
2. Run the script using the following command:

      ```bash
      python script.py <YouTube_URL>
      ```
      Replace <YouTube_URL> with the URL of the YouTube video you want to download audio from.
   
      Example:
      ```bash
      python script.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
      ```

## License

This project is open source and available under the MIT License.

