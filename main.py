
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import BotCommand, InlineKeyboardMarkup, InlineKeyboardButton
import os
import logging
import time
from youtube.youtube_video import yukla, send_video, send_large_video, delete_video, videos_path
from youtube.music import music_yukla, send_music, remove_music, file
from config.config import TOKEN, CHAT_ID

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

def start(update, context):
    """botni boshlash funksiyasi"""
    update.message.reply_text('Assalomu alaykum! Botga xush kelibsiz!\n youtubedan videoni linkini yuboring\n men sizga videoni .mp4 formatda yuklab beraman')
    command = [BotCommand('start', 'boshlash')]
    context.bot.set_my_commands(command)


    keyboard = [[InlineKeyboardButton("YouTube-ni ochish", url="https://www.youtube.com/")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("YouTube ochish:", reply_markup=reply_markup)



def youtube(update, context):
    """youtubedan yuklab olish funksiani chqarib"""
    msg = update.message.reply_text(
    'Video uning hajmiga qarab vaqt olishi mumkin, \n'
    'bot sizga videoni yuklab beradi, bunga faqat \n'
    'ozroq vaqt olishi mumkin'
)
    time.sleep(5.0)
    context.bot.delete_message(chat_id=msg.chat.id, message_id=msg.message_id)
    update.message.reply_text('Audio yuklanmoqda...')
    print(update.message.text)

    url = update.message.text
    try:
        music_path = music_yukla(url)
        send_music(update, context)

    except Exception as e:
        logging.error(f"Error processing music: {e}")
        update.message.reply_text('Musiqa yuklashda xatolik yuz berdi.')

    try:
        update.message.reply_text('Video yuklanmoqda...')
        video_path = yukla(url)
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        get = os.path.getsize(video_path) / (1024 * 1024)
        if get > 50:
            update.message.reply_text('video hajmi katta bulakka bulib yuboryabman')
            chat_id = update.effective_chat.id
            send_large_video(update, context, chat_id=chat_id)
            delete_video(video_path)
        else:
            send_video(update, context, video_path)
        update.message.reply_text('Video muvaffaqiyatli yuklandi!')

    except Exception as e:
        logging.error(f"Error processing video: {e}")
        # update.message.reply_text('Video yuklashda xatolik yuz berdi.')

    try:
        remove_music(file)
        delete_video(videos_path)

    except:
        logging.error("Xatolik yuz berdi", exc_info=True)




if __name__ == '__main__':
    print("Bot is starting...")
    updater = Updater(token=TOKEN)
    dispatcher = updater.dispatcher


    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.regex(r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/') & ~Filters.command, youtube))
    updater.start_polling()
    updater.idle()


file = r"C:\Users\User\Downloads\kuynavo\music\Music.mp3"
remove_music(file)


