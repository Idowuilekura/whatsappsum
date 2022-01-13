from pydantic import BaseModel
from typing import List

class WhatsappSum(BaseModel):
    text_to_summ : List[str]

