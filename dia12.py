
# Big data
# Se utiliza Pandas que por debajo utiliza Numpy


import pandas as pd
import numpy as np


df = pd.DataFrame({'col1':1.0, 'col2': np.asarray([1,2,3,4])})

print(df)
print(df.col1)
print(df.mean(1))

from tkinter import Frame, Button, Entry, Label, Text, END
from dia9 import search_in_urls
import asyncio
from threading import Thread

def statistics():
	


class MyApp(Frame):

    def __init__(self):
        super(MyApp, self).__init__()

        self.master.title("Web parser GUI")

        Label(self, text="Pattern").grid(column=0, row=0)
        self.pattern = Entry(self, width=50)
        self.pattern.grid(column=1, row=0, sticky="nsew")
        self.pattern.insert(0, '<h2.*>(.*)</h2>')

        Label(self, text="Url").grid(column=0, row=1)
        self.url = Entry(self, width=50)
        self.url.grid(column=1, row=1, sticky="nsew")
        self.url.insert(0, 'https://avesexoticas.org https://decalaveras.com')

        parse = Button(self, text="Parse Sync", command=self.enter_sync)
        parse.grid(column=1, row=2)
        parse = Button(self, text="Parse Async", command=self.enter_async)
        parse.grid(column=2, row=2)
        parse = Button(self, text="Parse After", command=self.enter_after)
        parse.grid(column=3, row=2)

        self.text = Text(self, width=100, height=20)
        self.text.grid(column=0, row=3, columnspan=2)
        self.pack()


    def enter_after(self):
    	# after es un metodo heredado de Frame
    	self.after(1, self.enter_sync)

    def enter_sync(self):
    	data = asyncio.run(
    		search_in_urls(self.url.get().split(), [self.pattern.get()]))
    	self.text.insert(1.0, data)
        #print(data)

    async def search(self, patterns, urls):
     	self.text.insert(1.0, await search_in_urls(patterns, urls))

    def enter_async(self):
    	try:
	    	Thread(target=lambda: asyncio.run(
	        	self.search(self.url.get().split(), [self.pattern.get()]))).start()
    	except NameError as e:
	    	print("Algo a ido mal:", e)

if __name__ == '__main__':
    myapp = MyApp()
    myapp.mainloop()