import _pickle as pickle  # for faster serialization
import socket

'''
Należy zmodyfikować adres IP w zmiennej self.host w konstruktorze na swój z sieci lokalnej
Należy uzupełnić metody connect(), disconnect(), send().
We wszystkich trzech przypadkach trzeba użyć metod na sockecie self.client
'''

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.0.1"
        self.port = 8999
        self.addr = (self.host, self.port)

    def connect(self):
        # Połączenie clienta z serverem

    def disconnect(self):
        # Rozłączenie clienta z serverem

    def send(self, data):
        # Wysłanie danych, najlepiej obsłużyć wyjątki instrukcją try
