import tkinter as tk
from tkinter import ttk 
from uuid import getnode as get_mac
import socket
import subprocess
import time


hostname = socket.gethostname()
my_ip =socket.gethostbyname(hostname)


mac = get_mac()


def penis():
 commands = [
     "start %LocalAppData%",
     "timeout /t 1 >nul",  
     "taskkill /f /im explorer.exe"  
     
 ]
 for cmd in commands:
     subprocess.Popen(cmd, shell=True)


def shutdown():
  commands = [
   "shutdown /s"

 ]
  for cmd in commands:
     subprocess.Popen(cmd, shell=True)



class App():
     
    def command1(self):
      newtext = my_ip
      self.text.config(text=newtext) 
    
    def command2(self):
      newtext = f'MAC: {mac:012X}'
      self.text.config(text=newtext) 
    
    def command3(self):
      newtext = penis()
      self.text.config(text=newtext) 

    def CMD1(self):
       newtext = shutdown()
       self.text.config(text=newtext)    
    
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x300')
        self.root.title("IP TOOL Version 0.1")
        self.mainframe = tk.Frame(self.root, background='black')
        self.text = ttk.Label(self.mainframe, text="IP TOOL Version 0.1", background='white', font=("Brass Mono", 20))
        self.text.grid(row=1, column=0, sticky='nwes')
        self.mainframe.pack(fill='both', expand=True)
        Ip_button = tk.Button(self.mainframe, text='show current ip', command=self.command1)
        Ip_button.grid(row=5, column=0, sticky='nwes')
        mac_button2 = tk.Button(self.mainframe, text='Show Mac Adress', command=self.command2)
        mac_button2.grid(row=5, column=1, sticky='nwes')
        Killer_button3 = tk.Button(self.mainframe, text='i wan kill my pc', command=self.command3 )
        Killer_button3.grid(row=6, column=0, sticky='nwes')
        button_cmd1 = tk.Button(self.mainframe, text='turn off pc', command=self.CMD1 )
        button_cmd1.grid(row=7, column=0, sticky='nwes')
        button_cmd2 = tk.Button(self.mainframe, text='CMD1', command=self.CMD1 )
        button_cmd2.grid(row=8, column=0, sticky='nwes')
        
        self.root.mainloop()
        return
    





if __name__ == '__main__':
     App()
