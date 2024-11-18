from dataclasses import dataclass

@dataclass
class ParticipantDTO:
    puuid: int
    championId: int
    championName: str
    kills: int
    assists: int
    deaths: int
    lane: str
    item0: int
    item1: int
    item2: int
    item3: int
    item4: int
    item5: int
    item6: int
    nexusLost: int
    riotIdGameName: str
    riotIdTagline: str
