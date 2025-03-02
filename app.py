import flask
import os

from dotenv import load_dotenv

from dynamodb_session_flask import DynamoDbSession

from utils.log import setup_logger

logger = setup_logger(__name__)


# Initialize Flask application and disable debug mode for production
app = flask.Flask(__name__)
app.config["DEBUG"] = False

# Constants - Log messages for HTTP responses
BAD_REQUEST = "Bad request (400)"
UNAUTHORIZED = "Unauthorized (401)"
RESOURCE_NOT_FOUND = "Resource not found (404)"
CONFLICT = "Conflict (409)"
HTTP_STATUS_DEFINITIONS_URL = "https://httpstatuses.io"


DOTENV_PATH = "./.env"
REQUIRED_BODY_FIELDS = ["functionality", "productCode", "version"]
RUNNING_IN_CONTAINER = os.getenv("RUNNING_IN_CONTAINER")

if RUNNING_IN_CONTAINER == "True":
    load_dotenv(dotenv_path=DOTENV_PATH, override=False)
else:
    load_dotenv(dotenv_path=DOTENV_PATH, override=True)


app.config.update(SESSION_DYNAMODB_IDLE_TIMEOUT=os.getenv('SESSION_TIMEOUT'))
app.session_interface = DynamoDbSession()
cache = RedisCache()


class ProcessRunner:
    """
    _summary_
    """
