from flask import Flask, redirect, url_for, request, render_template, Response
from models import db, Veiaco
import json 

app = Flask(
    __name__, 
    static_folder="public", 
    template_folder="templates")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"


@app.route("/")
def index():
    veiacos = Veiaco.query.all()
    result = [ v.to_dict() for v in veiacos ]
    return Response(response=json.dumps(result), status=200, content_type="application/json")


@app.route("/novo", methods=[ "POST"])
def novo():
    veiaco = Veiaco(request.form["nome"],request.form["valor"],)
    db.session.add(veiaco)
    db.session.commit()
    return app.response_class(
        response=json.dumps({'status': 'success', "data": veiaco.to_dict()}), 
        status=200, content_type="application/json")


@app.route("/edit/<int:id>", methods=[ "PUT", "POST"])
def edit(id):
    veiaco = Veiaco.query.get(id)
    veiaco.nome = request.form["nome"]
    veiaco.valor = request.form["valor"]
    db.session.commit()
    return Response(response=json.dumps(veiaco.to_dict()), status=201, content_type="application/json") 


@app.route("/delete/<int:id>", methods=[ "DELETE",])
def delete(id):
    veiaco = Veiaco.query.get(id)
    db.session.delete(veiaco)
    db.session.commit()
    return Response(response=json.dumps(veiaco.to_dict()), status=201, content_type="application/json") 


if __name__ == "__main__":
    db.init_app(app=app)
    with app.app_context(): 
        db.create_all()
    app.run(debug=True)
