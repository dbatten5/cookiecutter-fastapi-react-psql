"""Module to hold the `utils` router."""
from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/ping",
    status_code=200,
    include_in_schema=False,
)
def ping() -> str:
    """Return a `pong` message.

    Returns:
        a string to indicate the app is alive
    """
    return "pong"
