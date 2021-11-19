import pyautogui
import webbrowser
import time
import random
x = int(input("enter hours(1 email every hour):"))

# open web (fire fox) to gmail and type out the bee movie script.
# make this happen every 60 seconds or so.
def main():

    webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
    for i in range(x):

        time.sleep(10.0)
        pyautogui.click(x=95, y=230,interval=1, button="left")
        message = random.randint(1,10000000)
        subject = random.randint(1,10000000)
        target = ("loganbitt1@gmail.com")
        text = (random.randint(1,100000000))
        print("message =", message)
        print("subject = ", subject)
        print("target =", target)


        pyautogui.typewrite(target)
        pyautogui.click(x=998,y=362,interval=3,button="left")
        time.sleep(2)

        pyautogui.typewrite(str(subject))
        time.sleep(2)
        pyautogui.click(x=932,y=441,button="left")
        time.sleep(1)
        pyautogui.typewrite(str(text))
        pyautogui.click(x=833,y=703,button="left")
        time.sleep(3600)

        for i in range(10):
            print("EMAIL HAS BEEN SENT")
    # owo its done owo
main()