from socket import *
from select import *

host = gethostname()
ipaddr = gethostbyname(host)
sock = socket(AF_INET, SOCK_STREAM)
sock.bind("", 61257)
sock.listen(1)

lConnections = []

def Log(lTree):
	# Check for new connections.
	lConnects, lWrites, lExceptions = select([sock.fileno()], [], [], 0)
	if lConnects:
		try:
			conn = sock.accept()[0]
			lConnections.append(conn)
		except:
			pass

	# Send this tree to every open connection.
	if len(lConnections):
		# Encode the tree into a string..
		import cPickle
		sTree = cPickle.dumps(lTree)

		for conn in lConnections:
			try:
				conn.send(("%d*" % len(sTree)) + sTree)
			except:
				lConnections.remove(conn)
				conn.shutdown(2)

if __name__ == "__main__":
    print "Outputting test log.."
    import time
    while(1):
        Log([(0, "Test!"), (1, "Inner test!")])
        time.sleep(1)
