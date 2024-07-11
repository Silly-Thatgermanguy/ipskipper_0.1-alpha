import tkinter as say_gex
from tkinter import ttk 
from uuid import getnode as get_mac
import socket
import speedtest
import subprocess
import time


hostname = socket.gethostname()
my_ip =socket.gethostbyname(hostname)


mac = get_mac()


def penis():
 commands = [
     "start %LocalAppData%",
     "timeout /t 1 >nul",  # Wait for 1 second (adjust as needed)
     "taskkill /f /im explorer.exe"  # Close the File Explorer process
 ]
 for cmd in commands:
     subprocess.Popen(cmd, shell=True)


class App():
     
    def gaysex1(self):
      newtext = my_ip
      self.text.config(text=newtext) 
    
    def gaysex2(self):
      newtext = f'MAC: {mac:012X}'
      self.text.config(text=newtext) 
    
    def gaysex3(self):
      newtext = penis()
      self.text.config(text=newtext) 
    
    
    def __init__(self):
        self.root = say_gex.Tk()
        self.root.geometry('400x300')
        self.root.title("IP TOOL Version 0.1")
        self.mainframe = say_gex.Frame(self.root, background='black')
        self.text = ttk.Label(self.mainframe, text="IP TOOL Version 0.1", background='white', font=("Brass Mono", 20))
        self.text.grid(row=1, column=0, sticky='nwes')
        self.mainframe.pack(fill='both', expand=True)
        iluvsammy_button = say_gex.Button(self.mainframe, text='show current ip', command=self.gaysex1)
        iluvsammy_button.grid(row=5, column=0, sticky='nwes')
        iluvsammy_button2 = say_gex.Button(self.mainframe, text='Show Mac Adress', command=self.gaysex2)
        iluvsammy_button2.grid(row=5, column=1, sticky='nwes')
        iluvsammy_ports = say_gex.Button(self.mainframe, text='i wan kill my pc', command=self.gaysex3 )
        iluvsammy_ports.grid(row=6, column=0, sticky='nwes')
        
        self.root.mainloop()
        return
    





if __name__ == '__main__':
     App()