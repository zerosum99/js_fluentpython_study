import asyncio

async def print_numbers():
    for i in range(5):
        print(i)
        await asyncio.sleep(1)

async def print_letters():
    for letter in 'ABCDE':
        print(letter)
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_letters())

    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    await main()
