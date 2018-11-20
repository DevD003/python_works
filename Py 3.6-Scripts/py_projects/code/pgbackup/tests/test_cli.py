#importing the pytest module to use pytest.raises functionality
import pytest

from pgbackup import cli
#creating a test, for as CLI will have an issue if driver is not givem
# $ pgbackup postgres://bob@example.com;5432/db_one --driver s3 backups

url = "postgres://bob@example.com:5432/db_one"

#test without driver
def test_parser_without_driver():

    """
    Without a specified driver the parser will exit
    """
    #pytest.raises  raises sys exit error - if test fails
    with pytest.raises(SystemExit):
        #create a parser to  creates args that go in, checks for errors
        parser = cli.create_parser()
        #parsing the parse args, to url - the db string
        parser.parse_args([url])

#test with driver, but no destination
def test_parser_with_driver():

    """
    The parser will exit if it receives a driver without a destibation
    """

    parser=cli.create_parser()
    #parsing an arg to check for the destination
    with pytest.raises(SystemExit):
        parser.parse_args([url,"--driver","local"])

#happypath test(below) - test successful and sends us useful info

#test with driver and destination
def test_parser_with_driver_and_destination():
    """
    The parser will not exit if it receives driver and destination
    """
    parser = cli.create_parser()

    args=parser.parse_args([url,'--driver','local','/some/path'])

    assert args.driver == 'local'
    assert args.desitnation == '/some/path'
    assert args.url == url

