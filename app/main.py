from flask import Flask
from flask import abort
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import herder

app = Flask('whaleherder')
limiter = Limiter(app,
                  key_func=get_remote_address,
                  default_limits=["1 per minute", "1 per second"])
herder.init()


@app.route("/ping", methods=['GET'])
@limiter.limit("1 per second")
def hello():
    if herder.ping():
        return "Connected to Docker"
    else:
        abort(500)


@app.route("/services/<service>", methods=['POST'])
def receive_trigger(service):
    services = herder.get_services()
    if services and service in services.keys():
        if herder.reload(service):
            return f"Reloading {service}"
        else:
            abort(500)
    elif services and service not in services.keys():
        abort(404)
    else:
        abort(500)


if __name__ == "__main__":
    app.run(host='localhost', debug=True, port=8080)
