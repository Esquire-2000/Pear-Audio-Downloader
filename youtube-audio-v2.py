import youtube_dl
import requests
import time
import os
import getpass
import colorama
import sys
from colorama import Fore, Back, Style
# pear youtube audio downloader
def check_conn (): # check internet connection
	try:
		response=requests.get ("https://www.google.com/")
		return True
	except requests.ConnectionError: pass
	return False

def get_audio (url): #get audio only using youtube-dl
	ydl_opts = {
				'format': 'bestaudio/best', #best audio stream
				'outtmpl': 'Downloads/%(title)s.%(ext)s', #set path to Downloads
				'postprocessors': [{
				'key': 'FFmpegExtractAudio', # use ffmpeg to convert audio
				'preferredcodec': 'mp3', # prefered format mp3
				'preferredquality': '320',}]} # 320 kbps
	with youtube_dl.YoutubeDL (ydl_opts) as ydl:
		ydl.download ([url]) #download

def mk_dir(): #make folder if it doesn't exists
	if not os.path.exists('Downloads'):
		os.makedirs('Downloads')

def get_title (url): # get the video title
	opts={
		"quiet":True} # quietly
	with youtube_dl.YoutubeDL (opts) as ydl:
		info_dict = ydl.extract_info(url, download=False)
		video_title = info_dict.get('title', None)
	return video_title

def get_name ():
	name=getpass.getuser()
	name=name[:1].upper()+name[1:]
	return name

def check_url(): #check for url as argument
	if len(sys.argv) > 1:
		return True
	else:
		return False


colorama.init()
mk_dir()
print(Fore.YELLOW+"Welcome "+get_name()+" to Pear Audio Downloader"+ Style.RESET_ALL)
if not check_conn():
	print(Fore.RED+"No internet connection found. "+ Style.RESET_ALL)
	time.sleep(5)
else:
	if (check_url()==True):
		link=sys.argv[1]
	else:
		link=input("Enter the video URL: ")

	print(Fore.CYAN+"Title: "+get_title(link)+Style.RESET_ALL)
	get_audio(link) #test url: https://youtu.be/AOeY-nDp7hI
	print ("File(s) stored at:",os.getcwd()+"/"+"Downloads")
	print (Fore.GREEN+"Complete."+Style.RESET_ALL)
