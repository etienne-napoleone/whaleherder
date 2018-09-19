from flask import Flask

__version__ = '0.0.1'


def create_app(test_config=None):
    """Create and configure an instance of whaleherder."""
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        if Flask.env == 'production':
            app.config.from_object('whaleherder.config.ProductionConfig')
        elif Flask.env == 'development':
            app.config.from_object('whaleherder.config.DevelopmentConfig')
    else:
        app.config.update(test_config)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app
