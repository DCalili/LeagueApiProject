from dataclasses import dataclass
from typing import List

@dataclass
class MetadataDTO:
    dataVersion: str
    matchId: str
    participants: List[str]