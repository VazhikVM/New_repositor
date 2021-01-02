import tkinter
from time import sleep


class TrafficLight:
    def __init__(self, color):
        self.__c = color

    def running(self):
        my_host = tkinter.Tk()
        my_host.title('TrafficLight')
        my_can = tkinter.Canvas(my_host, width=500, height=400)
        my_can.pack()
        my_can.create_oval(200, 50, 300, 150, fill=self.__c)
        my_can.update()


while True:
    red = TrafficLight('Red')
    red.running()
    sleep(7)
    yellow = TrafficLight('yellow')
    yellow.running()
    sleep(2)
    green = TrafficLight('green')
    green.running()
    sleep(5)
    yellow = TrafficLight('yellow')
    yellow.running()
    sleep(2)
