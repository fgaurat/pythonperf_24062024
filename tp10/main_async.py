import asyncio
import time


async def add(a,b):
    await asyncio.sleep(1)
    return a+b

async def main():
    start = time.perf_counter()

    # print('Hello ...')
    # asyncio.sleep(1)
    # print('... World!')
    # a = await add(1,2)
    # b = await add(15,72)
    # print(a)
    # print(b)
    
    all = [add(1,1),add(2,2),add(3,3),add(4,4)]

    r = await asyncio.gather(*all)
    print(r)
    end = time.perf_counter()
    print(f"{end-start:.2f}s")
if __name__=='__main__':
    asyncio.run(main())
