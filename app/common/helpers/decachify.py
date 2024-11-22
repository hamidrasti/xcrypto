import itertools

from django.conf import settings
from django.core.cache import cache

from app.common import constants


def decachify(
    cache_key: str | None = None,
    keys_group: str | None = None,
    keys_args: dict | None = None,
):
    if settings.LOG_CACHE:
        print(
            f"CACHE DELETE: cache_key={cache_key}, keys_group={keys_group}, keys_args={keys_args}"
        )

    if cache_key is not None:
        pattern = cache_key.split("{")[0] + "*"
        cache.delete_pattern(pattern)
        return

    if keys_group is None:
        keys = itertools.chain(*constants.CACHE_MAP.values())
    else:
        keys = constants.CACHE_MAP[keys_group]

    for key in keys:
        if keys_args is None:
            key_pattern = key.split("{")[0] + "*"
            cache.delete_pattern(key_pattern)
        else:
            # cache.delete(key)
            cache.delete(key.format(**keys_args))
