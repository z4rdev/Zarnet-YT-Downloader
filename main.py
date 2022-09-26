#!/usr/bin/python3

from threading import Thread
import numpy as np
import os
import glob
from pytube import YouTube
from tqdm import tqdm
import time
import math
import pathlib
from pathlib import Path
import logging
import os
from datetime import datetime
from pytube.monostate import Monostate
from pytube import Stream, StreamQuery
from pytube import extract, request
import sys

print("Welcome to Youtube Video Downloader!")
print("          Made by Zarko		   ")
print("       NoMercyNet | NMTools	   ")

print("Type the URL of the video to be downloaded:")
url = input()
yt = YouTube(url)
print("Checking availability...")
availability = yt.check_availability()


if availability != None:
        print("Video Status: Unavailable...")
#       print("Do you want to bypass Age Restriction?")
#       print("Type: 'Yes' or 'No'")
#       bypass = int()
#       if bypass == Yes:
#               gate = yt.bypass_age_gate()
#                       if gate == 1:
#                       return
#                       else:
#                               sys.exit()
#               return
#       return
        sys.exit(1)

#if yt.bypass_age_gate() == None:
#	print("Bypassed Age Verification ")


print("Video Status: Available")
print("Video Title:")
title = yt.title
length = yt.length
print(title, "\n\n")
print("Duration: ", round(np.divide(length, 60), 2), "Minutes")
print("Views: ", yt.views)
print("Description:\n\n")
print(yt.description)
print("Calculating expected file size...")
yt = yt.streams.get_highest_resolution()
size_bytes = yt.filesize
bytes_to_mb = 1024
semi_result = np.divide(size_bytes, bytes_to_mb)
mb =round(np.divide(semi_result, bytes_to_mb))
print(mb, "MB")


print("Press Enter to START the Download...")
input()
print("Downloading video!")


#def download():
#	def register_on_progress_callback():
#		self.stream_monostate.on_progress = func

#def on_progress(yt, chunk, bytes_remaining):
#    total_size = yt.filesize
#    bytes_downloaded = total_size - bytes_remaining
#    percentage_of_completion = bytes_downloaded / total_size * 100
#    totalsz = (total_size/1024)/1024
#    totalsz = round(totalsz,1)
#    remain = (bytes_remaining / 1024) / 1024
#    remain = round(remain, 1)
#    dwnd = (bytes_downloaded / 1024) / 1024
#    dwnd = round(dwnd, 1)
#    percentage_of_completion = round(percentage_of_completion,2)
#
#    #print(f'Total Size: {totalsz} MB')
#    print(f'Download Progress: {percentage_of_completion}%, Total Size:{totalsz} MB, Downloaded: {dwnd} MB, Remaining:{remain} MB')


yt.download()
name = os.path.basename(__file__)
print(name)


#dir_path = '/home/kali/Desktop/tools/ytdl-zarnet/*.mp4'
dir = os.scandir()
print(dir)
#temp = os.path.getsize(dir_path)
#print(temp)


#while yt.download():
#	os.
#	for i in tqdm(range(size_bytes)):
#		time.sleep(0.000001)

for i in tqdm(range(int(size_bytes))):
	pass


print("Download Finished!")
