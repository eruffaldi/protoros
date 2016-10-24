# TODO: threading is as follows
# - rpc thread for management
import common
import sys
import zmq
from tinyrpc.dispatch import public
from tinyrpc.transports.zmq import ZmqServerTransport
from tinyrpc.server import RPCServer

class Master(object):
	def __init__(self):
		# create the RPC with the Master API
		pass
	@public('pippo')
	def pippo(self):
		pass

# create the RPC with MULTIPLE services ALL OF master.proto
def main():
	# mark for master, the rest is in common?
	m = Master()
	ctx = zmq.Context()
	dispatcher = RPCDispatcher()
	dispatcher.register_instance(m, '')
	transport = ZmqServerTransport.create(ctx, 'tcp://127.0.0.1:5001')
	rpc_server = RPCServer(
	    transport,
    	common.ProtoProtocol(),
    	dispatcher
	)
	rpc_server.serve_forever()

if __name__ == '__main__':
	main()