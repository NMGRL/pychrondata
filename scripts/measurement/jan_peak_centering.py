#!Measurement
'''
'''

#===============================================================================
# parameter definitions
#===============================================================================

#===============================================================================
# 
#===============================================================================


def main():
    #this is a comment
    '''
        this is a multiline 
        comment aka docstring
    '''
    #display information with info(msg)
    info('unknown measurement script')
    
    peak_center(isotope='Ar40',detector='H1')
    sleep(3)
    position_magnet('Ar40', detector='L1')
    sleep(3)
    peak_center(isotope='Ar40', detector='L1', save=False)
    info('finished measure script')
    
#========================EOF==============================================================
    #peak_hop(detector='CDD', isotopes=['Ar40','Ar39','Ar36'], cycles=2, integrations=3)    
    #baselines(counts=50,mass=0.5, detector='CDD')s
    
#isolate sniffer volume
    # close('S')
#     sleep(1)
#     
#     #open to mass spec
#     open('R')
#     
#     set_time_zero()
#     #display pressure wave
#     sniff(5)
#     
#     #define sniff/split threshold
#     sniff_threshold=100
#     
#     #test condition
#     #if get_intensity('H1')>sniff_threshold:
#     if True:
#         gosub('splits:jan_split', klass='ExtractionLinePyScript')
#     