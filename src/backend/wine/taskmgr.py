from typing import NewType

from bottles.backend.logger import Logger  # pyright: reportMissingImports=false
from bottles.backend.wine.wineprogram import WineProgram

logging = Logger()


class Taskmgr(WineProgram):
    program = "WINE Task Manager"
    command = "taskmgr"
