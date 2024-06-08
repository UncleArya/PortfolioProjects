from src.forms import AddGameForm, EditGameForm
from src.database import FavVideoGames, db
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5


# Creating Flask app
app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{
    app.root_path}/video-games.db"
db.init_app(app)


# WTForms secret key
app.secret_key = "12345"


# Home Page
@app.route("/")
def home():
    with app.app_context():
        data = (
            db.session.execute(
                db.select(FavVideoGames).order_by(FavVideoGames.rating.desc())
            )
            .scalars()
            .all()
        )
    return render_template("home.html", video_games=data)


# Add new game functionality
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_game = FavVideoGames(
                title=request.form["title"],
                year=request.form["year"],
                developer=request.form["developer"],
                genre=request.form["genre"],
                description=request.form["description"],
                rating=request.form["rating"],
                review=request.form["review"],
                cover_art=request.form["cover_art"],
            )
            db.session.add(new_game)
            db.session.commit()
        return redirect(url_for("home"))
    new_form = AddGameForm()
    return render_template("add.html", form=new_form)


# Edit functionality
@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        game_id = request.form["game_id"]
        current_game = db.get_or_404(FavVideoGames, game_id)
        if request.form["title"]:
            current_game.title = request.form["title"]
        if request.form["year"]:
            current_game.year = request.form["year"]
        if request.form["developer"]:
            current_game.developer = request.form["developer"]
        if request.form["genre"]:
            current_game.genre = request.form["genre"]
        if request.form["description"]:
            current_game.description = request.form["description"]
        if request.form["rating"]:
            current_game.rating = request.form["rating"]
        if request.form["review"]:
            current_game.review = request.form["review"]
        if request.form["cover_art"]:
            current_game.cover_art = request.form["cover_art"]
        db.session.commit()
        return redirect(url_for("home"))
    else:
        edit_form = EditGameForm()
        game_id = request.args.get("id")
        current_game = db.get_or_404(FavVideoGames, game_id)
        return render_template("edit.html", form=edit_form, game=current_game)


# Delete functionality
@app.route("/delete", methods=["GET", "POST"])
def delete():
    game_id = request.args.get("id")
    current_game = db.get_or_404(FavVideoGames, game_id)
    db.session.delete(current_game)
    db.session.commit()
    return redirect(url_for("home"))


# Flask Debugging
if __name__ == "__main__":
    app.run(debug=True)
