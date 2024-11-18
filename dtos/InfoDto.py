from dataclasses import dataclass
from typing import List
from dtos.ParticipantDto import ParticipantDTO

@dataclass
class InfoDTO:
    endOfGameResult: str
    gameCreation: int
    gameDuration: int
    gameId: int
    gameMode: str
    participants: List[ParticipantDTO]