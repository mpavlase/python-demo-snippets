# asyncio, run in executor

## findings
- executing async loop blocks main execution flow
- awaitable is run from same OS thread as loop has started
- `loop.run_in_executor` run given awaitable in **separate thread** and as benefit,
  allows loop to execute another async task (due `run_in_executor` is awaitable)

Output:
```
13:26:00.412 | proc MainProcess | threadid  3164| thr MainThread | main - begin
13:26:00.412 | proc MainProcess | threadid  3164| thr MainThread | async_run_in_exec: going to sleep
13:26:00.412 | proc MainProcess | threadid  1676| thr  asyncio_0 | blocking_sleep: going to sleep
13:26:00.412 | proc MainProcess | threadid  3164| thr MainThread | async_run_in_exec: going to sleep
13:26:00.412 | proc MainProcess | threadid 26024| thr  asyncio_1 | blocking_sleep: going to sleep
13:26:05.438 | proc MainProcess | threadid 26024| thr  asyncio_1 | blocking_sleep: waking up
13:26:05.438 | proc MainProcess | threadid  1676| thr  asyncio_0 | blocking_sleep: waking up
13:26:05.438 | proc MainProcess | threadid  3164| thr MainThread | async_run_in_exec: waking up
13:26:05.438 | proc MainProcess | threadid  3164| thr MainThread | async_run_in_exec: waking up
13:26:05.438 | proc MainProcess | threadid  3164| thr MainThread | main - end
```

## Reference
https://stackoverflow.com/questions/55027940/is-run-in-executor-optimized-for-running-in-a-loop-with-coroutines

