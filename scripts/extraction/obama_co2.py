def main():
	info('Obama unknown laser analysis')
	
	gosub('obama:PrepareForCO2Analysis')
	
	if analysis_type=='blank':
		info('is blank. not heating')
	else:
		info('move to position {}'.format(position))
		#move_to_position(position)
		info('set heat to {}'.format(extract_value))
		moving_extract(extract_value, position)
	
		
	sleep(duration)
	if not analysis_type=='blank':
		end_extract()
	sleep(cleanup)