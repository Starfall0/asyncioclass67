# example of using an asyncio queue
from random import random
import asyncio
import time

# coroutine to generat work
async def producer(queue):
    start_time = time.perf_counter()
    print('Producer: Running')
    # generate work
    for i in range(10):
        #generate a value
        value = i
        # block to simulate work
        await asyncio.sleep(random())
        # add to the queue
        print(f'> Producer put {value}')
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    print('Producer: Done')
    # print produce time
    print(f'Produce time: {time.perf_counter() - start_time}')

# coroutine to consume work
async def consumer(queue):
    start_time = time.perf_counter()
    print('Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        item = await queue.get()
        # check for stop signal
        if item is None:
            break
        # report
        print(f'\t>Consumer got {item}')
    # all done
    print('Consumer: Done')
    # print consume time
    print(f'Consume time: {time.perf_counter() - start_time}')

async def main():
    # entry point coroutine
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

if __name__ == '__main__':
    # start the asyncio program
    asyncio.run(main())