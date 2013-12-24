'''
'''
def main():
	#this is a comment
	'''
		this is a multiline 
		comment aka docstring
	'''
    #dgfd
	#display information with info(msg)
	info('air measurement script')
	
	#set the spectrometer parameters
	#provide a value
	set_source_parameters(YSymmetry=10)
	
	#or leave blank and values are loaded from a config file (setupfiles/spectrometer/config.cfg)
	set_source_optics()
	
	#set the cdd operating voltage
	set_cdd_operating_voltage(100)
	
	#open a plot panel for this detectors
	activate_detectors('H1','AX','CDD')

	#set default regression
	regress('parabolic')

	#position mass spectrometer	
	position_magnet('Ar40', detector='H1')

	#gas is staged behind inlet
	#isolate sniffer volume
	close('S')
	sleep(1)
	
	#open to mass spec
	open('R')
	
	set_time_zero()
	#display pressure wave
	sniff(5)
	
	#define sniff/split threshold
	sniff_threshold=100
	
	#test condition
	#if get_intensity('H1')>sniff_threshold:
	if True:
		gosub('splits:jan_split', klass='ExtractionLinePyScript')
	
	#gas has been split down and staged behind the inlet	
	#post equilibration script triggered after eqtime elapsed
	#equilibrate is non blocking	
	#so use either a sniff of sleep as a placeholder until eq finished
	equilibrate(eqtime=20, inlet='R', outlet='V')
	
	#equilibrate returns immediately after the inlet opens
	set_time_zero()
	
	sniff(20)
               
	#multicollect on active detectors
	multicollect(ncounts=10, integration_time=1)
	
	baselines(ncounts=5,mass=40.5)
	peak_center(detector='H1',isotope='Ar40')
	info('finished measure script')
	
#========================EOF==============================================================
	#peak_hop(detector='CDD', isotopes=['Ar40','Ar39','Ar36'], cycles=2, integrations=3)	
	#baselines(counts=50,mass=0.5, detector='CDD')s