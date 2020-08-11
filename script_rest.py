from config_main import host, port, threaded, debug, message, scode
from flask import Flask, jsonify, make_response
from config_ssl import context

app = Flask('__name__')
host_config = {
    "host": host,
    "port": port,
    "threaded": threaded,
    "debug": debug,
    "ssl_context": context
}


@app.route('/')
def home():
    return make_response(jsonify(message), scode)


if __name__ == "__main__":
    app.run(**host_config)
