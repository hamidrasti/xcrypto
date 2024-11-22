from django.conf import settings
from django.core.cache import cache


def cachify(key, lazy_value, timeout):
    cached_value = cache.get(key)

    if timeout == 0:
        # don't add redis overhead if it's cached for 0 seconds
        return lazy_value()

    if cached_value is not None and settings.CACHE_ENABLED:
        if settings.LOG_CACHE:
            print("CACHE HIT", key, "->", cached_value)
        return cached_value
    else:
        value = lazy_value()
        cache.set(key, value, timeout)
        if value is not None:
            # if isinstance(value, QuerySet):
            # 	value = list(value)
            if settings.LOG_CACHE:
                print("CACHE EVALUATED", key, "->", value)
    return value
