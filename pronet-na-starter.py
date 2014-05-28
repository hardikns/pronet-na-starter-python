#!/usr/bin/env python
from PronetNetworkApp.na import Application
import argparse 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test RestServer config parameters')
    parser.add_argument('--host', dest='host', type=str,
                help="Host IP on which the server would listen. (default 127.0.0.1)")
    parser.add_argument('--port', dest='port', type=int,
                help="Port on which the server would listen. (default 5000)")

    args = parser.parse_args()
    host = args.host or '127.0.0.1'
    port = args.port or  5000
    Application.main(host, port)
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
