#Snap! extension base by Technoboy10
import SimpleHTTPServer
class CORSHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def send_head(self):
	path = self.path
	print path
	ospath = os.path.abspath('')
	if 'say' in path:
		regex = re.compile("\/say(.*)")
		m = regex.match(urllib2.unquote(path))
		engine.say(m.group(1))
	engine.runAndWait()
if __name__ == "__main__":
    import os
    import re
    import SocketServer
    import pyttsx
    import urllib2
    PORT = 59591 #T+T+S twice
    engine = pyttsx.init()
    Handler = CORSHTTPRequestHandler
    #Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print "serving at port", PORT
    print "Go ahead and launch Snap!."
    httpd.serve_forever()

