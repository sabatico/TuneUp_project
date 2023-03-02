import os as os
from flask import Flask

from routes import pages

def create_app():
    app= Flask(__name__)
    port = os.environ.get("PORT", 5000)
    host = os.environ.get("HOST", "127.0.0.1")
    
    app.run(port=port, host=host)
    app.register_blueprint(pages)
    
    return app