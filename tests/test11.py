class person:
    def __init__(self,num,name,sal):
        self._num=num
        self._name=name
        self._sal=sal
    def info(self):
        print(self._num, self._name,self._sal )
sample=person(4,'mohammed',100000000)
sample.info()