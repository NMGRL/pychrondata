'''
equilibration_time: 15
inlet_valve: H
outlet_valve: V
'''

def func():
	info('action performed')
	
def main():
	info('air measurement script')
	
	set_time_zero()
	
	set_source_parameters(YSymmetry=10)
	set_source_optics()
	set_cdd_operating_voltage(100)
	
	activate_detectors('H1','AX','CDD')
	regress('parabolic')
	
	position_magnet('Ar40', detector='H1')

	#sniff the gas during equilibration
	sniff(10)
	sleep(1)
		
	#set conditions
	'''
		order added defines condition precedence.
		conditions after the first true condition are NOT evaluated
		
	'''
	add_termination('age','>',10.6, start_count=20, frequency=10)
	add_truncation('age','>',10.6, start_count=20, frequency=10)
	add_action('age','>',10.6, start_count=20, frequency=10, 
				action='sleep(10)')
	add_action('age','>',10.6, start_count=20, frequency=10,
			  	action=func)
			  	
	multicollect(ncounts=150, integration_time=1)
	
	
	
	#peak_hop(detector='CDD', isotopes=['Ar40','Ar39','Ar36'], cycles=2, integrations=3)	
	
	#baselines(counts=50,mass=0.5, detector='CDD')
	if truncated:
		baselines(ncounts=20,mass=39.5)
	else:
		baselines(ncounts=50,mass=39.5)
		peak_center(detector='H1',isotope='Ar40')
	info('finished measure script')