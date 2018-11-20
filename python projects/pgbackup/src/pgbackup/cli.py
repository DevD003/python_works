#from the argparse importing Argument Parser
from argparse import ArgumentParser

#defining a user customized action class called the driver action to take in driver, destination
class DriverAction(Action):
    #defining __call__ function as per the dcoumentation of Action arg of argparse
    #self  - callin in the parser itself, action (here)
    def __call__(self, parser, namespace, values, option_string=None):
        #unpacking of sequence type assigning
        driver,destination = values
        namespace.driver=driver.lower()
        namespace.destination=destination


#defining the create_parser
def create_parser():
    #parsing
    parser = ArgumentParser()
    #adding url argument
    parser.add_argument('url',help="URL of the Postgres SQL Db to backup")
    #adding the driver argument that has 2 args - driver,destination
    parser.add_argument('--driver',
            help='How and where to store the backup',
            #number of argumetns is 2
            nargs=2,
            action=DriverAction,
            required=True
            )
    return parser

