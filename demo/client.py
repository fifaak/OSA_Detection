import httpx
import asyncio
import json
async def fetch_data():
    url = "http://127.0.0.1:8000/stream"
    async with httpx.AsyncClient() as client:
        async with client.stream("GET", url) as response:
            async for chunk in response.aiter_text():
                if chunk.strip():
                    data = json.loads(chunk)
                    print(data)

if __name__ == "__main__":
    asyncio.run(fetch_data())
