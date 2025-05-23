import json
from flask import Flask, request, Response

app = Flask(__name__)
@app.route('/summa/<luku1>/<luku2>')
def summa(luku1, luku2):
    try:
        luku1 = float(luku1)
        luku2 = float(luku2)
        summa = float(luku1) + float(luku2)

        tilakoodi = 200
        vastaus = {
            'status' : tilakoodi,
            'luku1': luku1,
            'luku2': luku2,
            'summa': summa
        }
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen yhteenlaskettava"
        }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype='application/json')

@app.errorhandler(404)
def page_not_found(virhe):
    tilakoodi = 404
    vastaus = {
        "status" : tilakoodi,
        "teksti" : "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
