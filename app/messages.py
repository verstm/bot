import os
import sys
from .funcs import gptask
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class Page:
    def __init__(self, wrd, bname="Default", text=" "):
        self.v = []
        self.text = text
        self.codeword = wrd
        self.markup = InlineKeyboardMarkup()
        self.bname = bname
    def bind(self, cls, nm=""):
        if nm == "": nm = cls.bname
        self.v.append(cls)
        self.markup.add(InlineKeyboardButton(nm, callback_data=cls.codeword))


V = dict()


def f(path, name):
    name = name.split('_')[-1]
    global V
    tmp = os.listdir(path)
    fl = None
    for i in tmp:
        npath = path + '/' + i
        if os.path.isdir(npath):
            f(npath, i)
        else:
            fl = i
    t = None
    with open(path + '/' + fl, 'r', encoding='utf-8') as file:
        t = file.read()
    t = t.replace("{x}", name)
    pg = Page(name, name, t)
    V[name] = pg
    for i in tmp:
        npath = path + '/' + i
        if os.path.isdir(npath):
            V[name].bind(V[i.split('_')[-1]])
    for i in tmp:
        npath = path + '/' + i
        if os.path.isdir(npath):
            V[i.split('_')[-1]].bind(V[name], "Назад")

path = '/'.join(sys.argv[0].split('/')[:-1]) + '/app/content/Главная'
f(path, 'Главная')
