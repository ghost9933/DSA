from  threading import Lock
class Foo:
    def __init__(self):
        self.f=Lock()
        self.s=Lock()
        self.f.acquire()
        self.s.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.f.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.f:
        # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.s.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.s:
        # printThird() outputs "third". Do not change or remove this line.
            printThird()