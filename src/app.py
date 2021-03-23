from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app, Gauge

# Create my app
app = Flask(__name__)

g = Gauge("my_test_metric", "Description of gauge")
g.set(4.2)  # Set to a given value

# Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})
