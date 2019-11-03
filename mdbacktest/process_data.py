class ProcessData:

    def __init__(self, list_of_securities):
        '''Tries to load download CSVs of all the tickers that can be
        traded. First should check if the CSVs already exist

        arguments:
        self :
        list_of_securities (list): list of the tickres that are able to
                                  be traded

        returns:
        None (saves CSVs)
        '''
