def delete_cache(name: str):
    """
    Use the core of django to delete cache.
    Just a little nutshell to delete cache.
    :param name: key_value to delete on cache
    :return: None
    """
    from django.core.cache import cache
    if cache.get(name):
        cache.delete(name)