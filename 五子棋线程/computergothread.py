import threading


class ComputerGoThread(threading.Thread):
    def __init__(self,engine,chessmanPC):
        super().__init__()
        self.engine = engine
        self.chessmanPC = chessmanPC
    def run(self):
        print('ComputerGoThread run启动')
        while True:
            self.chessmanPC.doWait()
            self.engine.computerGo(self.chessmanPC)
            self.chessmanPC.doNotify()