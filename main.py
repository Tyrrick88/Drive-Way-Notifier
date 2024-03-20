import telegram
import cv2
import tkinter as tk
import smtplib
import sys

email_address  = input("Enter Your Email address: ")
email_password = input("Please enter your emails passwords: ")

# First we set up the Telegram parameters
bot = telegram.Bot(token='YOU_TELEGRAM_BOT_TOKEN')

# Secondly set up your Gmail notification parameters
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("YOUR_EMAIL_ADDRESS", "YOUR_EMAIL_PASSWORD")

# Thirdly setup your Python GUI

window = tk.Tk()
window.title("Driveway motion detector")
window.geometry("300 x 100")


window.update()
window.mainloop()



def detect_motion():
    
    #Initialize the camera
    cap = cv2.VideoCapture(0)

    #Load the car Model
    car_model = cv2.dnn.readNetfromCaffe("caffe_model/caffe.proto", "caffe_model/res10_300x300_ssd_iter_140000_fp16.caffemode")
    

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        
        # Detect the car
        cars = car_model.detect(frame, 0.5, 0.4)

        # If a cre is not detected
        if len(cars) > 0:
            #Send a telegram notification
            bot.send_message(chat_id="YOUR_TELEGRAM_ID", text="A car has been detected on your driveway!")

            # Now send a E-mail notification
            msg = 
