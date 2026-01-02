from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):        
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random", methods=['GET'])
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    serialized_obj = jsonify(random_cafe.to_dict())

    return serialized_obj

@app.route("/all", methods=['GET'])
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes_objs = result.scalars().all()
    all_cafes = []
    for cafe_obj in all_cafes_objs:
        all_cafes.append(cafe_obj.to_dict())
    
    return all_cafes

@app.route("/search", methods=['GET'])
def get_cafes_by_location():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_cafes_objs = result.scalars().all()

    if len(all_cafes_objs) > 0:
        all_cafes = []
        for cafe_obj in all_cafes_objs:
            all_cafes.append(cafe_obj.to_dict())
        
        return all_cafes
    else:
        return {"error": {"Not found": "Sorry, we don't have a location in that lcoation."}}

@app.route("/add", methods=['POST'])
def add_cafe():
    try:
        new_cafe = Cafe(
            name = request.args.get("name"),
            map_url = request.args.get("map_url"),
            img_url = request.args.get("img_url"),
            location = request.args.get("location"),
            seats = request.args.get("seats"),
            has_toilet = bool(request.args.get("has_toilet")),
            has_wifi = bool(request.args.get("has_wifi")),
            has_sockets = bool(request.args.get("has_sockets")),
            can_take_calls = bool(request.args.get("can_take_calls")),
            coffee_price = request.args.get("coffee_price")
        )

        db.session.add(new_cafe)
        db.session.commit()
        return {"success": {"Added": new_cafe.to_dict()}}
    except Exception as e:
        return {"error": {"Someting went wrong": {e}}}

@app.route("/update-price/<cafe_id>", methods=['PATCH'])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    try:
        cafe = db.session.get(Cafe, cafe_id)
    except AttributeError:
        return jsonify(error={"Not Found": f"Sorry a cafe with id {cafe_id} was not found in the database."}), 404
    else:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}), 200

@app.route("/report-closed/<cafe_id>", methods=['DELETE'])
def remove_cafe(cafe_id):
    api_key = request.args.get("api_key")
    if api_key != "TopSecretAPIKey":
        return jsonify(error={"Action not permitted": f"Sorry, that action in not allowed. Check you api key and try again."}), 403

    try:
        cafe = db.session.get(Cafe, cafe_id)
    except AttributeError:
        return jsonify(error={"Not Found": f"Sorry a cafe with id {cafe_id} was not found in the database."}), 404
    else:
        db.session.delete(cafe)
        db.session.commit()
        return jsonify(response={"success": f"Successfully deleted cafe."}), 200


if __name__ == '__main__':
    app.run(debug=True)
