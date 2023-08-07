from app.controllers.auth_controller import app as auth_routes
from app.controllers.user_controller import app as user_routes

def register_routes(app):
    app.register_blueprint(auth_routes, url_prefix='/api/auth')
    app.register_blueprint(user_routes, url_prefix='/api')
