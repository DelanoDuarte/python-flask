from flask import Flask, jsonify
from modules.employee_module import employee_blueprint
from database.repository import init_database, db

def create_app():    
    app = Flask(__name__)
    app.config.from_object('config.Config')

    init_database(app)

    with app.app_context():
        db.create_all()
    
    app.register_blueprint(employee_blueprint, url_prefix='/employee')
    return app

app = create_app()

@app.route("/")
def index():
    return {"status":"App Running"}

@app.errorhandler(404)
def error_handler(ex):
    return jsonify(error=str(ex))
    

app.run()