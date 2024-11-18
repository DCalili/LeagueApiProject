from flask import Flask, jsonify, request
import requests
from config import API_KEY
from dtos.AccountDto import AccountDTO
from dtos.ChampionMasteryDto import ChampionMasteryDTO
from dtos.ChampionInfoDto import ChampionInfoDTO
from dtos.MatchDto import MatchDTO
from dtos.MetadataDto import MetadataDTO
from dtos.InfoDto import InfoDTO
from dtos.ParticipantDto import ParticipantDTO

class LeagueApiService:
    
    @staticmethod
    def GetSummonerByGameNameAndTag(name: str, tag: str):
        url = "https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/"+name+"/"+tag
        headers = {
            "X-Riot-Token": API_KEY 
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            account_dto = AccountDTO(
                puuid=data['puuid'],
                gameName=data['gameName'],
                tagLine=data['tagLine']
                )
            return account_dto
        else:
            return {"error": "Could not get data", "status": response.status_code}

    @staticmethod
    def GetChampionMasteryByPuuId(puuid: str):
        url = "https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/"+puuid+"/top"
        headers = {
            "X-Riot-Token": API_KEY 
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()

            champion_mastery_dtos = []

            for item in data:
                champion_mastery_dto = ChampionMasteryDTO(
                    puuid=item['puuid'],
                    championId=item['championId'],
                    championLevel=item['championLevel'],
                    championPoints=item['championPoints']
                    )
                champion_mastery_dtos.append(champion_mastery_dto)
            return champion_mastery_dtos
        else:
            return {"error": "Could not get data", "status": response.status_code}


    @staticmethod
    def GetChampionNameByChampionId(championId: int):
        url = "https://ddragon.leagueoflegends.com/cdn/14.22.1/data/en_US/champion.json"
        response = requests.get(url)

        if response.status_code == 200:
            champions = response.json()

            for x_key, value in champions['data'].items():
                if value['key'] == str(championId):
                    champion_info_dto = ChampionInfoDTO(
                        name=value['id'],
                        key=value['key']
                    )
                    return champion_info_dto
            else:
                return None

    @staticmethod
    def GetMatchesByPuuId(puuid: str):
        url = "https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/"+puuid+"/ids"
        headers = {
            "X-Riot-Token": API_KEY 
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            matches = data
            return matches
        else:
            return {"error": "Could not get data", "status": response.status_code}

    
    @staticmethod
    def GetMatchByMatchId(matchId: str):
        url = "https://americas.api.riotgames.com/lol/match/v5/matches/"+matchId
        headers = {
            "X-Riot-Token": API_KEY
        }

        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            
            metadata = data['metadata']
            info = data['info']
            
            participant_dtos = []
            participant_puuid = []
            
            if 'info' in data and 'participants' in data['info']:
                participants = data['info']['participants']  # Lista de dicionários completos

                for participant in participants:
                    participant_dto = ParticipantDTO(
                        puuid=participant['puuid'],
                        championId=participant['championId'],
                        championName=participant['championName'],
                        kills=participant['kills'],
                        assists=participant['assists'],
                        deaths=participant['deaths'],
                        lane=participant['lane'],
                        item0=participant['item0'],
                        item1=participant['item1'],
                        item2=participant['item2'],
                        item3=participant['item3'],
                        item4=participant['item4'],
                        item5=participant['item5'],
                        item6=participant['item6'],
                        nexusLost=participant['nexusLost'],
                        riotIdGameName=participant['riotIdGameName'],
                        riotIdTagline=participant['riotIdTagline']
                    )
                    participant_dtos.append(participant_dto)
                    participant_puuid.append(participant_dto.puuid)

            metadata_dto = MetadataDTO(
                dataVersion=metadata['dataVersion'],
                matchId=metadata['dataVersion'],
                participants=participant_puuid
            )

            info_dto = InfoDTO(
                endOfGameResult=info['endOfGameResult'],
                gameCreation=info['gameCreation'],
                gameDuration=info['gameDuration'],
                gameMode=info['gameMode'],
                gameId=info['gameId'],
                participants=participant_dtos
            )

            match_dto = MatchDTO(
                metadata=metadata_dto,
                info=info_dto
            )

            return match_dto



        
        else:
            return {"error": "Could not get Match data", "status": response.status_code}



