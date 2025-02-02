from dotenv import load_dotnev
import flask
from utils.log import setup_logger

logger = setup_logger(__name__)

# Set environment variables.


# Initialize Flask application and disable debug mode for production
app = flask.Flask(__name__)
app.config['DEBUG'] = False
