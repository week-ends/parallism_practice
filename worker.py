from celery import Celery
from celery.signals import worker_init
from celery.signals import worker_shutdown
from celery.bin.celery import result

//rabbitmq를 설정해준다
//celery는 default로 rabbitmq를 브로커(messagequeue)로 사용한다.
//guest는 rabbitmq에서 지원해주는 가장 default 큐다.
app = Celery('tasks', broker='amqp://guest:guest@localhost:5672//')

//워커가 초기화됬을때 
@worker_init.connect
def init_worker(**kwargs):
	print('init')

//워커가 종료됬을때
@worker_shutdown.connect
def shutdown_worker(**kwargs):
	print('shut')

//실제 task들을 받는 부분.
//받은데이터를 thread로 처리한다.
@app.task(name='task')
def worker(data):
	Thread = threading.Thread(target=run, args=(data,))
	Thread.start()

def run(data):
	//working
