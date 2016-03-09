def main():
    info('Furnace extraction script')
    gosub('jan:PrepareForFurnaceAnalysis')

    if analysis_type=='blank':
        info('is blank. not heating')
    else:
        info('move to position {}'.format(position))
        for p in position:
            move_to_position(p)
            dump_sample()

        info('prepare for heating')

    gosub('jan:PrepareForFurnaceHeating')

    start_response_recorder()
    info('set furnace to {}'.format(extract_value))
    extract(extract_value)
    info('sleep for extraction duration {}s'.format(duration))
    sleep(duration)
    extract(0)

    info('sleep for cleanup {}s'.format(cleanup))
    sleep(cleanup)
    stop_response_recorder()
