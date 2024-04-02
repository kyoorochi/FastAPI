from fastapi import APIRouter
import time, asyncio
from concurrent.futures import ProcessPoolExecutor
# 동기, 비동기 차이

route = APIRouter()

@route.get('/slow-sync-ping')
def slow_sync_ping():
    time.sleep(10)

    return {'msg':'pong'}

@route.get('/slow-async-ping')
async def slow_async_ping():
    await asyncio.sleep(10) # 10초를 기다린다. 그러나 다른 코드가 있으면 그 작업들은 계속 실행된다.

    return {'msg':'pong'}

# 피보나치 수열 -> 무거운 연산작업
# CPU에 부하가 걸리는 작업 (복잡한 연산): 동기
# I/O: 비동기
def cpu_intensive_task():
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n-1) + fibonacci(n-2)        
    result = fibonacci(35)
    return result

# Worst case
# CPU 부하가 되면 Event Loop에 부하가 걸림.
async def cpu_hard_task():
    result = await cpu_intensive_task()
    return {'msg':result}

# Good Case
# CPU에 부하가 많이 걸리는 작업은 이벤트 루프에서 분리 후, 별도의 프로세스에서 실행하게 만들어준다.
def cpu_bound_task():
    with ProcessPoolExecutor() as executor:
        result = asyncio.get_event_loop().run_in_executor(executor, cpu_intensive_task)
    return {'result': result}