import yt_dlp
import re

def download_audio():
    url = input("Masukkan URL YouTube: ").strip()
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            title = info_dict.get('title', 'audio')
            
            print(f"Judul video: {title}")
            
            # Set nama file output
            ydl_opts['outtmpl'] = f"{title}.%(ext)s"
            with yt_dlp.YoutubeDL(ydl_opts) as ydl_with_name:
                print("Mendownload dan mengonversi ke MP3...")
                ydl_with_name.download([url])

            print(f"File MP3 berhasil disimpan: {title}.mp3")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    download_audio()
