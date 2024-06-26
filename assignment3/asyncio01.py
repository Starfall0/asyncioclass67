# check the type of a coroutine
import asyncio
# define a coroutine
async def custom_coro():
    # await another coroutine
    await asyncio.sleep(1) #sleep แบบไม่ต้องรอฉัน

# create the coroutine
coro = custom_coro() # return function
# check the type of the coroutine
print(type(coro))