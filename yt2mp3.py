import yt_dlp
import re

def sanitize_filename(title):
    # Menghapus spasi ganda
    title = re.sub(r'\s+', ' ', title).strip()
    # Menghapus karakter selain huruf dan angka di awal judul
    title = re.sub(r'^[^a-zA-Z0-9]+', '', title)
    # Memotong judul sebelum karakter selain huruf dan angka
    title = re.split(r'[^a-zA-Z0-9\s]', title)[0]
    # Mengubah spasi menjadi underscore
    sanitized = title.replace(" ", "_")
    # Menghapus underscore di akhir jika ada
    return sanitized.rstrip("_")

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
            sanitized_name = sanitize_filename(title)
            
            print(f"Judul video: {title}")
            
            # Set nama file output
            ydl_opts['outtmpl'] = f"{sanitized_name}.%(ext)s"
            with yt_dlp.YoutubeDL(ydl_opts) as ydl_with_name:
                print("Mendownload dan mengonversi ke MP3...")
                ydl_with_name.download([url])

            print(f"File MP3 berhasil disimpan: {sanitized_name}.mp3")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    download_audio()
