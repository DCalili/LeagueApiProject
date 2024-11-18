from flask import Flask, request, jsonify
from services.LeagueApiService import LeagueApiService


app = Flask(__name__)

@app.route('/')
def home():
    return "LeagueApiProject"

@app.route('/summoner', methods=['GET'])
def GetSummonerByGameNameAndTag():
    name = request.args.get('name')
    tag = request.args.get('tag')

    if not name or not tag:
        return jsonify({"erro": "name and tag are needed"}), 400

    dados_summoner = LeagueApiService.GetSummonerByGameNameAndTag(name, tag)

    return jsonify(dados_summoner)


@app.route('/summoner/mastery', methods=['GET'])
def GetChampionMasteryByPuuId():
    puuid = request.args.get('puuid')

    if not puuid:
        return jsonify({"error": "puuid is needed"}), 400

    data_mastery = LeagueApiService.GetChampionMasteryByPuuId(puuid)

    return jsonify(data_mastery)

@app.route('/summoner/champion', methods=['GET'])
def GetChampionNameByChampionId():
    championId = request.args.get('championId')

    if not championId:
        return jsonify({"error": "championId is needed"}), 400
    
    data_champion = LeagueApiService.GetChampionNameByChampionId(championId)

    return jsonify(data_champion)

@app.route('/summoner/matches', methods=['GET'])
def GetMatchesByPuuId():
    puuid = request.args.get('puuid')

    if not puuid:
        return jsonify({"error": "puuid is needed"}), 400

    matchesId = LeagueApiService.GetMatchesByPuuId(puuid)

    return jsonify(matchesId)

@app.route('/summoner/matches/match', methods=['GET'])
def GetMatchByMatchId():
    matchId = request.args.get('matchId')

    if not matchId:
        return jsonify({"error": "matchId is needed"}), 400

    matchData = LeagueApiService.GetMatchByMatchId(matchId)

    return jsonify(matchData)

if __name__ == '__main__':
    app.run(debug=True)

