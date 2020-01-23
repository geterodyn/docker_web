import celery

app = celery.Celery(
    'hw-docerized-tasks',
    broker='amqp://admin:mypass@rabbit:5672',
    backend='redis://redis'
)

@app.task
def divide(x, y):
    return x/y
