'''
inherent_concepts_test

This module serves as the unit test for inherent_concepts
'''

import argparse
from self_concepts import Concept
from self_concepts import Property
from self_concepts import Relationship
from self_concepts import Ontology
from self_concepts import Blackboard
from self_concepts import Agent
from self_concepts import SelfException
import inherent_concepts

# Helper functions in support of concise and verbose reporting

def parseArguments():
    '''Collect and return the test's arguments.'''

    parser = argparse.ArgumentParser(description='Test ')
    parser.add_argument('-c',
            '--concise',
            action='store_true',
            help='test self_concept with concise results')
    return parser.parse_args()

def reportHeader(message):
    '''Print a report header.'''

    if arguments.concise != True:
        print(message)
    else:
        print('#', end='')

def reportSection(message):
    '''Print a section header.'''

    if arguments.concise != True:
        print('    ' + message)
    else:
        print('*', end='')

def reportDetail(message):
    '''Print a report detail.'''

    if arguments.concise != True:
        print('        ' + message)
    else:
        print('.', end='')

def reportDetailFailure(message):
    '''Print a report failure.'''

    if arguments.concise != True:
        print('!!!!!!! ' + message)
    else:
        print('!')
    exit()

def reportConceptName(concept: 'Concept'):
    '''Print the name of the concept.'''

    reportDetail('        Function applied to ' + concept.__class__.__name__ + ' (' + concept.name + ')')


# Various functions, classes, and instances used for testing

# TBD unit test

def testInherentConcepts():

    reportHeader('Inherent Concepts')    

# Test all of Self's foundational classes

arguments = parseArguments()

testInherentConcepts()

# Clean up the output stream if reporting concisely

if arguments.concise == True:
  print()
