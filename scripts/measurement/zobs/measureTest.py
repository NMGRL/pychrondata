'''
equilibration_time: 1
'''
def set_source_params():
	set_ysymmetry(100)
	set_zsymmetry(100)
	set_zfocus(100)
	set_extraction_lens(100)
	
def set_deflections():
	set_deflection('H2',100)
	set_deflection('H1',100)
	set_deflection('AX',100)
	set_deflection('L1',100)
	set_deflection('L2',100)
	set_deflection('CDD',100)
	
def main():
	set_time_zero()
	
	info('starting measure script')
	set_source_params()
	set_deflections()
	
	position('Ar40', detector='H1')
	activate_detectors('H1','AX','CDD')
	h1s=detector['H1'].signal
	if h1s <10:
		info('H1 signal is to low {}'.format(h1s))

	#sniff the gas during equilibration
	sniff(100)
	sleep(1)
	
	collect(ncounts=200, integration_time=1)
	regress('cubic')
	
	peak_center(detector='H1',isotope='Ar40')
	#sleep(1)
	#baselines(100,detector='CDD')
	#baselines(100)
	info('finished measure script')