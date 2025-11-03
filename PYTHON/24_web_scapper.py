# import asyncio
# import aiohttp
# from bs4 import BeautifulSoup


# async def scrape(url):
#     async with aiohttp.ClientSession() as session:
       
#         async with session.get(url) as response:
            
#             html = await response.text()

#             soup = BeautifulSoup(html, "html.parser")

#             if soup.title:
#                 title = soup.title.string
#             else:
#                 title = "No title found"

#             with open("data.txt", "a") as f:
#                 f.write(url + " - " + title + "\n")

#             print("Saved:", title)

# async def main():
#     urls = [
#         "https://google.com"
#     ]

#     tasks = []

#     for url in urls:
#         task = await scrape(url)


#     await asyncio.gather(*tasks)

# asyncio.run(main())





# import asyncio

# async def main():
#     print("Saving the output of extracted information")

# asyncio.run(main())






# import asyncio
# import time

# async def main():
#     start_time = time.time()
#     print("Saving the output of extracted information")
#     time_difference = time.time() - start_time
#     print(f"Scraping time: {time_difference:.2f} seconds")

# asyncio.run(main())




# import asyncio
# import csv
# import time

# async def main():
#     start_time = time.time()

#     with open('urls.csv') as file:
#         csv_reader = csv.DictReader(file)
#         for csv_row in csv_reader:
#             print(csv_row['url'])

#     time_difference = time.time() - start_time
#     print(f"Scraping time: {time_difference:.2f} seconds")

# asyncio.run(main())






# import asyncio
# import csv

# async def scrape(url):
#     print(f"Scraping {url}...")  # Placeholder

# async def main():
#     tasks = []

#     with open('urls.csv') as file:
#         csv_reader = csv.DictReader(file)
#         for csv_row in csv_reader:
#             task = asyncio.create_task(scrape(csv_row['url']))
#             tasks.append(task)

#     await asyncio.gather(*tasks)

# asyncio.run(main())



import asyncio
import csv
import aiohttp
from bs4 import BeautifulSoup

async def scrape(session, url):
    async with session.get(url) as resp:
        body = await resp.text()
        soup = BeautifulSoup(body, 'html.parser')
        book_name = soup.select_one('.product_main').h1.text
        rows = soup.select('.table.table-striped tr')
        product_info = {row.th.text: row.td.text for row in rows}
        print(f"{book_name}: {product_info}")

async def main():
    tasks = []

    async with aiohttp.ClientSession() as session:
        with open('urls.csv') as file:
            csv_reader = csv.DictReader(file)
            for csv_row in csv_reader:
                task = asyncio.create_task(scrape(session, csv_row['url']))
                tasks.append(task)

        await asyncio.gather(*tasks)

asyncio.run(main())
