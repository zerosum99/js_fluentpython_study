import asyncio, time 

async def main2() :
    print(f"{time.ctime()} Hello ")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye ")

# 현재 실행 중인 이벤트 루프 가져오기
loop = asyncio.get_event_loop()

print(loop)
loop.stop()
