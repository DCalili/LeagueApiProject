from flask import Flask, request, jsonify
from services.LeagueApiService import LeagueApiService
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

CORS(app, resources={
    r"/api/*": {
        "origins": ["http://localhost:5000"],
        "methods": ["GET", "POST"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})


@app.route('/')
def home():
    return "LeagueApiProject"

@app.route('/api/summoner', methods=['GET'])
def GetSummonerByGameNameAndTag():
    name = request.args.get('name')
    tag = request.args.get('tag')

    if not name or not tag:
        return jsonify({"erro": "name and tag are needed"}), 400

    dados_summoner = LeagueApiService.GetSummonerByGameNameAndTag(name, tag)

    return jsonify(dados_summoner)


@app.route('/api/summoner/mastery', methods=['GET'])
def GetChampionMasteryByPuuId():
    puuid = request.args.get('puuid')

    if not puuid:
        return jsonify({"error": "puuid is needed"}), 400

    data_mastery = LeagueApiService.GetChampionMasteryByPuuId(puuid)

    return jsonify(data_mastery)

@app.route('/api/summoner/champion', methods=['GET'])
def GetChampionNameByChampionId():
    championId = request.args.get('championId')

    if not championId:
        return jsonify({"error": "championId is needed"}), 400
    
    data_champion = LeagueApiService.GetChampionNameByChampionId(championId)

    return jsonify(data_champion)

@app.route('/api/summoner/matches', methods=['GET'])
def GetMatchesByPuuId():
    puuid = request.args.get('puuid')

    if not puuid:
        return jsonify({"error": "puuid is needed"}), 400

    matchesId = LeagueApiService.GetMatchesByPuuId(puuid)

    return jsonify(matchesId)

@app.route('/api/summoner/matches/match', methods=['GET'])
def GetMatchByMatchId():
    matchId = request.args.get('matchId')

    if not matchId:
        return jsonify({"error": "matchId is needed"}), 400

    matchData = LeagueApiService.GetMatchByMatchId(matchId)

    return jsonify(matchData)

if __name__ == '__main__':
    app.run(debug=True)

