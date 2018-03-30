from sanic.response import json, text
from sanic import Blueprint
from sanic.views import HTTPMethodView
from utils import response_wrapper

bp = Blueprint('demo_view')


@bp.get('/demo/person')
@response_wrapper
async def get_demo_person(request):

    pg_pool = request.app.pg_pool

    con = await pg_pool.acquire()
    try:
        data1 = await con.fetch('SELECT * from person;')
        data2 = await con.fetchval('SELECT * from person;')
        data3 = await con.fetchrow('SELECT * from person;')
    finally:
        await pg_pool.release(con)


    redis_pool = request.app.redis_pool
    val = await redis_pool.get('key1')
    print(val)

    return {'hello': 'blueprint'}

@bp.post('/demo/person')
@response_wrapper
async def post_demo_person(request):

    # pg_pool = request.app.pg_pool
    #
    # con = await pg_pool.acquire()
    #
    # try:
    #     await con.execute('''
    #        INSERT INTO person (name, age) VALUES (12 ,25);
    #        ''')
    #
    # finally:
    #     await pg_pool.release(con)

    # redis_pool = request.app.redis_pool
    # x = await redis_pool.set('key1', 'v1')

    async with request.app.pg_pool.acquire() as connection:
        # Open a transaction.
        async with connection.transaction():
            # Run the query passing the request argument.
            await connection.execute('''
                       INSERT INTO person (name, age) VALUES ('nisen1' ,25);
                       ''')

    return ['1', '3']

# class view demo
class DemoStudentAsyncView(HTTPMethodView):
    decorators = [response_wrapper]

    async def get(self, request):
        # if not request['session'].get('foo'):
        #     request['session']['foo'] = 0
        #
        # request['session']['foo'] += 1
        #
        # # from sanic.exceptions import abort
        # # abort(401)
        # 1/0
        # from sanic.exceptions import ServerError
        # raise ServerError("bad", status_code=500)

        return 'I am async get method'

    async def post(self, request):
        print(request)

        return ['aa', 'bb']


bp.add_route(DemoStudentAsyncView.as_view(), '/demo/student')
