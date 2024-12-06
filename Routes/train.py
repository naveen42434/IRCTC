from flask import Blueprint, request, jsonify
from app import db
from models import Train

train_bp = Blueprint('train', __name__)
ADMIN_API_KEY = "AOFrXVtgjyaNzjEZELxtFrlbNkJUUpKt6aADsNGJk20"

@train_bp.route('/add', methods=['POST'])
def add_train():
    if request.headers.get('Api-Key') != ADMIN_API_KEY:
        return jsonify({"error": "Unauthorized"}), 403
    data = request.json
    new_train = Train(
        name=data['name'],
        source=data['source'],
        destination=data['destination'],
        total_seats=data['total_seats'],
        available_seats=data['total_seats']
    )
    db.session.add(new_train)
    db.session.commit()
    return jsonify({"message": "Train added successfully!"})

@train_bp.route('/get', methods=['GET'])
def get_trains():
    source = request.args.get('source')
    destination = request.args.get('destination')
    trains = Train.query.filter_by(source=source, destination=destination).all()
    return jsonify([{
        "id": train.id,
        "name": train.name,
        "available_seats": train.available_seats
    } for train in trains])