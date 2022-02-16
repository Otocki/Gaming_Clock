import tkinter as interface
import time
import psutil

'''Program will display a big digital clock in seperate window, showing real time. Window will appear on the side of the screen, or on the secondary monitor.
This clock checks all of the running processes for games and calculates how long were they opened.'''

"""TO DO:
-games list should be started automatically
-program senses only processes thet werw working before runing the script, it should be checking for them on the spot
-after killing the game process - program should kill the timer on its own
-after killing the game process we could log the runtime
-if another game is opened, program should display another timer in the new line
-clock window should change its geometry acordingly to the displayed elements"""


def window():
        '''this function gives the window its size, and puts it on the top-right corner of the secondary screen'''
        
        window1.title("zegarek")
        window1.attributes("-topmost",True) #window will be always on the top of another windows
        
        w=500                   #width
        h=400                  #height
        x = 1920+1024-w         #horizontal distance from the edge of the screen
        # 2594 = 1920(width_4)+1024(width_1)-350(window_width)
        y = 314                 #vertical distance from the edge of the screen
        
        window1.geometry("{}x{}-{}+{}".format(w,h,x,y))
        #(px)width x height + horizontal space to the edge of screen + vertical space to the egde of screen
        """screeninfo output:
                Monitor(x=0, y=0, width=1920, height=1080, width_mm=527, height_mm=296, name='\\\\.\\DISPLAY4', is_primary=True)
                Monitor(x=-1024, y=314, width=1024, height=768, width_mm=271, height_mm=203, name='\\\\.\\DISPLAY1', is_primary=False)
        """
        window1.configure(background="#7d84a1")

def Clock_mechanism():
        '''this function will update displayed time after every half a second'''
        
        hour = time.strftime("%H")
        minute = time.strftime("%M")
        second = time.strftime("%S")
        digit_display = "{}:{}:{}".format(hour,minute,second)
        digital_clock.configure(text=digit_display) #modifying given parameter
        digital_clock.after(500,Clock_mechanism) #recursion after half a second

def find_proces(nazwa):
        '''create a list of working processes that have a given string in their name'''
        
        process_amount=0
        process_list=[]
        
        for proc in psutil.process_iter(): #iterate through every running process
                try:
                        info=proc.as_dict(attrs=['create_time','name'])
                        if nazwa.lower() in info['name'].lower(): #check the name for given string
                                process_list.append(info)
                                process_amount=process_amount+1
                                
                except(psutil.NoSuchProcess,psutil.AccessDenied):
                        continue
        return process_list,process_amount

def stoper():
        '''this function will check game processes, dissplay the process name, and time it has been running'''
        message_tab=[]

        "this loop displays messages about every opened game"
        for i in range(amount_runing):
                
                informations,*_=find_proces(games_list[i])
                
                if (not informations): #check if list is empty
                        break
                else:
                        
                        #print(i,"nested: ",informations)
                        informations =informations[0]  #untangle nested results
                        #print("extracted: ",informations)        
                        #print("wartość :",informations['name'])
                        
                        title = informations['name']
                        
                        "here we change seconds since activated to the standard time format"
                        started_seconds = informations['create_time']
                        now_seconds = time.time()#get present date in seconds
                        subracted_seconds = now_seconds-started_seconds#subtract latter seconds from present ones
                        
                        #print(time.gmtime(subracted_seconds))#this is not good solution, but it works
                        
                        started_date = time.strftime("%H:%M:%S", time.gmtime(subracted_seconds))
                        
                        message ="{} jest uruchomiona już:\n {}".format(title,started_date)
                        print(message)
                        
                        #message_tab.append(message)
                        #print(message_tab)
                        #stoper_proces.config(text ="{}".format(message_tab[0]))
                        stoper_proces_1.configure(text= message)
                        
                        stoper_proces_1.after(500,stoper)
def fill_window():
        global window1,digital_clock,stoper_proces_1
        window1 = interface.Tk() #create the window
        window()
        digital_clock = interface.Label(window1, anchor="n",background="#7d84a1",foreground="#1F1F1F", text="", font="TimesNewRoman 60 bold")
        digital_clock.pack() #put the clock display inside the window
        Clock_mechanism()

        stoper_proces_1=interface.Label(window1, anchor="s",background="#7d84a1",foreground="#1F1F1F", text="", font="TimesNewRoman 20")
        stoper_proces_1.pack() #put the timer messages inside the window
        
def main():
        global amount_runing,games_list
        
        games_list=["Tumblebugs","oolite","LEGOMARVEL2_DX11.exe"] #for now games list must be started manually here
        amount_runing=0

        "this loop counts how many games are running"
        for i in range(len(games_list)):
                amount_runing=amount_runing+int(find_proces(games_list[i])[-1])
                print("liczba otwartych gierek: ",amount_runing)

        fill_window()
        stoper()
        window1.mainloop() #execute the whole script for this window
if __name__ == '__main__':
        main()