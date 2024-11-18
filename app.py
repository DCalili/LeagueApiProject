from flask import Flask, request, jsonify
from services.LeagueApiService import LeagueApiService


app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, Flask!"

@app.route('/summoner', methods=['GET'])
def GetSummonerByGameNameAndTag():
    # Captura os parâmetros da URL
    name = request.args.get('name')
    tag = request.args.get('tag')

    # Verifica se os parâmetros foram passados corretamente
    if not name or not tag:
        return jsonify({"erro": "Os parâmetros 'name' e 'tag' são obrigatórios"}), 400

    # Chama o serviço e obtém os dados
    dados_summoner = LeagueApiService.GetSummonerByGameNameAndTag(name, tag)

    return jsonify(dados_summoner)


@app.route('/summoner/mastery', methods=['GET'])
def GetChampionMasteryByPuuId():
    puuid = request.args.get('puuid')

    if not puuid:
        return jsonify({"error": "puuid is needed"}), 400

    data_mastery = LeagueApiService.GetChampionMasteryByPuuId(puuid)

    return jsonify(data_mastery)

if __name__ == '__main__':
    app.run(debug=True)

