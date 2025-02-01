from flask import Flask
from config import Config
from flask_jwt_extended import JWTManager
from app.routes import student_routes

app = Flask(__name__)
app.config.from_object(Config)

jwt = JWTManager(app)

# Register Blueprints
app.register_blueprint(student_routes)

if __name__ == "__main__":
    app.run(debug=True)
