import logging
import asyncio
import time

logger = logging.getLogger('main')
fmt = logging.Formatter(
    fmt='%(asctime)s.%(msecs)03d | proc %(processName)s | threadid %(thread)5s| thr %(threadName)10s | %(message)s',
    datefmt='%H:%M:%S'
)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(fmt)

logger.addHandler(handler)



async def async_run_in_exec():
    loop = asyncio.get_event_loop()
    logger.info('async_run_in_exec: going to sleep')
    await loop.run_in_executor(None, blocking_sleep, 5)
    #time.sleep(5)
    logger.info('async_run_in_exec: waking up')

def blocking_sleep(duration):
    logger.info('blocking_sleep: going to sleep')
    time.sleep(duration)
    logger.info('blocking_sleep: waking up')


async def parallel():
    # run two sleep_tests in parallel and wait until both finish
    await asyncio.gather(async_run_in_exec(), async_run_in_exec())


def main():
    logger.info('main - begin')
    asyncio.run(parallel())
    logger.info('main - end')


main()
