from dataclasses import dataclass

@dataclass
class ChampionMasteryDTO:
    puuid: str
    championId: int
    championLevel: int
    championPoints: int
