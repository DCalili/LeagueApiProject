from dataclasses import dataclass
from ChampionInfoDto import ChampionInfoDTO

@dataclass
class ChampionDTO:
    data: dict

    def add_champion(self,championInfo: ChampionInfoDTO):
        self.data[championInfo.key] = championInfo.name