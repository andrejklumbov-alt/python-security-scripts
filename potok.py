import threading as th

def hello(artem):
    print("запуск потока...")

potok1 = th.Thread(target=hello, args=("tema1",))
potok2 = th.Thread(target=hello, args=("tema2",))
potok3 = th.Thread(target=hello, args=("tema3",))

potok1.start()
potok2.start()
potok3.start()
print("запустили потоки")
potok1.join()
potok2.join()
potok3.join()
print("потоки закончили работать")
