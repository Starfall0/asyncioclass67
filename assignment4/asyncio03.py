# example of gather for many coroutines in a list
import asyncio

# coroutine for a task
async def task_coro(value):
    # report a message
    print(f'>task {value} executing')
    # block for a moment
    await asyncio.sleep(1)

# define a main coroutine
async def main():
    # report a message
    print('main starting')
    # create many coroutines
    coros = [task_coro(i) for i in range(10)]
    # run the tasks
    await asyncio.gather(*coros)
    # report a message
    print('main done')

if __name__ == "__main__":
    #start the asyncio program
    asyncio.run(main())