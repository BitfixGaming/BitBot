from bs4 import BeautifulSoup
import aiohttp
import asyncio
import json


async def write_game_json():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://en.wikipedia.org/wiki/List_of_video_games_considered_the_best') as resp:
            print(resp.status)

            html = await resp.text()

            soup = BeautifulSoup(html, features="html.parser")

            table = soup.find_all("table", "wikitable")[0]

            rows = table.find_all("tr")

            games = []

            for row in rows:
                for title in row.find_all("i", recursive=True):
                    print(title.text)
                    games.append(title.text)

            with open("games.json", "w") as f:
                f.write(json.dumps(games))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(write_game_json())