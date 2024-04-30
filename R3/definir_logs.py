import logging

def logs():

    logFile = 'boges.log'
    logFormat='%(asctime)s %(levelname)s %(message)s'
    logLevel= logging.DEBUG
    logMode = 'w'

    logging.basicConfig(level=logLevel,format=logFormat,filename=logFile,filemode=logMode)

    logging.debug("Debug message")
    logging.info("Informative message")
    logging.error("Error message")
    logging.warning('Protocol problem: %s', 'connection reset')