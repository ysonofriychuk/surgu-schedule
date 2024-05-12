import argparse
import logging
import ssl

from flask import Flask

from internal.api.routers.user_group import blueprint as blueprint_user
from internal.api.routers.schedule import blueprint as blueprint_schedule


app = Flask(__name__)

app.register_blueprint(blueprint_user)
app.register_blueprint(blueprint_schedule)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="SurSU Schedule"
    )

    parser.add_argument("--cert-file", help="SSL certificate file (for HTTPS)")
    parser.add_argument("--key-file", help="SSL key file (for HTTPS)")
    parser.add_argument(
        "--host", default="0.0.0.0", help="Host for HTTP server (default: 0.0.0.0)"
    )
    parser.add_argument(
        "--port", type=int, default=8080, help="Port for HTTP server (default: 8080)"
    )
    parser.add_argument("--verbose", "-v", action="count")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    if args.cert_file:
        ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        ssl_context.load_cert_chain(args.cert_file, args.key_file)
    else:
        ssl_context = None

    app.run(ssl_context=ssl_context, host=args.host, port=args.port)
