
# Peticiones a pagina web
# Ejemplo, spider a pagina web de forma no asincrona para que no te corten las
# alas, peticiones no intensivas.Ejemplo

# Modulo aiohttp: peticiones a una url.

import aiohttp
import asyncio
import re

async def fetch (session, url):
    async with session.get(url) as response:
        if response.status != 200:
            response.raise_for_status()
        return await response.text()

async def fetch_all (session, urls):
    results = await asyncio.gather(*[asyncio.create_task(fetch(session, url)) for url in urls])
    return results

async def search_in_urls(urls, regexs):
    async with aiohttp.ClientSession() as session:
        htmls = await fetch_all(session, urls)
        return [re.findall(regex, html, re.DOTALL) for regex in regexs for html in htmls]

async def main():
    urls = ['https://avesexoticas.org'] #, 'https://cnn.com', 'https://google.com']
    async with aiohttp.ClientSession() as session:
        htmls = await fetch_all(session, urls)
        for html in htmls:
            print (re.findall("<h3.*>(.*)</h3>", html, re.DOTALL))
            #print (html.encode("utf-8"))

if __name__ == '__main__':
    #asyncio.run(main())
    data = asyncio.run(
        search_in_urls(['https://avesexoticas.org'], ['<h2>(.*)</h2>']))
    print(data)