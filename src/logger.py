"""_summary_
Logger setup for the TEST-OK package manager.
Please use this logger for all logging related things in this project.

Returns:
    _type_: _description_
"""
import os
import logging

def setup_logger(log_file_name, info_level=logging.INFO):
    """_summary_

    Args:
        log_file_name (_type_): _description_
        info_level (_type_, optional): _description_. Defaults to logging.INFO.
        
    Ssage:
        logger = setup_logger('<filename>')
    
    Returns:
        _type_: logger object.
    """
    try:
        log_dir = os.path.join(os.path.normpath(os.getcwd() + os.sep), 'logs\\')
        log_fname  = os.path.join(log_dir,log_file_name)
        
        #Setup for file logging
        logging.basicConfig(
            filename=log_fname,
            level=info_level, 
            format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
            datefmt='%H:%M:%S'
            )
    except FileNotFoundError:
        
        os.makedirs(os.path.dirname(log_dir),exist_ok=True)
        with open(log_fname, "w") as f:
            f.write("TEST-OK package manager log file\n")
        print("Created logs folder, please rerun app")
        
    
    # set up logging to console
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)

    logger = logging.getLogger(__name__)
        
    return logger

"""
logger = setup_logger('__init__')

logger.debug('This is a debug message') #shows up only when loggin.DEBUG is called.
logger.info('This is an info message') #always shows up, but should only be used for non critical info.
logger.warning('This is a warning message')#always shows up, but should only be used for actual warnings.
logger.error('This is an error message')#always shows up, but should only be used for error expections.
logger.critical('This is a critical message')#always shows up, should only be used if the app cannot continue.
"""
