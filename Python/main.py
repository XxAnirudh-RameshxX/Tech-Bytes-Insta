import datetime
from selenium import webdriver
import time
from InstagramAPI import InstagramAPI
from write_image import *
import numpy as np
import cv2
import textwrap
import random
import praw
import csv

#https://www.instagram.com/tilbot/

dt=datetime.datetime.today()
print(dt.weekday())

#monday=0,wednesday=2,friday=4

while(True):
    count = 0
    nw=datetime.datetime.now()
    print("test")
    #while(nw.hour == 10 and nw.minute == 5):
    if(count<1):
        callscraper()
        InstagramAPI = InstagramAPI("username", "password")
        InstagramAPI.login()  # login
        photo_path = 'post_new.jpg'
        caption = "Beep-Bop, I'm a bot. \n "
        InstagramAPI.uploadPhoto(photo_path, caption=caption)
        print("TEST TEST")
        count = count + 1
    time.sleep(86400)
            


