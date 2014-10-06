'''
sensitivity_multiplier: 0.5
modifier: 1
'''

APIS_ID=1
def main():
    info('Jan Apis {} Pipette'.format(APIS_ID))
    gosub('apis:PrepareForApis')
    if analysis_type=='blank':
        gosub('apis:LoadApisShot', argv=('Air{}'.format(APIS_ID),))
    else:
        gosub('apis:LoadApisShot', argv=('Blank{}'.format(APIS_ID),))

    #ready for equilibration