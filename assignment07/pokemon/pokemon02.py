import aiofiles
import asyncio
import json

pokemonapi_directory = './asyncioclass67/assignment07/pokemon/pokemonapi'
pokemonmove_directory = './asyncioclass67/assignment07/pokemon/pokemonmove'

async def main():
    # Read the content of the json file.
    async with aiofiles.open(f'{pokemonapi_directory}/articuno.json', mode ='r') as f:
        contents = await f.read()

    # Load it into a dictionary and create a list of moves.
    pokemon = json.loads(contents)
    moves = [move['move']['name'] for move in pokemon['moves']]
    print(moves)

if __name__ == '__main__':
    asyncio.run(main())