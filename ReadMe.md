# Password Manager with MongoDB Integration

A simple yet secure password manager GUI application built with Python's Tkinter for the frontend and MongoDB for the backend. It allows you to generate, store, and search for passwords, ensuring your credentials are always within reach.

---

## Features

- 🔐 Password generation (secure mix of letters, numbers, and symbols)
- 💾 Save passwords with website & email/user
- 🔍 Search passwords by website
- 📋 Copy passwords to clipboard automatically
- 🗃️ MongoDB integration for persistent storage

---

## Tech Stack

- Python 3.10+
- Tkinter
- MongoDB (local instance)
- Pyperclip
- Pymongo

---

## Installation & Setup

### 1. Clone the Repository
```bash
https://github.com/yourusername/password-manager.git
cd password-manager
```

### 2. Install Dependencies
```bash
pip install pymongo pyperclip pandas
```

### 3. Setup MongoDB
Ensure you have a local MongoDB instance running.

Default connection:
```bash
mongodb://localhost:27017/
```

Database: `Password_unite`

Collection: `password`

You can adjust this inside the script if needed:
```python
Client=MongoClient("mongodb://localhost:27017/")
```

### 4. Run the Application
```bash
python password_manager.py
```

---

## Usage

- Enter the website name and associated email/user
- Generate a strong password using the **Generate Password** button
- Click **ADD** to save it into the MongoDB database
- Use **Search** to retrieve existing password data

---

## File Structure
```
password-manager/
│
├── logo.png              # Logo for GUI window
├── password_manager.py   # Main Python script
├── README.md             # Project documentation
```

---

## TODO / Improvements

- [ ] Add encryption for stored passwords
- [ ] Improve UI styling
- [ ] Add password strength indicator
- [ ] Add cloud-based MongoDB support (Atlas)

---

## Screenshots
![Screenshot 2025-04-09 191652](https://github.com/user-attachments/assets/d8ac541a-fb58-4d1f-b6ef-793ff3db86e8)
