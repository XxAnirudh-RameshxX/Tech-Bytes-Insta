import numpy as np
import cv2
import textwrap
import random
import praw
import csv
import pyrebase
import random
import time

# Made by the amazing Arun and Abhinav
# stay wired

#reddit = praw.Reddit(client_id='3bniLTu50WAOYg', client_secret='9X9f5WFLz_AEYT6S1f7dieDtr8Q', user_agent='til-2-insta')

config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://tech-bytes-560cb.firebaseio.com/",
  "storageBucket": "projectId.appspot.com"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def callscraper():
    j = random.randint(1,16)
    img = cv2.imread('images/' + str(j) + '.png')

    print(img.shape)

    height, width, channel = img.shape

    text_img = np.ones((height, width))
    print(text_img.shape)
    font = cv2.FONT_HERSHEY_SIMPLEX

    text = db.child("TIL").get().val()
    wrapped_text = textwrap.wrap(text, width=25)
    x, y = 0,0
    font_size = int(img.shape[0] / 1000) * 2
    if j == 13 or j == 5:
        font_size = 1
    font_thickness = 2

    i = 0
    for line in wrapped_text:
        textsize = cv2.getTextSize(line, font, font_size, font_thickness)[0]

        gap = textsize[1] + 10

        y = int((img.shape[0] + textsize[1]) / 2) - (int(len(wrapped_text)/2) - i) * gap
        x = int((img.shape[1] - textsize[0]) / 2)

        cv2.putText(img, line, (x, y), font,
                    font_size, 
                    (255,255,255), 
                    font_thickness, 
                    lineType = cv2.LINE_AA)
        i +=1

    cv2.imwrite('post_new.jpg',img)
    cv2.imshow('image',img)
    cv2.waitKey(0)
