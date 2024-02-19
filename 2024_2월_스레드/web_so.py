
import asyncio
import websockets

# 클라이언트가 서버로 메시지를 보낼 때 실행될 함수
async def receive_message(websocket, path):
    async for message in websocket:
        # 클라이언트로부터 메시지를 받으면 콘솔에 출력
        print(f"Received message from client: {message}")

# 웹소켓 서버를 실행하는 메인 함수
async def main():
    # 웹소켓 서버를 5678 포트에서 시작
    async with websockets.serve(receive_message, "localhost", 5678):
        # 서버가 종료될 때까지 대기
        await asyncio.Future()


if __name__ == "__main__":
    # 현재 실행 중인 이벤트 루프 가져오기
    asyncio.run(main())
