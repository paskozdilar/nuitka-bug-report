#!/usr/bin/env python3

import asyncio
from grpc.aio import insecure_channel
from proto import test_pb2_grpc
from proto import test_pb2


async def main():
    async def test_task():
        while True:
            try:
                async for _ in Listener().listen():
                    pass

            except Exception as exc:
                print("Exception:", exc, flush=True)
                await asyncio.sleep(1)

    async with asyncio.TaskGroup() as tg:
        tg.create_task(test_task())


class Listener:
    async def listen(self):
        async with insecure_channel("localhost:1234") as channel:
            stub = test_pb2_grpc.TestServiceStub(channel)
            async for message in stub.ServerStream(test_pb2.Request(data="foo")):
                yield message



if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
