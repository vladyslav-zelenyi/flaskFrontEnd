import flask

import routes

flask_application = flask.Flask(__name__, static_url_path='/static')
flask_application.secret_key = 'test_secret_key'
flask_application.register_blueprint(routes.main)

static = flask.Blueprint('static', __name__, static_folder='static')
flask_application.register_blueprint(static)


if __name__ == '__main__':
    flask_application.run()
