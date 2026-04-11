import time
from concurrent.futures import ThreadPoolExecutor
import asyncio
def check_status(item):
    print(item,"Check kar rela vidu")
    time.sleep(3)
    return f"{item} is eligible"
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, 
        check_status, "Socks")
        print(result)
        
asyncio.run(main())