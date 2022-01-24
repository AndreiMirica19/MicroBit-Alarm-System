# Add your Python code here. E.g.
from microbit import *
import utime
import music
import os
users=[]
arm=1
s=""
exit=True
h=False



initialTime=utime.ticks_ms()

armed=False
shake=False
alarmed_active=False
minutes=0
hours=0

log="" 
message=""
def readLog():
    l=""
    
    if len(os.listdir())>1:
        file=open("logs.txt")
        log=(file.read())
        file.close()
        if len(os.listdir())>2:
            file=open("time.txt")
            tt=(file.read())
            tt=tt.split(" ")
        
            hours=int(tt[0])
            minutes=int(tt[1])
            initialTime=int(tt[2])
            file.close()
            return log,hours,minutes
        else:    
            return log,0,0
    else:
        return l,0,0
def logs(log):
   
    if log!="":
        log=log+"\n"
    if hours<10:
        log=log+"0"+str(hours)+":"
    elif hours>9:
        log=log+str(hours)+":"
    if  minutes<10:
        log=log+"0"+str(minutes)
    elif minutes>9:
        log=log+" "+str(minutes)
    log=log+" "+message
    file=open("logs.txt","w")
    file.write(log)
    file.close()
    return log
full=Image("99999:"
           "99999:"
           "99999:"
           "99999:"
           "99999")
empy= Image("00000:"
           "00000:"
           "00000:"
           "00000:"
           "00000")            
           
def time(minutes,hours):
    currentTime=utime.ticks_ms()
    if utime.ticks_diff(currentTime,initialTime)%60000==0:
        
        minutes=minutes+1
        if minutes==60:
           hours=hours+1
           minutes=0
        file=open("time.txt","w")
        file.write(str(hours)+" "+str(minutes)+" "+str(initialTime))
        file.close()   
    return minutes,hours
log,hours,minutes=readLog()
if(log=="None"):
    log=str(log)
    log=""
while True:
    
    minutes,hours=time(minutes,hours)
    msg_bytes = uart.read()
    if armed==False and alarmed_active==False:
        display.clear()
    if alarmed_active==True:
        minutes,hours=time(minutes,hours)
        display.show(full)
        music.play("F#")
        display.show(full)
        sleep(100)
        display.clear()
        sleep(100)
        display.show(full)
       
    if armed==True:
        #minutes,hours=time(minutes,hours)
        t1 =((utime.ticks_ms()))
        if utime.ticks_diff(t1,t)==arm*60000:
            armed=False
            display.show(Image.HAPPY)
            message="Automatic disarmed system."
            log=logs(log)
            sleep(3000)
            display.clear()
        gesture = accelerometer.current_gesture()
        if gesture=="shake" and shake==False:
            ts =((utime.ticks_ms()))
            shake=True
        if shake==True and gesture=="shake":
           
            ts2=((utime.ticks_ms()))
            if utime.ticks_diff(ts2,ts)>=2000:
                alarmed_active=True
                message="Alarm activated."
                log=logs(log)
                
                armed=False
        else:
            shake=False
                 
                 
    if button_a.is_pressed() and button_b.is_pressed() and exit==True:
        i=0
        x=0
        display.show(x)
        sleep(500)
        pin=""
        
        while i<4:
            #minutes,hours=time(minutes,hours)
            if button_a.is_pressed() and x<10:
                x=x+1
                display.clear()
                display.show(x)
                sleep(500)
                
            elif button_a.is_pressed() and x>=9:
                x=0               
                display.clear()
                display.show(x)
                sleep(500)
                
            elif button_b.is_pressed() and x>0:
                x=x-1
                display.clear()
                display.show(x)
                sleep(500)
                
            elif button_b.is_pressed() and x==0:
                x=9               
                display.clear()
                display.show(x)
                sleep(500)
               
            elif  pin_logo.is_touched():
                pin=pin+str(x)
                sleep(500)
                x=0
                display.show(x)
                i=i+1
        
        ss=""
        l=-1
        for u in users:
            if(u["pin"]==pin):
                display.show(Image.HAPPY)
                sleep(3000)
                display.clear()
                l=0
                if armed==False and alarmed_active==False:
                    display.show(full)
                    armed=True
                    t =((utime.ticks_ms()))
                   
                    message=u["name"]+" armed the system."
                    log=logs(log)
                elif armed==True:
                    armed=False
                    message=u["name"]+" disarmed the system."
                    logs(log)
                    log=logs(log)
                if alarmed_active==True:
                    armed=False
                    alarmed_active=False
                    message=u["name"]+" disarmed the system."
                    logs(log)
                    log=logs(log)
        if l==-1:
            display.show(Image.SAD)
            sleep(3000)
            display.clear()
    elif str(msg_bytes)!="None"and armed==False and alarmed_active==False  :
        exit=False
           
            
        
    if exit==False:
        minutes,hours=time(minutes,hours)
        s=input("alarm cmd>")
        c=0
        s=s.split(" ")
   
    if len(s)==4 and s[0]=="profile" and s[1]=="add" :
        if s[3].isdigit() and len(s[3])==4:
            
            if len(users)<3:
                user={
                  "name":s[2],
                  "pin":s[3]
                }
                d=0
                for u in users:
                    if (u["name"] == s[2]):
                        d=1
                        u["pin"]=s[3]
                if(d==0):        
                    users.append(user)
                    print("Profile added.")
                   
                   
            else:
                print("Could not save profile. Limit exceeded.")
        else:
           print("Could not save profile. Invalid pin.")
               
    elif  len(s)==3 and s[0]=="profile" and s[1]=="delete" :
        
        for u in users:
            if(u["name"]==s[2]):
                users.remove(u)
                print("Profile deleted")
                c=1
        if(c!=1):        
            print("Could not delete profile. Profile name does not exist.")
    elif len(s)==3 and s[0]=="arm" and s[1]=="time" and s[2].isdigit() :
        arm=int(s[2])
    elif len(s)==1 and s[0]=="exit":
        exit=True
        h=False
    elif len(s)==2 and s[0]=="log" and s[1]=="print":
        file=open("logs.txt")
        print(file.read())
        file.close()
    elif len(s)==2 and s[0]=="log" and s[1]=="delete":
        log=""
        log=logs(log)
        print("Logs deleted.")
   
      
