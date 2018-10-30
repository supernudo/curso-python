
# Aplicaciones graficas con Tkinter
# Mejor Pysimple GUI

from tkinter import Frame, Button, Entry, Label, Text, END
from dia9 import search_in_urls
import asyncio




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

        parse = Button(self, text="Parse", command=self.search_in_url)
        parse.grid(column=1, row=2)

        self.text = Text(self, width=100, height=20)
        self.text.grid(column=0, row=3, columnspan=2)
        self.pack()

    def prueba(self):
        print("Funciona")

    def search_in_url(self):
        data = asyncio.run(
        search_in_urls(self.url.get().split(), [self.pattern.get()]))
        self.text.insert(1.0, data)
        print(data)
        #for url in data:
        #    self.text.insert(1.0, '\n')
        #    print()
        #    for item in url:
        #        self.text.insert(1.0, item + '\n')
        #        print(item)


    def search_in_url_and_print(self):
        data = asyncio.run(
        search_in_urls(['https://avesexoticas.org'], ['<h2.*>(.*)</h2>']))
        self.text.insert(0.0, data[0][0])
        print(data[0])

    async def search_in_url_nowait(self):
        asyncio.create_task(search_in_url_and_print())





if __name__ == '__main__':
    myapp = MyApp()
    myapp.mainloop()