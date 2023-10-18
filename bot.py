from aiogram import Bot, Dispatcher, types, executor

token_api = "6565587911:AAGG80wsIafXZdshqZXwkLuNWfXk735rmkk"

bot = Bot(token=token_api)
dp = Dispatcher(bot=bot)


@dp.message_handler(content_types=["video"])
async def download_video(message: types.Message):
    file_id = message.video.file_id # Get file id
    file = await bot.get_file(file_id) # Get file path
    print(file_id, file, sep = "\n")
    await bot.download_file(file.file_path, f"media/{file.file_unique_id}.mp4") # Download video and save output in file "video.mp4"

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)