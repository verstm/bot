import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from .messages import V
from .config import STARTMSG

class App:
    def __init__(self):
        self.token = '6884410200:AAFM5uRITxBdccsLNO1LxTSqP7_MsvMYE3k'
        self.bot = telebot.TeleBot(self.token)
        self.commands = {"start": self.c_start}
    def run(self):
        @self.bot.callback_query_handler(func=lambda call: True)
        def callback_query(call):
            req = call.data.split('_')
            pg = V[req[0]]
            msg = pg.text
            markup = pg.markup
            self.bot.edit_message_text(chat_id=call.message.chat.id, text=msg, message_id=call.message.id, reply_markup=markup, parse_mode="Markdown")

        @self.bot.message_handler(content_types=['text'])
        def message_reply(message):
            self.textprocessing(message)

        self.bot.polling()

    def textprocessing(self, message):
        author = message.from_user
        text = message.text
        if text.startswith("/"):
            cmd = text[1:].split()[0]
            if self.commands.get(cmd, -1) == -1:
                print("Не найдено")
            else:
                self.commands[cmd](message)

    def c_start(self, message):
        markup = InlineKeyboardMarkup()
        buttons = [
            InlineKeyboardButton('Главная', callback_data='Главная'),
        ]
        for i in buttons: markup.add(i)
        self.bot.send_message(message.from_user.id, STARTMSG, reply_markup=markup)


app = App()

'''
['content_type', 'id', 'message_id', 'from_user', 'date', 'chat', 'sender_chat', 'forward_from',
'forward_from_chat', 'forward_from_message_id', 'forward_signature', 'forward_sender_name', 'forward_date',
'is_automatic_forward', 'reply_to_message', 'via_bot', 'edit_date', 'has_protected_content', 
'media_group_id', 'author_signature', 'text', 'entities', 'caption_entities', 'audio', 'document', 'photo',
'sticker', 'video', 'video_note', 'voice', 'caption', 'contact', 'location', 'venue', 'animation', 'dice',
'new_chat_member', 'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo',
'group_chat_created', 'supergroup_chat_created', 'channel_chat_created', 'migrate_to_chat_id', 'migrate_from_chat_id',
'pinned_message', 'invoice', 'successful_payment', 'connected_website', 'reply_markup', 'message_thread_id',
'is_topic_message', 'forum_topic_created', 'forum_topic_closed', 'forum_topic_reopened', 'has_media_spoiler',
'forum_topic_edited', 'general_forum_topic_hidden', 'general_forum_topic_unhidden', 'write_access_allowed',
'user_shared', 'chat_shared', 'story', 'json', '__module__', '__doc__', 'de_json', 'parse_chat',
'parse_photo', 'parse_entities', '__init__', '_Message__html_text', 'html_text', 'html_caption', 'check_json']
'''
