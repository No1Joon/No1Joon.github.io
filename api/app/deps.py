from typing import Annotated

from fastapi import Depends, Request
from pymongo.asynchronous.database import AsyncDatabase


def get_db(request: Request) -> AsyncDatabase:
    db = getattr(request.app.state, "db", None)
    if db is None:
        raise RuntimeError("Database not initialized")
    return db


DbDep = Annotated[AsyncDatabase, Depends(get_db)]
