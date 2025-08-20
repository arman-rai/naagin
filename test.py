# asyync processes 
# sab ekai choti bam bam, its best accourding to chatgpt re

import asyncio

async def say(msg, delay):
    await asyncio.sleep(delay)
    print(msg)

async def main():
    await asyncio.gather(
        say("Hello", 1),
        say("This", 2),
        say("is", 3),
        say("Asyncio", 4)
    )

asyncio.run(main())