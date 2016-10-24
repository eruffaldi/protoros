# TODO: threading is as follows
# - main thread for user
# - rpc thread for management
# - one thread for all pub/sub OR one each
import client_pb2
import master_pb2
import common_pb2
import tinyrpc_proto

# as seen from Client, exposes the MasterService and ParamService
class MasterProxy(object):
	pass

# the real one, exposes the ClientService API
class Node(object):
	def __init__(self,name):
		# create the RPC with the Slave API
		self.masterproxy = None
		pass
	# local API functions
	# RPC API calls

currentnode = None

def init_node(name, args, anonymous=False):
	global currentnode
	pass

def spin():
	global currentnode
	pass

def _get_master():
	global currentnode
	return currentnode.masterproxy

def spinOnce():
	global currentnode
	pass

def get_param(name):
	global currentnode
	pass

def is_shutdown():
	global currentnode
	pass

def loginfo(name):
	global currentnode
	pass

class Time:
	@staticmethod
	def now():
		pass

def get_time():
	global currentnode
	pass

def sleep(duration):
	global currentnode
	pass

class Time:
	def __init__(self):
		pass
	@staticmethod
	def sleep(self):
		pass

class Duration:
	def __init__(self,secs,nsecs):
		pass

class Subscriber:
	def __init__(self,name,type,fx,*args):
		global currentnode
		pass

class Publisher:
	def __init__(self,name,type,queue):
		global currentnode
		pass
	def publish(self,value):
		pass
	def get_num_subscribers(self):
		pass