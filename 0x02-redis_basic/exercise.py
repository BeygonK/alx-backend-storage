#!/usr/bin/env python3
"""This module creates a cache class"""
import uuid
import redis
from typing import Union, Optional, Callable
import functools


def count_calls(method: Callable) -> Callable:
    """Decorator to count number of times method is called"""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    def __init__(self):
        """Initialize cache and flush db"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis with a random key and return the key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """Retrieves data and optionally convert

        Args:
            key (str): The key under which the data is stored.
            fn (Optional[Callable]): A function to convert the data to
            the desired format.

        Returns:
            Union[str, bytes, int, float, None]: The retrieved data,
            optionally converted.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve a string from Redis.

        Args:
            key (str): The key under which the string is stored.

        Returns:
            Optional[str]: The retrieved string, or
            None if the key does not exist.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve an integer from Redis.

        Args:
            key (str): The key under which the integer is stored.

        Returns:
            Optional[int]: The retrieved integer,
            or None if the key does not exist.
        """
        return self.get(key, lambda d: int(d))
