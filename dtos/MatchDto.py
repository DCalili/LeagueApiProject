from dataclasses import dataclass
from dtos.MetadataDto import MetadataDTO
from dtos.InfoDto import InfoDTO

@dataclass
class MatchDTO:
    metadata: MetadataDTO
    info: InfoDTO