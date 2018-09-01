
#  2:30 PM, Thứ Bảy, ngày 1/9/2018 <--------- NGUYỄN MINH PHONG --------->

from gtts import gTTS
import speech_recognition as sr
import os
import re
import pyglet
import webbrowser
import smtplib
import requests
import time, os
import traloi
import random
from weather import Weather

#####################################
# NHIỆM VỤ:
# >>> tối ưu hóa lại phần khai báo ngôn ngữ (lang = )
# >>> điều chỉnh tốc độ nói của bot
# >>> mảng (Array) và random cho statement
# >>> cho chạy thử nghiệm trên máy tính nhúng (...)
# >>> áp dụng IoT (...)


# hàm khởi tạo và chuyển văn bản sang giọng nói !
def tts(text, lang):
    
    file = gTTS(text = text, lang= lang, slow= False)
    filename = 'audio.mp3' # đặt tên cho file âm thanh
    file.save(filename) #lưu file âm thanh

    voice = pyglet.media.load(filename, streaming = False) # mở file âm thanh
    voice.play() # đọc file âm thanh

    time.sleep(voice.duration)
    os.remove(filename)  # xóa giọng nói vừa ghi để chuẩn bị cho giọng nói mới !

# lời chào đầu tiên :))
tts(random.choice(traloi.chaohoi),lang = 'vi') #chọn ngẫu nhiên từ list trong file traloi.py


def myCommand():
    
    # nghe từ khóa và in ra màn hình, nếu tương ứng với statement mở hàm hanhdong()

    rec = sr.Recognizer()

    with sr.Microphone() as source:
        print('Đang nghe...')
        rec.pause_threshold = 1
        rec.adjust_for_ambient_noise(source, duration=1)
        audio = rec.listen(source)

    try:
        command = rec.recognize_google(audio, language='vi-VN')
        print('Lệnh : ' + command + '\n')


    #   không rõ - nghe lại
    except sr.UnknownValueError:
        print(random.choice(traloi.khongnghero))
        tts(random.choice(traloi.khongnghero), lang = 'vi')
        command = myCommand();

    return command

def hanhdong(command):
    
    # bot sẽ trả lời những câu hỏi của bạn tương ứng trong statment

    if command in traloi.batmaylanh:      
        print('Đã bật máy lạnh ! \n')
        tts('Đã bật máy lạnh', lang = 'vi') 

    elif command in traloi.tatmaylanh:
        print('Đã tắt máy lạnh ! \n')
        tts('Đã tắt máy lạnh', lang = 'vi')

    elif command in traloi.mocua:       
        print('Cửa mở ! \n')
        tts('Đã mở cửa', lang = 'vi') 

    elif command in traloi.dongcua:
        print('Đóng cửa ! \n')
        tts('Đã đóng cửa', lang = 'vi')    

    elif command in traloi.batden:
        print('Đèn đã bật ! \n')
        tts('Đèn đã bật', lang = 'vi')

    elif command in traloi.tatden:
        print('Đã tắt đèn ! \n')
        tts('Đèn đã tắt', lang = 'vi')   

    elif command in traloi.batwifi:
        print('Đã bật wifi ! \n')
        tts('Đã bật wifi', lang = 'vi')

    elif command in traloi.tatwifi:
        print('Đã tắt wifi ! \n')
        tts('Đã tắt wifi', lang = 'vi')         

    elif 'Mở nhạc' in command:
        print('Nhạc mở ! \n')
        tts('Cu nghe nhạc vui vẻ nhé !', lang = 'vi')

    elif 'Mở nhạc' in command:
        print('Tắt nhạc ! \n')
        tts('Đã tắt nhạc', lang = 'vi') 
        

    elif 'nhiệt độ ở' in command:
        reg_ex = re.search('nhiệt độ ở (.*)', command)
        if reg_ex:
            city = reg_ex.group(1)
            weather = Weather()
            location = weather.lookup_by_location(city)
            condition = location.condition()
            print('Nhiệt độ ở %s là %.1f độ \n' % (city, (int(condition.temp())-32)/1.8))
            tts('Nhiệt độ ở %s là %.1f độ \n' % (city, (int(condition.temp())-32)/1.8),lang = 'vi')                

# vòng lặp tiếp tục nghe
while True:
    hanhdong(myCommand())