from functools import wraps
from sanic.response import json


def response_wrapper(decorated_=None):
    """将接口返回数据 标准化"""

    def actual_decorator(f):

        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            try:
                r = await f(request, *args, **kwargs)
                response = {'code': 0, 'message': 'Good day!', 'data': r}
            except Exception as e:
                response = {'code': -1, 'message': e.__repr__(), 'data': {}}

            return json(response)

        return decorated_function

    if decorated_:
        return actual_decorator(decorated_)
    else:
        return actual_decorator
