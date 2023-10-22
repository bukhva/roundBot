import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile
from editor import video_to_video_note
from os import remove

token_api = "6565587911:AAGG80wsIafXZdshqZXwkLuNWfXk735rmkk"
bot = Bot(token=token_api)
dp = Dispatcher(bot=bot)


@dp.message()
async def download_video(message: types.Message):
    file_id = message.video.file_id
    file = await bot.get_file(file_id)
    path = f"media/{file.file_unique_id}.mp4"
    await bot.download_file(file.file_path, path) # Download video and save output in file "video.mp4"
    await message.reply("Получили! Обрабатываем...")
    await send_video(message, file.file_unique_id)


async def send_video(message, videoId):
    path = f"media/{videoId}.mp4"
    newPath = f"media/result{videoId}.mp4"

    if(video_to_video_note(path, newPath)):
        video_note = FSInputFile(newPath)
        await bot.send_video_note(message.chat.id, video_note)
        #remove_files(path, newPath)


def remove_files(path, newPath):
    remove(path)
    remove(newPath)



async def main():

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())