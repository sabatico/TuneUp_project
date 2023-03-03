import os as os
from flask import Flask


from routes import pages

def create_app():
    app= Flask(__name__, static_folder="../static", template_folder="../templates")
    
    port = os.environ.get("PORT", 5000)
    host = os.environ.get("HOST", "127.0.0.1")
    
    #check if its a test run, and return app without running it, for the test_client to run instead
    try:
        if os.environ['PYTEST_RUNNING'] == 'true':
            app.register_blueprint(pages)
            return app
    except:
        pass
    
    app.register_blueprint(pages)
    app.run(port=port, host=host)
    
    
    return app

