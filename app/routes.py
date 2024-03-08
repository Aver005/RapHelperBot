from app import router, bot
from app.utils import extract_hashtags, extract_status

from aiogram import F, types
from aiogram.fsm.context import FSMContext


@router.message(F.audio)
async def process_mp3(message: types.Message, state: FSMContext):
    text = message.text
    chat_name = message.chat.full_name
    hashtags = extract_hashtags(text)
    status = extract_status(text)
    
    if message.reply_to_message.forum_topic_created is not None:
        chat_name = message.reply_to_message.forum_topic_created.name
        
    if chat_name != "Готовые | mp3":
        return
    
    audio_file_name = message.audio.file_name.replace(".mp3", "")
    
    await bot.send_audio(
        chat_id=message.chat.id,
        message_thread_id=message.message_thread_id,
        audio=message.audio.file_id,
        caption=f"<b>Curly Aver</b> - {audio_file_name}\n\n🔹 Статус: <b>{status}</b>\n\n{hashtags}"
    )
    
    await message.delete()


@router.message(F.reply_to_message.from_user.id == bot.id)
async def process_reply_to_bot(message: types.Message, state: FSMContext):
    text = message.text
    replied_msg = message.reply_to_message
    replied_text = replied_msg.caption
    tags = extract_hashtags(replied_text + text)
    
    to_replace = "Тэгов нет"
    if to_replace not in replied_text:
        to_replace = extract_hashtags(replied_text)
    replied_text = replied_text.replace(to_replace, tags)
    
    await bot.edit_message_caption(
        chat_id=replied_msg.chat.id,
        message_id=replied_msg.message_id,
        caption=replied_text
    )
    
    await message.delete()
