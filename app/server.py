from collections import defaultdict
from random import randint
from bottle import route, run
from db import DivisionResult
from tasks import divide

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('postgres://postgres:postgres@database:5432/divide_service_db')

Session = sessionmaker(bind=engine)
s = Session()

def divide_stuff(top=None, bottom=None):
    top = top or randint(0,100)
    bottom = bottom or randint(1,100)   # за счёт этой конструкции знаменатель не принимает нулевое значение, даже если явно введён
    db_object = s.query(DivisionResult).filter(DivisionResult.top == top, DivisionResult.bottom == bottom).first()
    if db_object:
        result = str(db_object.answer)
    else:
        db_object = DivisionResult(top,bottom)
        division = divide.delay(top, bottom)
        db_object.uuid = division.id
        db_object.answer = division.get(timeout=3)
        result = 'processing...wait'
        s.add(db_object)
        s.commit()
    return {
        'числитель': top,
        'знаменатель': bottom,
        'результат': result,
        'создано': db_object.created.strftime('%d/%m/%Y - %H:%M:%S'),
        'идентификатор задачи': str(db_object.uuid)
        }


@route('/')
def random_division():
    return divide_stuff()

@route('/divide/<top:int>/<bottom:int>')
def explicit_division(top, bottom):
    return divide_stuff(top, bottom)

@route('/statistics')
def statistics():
    ops_amount = s.query(DivisionResult).count()
    d = defaultdict(int)
    all_numbers = s.query(DivisionResult.top, DivisionResult.bottom).all()
    for i in all_numbers:
        for j in i:
            d[j] += 1
    max_count = max(d.values())
    if max_count == 1:
        most_frequent_nums = 'Пока цифры не повторяются!'
    else:
        most_frequent_nums = ', '.join([str(k) for k,v in d.items() if v == max_count])
    return {
        'Количество вычислительных операций': ops_amount,
        'Наиболее частые числа, участвующие в расчётах': most_frequent_nums,
        'Количество вычислений с этими числами': max_count
    }


if __name__ == "__main__":
    run(
        host='0.0.0.0',
        port=5000
    )
