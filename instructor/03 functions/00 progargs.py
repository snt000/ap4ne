from jinja2 import Template
import yaml
from argparse import ArgumentParser
from pprint import pprint

parser = ArgumentParser("YML file")
parser.add_argument("-f", "--file",
                    help="specify yml file",
                    required=True)
args = parser.parse_args()
file_name = args.file

print (args)
print (file_name)