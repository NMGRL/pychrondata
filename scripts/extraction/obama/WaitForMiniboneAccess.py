def main():
	info('Waiting for minibone access')
	acquire('ObamaMiniboneFlag')
	wait('MinibonePumpTimeFlag', 0)
	
	
	