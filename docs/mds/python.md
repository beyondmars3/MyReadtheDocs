# python

## 线程 
1. threading 类 t = threading.Thread()
2. 线程锁 threading.lock
3. 线程内部的私有变量 threading.local()


## 进程
1. multiprocessing 类 
```python
from multiprocessing import Process
p = Process(target=run_proc, args=('test',))
p.start()
p.join()
```
2. 进程池 用 Pool
3. 进程间通信用 Queue 。 from multiprocessing import Process, Queue
4. 线程内部隔离的类全局变量 threading.local()

## 异步IO
1. asyncio 直接内置了异步IO实现
2. asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
3. async/await 是python 3.5 对asyncio 的简写

## 引用传递
1. 对不可变对象，是值传递。 可变对象是引用传递
   
## flask 请求上下文
1. 当接收一个请求，flask会将这个请求的所有相关信息进行打包，打包形成的环境称为“请求上下文”(request context)。存放在堆栈中
2. 获取程序上下文对象 current_app、 g 
3. 获取请求上下文对象 request、session

## uWsgi
1. uwsgi yourfile.ini
```python
[uwsgi]
socket = 127.0.0.1:3031
chdir = /home/foobar/myproject/
wsgi-file = myproject/wsgi.py
processes = 4
threads = 2
stats = 127.0.0.1:9191
```
