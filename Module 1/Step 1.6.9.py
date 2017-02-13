import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, item):
        self.log(str(item))
        super(LoggableList, self).append(item)
