# local dev server for the site: same as `python3 -m http.server` but tells the browser never to cache,
# so a refresh can never mix a new CSS file with an old JS file
import http.server, functools, sys
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store'); super().end_headers()
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8123
http.server.ThreadingHTTPServer(('', port), functools.partial(H, directory='site')).serve_forever()
