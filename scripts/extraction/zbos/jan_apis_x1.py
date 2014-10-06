'''
sensitivity_multiplier: 0.5
modifier: 1
'''
def main():
    info('Jan Apis 1 Pipette)
    gosub('apis:PrepareForApis')
    if analysis_type=='blank':
        gosub('apis:LoadApisShot', argv=('Air1',))
    else:
        gosub('apis:LoadApisShot', argv=('Blank1',))

    #ready for equilibration