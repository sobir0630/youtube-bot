import os
from yt_dlp import YoutubeDL

SAVE_DIR = r"C:\Users\User\Downloads\kuynavo\music"
MUSIC_FILE = os.path.join(SAVE_DIR, "Music.mp3")
file = r"C:\Users\User\Downloads\kuynavo\music\Music.mp3"

def music_yukla(url: str):
    os.makedirs(SAVE_DIR, exist_ok=True)
    temp_path = os.path.join(SAVE_DIR, "%(title)s.%(ext)s")

    ydl_opts = {
        "format": "bestaudio/best",
        "ffmpeg_location": r"C:\Users\User\Downloads\ffmpeg\ffmpeg-8.0.1-full_build\bin",
        "outtmpl": temp_path,
        "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}],
        "timeout": 200,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        temp_file = ydl.prepare_filename(info).rsplit(".", 1)[0] + ".mp3"

    # Doimiy nomga o‘zgartirish
    if os.path.exists(MUSIC_FILE):
        os.remove(MUSIC_FILE)
    os.rename(temp_file, MUSIC_FILE)

    return MUSIC_FILE

def send_music(update, context):
    with open(MUSIC_FILE, 'rb') as music_file:
        context.bot.send_audio(
            chat_id=update.effective_chat.id,
            audio=music_file,
            timeout=200
        )


def remove_music(file):
    if os.path.exists(file):
        os.remove(file)

