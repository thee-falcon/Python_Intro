# import ABC Class from abc module
from abc import ABC, abstractmethod

class   InvalidOperationsError(Exception):
    pass

class Stream(ABC):
    def __init__(self) -> None:
        self.opend = False

    def open(self):
        if (self.open):
            raise IndentationError("Stream is already opend")
        self.open = True

    def close(self):
        if not (self.open):
            raise InvalidOperationsError("Sream is already closed")
        self.open = False

    @abstractmethod
    def read(self):
        pass

class   FileStream(Stream):
    # we Implement the read() method from Abstract Class
    def read(self):
        print("Reading DATA from File")

class   NetworkStream(Stream):
    # we Implement the read() method from Abstract Class
    def read(self):
        print("Reding DATA from Network.")

class MemoryStream(Stream):
    def read(self):
        print("Reading DATA from a memory stream")

stream = MemoryStream()
stream.read()
