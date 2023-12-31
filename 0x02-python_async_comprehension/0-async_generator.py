#!/usr/bin/env python3
"""This module defines a function called `async_generator`"""
from asyncio import sleep
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Asynchronously iterate over the values generated by async_generator"""
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)
