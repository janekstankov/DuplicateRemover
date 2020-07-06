import os
from tkinter import *
import ctypes
import time
from tkinter import filedialog
from sys import exit



clear = lambda: os.system('cls')



root = Tk()
root.withdraw()

ctypes.windll.kernel32.SetConsoleTitleW('Duplicate Remover by Xubiz#0001 - Welcome!')
print("Welcome in duplicate remover!")
print("\n")
time.sleep(2)
print('Choose your file to remove duplicate:')
plik = filedialog.askopenfilename(initialdir="/downloads", title="Choose file to remove duplicates",filetypes=(("TXT", "*.txt"), ("ALL", "*.*")))
print('Starting...')
time.sleep(1)
clear()


czasl = time.localtime()
czas = time.strftime("%d.%m_%H.%M.%S", czasl)


f = open(f'results({czas}).txt', 'w+')

lines = 0
duplicates = 0
check = 0


with open (plik, 'r') as z:
    for line in z:
        lines += 1


flag = False
start = time.time()
with open(plik) as fp:
		for line in fp:
			check += 1
			check_time = time.time() - start
			tz = time.strftime("%H:%M:%S", time.gmtime(check_time))
			ctypes.windll.kernel32.SetConsoleTitleW(f'Lines: {lines}  Checked: {check} Duplicates: {duplicates} Time: {tz}')
			for temp in f:
				if temp == line:
					flag = True
					print(f'Duplicate Found! ({check} line)')
					duplicates += 1
					break
			if flag == False:
				f.write(line)
			elif flag == True:
				flag = False
			f.seek(0)
		f.close()
stop = time.time()
elapsed_time = time.time() - start
t = time.strftime("%H:%M:%S", time.gmtime(elapsed_time))


lns = 0
with open (f'results({czas}).txt', 'r') as y:
    for line in y:
        lns += 1

clear()
ctypes.windll.kernel32.SetConsoleTitleW(f'All duplicates removed | Duplicates Remover by Xubiz#0001')
print(f'All duplicates have been removed || {duplicates} duplicates in {lines} lines / {lns} lines in file | Time: {t}')
print('\n')
input('Press any key to exit')
exit(0)