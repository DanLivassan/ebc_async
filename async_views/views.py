import asyncio

import time
import httpx

from django.http import JsonResponse


def api(request):
    time.sleep(1)
    payload = {"message": "Hellow Async"}

    if "task_id" in request.GET:
        payload['task_id'] = request.GET['task_id']
    return JsonResponse(payload)


async def http_call_async():
    for num in range(6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)


async def async_view(request):
    e_loop = asyncio.get_event_loop()
    e_loop.create_task(http_call_async())
    return JsonResponse({"its": "OK"})
