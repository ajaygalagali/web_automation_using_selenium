# This program automatically fills google contact form.
# Keep contact form tab open and use windows hotkey to launch this program.

from time import sleep
import pyautogui as aa

mX,mY = 1759,27
gx,gy = 569,815

t = 'tab'
name = "Astr0"
email = "astro@email.com"
address = "Halsangi"
phone = "1234567890"
comments = "I am python"

def enterDet(keyToPress,msg):
    #sleep(1)
    aa.press(keyToPress)
    #sleep(1)
    aa.write(msg)
# contact form Point(x=569, y=815)

#sleep(1)
#aa.click(mX,mY)
sleep(1)
aa.click(gx,gy)
sleep(1)
aa.write("Hello")
enterDet(t,email)
enterDet(t,address)
enterDet(t,phone)
enterDet(t,comments)
aa.press(t)
aa.press('enter')


