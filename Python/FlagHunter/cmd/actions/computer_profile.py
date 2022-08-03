import socket
from pathlib import Path
import os
import uuid as id

def getComputerProfile():
    home = Path.home()
    user = os.path.basename(home)
    hostname = socket.gethostname()
    ID = hex(id.getnode())

    return {"hostname":hostname, "user": user, "uuid":ID}