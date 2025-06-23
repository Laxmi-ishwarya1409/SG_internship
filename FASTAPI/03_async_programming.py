# import time

# def sync_task():
#     print("Task1 started")
#     time.sleep(3)
#     print("Task1 ended")

# def main():
#     sync_task()
#     print("Task 2 started")

# main()

import asyncio
async def async_task1():
    print("Task1 statred")
    await asyncio.sleep(5)
    print("Task1 ended")

async def async_task2():
    print("Task2 started")
    await asyncio.sleep(2)
    print("Task2 ended")

async def main():
    # task1 = asyncio.create_task(async_task1())
    # task2 = asyncio.create_task(async_task2())

    # await task1
    # await task2

    # await asyncio.gather(task1,task2)
    await asyncio.gather(async_task1(),async_task2())

asyncio.run(main())