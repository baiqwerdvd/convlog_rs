from pathlib import Path
from typing import Union, List, TypeAlias

__version__: str

PathOrStr: TypeAlias = Union[Path, str]

def tenhou_to_mjai(
    filename: PathOrStr, *, mjai_out: Union[PathOrStr, None] = None
) -> List[str]: ...

class TenhouLogParsingError(ValueError): ...
class TenhouToMjaiError(ValueError): ...
class JsonSerializationError(ValueError): ...
class JsonParsingError(ValueError): ...
