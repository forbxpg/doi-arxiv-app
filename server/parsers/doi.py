import aiohttp
import asyncio

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:144.0) Gecko/20100101 Firefox/144.0",
    "Accept": "*/*",
    "Accept-Language": "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3",
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    "Referer": "https://www.sciencedirect.com/",
    "Origin": "https://www.sciencedirect.com",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
}

params = {
    "type": "doi",
    "id": "10.1016/j.cogsys.2023.101185",
}


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://api.plu.mx/widget/elsevier/artifact",
            params=params,
            headers=headers,
        ) as response:
            res = await response.json()
            print(res)


if __name__ == "__main__":
    asyncio.run(main())
