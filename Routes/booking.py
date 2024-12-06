from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from models import Booking, Train

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/book', methods=['POST'])
@jwt_required()
def book_seat():
    user_id = get_jwt_identity()
    data = request.json
    train = Train.query.filter_by(id=data['train_id']).first()

    if train and train.available_seats > 0:
        train.available_seats -= 1
        booking = Booking(user_id=user_id, train_id=data['train_id'], status="Confirmed")
        db.session.add(booking)
        db.session.commit()
        return jsonify({"message": "Seat booked successfully!"})

    return jsonify({"error": "No seats available"}), 400

@booking_bp.route('/details', methods=['GET'])
@jwt_required()
def get_booking_details():
    user_id = get_jwt_identity()
    bookings = Booking.query.filter_by(user_id=user_id).all()
    return jsonify([{
        "id": booking.id,
        "train_id": booking.train_id,
        "status": booking.status
    } for booking in bookings])