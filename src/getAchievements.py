import asyncio
import aiohttp
import logging
import pyxivapi

async def getAchievements():
    client = pyxivapi.XIVAPIClient(api_key="")

    character = await client.character_by_id(
        lodestone_id=0,
        extended=True,
        include_achievements=True        
    )

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='%H:%M')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getAchievements())
