'''
equilibration_time: 7
inlet_valve: H
outlet_valve: V
'''
	
def main():
	info('air measurement script')
	
	set_time_zero()
	
	set_source_parameters()
	set_source_optics()
	set_cdd_operating_voltage()
	
	activate_detectors('H1','AX','CDD')
	regress('parabolic')
	
	position_magnet('Ar40', detector='H1')

	#sniff the gas during equilibration
	sniff(2)
	sleep(1)
	
	multicollect(ncounts=150, integration_time=1)
	#peak_hop(detector='CDD', isotopes=['Ar40','Ar39','Ar36'], cycles=2, integrations=3)	
	
	#baselines(counts=50,mass=0.5, detector='CDD')

	baselines(ncounts=50,mass=40.5)
	peak_center(detector='H1',isotope='Ar40')
	info('finished measure script')