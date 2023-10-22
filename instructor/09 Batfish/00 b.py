import pandas as pd
from pybatfish.client.session import Session
from pybatfish.client.commands import *
from pybatfish.question.question import load_questions, list_questions
from pybatfish.question import bfq
#import re
import logging


def initialize():
    logging.getLogger("pybatfish").setLevel(logging.WARN)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', 2000)
    bf = Session(host="172.17.0.1")
    load_questions(session=bf)
    bf.init_snapshot('generated', name='generated', overwrite=True)
    bf.init_snapshot('running', name='running', overwrite=True)

def validate(question):
    # Compare both network configs to each other
    answer = question().answer(snapshot='running', reference_snapshot='generated')

    # If they match then skip
    if answer.table_data.empty:
        print (question)
        print('Configurations match!')
    else:
        print (question)
        print('Configuration Mismatch!')
        for property in question().answer().metadata.column_metadata:
            if property.isKey == False:
                comparison = question(properties=property.name).answer(snapshot='running', reference_snapshot='generated')
                if not comparison.table_data.empty:
                    print(comparison)

def main():
    initialize()
    functions = [bfq.nodeProperties, bfq.bgpPeerConfiguration, bfq.bgpProcessConfiguration, bfq.interfaceProperties]
    for f in functions:
        validate(f)

if __name__ == '__main__':
    main()