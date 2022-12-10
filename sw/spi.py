
class SPI():

    MSB = 1
    MASTER = 1

    def __init__(self):
        pass

    def init(self,baudrate=1000000, *, polarity=0, phase=0, bits=8, 
             firstbit=SPI.MSB, sck=None, mosi=None, miso=None, 
             pins=(None)):
        pass

    def send(self):
        pass

    def read(self):
        pass

    def send_recv(self):
        pass
