'''
	equilibration_time: 15
	inlet_valve: H
	outlet_valve: V
'''

def set_source_params():
	set_ysymmetry(100)
	set_zsymmetry(100)
	set_zfocus(100)
	set_extraction_lens(100)
	
def set_deflections():
	set_deflection('H2',200)
	set_deflection('H1',0)
	set_deflection('AX',100)
	set_deflection('L1',215)
	set_deflection('L2',470)
	set_deflection('CDD',125)
	
def main():
	info('generic measurement script')
	
	set_time_zero()
	
	#set_source_params()
	set_deflections()

	activate_detectors('H1','AX','CDD')
	
	position('Ar40', detector='H1')

	#h1s=detector['H1'].signal
	#if h1s <10:
#		info('H1 signal is to low {}'.format(h1s))

	#sniff the gas during equilibration
	sniff(20)
	sleep(1)
	
	collect(ncounts=400, integration_time=1)
	#peak_hop(detector='CDD', isotopes=['Ar40','Ar39','Ar36'], cycles=5)	
	
	regress('parabolic')
	
	#baselines(ncounts=60,mass=0.5, detector='CDD')
	baselines(ncounts=60,mass=40.5)
	peak_center(detector='H1',isotope='Ar40')

	info('finished measure script')