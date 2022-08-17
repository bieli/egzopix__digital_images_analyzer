from typing import Union, List
from pydantic import BaseModel
from pydantic.dataclasses import dataclass


@dataclass(frozen=True)
class VisualModuleProperty:
    name: str
    description: str
    type: type
    hidden: bool
    payload: Union[str, bytes, dict, List, None] = None


class VisualModule(BaseModel):
    pass
