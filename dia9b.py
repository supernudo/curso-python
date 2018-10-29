
# Aplicaciones graficas con Tkinter
# Mejor Pysimple GUI

from tkinter import Frame, Button, Entry
from dia9 import search_in_urls
import asyncio




class MyApp(Frame):

    def __init__(self):
        super(MyApp, self).__init__()
        pattern = Entry(self)
        pattern.grid(column=0, row=0)
        parse = Button(self, text="Parse", command=self.search_in_url)
        parse.grid(column=0, row=1)
        self.pack()

    def prueba(self):
        print("Funciona")

    def search_in_url(self):
        data = asyncio.run(
        search_in_urls(['https://avesexoticas.org'], ['<h2>(.*)</h2>']))
        print(data)


if __name__ == '__main__':
    myapp = MyApp()
    myapp.mainloop()