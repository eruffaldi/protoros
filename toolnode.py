import common,sys

if __name__ == '__main__':
	common.init_node("tmp",anonymous=True)

	print "listing all topics"
	mp = common._get_master()
	for p in mp.getState().node:
		print p