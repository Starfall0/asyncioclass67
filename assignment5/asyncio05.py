# assignment05 Cook wait()
from random import random
import asyncio

async def make_rice():    # fried rice
    value = 1 + random()
    await asyncio.sleep(value)
    print(f"Microwave (Rice): Cooking {value} seceonds...")
    await asyncio.sleep(1)  # 2: pause, another tasks can be run
    return print("Microwave (Rice): Finished cooking")

async def make_noodle():   # noodle
    value = 1 + random()
    await asyncio.sleep(value)
    print(f"Microwave (Noodle): Cooking {value} seceonds...")
    await asyncio.sleep(1)  # 2: pause, another tasks can be run
    return print("Microwave (Noodle): Finished cooking")
    
async def make_curry():   # curry
    value = 1 + random()
    await asyncio.sleep(value)
    print(f"Microwave (Curry): Cooking {value} seceonds...")
    await asyncio.sleep(1)  # 2: pause, another tasks can be run
    return print("Microwave (Curry): Finished cooking")

# main coroutine
async def main():
    # create tasks
    rice_task = asyncio.create_task(make_rice(), name = 'Rice')
    noodle_task = asyncio.create_task(make_noodle(), name = 'Noodle')
    curry_task = asyncio.create_task(make_curry(), name = 'Curry')
    tasks = [rice_task, noodle_task, curry_task]
    # get the first task to complete
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    # report results
    print(f'Complete task: {len(done)}')
    first = done.pop()
    print(f'- {first.get_name()} is completed') # name of task
    print(f'Uncomplete task: {len(pending)}')

if __name__ == '__main__':
    # start the asyncio program
    asyncio.run(main())