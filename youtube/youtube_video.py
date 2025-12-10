from yt_dlp import YoutubeDL
import os

videos_path = "C:/Users/User/Downloads/kuynavo/youtube-bot/videos/video.mp4"

def yukla(url):
    save_dir = "C:/Users/User/Downloads/kuynavo/youtube-bot/videos/video.mp4"

    ydl_opts = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",   # 🔥 mp4 bo‘lishini majbur qiladi
        "ffmpeg_location": r"C:\Users\User\Downloads\ffmpeg\ffmpeg-8.0.1-full_build\bin",
        "outtmpl": "C:/Users/User/Downloads/kuynavo/youtube-bot/videos/%(title)s.%(ext)s",
        "noplaylist": True,
        "timeout": 200,
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        downloaded = ydl.prepare_filename(info)  # ko‘pincha .webm bo‘ladi

    # Final nom
    if os.path.exists(save_dir):
        os.remove(save_dir)

    # Yuklangan faylni video.mp4 deb o‘zgartiramiz
    if os.path.exists(downloaded):
        os.rename(downloaded, save_dir)
        return save_dir
    else:
        raise FileNotFoundError("Yuklangan video topilmadi!")



try:
    def send_video(update, context, video_path):
        with open(video_path, 'rb') as video_file:
            context.bot.send_video(
                chat_id=update.effective_chat.id,
                video=video_file,
                supports_streaming=True,
                timeout=200  # 30 sekund emas, 120 sekund kutadi
            )


    def send_large_video(update, context, chat_id):
        chunk_size = 1024 * 1024 * 10  # 10MB bo‘lak

        file_path = "C:/Users/User/Downloads/kuynavo/youtube-bot/videos/video.mp4"

        with open(file_path, "rb") as f:
            part = 1
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break

                context.bot.send_document(
                    chat_id=chat_id,
                    document=chunk,
                    supports_streaming=True,
                    filename=f"video_part_{part}.mp4",
                    timeout=200
                )
                part += 1


    def delete_video(file_path):
        if os.path.exists(file_path):
            os.remove(file_path)

except Exception as e:
    print(f"Error sending video: {e}")




