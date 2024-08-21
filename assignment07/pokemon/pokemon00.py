import aiofiles
import asyncio
import json

pokemonapi_directory = './asyncioclass67/assignment07/pokemon/pokemonapi'
pokemonmove_directory = './asyncioclass67/assignment07/pokemon/pokemonmove'

async def main():
    # Read the content of the json file.
    async with aiofiles.open(f'{pokemonapi_directory}/articuno.json', mode ='r') as f:
        contents = await f.read()
    
    print(contents)

if __name__ == '__main__':
    asyncio.run(main())