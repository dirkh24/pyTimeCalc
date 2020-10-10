import sys 
import os
from tkinter import Tk
from tkinter import ttk
from tkinter import IntVar, BooleanVar

from datetime import datetime, timedelta


# [*] create a Tkinter app with start/end time 
# [*] calculate the time between the two times
# [*] set the init value of the Combobox
# [*] note a pause 
# [*] make the pause configurable
# [*] grab the current time  

class MyApp(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # Variables
        self.chkValue = BooleanVar() 
        self.chkValue.set(False)

        # Packer
        self.grid()

        # Create the gui
        self.create_widgets()
    
    def create_widgets(self):
        # row 0
        self.label1 = ttk.Label(self, text="Starttime")
        self.label1.grid(column=0, row=0, columnspan=2)
        
        self.label2= ttk.Label(self, text="Endtime")
        self.label2.grid(column=2, row=0, columnspan=2)
        
        # row 1
        self.label3 = ttk.Label(self, text="Hour")
        self.label3.grid(column=0, row=1)
        self.label4 = ttk.Label(self, text="Minute")
        self.label4.grid(column=1, row=1)
        
        self.label5 = ttk.Label(self, text="Hour")
        self.label5.grid(column=2, row=1)
        self.label6 = ttk.Label(self, text="Minute")
        self.label6.grid(column=3, row=1)

        # define the values for hours and minutes
        self.hours = [str(hour) for hour in range(25)]
        self.minutes = [str(minute) for minute in range(61)]

        # row 2
        # combobox starttime
        self.hour1 = ttk.Combobox(self)
        self.hour1['values'] = self.hours
        self.hour1.grid(column=0, row=2, padx=10)
        self.hour1.set(self.hours[0])
        self.minute1 = ttk.Combobox(self)
        self.minute1['values'] = self.minutes
        self.minute1.grid(column=1, row=2, padx=10)
        self.minute1.set(self.minutes[0])

        # combobox endtime
        self.hour2 = ttk.Combobox(self)
        self.hour2['values'] = self.hours
        self.hour2.grid(column=2, row=2, padx=10)
        self.hour2.set(self.hours[0])
        self.minute2 = ttk.Combobox(self)
        self.minute2['values'] = self.minutes
        self.minute2.grid(column=3, row=2, padx=10)
        self.minute2.set(self.minutes[0])

        # row 3
        # Button to grap the actual time (Starttime)
        self.getTimeStart = ttk.Button(self, text="Current Time")
        self.getTimeStart.grid(column=0, row=3, columnspan=1, padx=10, pady=10)
        self.getTimeStart["command"] = self.set_current_start_time

        # Checkbox to note a pause
        self.checkbox = ttk.Checkbutton(self, text="Pause (0:45h)", var=self.chkValue)
        self.checkbox.grid(column=1, row=3, columnspan=2, padx=10, pady=10)

        # Button to grap the actual time (Endtime)
        self.getTimeEnd = ttk.Button(self, text="Current Time")
        self.getTimeEnd.grid(column=3, row=3, columnspan=1, padx=10, pady=10)
        self.getTimeEnd["command"] = self.set_current_end_time

        # row 4
        self.label7 = ttk.Label(self, text="Hour")
        self.label7.grid(column=1, row=4)
        self.label8 = ttk.Label(self, text="Minute")
        self.label8.grid(column=2, row=4)

        self.hour3 = ttk.Combobox(self)
        self.hour3['values'] = self.hours
        self.hour3.grid(column=1, row=5)
        self.hour3.set(self.hours[0])
        self.minute3 = ttk.Combobox(self)
        self.minute3['values'] = self.minutes
        self.minute3.grid(column=2, row=5)
        self.minute3.set(self.minutes[45])

        self.calc = ttk.Button(self, text="Calc")
        self.calc.grid(column=0, row=6, columnspan=6, padx=10, pady=10)
        self.calc["command"] = self.calculate
        
        self.label_result = ttk.Label(self, text="Results")
        self.label_result.grid(column=0, row=7, columnspan=6,padx=10, pady=10)

        self.label_result2 = ttk.Label(self, text="")
        self.label_result2.grid(column=0, row=8, columnspan=6)
        
    def get_current_time(self):
        # return the actual time
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        hour = now.strftime("%H")
        minute = now.strftime("%M")
        return (hour, minute)

    def set_current_start_time(self):
        hour, minute = self.get_current_time()
        # set the widgets
        self.hour1.set(hour)
        self.minute1.set(minute)
        

    def set_current_end_time(self):
        hour, minute = self.get_current_time()
        # set the widgets
        self.hour2.set(hour)
        self.minute2.set(minute)

    def calculate(self):
        # get the data form the widgets
        hour1 = self.hours[self.hour1.current()]
        minute1 = self.minutes[self.minute1.current()]
        hour2 = self.hours[self.hour2.current()]
        minute2 = self.minutes[self.minute2.current()]
        hour3 = self.hours[self.hour3.current()]
        minute3 = self.minutes[self.minute3.current()]
        #print(hour1, minute1, hour2, minute2)
        
        self.checkbox["text"] = "Pause (" + str(hour3) + ":" + str(minute3) + ")" 

        # start
        t1_hour=int(hour2)
        t1_min=int(minute2)

        # end
        t2_hour=int(hour1)
        t2_min=int(minute1)

        t1_year=2020
        t1_mon=1
        t1_day=1
        t1_sec=00
        t1_msec=0
        t1_wday=0
        t1_yday=0
        t1_isdst=0

        t1 = datetime(t1_year, t1_mon, t1_day, t1_hour, t1_min, t1_sec, t1_msec)

        t2_year=2020
        t2_mon=1
        t2_day=1
        t2_sec=00
        t2_msec=0
        t2_wday=0
        t2_yday=0
        t2_isdst=0

        t2 = datetime(t2_year, t2_mon, t2_day, t2_hour, t2_min, t2_sec,t2_msec)

        # define the pause
        t3_hour = int(hour3)
        t3_minute = int(minute3)
        t3 = timedelta(0,0,0,t3_hour,t3_minute,0,0)

        if self.chkValue.get():
            t_diff = t1 - t2 - t3
        else:
            t_diff = t1 - t2
        self.label_result2["text"] = str(t_diff)


if __name__ == "__main__":    
    root = Tk()
    app = MyApp(root)
    app.mainloop()
