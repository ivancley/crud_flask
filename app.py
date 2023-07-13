from flask import Flask, redirect, url_for, request, render_template
from models import db, Veiaco

app = Flask(
    __name__, 
    static_folder="public", 
    template_folder="templates")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"


@app.route("/")
def index():
    veiacos = Veiaco.query.all()
    return render_template("index.html", veiacos=veiacos)


@app.route("/novo", methods=[ "GET", "POST"])
def novo():
    if request.method == "POST":
        veiaco = Veiaco(request.form["nome"],request.form["valor"],)
        db.session.add(veiaco)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add.html", )


@app.route("/edit/<int:id>", methods=[ "GET", "POST"])
def edit(id):
    veiaco = Veiaco.query.get(id)
    if request.method == "POST":
        veiaco.nome = request.form["nome"]
        veiaco.valor = request.form["valor"]
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit.html", veiaco=veiaco )  


@app.route("/delete/<int:id>")
def delete(id):
    veiaco = Veiaco.query.get(id)
    db.session.delete(veiaco)
    db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    db.init_app(app=app)
    with app.app_context(): 
        db.create_all()
    app.run(debug=True)
