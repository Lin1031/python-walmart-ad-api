def fill_query_params(query, *args):
    return query.format(*args)


def endpoint(path, method="GET"):
    def decorator(function):
        def wrapper(*args, **kwargs):
            kwargs.update({"path": path, "method": method})
            return function(*args, **kwargs)

        wrapper.__doc__ = function.__doc__
        return wrapper

    return decorator
