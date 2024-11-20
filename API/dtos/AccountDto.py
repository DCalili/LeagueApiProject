from dataclasses import dataclass

@dataclass
class AccountDTO:
    puuid: str
    gameName: str
    tagLine: str