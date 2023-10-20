import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import FSInputFile

token_api = "6565587911:AAGG80wsIafXZdshqZXwkLuNWfXk735rmkk"
bot = Bot(token=token_api)
dp = Dispatcher(bot=bot)


async def download_video(message: types.Message):
    file_id = message.video.file_id # Get file id
    file = await bot.get_file(file_id) # Get file path
    print(file_id, file, sep = "\n")
    await bot.download_file(file.file_path, f"media/{file.file_unique_id}.mp4") # Download video and save output in file "video.mp4"

@dp.message()
async def send_video(message):
    video_note = FSInputFile("output.mp4")
    await bot.send_video_note(message.chat.id, video_note)



async def main():

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())