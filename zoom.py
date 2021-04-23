from datetime import datetime
from time import sleep
import webbrowser
from sys import platform
import os
import pandas as pd


def join(meetingid, passw):
	url = "zoommtg://zoom.us/join?confno={}&pwd={}".format(meetingid, passw)
	webbrowser.open(url)
	
read = pd.read_csv('time.csv')

while True:
    # checking of the current time exists in our csv file
    now = datetime.now().strftime("%H:%M")
    if now in str(read['starttime']):

       row = read.loc[read['starttime'] == now]

       m_id = str(row.iloc[0,1])
       m_pswd = str(row.iloc[0,2])
       endtime = str(row.iloc[0,3])

       join(m_id, m_pswd)
       sleep(2)

       print(f'Joining {m_id}')

       sleep(60*int(endtime))

       if platform == "linux" or platform == "linux2":
       	os.system('killall -q zoom')
       elif platform == "win32":
       	os.system('taskkill /F /IM zoom.exe /T')
       elif platform == "darwin":
       	os.system("pkill -x zoom")

       print(f'Left {m_id}')