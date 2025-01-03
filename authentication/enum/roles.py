from enum import Enum

class Role(Enum):
    ADMIN = 'admin'
    WORKER = 'worker'
    USER = 'user'