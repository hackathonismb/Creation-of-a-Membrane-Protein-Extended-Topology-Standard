
#########################
# API Error
#########################
class QueryRequestError(Exception):
    """ General error that is execite of the quere submitted is not valid"""
    
class QueryReturnedZero(Exception):
    """ Invoked when a valid query is submitted but returns no results"""
    
class CompileDataError(Exception):
    """ Error in compiling the data into a NamedTuple """
    