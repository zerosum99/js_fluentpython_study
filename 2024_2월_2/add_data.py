
import multiprocessing

# 공유 자원에 데이터를 추가하는 함수
def add_data(shared_list, data):
    shared_list.append(data)

if __name__ == "__main__":
    # Manager 객체 생성
    manager = multiprocessing.Manager()

    # 공유 리스트 생성
    shared_resource = manager.list()

    # 여러 프로세스를 생성하여 공유 자원에 데이터를 추가
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=add_data, args=(shared_resource, i))
        processes.append(p)
        p.start()

    # 모든 프로세스가 종료될 때까지 대기
    for p in processes:
        p.join()

    # 공유 자원 출력
    print("Shared Resource:", shared_resource)

