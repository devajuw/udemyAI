import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt(data):
    return f"🔐{data [::-1]}"
async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, encrypt,"Debit_Card_2343")
        print(f"{result}")
        
        # while using processes this is required
if __name__ == "__main__":
    asyncio.run(main())