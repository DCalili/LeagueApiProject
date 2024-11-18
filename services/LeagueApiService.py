from flask import Flask, jsonify, request
import requests
from config import API_KEY
from dtos.AccountDto import AccountDTO
from dtos.ChampionMasteryDto import ChampionMasteryDTO

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


