from pydantic import BaseModel
from typing import Optional

class ProcessRequest(BaseModel):
    file_id: str
    chunk_size: Optional[int] = 100   # it will be 100 if the user did not pass it
    overlap_size: Optional[int] = 20  # it will be 20 if the user did not pass it
    do_reset: Optional[int] = 100     # it will be 100 if the user did not pass it
    