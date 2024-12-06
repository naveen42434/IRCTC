# IRCTC Railway Management System API

This is a Flask-based API for a railway management system that allows users to register, log in, view trains, book seats, and manage bookings. Admins can add trains to the system.

---

## Features

### User
- Register and log in.
- View available trains between source and destination.
- Book seats on a train.
- View booking details.

### Admin
- Add new trains to the system (protected by an API key).

---

## File Structure

- `app.py` - Application setup
- `models.py` - Database models
- `routes/`
  - `__init__.py` - Routes initialization
  - `auth.py` - User authentication routes
  - `train.py` - Train management routes
  - `booking.py` - Booking management routes
- `config.py` - App configuration
- `run.py` - Application entry point




---

## Technologies Used
- **Python**: Core language.
- **Flask**: Web framework.
- **Flask-JWT-Extended**: For JWT-based authentication.
- **SQLAlchemy**: ORM for database interactions.
- **MySQL**: Relational database.

---

## Setup Instructions

### Prerequisites
- Python 3.10 or later
- MySQL installed and running
- A virtual environment (optional but recommended)

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/irctc-api.git
cd irctc-api
```

### 2. Create a Virtual Environment and Activate It
```bash
python -m venv .venv
source .venv/bin/activate  # For Linux/Mac
.venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up the Database
```bash
CREATE DATABASE irctc;
```

### 5. Initialize the Database
```bash
python run.py
```

---

# API Endpoints

## 1. Authentication

### Register
**Endpoint:** `POST /auth/register`

**Request Body:**
```json
{
  "username": "user1",
  "password": "password123"
}
```

### Login
**Endpoint:** `POST /auth/login`

**Request Body:**
```json
{
  "username": "user1",
  "password": "password123"
}
```

**Response:**
```json
{
  "token": "<JWT_TOKEN>",
  "role": "user"
}
```

## 2. Trains

### Add Train (Admin Only)

**Endpoint:** `POST /train/add`

**Headers:**
```json
"Api-Key": <admin_api_key>
```

**Request Body:**
```json
{
  "name": "Train A",
  "source": "Station1",
  "destination": "Station2",
  "total_seats": 100
}
```

### Get Trains
**Endpoint:** `GET /train/get?source=Station1&destination=Station2`


## 3. Booking

### Book Seat

**Endpoint:** `POST /booking/book`

**Headers:**
```json
"Authorization": Bearer <JWT_TOKEN>
```

**Request Body:**
```json
{
  "train_id": 1
}
```

### Get Booking Details

**Endpoint:** `GET /booking/details`

**Headers:**
```json
"Authorization": Bearer <JWT_TOKEN>
```

---