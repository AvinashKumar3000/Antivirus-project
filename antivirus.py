
#importing a modules
import os
from Tkinter import Tk
from Tkinter import *
import tkMessageBox
# global variables

# storing virus list..
#they are global variable...   
#C:\Users\PremaAvinash\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup 

# list of virus which will be presents in the computer
startvirus = ["\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\system.bat"
             ,"\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\windows.vbs"]
appdatavirus = ["\\setup.bat","\\set.bat","\\vol.bat","\\movie.bat","\\love_killer"]
alldrivevirus = ["movie.bat","love_killer.bat"]
appdata = "null"
# a global variable: scanstatusvalue 
global scanstatusvalue

scanstatusvalue = 0
noofvirus = 0
drivelist = ["D:\\","E:\\","F:\\","G:\\","H:\\","I:\\","J:\\","K:\\","L:\\"]
global temp

#helper function...
def setupfilecreation():
  sourcecode = """@echo off
color 0c
title setup-running

del  "%Appdata%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\system.bat"
del  "%Appdata%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\windows.vbs"
del  "%Appdata%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\explorer.vbs"
del  "%Appdata%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\love_killer.bat"
del  "%Appdata%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\movie.bat"
del  "%Appdata%\\set.bat"
del  "%Appdata%\\vol.bat"
del  "%Appdata%\\movie.bat"
del  "%Appdata%\\love_killer.bat"
del  "%Appdata%\\registery.reg"
echo %Appdata% > data_info.txt
echo t > data_status.txt

cls
color 0a
echo -------------------------
echo  setup process complete
echo -------------------------
pause"""

  try:
      check = open("setup.bat","r")
  except IOError:
      try:
          setfile = open("setup.bat","w")
      except IOError:
          tkMessageBox.showerror("requirnment error",text = " Please turn off your antivirus for a while...")
      else:    
          setfile.write(sourcecode)
          setfile.close()
  else:
      check.close()  






def scanprocess():
    setupfilecreation()
    scount = 0
    if(setupstatus()):
        #scan code
        lbl.config(text = "scanning ...")
        get_appdata()
        length = len(startvirus)
        
        # finding the virus in main location...
        for x in range(0,length):
            scount = filesearch(appdata+startvirus[x],scount)
        length = len(appdatavirus)    
        for x in range(0,length):
            scount = filesearch(appdata+appdatavirus[x],scount)
        length = len(alldrivevirus)
        for x in range(0,length):
            scount = filesearch(appdata+alldrivevirus[x],scount)
        
        #finding the virus in other drives
        length = len(drivelist)
        for x in range(0,length):
            scount = filesearch(drivelist[x]+alldrivevirus[0],scount)
            scount = filesearch(drivelist[x]+alldrivevirus[1],scount)
        global scanstatusvalue
        scanstatusvalue = 1
        global temp
        temp = scount
        message = "\nscanning complete \n\n " + str(scount) + " threads have been found."
        lbl.config(text = message)
        #set the scanstatusvalue to be 1 (that mean true)
        #indicating scan process is complete
    else:
        tkMessageBox.showerror("File not found","First you have to run setup.bat") 
        
def filesearch(file,count = 0): #code complete
    try:
        fp = open(file,"r")
    except IOError:
        return count
    else:
        fp.close()
        return count+1
    
def removeprocess():
    global scanstatusvalue
    
    if(setupstatus()):
        if(scanstatusvalue == 1):
           global temp
           rcount = temp
           lbl.config(text = "removing ...")
           get_appdata()
           length = len(startvirus)
         
           # finding the virus in main location...
           for x in range(0,length):
              rcount = fileremove(appdata+startvirus[x],rcount)
           length = len(appdatavirus)    
           for x in range(0,length):
              rcount = fileremove(appdata+appdatavirus[x],rcount)
           length = len(alldrivevirus)
           for x in range(0,length):
              rcount = fileremove(appdata+alldrivevirus[x],rcount)
        
           #finding the virus in other drives
           length = len(drivelist)
           for x in range(0,length):
              rcount = fileremove(drivelist[x]+alldrivevirus[0],rcount)
              rcount = fileremove(drivelist[x]+alldrivevirus[1],rcount)
           message ="process complete...\n\n"+ str(rcount)+" threads have been removed."
           lbl.config(text = message)
           finalnotes()
        else:
            tkMessageBox.showerror("scan error","Scan process had not take place")
    else:
        tkMessageBox.showerror("File not found","First you have to run setup.bat")    
    
def fileremove(filename,count):
    try:
        fp = open(filename,"r")
    except IOError:
        return count
    else:
        fp.close()
        if(os.remove(filename)):
            return count-1
        else:
            return count  
        
        
#geting the appdata 
def setupstatus(): #code complete
    try:
        fp = open("data_status.txt","r")
    except IOError:
        return False
    else:
        status = fp.read(1)
        if(status == "t"):
            fp.close()
            return True
        else:
            return False
        
       
    
def get_appdata(): #code complete
    try:
        fp = open("data_info.txt","r")
        appdata = fp.read(50)
        size = len(appdata)
        cvalue = size-2
        new = appdata[0:cvalue]
        appdata = new
    except IOError:
        tkMessageBox.showerror("file not found","data_info.txt is not found")
    else:
        fp.close()
    

def finalnotes():
    tkMessageBox.showinfo("important info:"," Restart the computer and run this application again...\n\nIf virus is still not removed from the computer, \n!!!! Run the setup.bat file once again !!!!...")    


    


window = Tk()
window.title("Baby care antivirus")
window.geometry('425x250')

m1 = PanedWindow(width=10,borderwidth = 8)
m1.pack(fill=BOTH, expand=1)

lbl = Label(m1,text="welcome to \nBABY-CARE \n    antivirus solution \n\n created by Avinash kumar.",bg="black",fg="green", width = 30,bd = 3)
m1.add(lbl)

m2 = PanedWindow(m1, orient=VERTICAL , width = 5 , borderwidth = 3)
m1.add(m2)

btnscan = Button(m2,text =" scan",fg="black",bg = "lightblue" , width = 7,command = scanprocess)
m2.add(btnscan)
btnscan.place(x=50,y=50)

btnremove = Button(m2,text ="remove",fg="black",bg = "lightblue" , width = 7,command = removeprocess)
m2.add(btnremove)
btnremove.place(x=50,y=100)

window.mainloop()
