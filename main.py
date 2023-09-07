import pyautogui as pa
import os
import webbrowser
import time
import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage with a default length of 12 characters
password = generate_random_password()


# ระบุเส้นทางสมบูรณ์ของไฟล์ "data.txt" ในโฟลเดอร์ "data"
data_file = os.path.join('data', 'data.txt')


def read_config(file_path):
    config = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line:
                key, value = line.split('=')
                config[key.strip()] = value.strip()
    return config

config = read_config(data_file)

# เรียกใช้ค่า name และ lastname
name = config.get('name', '')
lastname = config.get('lastname', '')



def main():
    webbrowser.open("https://accounts.google.com/signup/v2/createaccount?biz=false&cc=TH&continue=http%3A%2F%2Fsupport.google.com%2Fmail%2Fanswer%2F8494%3Fhl%3Dth%26co%3DGENIE.Platform%253DDesktop%26authuser%3D3&dsh=S-1627092410%3A1694072973690868&flowEntry=SignUp&flowName=GlifWebSignIn&hl=th&theme=glif&authuser=3")
    time.sleep(2)
    # ค้นหาตำแหน่งของรูปภาพบนหน้าจอ
    image_1 = pa.locateOnScreen('img/1.png')
    # ตรวจสอบว่าพบรูปภาพหรือไม่
    if image_1 is not None:
        # หากพบรูปภาพ ให้คลิก
        pa.click(image_1)
    else:
        print("ไม่พบรูปภาพ")

    # คุณอาจต้องปรับแต่งพารามิเตอร์เพิ่มเติมเช่นความแม่นยำ หรือตำแหน่งเริ่มต้นของการค้นหาใน PyAutoGUI ตามความเหมาะสม
    pa.typewrite(name)
    time.sleep(0.5)
    image_2 = pa.locateOnScreen('img/2.png')
    # ตรวจสอบว่าพบรูปภาพหรือไม่
    if image_2 is not None:
        # หากพบรูปภาพ ให้คลิก
        pa.click(image_2)
    else:
        print("ไม่พบรูปภาพ")
    pa.typewrite(lastname)
    time.sleep(0.5)
    image_3 = pa.locateOnScreen('img/3.png')
    # ตรวจสอบว่าพบรูปภาพหรือไม่
    if image_3 is not None:
        # หากพบรูปภาพ ให้คลิก
        pa.click(image_3)
    else:
        print("ไม่พบรูปภาพ")
    time.sleep(0.5)
    image_4 = pa.locateOnScreen('img/4.png', confidence=0.4)
    # ตรวจสอบว่าพบรูปภาพหรือไม่
    if image_4 is not None:
        time.sleep(0.5)
        # หากพบรูปภาพ ให้คลิก
        pa.click(image_4)
    else:
        print("ไม่พบรูปภาพ")
    time.sleep(1)
    pa.click
    pa.click
    pa.typewrite("1")
    time.sleep(0.5)
    image_5 = pa.locateOnScreen('img/5.png')
    # ตรวจสอบว่าพบรูปภาพหรือไม่
    if image_5 is not None:
        # หากพบรูปภาพ ให้คลิก
        pa.click(image_5)
    else:
        print("ไม่พบรูปภาพ")
    time.sleep(0.5)
    image_6 = pa.locateOnScreen('img/6.png')
    # ตรวจสอบว่าพบรูปภาพหรือไม่
    if image_6 is not None:
        # หากพบรูปภาพ ให้คลิก
        pa.click(image_6)
    else:
        print("ไม่พบรูปภาพ")
    time.sleep(0.5)
    image_7 = pa.locateOnScreen('img/7.png')
    # ตรวจสอบว่าพบรูปภาพหรือไม่
    if image_7 is not None:
        # หากพบรูปภาพ ให้คลิก
        pa.click(image_7)
    else:
        print("ไม่พบรูปภาพ")
    pa.typewrite("1999") #ปีเกิด
    time.sleep(0.5)
    image_8 = pa.locateOnScreen('img/8.png')
    # ตรวจสอบว่าพบรูปภาพหรือไม่
    if image_8 is not None:
        # หากพบรูปภาพ ให้คลิก
        pa.click(image_8)
    else:
        print("ไม่พบรูปภาพ")
    time.sleep(0.5)
    image_9 = pa.locateOnScreen('img/9.png')
    # ตรวจสอบว่าพบรูปภาพหรือไม่
    if image_9 is not None:
        # หากพบรูปภาพ ให้คลิก
        pa.click(image_9)
    else:
        print("ไม่พบรูปภาพ")
    time.sleep(0.5)
    image_10 = pa.locateOnScreen('img/10.png')
    # ตรวจสอบว่าพบรูปภาพหรือไม่
    if image_10 is not None:
        # หากพบรูปภาพ ให้คลิก
        pa.click(image_10)
    else:
        print("ไม่พบรูปภาพ")
    time.sleep(0.5)
    image_11 = pa.locateOnScreen('img/11.png', confidence=0.6)
    image_vv = pa.locateOnScreen('img/vv.png', confidence=0.6)
    # ตรวจสอบว่าพบรูปภาพหรือไม่
    if image_11 is not None:
        if image_vv is not None:
            pa.click(image_vv)
            print("GG44s")
        else:
            print("ไม่พบรูปภาพ")
        # หากพบรูปภาพ ให้คลิก
        print("GG")
    else:
        print("ไม่พบรูปภาพ")
    time.sleep(0.5)
    image_13 = pa.locateOnScreen('img/13.png')
    # ตรวจสอบว่าพบรูปภาพหรือไม่
    if image_13 is not None:
        # หากพบรูปภาพ ให้คลิก
        pa.click(image_13)
    else:
        print("ไม่พบรูปภาพ")
    time.sleep(0.5)
    image_14 = pa.locateOnScreen('img/14.png')
    # ตรวจสอบว่าพบรูปภาพหรือไม่
    if image_14 is not None:
        # หากพบรูปภาพ ให้คลิก
        pa.click(image_14)
    else:
        print("ไม่พบรูปภาพ")
    pa.typewrite(password)
    time.sleep(0.5)
    image_15 = pa.locateOnScreen('img/15.png')
    # ตรวจสอบว่าพบรูปภาพหรือไม่
    if image_15 is not None:
        # หากพบรูปภาพ ให้คลิก
        pa.click(image_15)
    else:
        print("ไม่พบรูปภาพ")
    pa.typewrite(password)
    time.sleep(0.5)
    image_16 = pa.locateOnScreen('img/16.png')
    # ตรวจสอบว่าพบรูปภาพหรือไม่
    if image_16 is not None:
        # หากพบรูปภาพ ให้คลิก
        pa.click(image_16)
    else:
        print("ไม่พบรูปภาพ")
    time.sleep(0.5)
    image_17 = pa.locateOnScreen('img/17.png')
    # ตรวจสอบว่าพบรูปภาพหรือไม่
    if image_17 is not None:
        # หากพบรูปภาพ ให้คลิก
        pa.click(image_17)
    else:
        print("ไม่พบรูปภาพ")
    time.sleep(0.5)
    pa.scroll(-100)
    image_18 = pa.locateOnScreen('img/18.png')
    # ตรวจสอบว่าพบรูปภาพหรือไม่
    if image_18 is not None:
        # หากพบรูปภาพ ให้คลิก
        pa.click(image_18)
    else:
        print("ไม่พบรูปภาพ")

def account():
    file_path = 'account.txt'

    if not os.path.exists(file_path):
        # ถ้าไฟล์ไม่มีอยู่ให้สร้างไฟล์ใหม่และเขียนข้อความลงไป
        with open(file_path, 'w') as file:
            file.write(lowercase_text)
        with open(file_path, 'a') as file:
            file.write('\n'+ password)

file_path = 'account.txt'

if os.path.exists(file_path):
    # ตรวจสอบว่าไฟล์มีอยู่หรือไม่
    os.remove(file_path)
    print(f'ไฟล์ {file_path} ถูกลบแล้ว')
else:
    print(f'ไฟล์ {file_path} ไม่มีอยู่')

text = name+lastname+"@gmail.com"
lowercase_text = text.lower()
account()
main()
