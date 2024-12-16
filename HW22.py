import os
import aiohttp
import asyncio
import requests

def fetch_json_with_requests(url, folder):
    response = requests.get(url)
    if response.status_code == 200:
        json_data = response.json()
        os.makedirs(folder, exist_ok=True)
        for i, obj in enumerate(json_data):
            file_path = os.path.join(folder, f"object_{i+1}.json")
            with open(file_path, 'w') as file:
                file.write(str(obj))
        print(f"JSON объекты сохранен в : {folder}")

async def fetch_json_with_aiohttp(url, folder):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                json_data = await response.json()
                os.makedirs(folder, exist_ok=True)
                for i, obj in enumerate(json_data):
                    file_path = os.path.join(folder, f"object_{i+1}.json")
                    with open(file_path, 'w') as file:
                        file.write(str(obj))
                print(f"JSON объекты сохранен в : {folder}")

def main():
    json_url = "https://jsonplaceholder.typicode.com/posts"
    fetch_json_with_requests(json_url, "json_requests")
    asyncio.run(fetch_json_with_aiohttp(json_url, "json_aiohttp"))

if __name__ == "__main__":
    main()