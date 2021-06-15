import time,threading
def f1():
    for i in 'network programming test':
        time.sleep(3)
        print(i)
def f2():
    for j in range(2,10):
        time.sleep(2)
        print(j)
print('end..')
class handle_thread(threading.Thread):
    def __init__(self):
        threading.thread.__init__(self)
    def run(self):
        f1()
class handle_thread(threading.Thread):
    def __init__(self):
        threading.thread.__init__(self)
    def run(self):
        f2()