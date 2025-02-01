# Student Management System

This is a **Flask-based Student Management System** that uses **MongoDB Cloud** for data storage. The project follows the **SOLID principles** and implements a structured architecture with models, services, repositories, and routes.

## Features

- **Student CRUD Operations** (Create, Read, Update, Delete)
- **MongoDB Cloud Integration**
- **Flask REST API**
- **SOLID Principles Applied**
- **JWT Authentication (Optional, can be added)**

## Project Structure

```
/student-management
│── /app
│   ├── /models         # Data Models (Single Responsibility)
│   ├── /services       # Business Logic (Service Layer)
│   ├── /repositories   # Data Access Layer (Repository Pattern)
│   ├── /routes         # Flask Routes (Interface Segregation)
│   ├── /utils          # Helper Functions
│── config.py           # Configuration File
│── app.py              # Main Entry Point
│── requirements.txt    # Dependencies
│── README.md           # Documentation
```

## Installation

### 1. Clone the Repository

```sh
git clone https://github.com/your-repo/student-management.git
cd student-management
```

### 2. Create and Activate a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a **.env** file in the project root and add:

```
MONGO_URI=mongodb+srv://your_username:your_password@cluster.mongodb.net/student_db
JWT_SECRET_KEY=supersecretkey
```

### 5. Run the Application

```sh
python app.py
```

## API Endpoints

### **1. Add Student**

```sh
POST /students
```

**Body:**

```json
{
  "name": "John Doe",
  "age": 20,
  "email": "john@example.com"
}
```

### **2. Get All Students**

```sh
GET /students
```

### **3. Get Student by Email**

```sh
GET /students/<email>
```

### **4. Delete Student**

```sh
DELETE /students/<email>
```

## License

This project is open-source and available under the **MIT License**.

## Author

Your Name - https\://github.com/Najeeb1110/

