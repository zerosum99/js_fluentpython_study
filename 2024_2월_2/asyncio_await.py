
import asyncio
import aiohttp

async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = 'https://example.com'
    page = await fetch_page(url)
    print(page)

asyncio.run(main())
