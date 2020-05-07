import io

from fastapi import FastAPI


class Client(FastAPI):

    def __init__(self, apache_log_file, buffer_size):
        self.stream = io.open(apache_log_file, buffering=buffer_size)
        super().__init__()

