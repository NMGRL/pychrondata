
def main():
	info('======== starting Bone blank===========')
	close('H')
	close('B')
	close('N')
	close('D')
	close('E')
	close('C')
	
	open('H')
	if is_open('H'):
		info('h is open')
	else:
		info('h is closed')
	move_to_position(10)
	heat_sample(100,1)
	
