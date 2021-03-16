import flask
import routes

app = flask.Flask(__name__, static_url_path='/static')
app.config["DEBUG"] = True

routes.route(app)

app.run()
