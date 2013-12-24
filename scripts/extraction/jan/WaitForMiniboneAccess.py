def main():
    info('Waiting for minibone access')
    acquire('JanMiniboneFlag')
    wait('MinibonePumpTimeFlag', 0)
    
    
    