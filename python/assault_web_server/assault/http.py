import time 
import asyncio


def fetch(url):
    """ Make a request and return the value """
    pass

def worker(name, queue, results):
    """A function to take unmade requests from a queue and perform the work, add results to results list"""
    pass

async def distribute_work(url, requests, concurrency, results):
    """Divide the work into batches and collect the final result"""
    
    queue = asyncio.Queue()
    for _ in range(requests):
        queue.put_nowait(url)

    tasks = []
    for i in range(concurrency):
        task = asyncio.create_task(worker(f"Worker-{i+1}", queue, results))
        tasks.append(task)

    started_at = time.monotonic()
    await queue.join()
    ended_at = time.monotonic()
    total_time = ended_at - started_at

    for task in tasks:
        task.cancel()

    print("---")
    print(f"{concurrency} workers took {total_time:.2f} seconds to complete {len(tasks)} requests.")

def assault(url, requests, concurrency):
    """entry point to making requests, the sync function which will help call async functions"""
    results = []
    asyncio.run(distribute_work(url, requests, concurrency, results))
    print(results)

