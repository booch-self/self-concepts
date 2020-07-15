'''
self_concepts_test

This module serves as the unit test for self_concepts
'''

import argparse
from self_concepts import Concept
from self_concepts import Property
from self_concepts import Relationship
from self_concepts import Ontology
from self_concepts import Blackboard
from self_concepts import Agent
from self_concepts import SelfException


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

class AnotherConcept(Concept): pass

CONCEPT_NAME_1 = 'A well-formed concept'
CONCEPT_NAME_2 = 'A well-formed concept'
CONCEPT_NAME_3 = 'Another well-formed concept'
CONCEPT_NAME_4 = 'A well-formed concept'

c1 = Concept(CONCEPT_NAME_1)
c2 = Concept(CONCEPT_NAME_2)
c3 = AnotherConcept(CONCEPT_NAME_3)
c4 = Concept(CONCEPT_NAME_4)

class AnotherProperty(Property): pass
class YetAnotherProperty(AnotherProperty): pass

PROPERTY_NAME_1 = 'A well-formed property'
PROPERTY_NAME_2 = 'A well-formed property'
PROPERTY_NAME_3 = 'Another well-formed property'
PROPERTY_NAME_4 = 'A well-formed property'

PROPERTY_VALUE_1 = 42
PROPERTY_VALUE_2 = 'A value'
PROPERTY_VALUE_3 = c1
PROPERTY_VALUE_4 = 'A value'

p1 = Property(PROPERTY_NAME_1, PROPERTY_VALUE_1)
p2 = Property(PROPERTY_NAME_2, PROPERTY_VALUE_2)
p3 = AnotherProperty(PROPERTY_NAME_3, PROPERTY_VALUE_3)
p4 = Property(PROPERTY_NAME_4, PROPERTY_VALUE_4)

class AnotherRelationship(Relationship): pass

RELATIONSHIP_NAME_1 = 'A well-formed relationship'
RELATIONSHIP_NAME_2 = 'A well-formed relationship'
RELATIONSHIP_NAME_3 = 'Another well-formed relationship'
RELATIONSHIP_NAME_4 = 'A well-formed relationship'

r1 = Relationship(RELATIONSHIP_NAME_1, c1, c2)
r2 = Relationship(RELATIONSHIP_NAME_2, c2, c3)
r3 = AnotherRelationship(RELATIONSHIP_NAME_3, c3, c1)
r4 = Relationship(RELATIONSHIP_NAME_4, c1, c4)

ONTOLOGY_NAME_1 = 'A well-formed ontology'

o1 = Ontology(ONTOLOGY_NAME_1)

BLACKBOARD_NAME_1 = 'A well-formed blackboard'

b1 = Blackboard(BLACKBOARD_NAME_1)

class AnotherAgent(Agent):

    def activity(self,
                 parameters: 'Concept' = None):

        super().activity(parameters)
        if parameters == None:
            reportDetail('        Activity ('
                         + self.name
                         + ')')
        else:
            reportDetail('        Activity ('
                         + self.name
                         + ') with parameters ('
                         + parameters.name
                         + ')')
                        
    def start(self,
              parameters: 'Concept' = None):

        super().start(parameters)
        if parameters == None:
            reportDetail('        Start ('
                         + self.name
                         + ')')
        else:
            reportDetail('        Start ('
                         + self.name
                         + ') with parameters ('
                         + parameters.name
                         + ')')

    def stop(self,
             parameters: 'Concept' = None):

        super().stop(parameters)
        if parameters == None:
            reportDetail('        Stop ('
                         + self.name
                         + ')')
        else:
            reportDetail('        Stop ('
                         + self.name
                         + ') with parameters ('
                         + parameters.name
                         + ')')

    def pause(self,
              parameters: 'Concept' = None):

        super().pause(parameters)
        if parameters == None:
            reportDetail('        Pause ('
                         + self.name
                         + ')')
        else:
            reportDetail('        Pause ('
                         + self.name
                         + ') with parameters ('
                         + parameters.name
                         + ')')
    
    def isAlive(self) -> bool:

        state = super().isAlive()
        reportDetail('        isAlive ('
                     + self.name
                     + ')')
        return True

    def status(self) -> Concept:

        state = super().status()
        reportDetail('        Status ('
                    + self.name
                    + ')')
        return Concept('Status')

    def signal(self,
               source: 'Concept',
               message: 'Concept',
               parameters: 'Concept' = None):

        super().signal(source, message, parameters)
        reportDetail('        Signal to '
                + self.__class__.__name__ 
                + ' ('
                + self.name
                + ') by '
                + source.__class__.__name__
                + ' ('
                + source.name
                + ') regarding '
                + message.__class__.__name__
                + ' ('
                + message.name
                + ')')

    def connect(self,
                channel: 'Relationship',
                parameters: 'Concept' = None):

        super().connect(channel, parameters)
        if parameters == None:
            reportDetail('        Connect ('
                         + self.name
                         + ') to a channel ('
                         + channel.name
                         + ')')
        else:
            reportDetail('        Connect ('
                         + self.name
                         + ') with parameters ('
                         + parameters.name
                         + ') to a channel ('
                         + channel.name
                         + ')')

AGENT_NAME_1 = 'A well-formed agent'
AGENT_NAME_2 = 'Another well-formed agent'
AGENT_NAME_3 = 'Yet another well-formed agent'

a1 = AnotherAgent(AGENT_NAME_1)
a2 = AnotherAgent(AGENT_NAME_2)
a3 = AnotherAgent(AGENT_NAME_3)

# Concept unit test

def testConcept():

    reportHeader('Concept')

    reportSection('attributes')
    if c1.name == CONCEPT_NAME_1:
        reportDetail('Correctly set and retrived name')
    else:
        reportDetailFailure('Name was not set or retrived')
    try:
        s = c1.properties
        reportDetailFailure('Properties were directly accessed')
    except SelfException:
        reportDetail('Correctly denied direct access to properties')
    try:
        c1.properties = set()
        reportDetailFailure('Properties were directly assigned')
    except SelfException:
        reportDetail('Correctly denied direct assignment to properties')

    reportSection('addProperty')
    c1.addProperty(p1)
    if c1.propertyExists(p1):
        reportDetail('Correctly added property')
    else:
        reportFailure('Property was not added')
    try:
        c1.addProperty(p1)
        reportDetailFailure('Property already exists')
    except SelfException:
        reportDetail('Correctly denied adding property that already exists')
    try:
        c1.addProperty('An ill-formed property')
        reportDetailFailure('Property is ill-formed')
    except SelfException:
        reportDetail('Correctly denied adding ill-formed property')

    reportSection('removeProperty')
    c1.removeProperty(p1)
    if not c1.propertyExists(p1):
        reportDetail('Correctly removed property')
    else:
        reportFailure('Property was not removed')
    try:
        c1.removeProperty(p2)
        reportDetailFailure('Property exists')
    except SelfException:
        reportDetail('Correctly denied removing property that does not exist')
    try:
        c1.removeProperty('An ill-formed property')
        reportDetailFailure('Property is ill-formed')
    except SelfException:
        reportDetail('Correctly denied removing ill-formed property')

    reportSection('removeAllProperties')
    c1.addProperty(p1)
    c1.addProperty(p2)
    c1.removeAllProperties()
    if c1.numberOfProperties() == 0:
        reportDetail('Correctly removed all properties')
    else:
        reportDetailFailure('Properties were not removed')

    reportSection('propertyExists')
    c1.addProperty(p1)
    if c1.propertyExists(p1):
        reportDetail('Correctly checked that property exists')
    else:
        reportDetailFailure('Property does not exist')
    if not c1.propertyExists(p2):
        reportDetail('Correctly checked that property does not exist')
    else:
        reportDetailFailure('Property exists')
    try:
        c1.propertyExists('An ill-formed property')
        reportDetailFailure('Property is ill-formed')
    except SelfException:
        reportDetail('Correctly denied checking existence of ill-formed property')

    reportSection('numberOfProperties')
    c1.addProperty(p2)
    if c1.numberOfProperties() == 2:
        reportDetail('Correctly reported number of properties')
    else:
        reportDetailFailure('Number of properties is wrong')

    reportSection('iterateOverProperties')
    c1.iterateOverProperties(reportConceptName)
    reportDetail('Correctly iterated over properties')
    c1.iterateOverProperties(reportConceptName, PROPERTY_NAME_1)
    reportDetail('Correctly iterated over properties with given name')
    c1.iterateOverProperties(reportConceptName, None, AnotherProperty)
    reportDetail('Correctly iterated over properties with given property class')
    c1.iterateOverProperties(reportConceptName, PROPERTY_NAME_2, Property)
    reportDetail('Correctly iterated over properties with given name and property class')
    try:
        c1.iterateOverProperties(reportConceptName, None, SelfException)
        reportDetailFailure('Property class is ill-formed')
    except SelfException:
        reportDetail('Correctly denied iterating over ill-formed property class')
    try:
        c1.iterateOverProperties(reportConceptName, None, 'An ill-formed property class')
        reportDetailFailure('Property class is ill-formed')
    except SelfException:
        reportDetail('Correctly denied iterating over ill-formed property class')

# Property unit test

def testProperty():

    reportHeader('Property')

    reportSection('attributes')
    if p3.name == PROPERTY_NAME_3:
        reportDetail('Correctly set and retrived name')
    else:
        reportDetailFailure('Name was not set or retrived')
    if p3.value == c1:
        reportDetail('Correctly set and retrieved value')
    else:
        reportDetailFailure('Value was not set or retrieved')

# Relationship unit test

def testRelationship():

    reportHeader('Relationship')

    reportSection('constructor')
    try:
        r0 = Relationship('A well-formed relationship', c1, c2)
        reportDetail('Correctly constructed relationship')
    except SelfException:
        reportDetailFailure('Relationship was not constructed')
    try:
        r0 = Relationship('A well-formed relationship', Concept, Concept)
        reportDetail('Correctly constructed relationship')
    except SelfException:
        reportDetailFailure('Relationship was not constructed')
    try:
        r0 = Relationship('An ill-formed relationship', 'An ill-formed edge', c2)
        reportDetailFailure('Edge is ill-formed')
    except SelfException:
        reportDetail('Correctly denied constructing relationship with ill-formed edge')
    try:
        r0 = Relationship('An ill-formed relationship', c1, 'An ill-formed edge')
        reportDetailFailure('Edge is ill-formed')
    except SelfException:
        reportDetail('Correctly denied constructing relationship with ill-formed edge')
    

    reportSection('attributes')
    r1.name = RELATIONSHIP_NAME_1;
    if r1.name == RELATIONSHIP_NAME_1:
        reportDetail('Correctly set and retrived name')
    else:
        reportDetailFailure('Name was not set or retrieved')
    r1.edge1 = c1
    if r1.edge1 == c1:
        reportDetail('Correctly set and retrieved edge')
    else:
        reportDetailFailure('Edge was not set or retrieved')
    try:
        r1.edge1 = 'An ill-formed edge'
        reportDetailFailure('Edge is ill-formed')
    except SelfException:
        reportDetail('Correctly denied assigning ill-formed edge')
    try:
        r1.edge2 = 'An ill-formed edge'
        reportDetailFailure('Edge is ill-formed')
    except SelfException:
        reportDetail('Correctly denied assigning ill-formed edge')
    try:
        s = r1.edge1Properties
        reportDetailFailure('Edge properties were directly accessed')
    except SelfException:
        reportDetail('Correctly denied direct access to edge properties')
    try:
        r1.edge1Properties = set()
        reportDetailFailure('Edge properties were directly assigned')
    except SelfException:
        reportDetail('Correctly denied direct assignment to edge properties')
    try:
        s = r1.edge2Properties
        reportDetailFailure('Edge properties were directly accessed')
    except SelfException:
        reportDetail('Correctly denied direct access to edge properties')
    try:
        r1.edge2Properties = set()
        reportDetailFailure('Edge properties were directly assigned') 
    except SelfException:
        reportDetail('Correctly denied direct assignment to edge properties')

    reportSection('addEdgeProperty')
    r1.addEdgeProperty(Relationship.EDGE1, p1)
    if r1.edgePropertyExists(Relationship.EDGE1, p1):
        reportDetail('Correctly added edge property')
    else:
        reportFailure('Edge property was not added')
    try:
        r1.addEdgeProperty(Relationship.EDGE1, p1)
        reportDetailFailure('Edge property already exists')
    except SelfException:
        reportDetail('Correctly denied adding edge property that already exists')
    try:
        r1.addEdgeProperty(Relationship.EDGE1, 'An ill-formed property')
        reportDetailFailure('Edge property is ill-formed')
    except SelfException:
        reportDetail('Correctly denied adding ill-formed edge property')
    r1.addEdgeProperty(Relationship.EDGE2, p1)
    if r1.edgePropertyExists(Relationship.EDGE2, p1):
        reportDetail('Correctly added edge property')
    else:
        reportFailure('Edge property was not added')
    try:
        r1.addEdgeProperty(Relationship.EDGE2, p1)
        reportDetailFailure('Edge property already exists')
    except SelfException:
        reportDetail('Correctly denied adding edge property that already exists')
    try:
        r1.addEdgeProperty(Relationship.EDGE2, 'An ill-formed property')
        reportDetailFailure('Edge property is ill-formed')
    except SelfException:
        reportDetail('Correctly denied adding ill-formed edge property')

    reportSection('removeEdgeProperty')
    r1.removeEdgeProperty(Relationship.EDGE1, p1)
    if not r1.edgePropertyExists(Relationship.EDGE1, p1):
        reportDetail('Correctly removed edge property')
    else:
        reportFailure('Edge property was not removed')
    try:
        r1.removeEdgeProperty(Relationship.EDGE1, p2)
        reportDetailProperty('Edge property exists')
    except SelfException:
        reportDetail('Correctly denied removing edge property that does not exist')
    try:
        r1.removeEdgeProperty(Relationship.EDGE1, 'An ill-formed property')
        reportDetailFailure('Edge property is ill-formed')
    except SelfException:
        reportDetail('Correctly denied removing ill-formed edge property')
    r1.removeEdgeProperty(Relationship.EDGE2, p1)
    if not r1.edgePropertyExists(Relationship.EDGE2, p1):
        reportDetail('Correctly removed edge property')
    else:
        reportFailure('Edge property was not removed')
    try:
        r1.removeEdgeProperty(Relationship.EDGE2, p2)
        reportDetailFailure('Edge property exists')
    except SelfException:
        reportDetail('Correctly denied removing edge property that does not exist')
    try:
        r1.removeEdgeProperty(Relationship.EDGE2, 'An ill-formed property')
        reportDetailFailure('Edge property is ill-formed')
    except SelfException:
        reportDetail('Correctly denied removing ill-formed edge property')

    reportSection('removeAllEdgeProperties')
    r1.addEdgeProperty(Relationship.EDGE1, p1)
    r1.addEdgeProperty(Relationship.EDGE1, p2)
    r1.removeAllEdgeProperties(Relationship.EDGE1)
    if r1.numberOfEdgeProperties(Relationship.EDGE1) == 0:
        reportDetail('Correctly removed all edge properties')
    else:
        reportDetailFailure('Edge properties were not removed')
    r1.addEdgeProperty(Relationship.EDGE2, p1)
    r1.addEdgeProperty(Relationship.EDGE2, p2)
    r1.removeAllEdgeProperties(Relationship.EDGE2)
    if r1.numberOfEdgeProperties(Relationship.EDGE2) == 0:
        reportDetail('Correctly removed all edge properties')
    else:
        reportDetailFailure('Edge properties were not removed')

    reportSection('edgePropertyExists')
    r1.addEdgeProperty(Relationship.EDGE1, p1)
    r1.addEdgeProperty(Relationship.EDGE2, p1)
    if r1.edgePropertyExists(Relationship.EDGE1, p1):
        reportDetail('Correctly checked that edge property exists')
    else:
        reportDetailFailure('Edge property does not exist')
    if not r1.edgePropertyExists(Relationship.EDGE1, p2):
        reportDetail('Correctly checked that edge property does not exist')
    else:
        reportDetailFailure('Edge property exists')
    try:
        r1.edgePropertyExists(Relationship.EDGE1, 'An ill-formed property')
        reportDetailFailure('Edge property is ill-formed')
    except SelfException:
        reportDetail('Correctly denied checking existence of ill-formed edge property')
    if r1.edgePropertyExists(Relationship.EDGE2, p1):
        reportDetail('Correctly checked that edge property exists')
    else:
        reportDetailFailure('Edge property does not exist')
    if not r1.edgePropertyExists(Relationship.EDGE2, p2):
        reportDetail('Correctly checked that edge property does not exist')
    else:
        reportDetailFailure('Edge property exists')
    try:
        r1.edgePropertyExists(Relationship.EDGE2, 'An ill-formed property')
        reportDetailFailure('Edge property is ill-formed')
    except SelfException:
        reportDetail('Correctly denied checking existence of ill-formed edge property')

    reportSection('numberOfEdgeProperties')
    r1.addEdgeProperty(Relationship.EDGE1, p2)
    r1.addEdgeProperty(Relationship.EDGE2, p2)
    if r1.numberOfEdgeProperties(Relationship.EDGE1) == 2:
        reportDetail('Correctly reported number of edge properties')
    else:
        reportDetailFailure('Number of edge properties is wrong')
    if r1.numberOfEdgeProperties(Relationship.EDGE2) == 2:
        reportDetail('Correctly reported number of edge properties')
    else:
        reportDetailFailure('Number of edge properties is wrong')


    reportSection('iterateOverEdgeProperties')
    r1.iterateOverEdgeProperties(Relationship.EDGE1, reportConceptName)
    reportDetail('Correctly iterated over edge properties')
    r1.iterateOverEdgeProperties(Relationship.EDGE1, reportConceptName, PROPERTY_NAME_1)
    reportDetail('Correctly iterated over edge properties with given name')
    r1.iterateOverEdgeProperties(Relationship.EDGE1, reportConceptName, None, AnotherProperty)
    reportDetail('Correctly iterated over edge properties with given property class')
    r1.iterateOverEdgeProperties(Relationship.EDGE1, reportConceptName, PROPERTY_NAME_2, Property)
    reportDetail('Correctly iterated over edge properties with given name and property class')
    try:
        r1.iterateOverEdgeProperties(Relationship.EDGE1, reportConceptName, None, SelfException)
        reportDetailFailure('Property class is ill-formed')
    except SelfException:
        reportDetail('Correctly denied iterating over ill-formed property class')
    try:
        r1.iterateOverEdgeProperties(Relationship.EDGE1, reportConceptName, None, 'An ill-formed property class')
        reportDetailFailure('Edge property class is ill-formed')
    except SelfException:
        reportDetail('Correctly denied iterating over ill-formed edge property class')
    r1.iterateOverEdgeProperties(Relationship.EDGE2, reportConceptName)
    reportDetail('Correctly iterated over edge properties')
    r1.iterateOverEdgeProperties(Relationship.EDGE2, reportConceptName, PROPERTY_NAME_1)
    reportDetail('Correctly iterated over edge properties with given name')
    r1.iterateOverEdgeProperties(Relationship.EDGE2, reportConceptName, None, AnotherProperty)
    reportDetail('Correctly iterated over edge properties with given property class')
    r1.iterateOverEdgeProperties(Relationship.EDGE2, reportConceptName, PROPERTY_NAME_2, Property)
    reportDetail('Correctly iterated over edge properties with given name and property class')
    try:
        r1.iterateOverEdgeProperties(Relationship.EDGE2, reportConceptName, None, SelfException)
        reportDetailFailure('Property class is ill-formed')
    except SelfException:
        reportDetail('Correctly denied iterating over ill-formed property class')
    try:
        r1.iterateOverEdgeProperties(Relationship.EDGE2, reportConceptName, None, 'An ill-formed property class')
        reportDetailFailure('Edge property class is ill-formed')
    except SelfException:
        reportDetail('Correctly denied iterating over ill-formed edge property class')
    
# Ontology unit test

def testOntology():

    reportHeader('Ontology')

    reportSection('attributes')
    if o1.name == ONTOLOGY_NAME_1:
        reportDetail('Correctly set and retrived name')
    else:
        reportDetailFailure('Name was not set or retrived')
    try:
        s = o1.concepts
        reportDetailFailure('Concepts were directly accessed')
    except SelfException:
        reportDetail('Correctly denied direct access to concepts')
    try:
        o1.concepts = set()
        reportDetailFailure('Concepts were directly assigned')
    except SelfException:
        reportDetail('Correctly denied direct assignment to concepts')
    try:
        s = o1.relationships
        reportDetailFailure('Relationships were directly accessed')
    except SelfException:
        reportDetail('Correctly denied direct access to relationships')
    try:
        o1.relationships = set()
        reportDetailFailure('Relationships were directly assigned')
    except SelfException:
        reportDetail('Correctly denied direct assignment to relationships')
 
    reportSection('addConcept')
    o1.addConcept(c1)
    if o1.conceptExists(c1):
        reportDetail('Correctly added concept')
    else:
        reportFailure('Concept was not added')
    try:
        o1.addConcept(c1)
        reportDetailFailure('Concept already exists')
    except SelfException:
        reportDetail('Correctly denied adding concept that already exists')
    try:
        o1.addConcept('An ill-formed concept')
        reportDetailFailure('Concept is ill-formed')
    except SelfException:
        reportDetail('Correctly denied adding ill-formed concept')

    reportSection('removeConcept')
    o1.removeConcept(c1)
    if not o1.conceptExists(c1):
        reportDetail('Correctly removed concept')
    else:
        reportFailure('Concept was not removed')
    try:
        o1.removeConcept(c2)
        reportDetailFailure('Concept exists')
    except SelfException:
        reportDetail('Correctly denied removing concept that does not exist')
    try:
        o1.removeConcept('An ill-formed concept')
        reportDetailFailure('Concept is ill-formed')
    except SelfException:
        reportDetail('Correctly denied removing an ill-formed concept')
    o1.addConcept(c1)
    o1.addConcept(c2)
    o1.addRelationship(r1)
    try:
        o1.removeConcept(c1)
        reportDetailFailure('Concept is bound')
    except SelfException:
        reportDetail('Correctly denied removing concept that is bound')

    reportSection('removeAllConcepts')
    o1.removeRelationship(r1)
    o1.removeAllConcepts()
    if o1.numberOfConcepts() == 0:
        reportDetail('Correctly removed all concepts')
    else:
        reportDetailFailure('Concepts were not removed')
    o1.addConcept(c1)
    o1.addConcept(c2)
    o1.addRelationship(r1)
    try:
        o1.removeAllConcepts()
        reportDetailFailure('Concepts are bound')
    except SelfException:
        reportDetail('Correctly denied removing concepts that are bound')
    o1.removeRelationship(r1)
    o1.removeConcept(c2)
    o1.removeConcept(c1)

    reportSection('conceptExists')
    o1.addConcept(c1)
    if o1.conceptExists(c1):
        reportDetail('Correctly checked that concept exists')
    else:
        reportDetailFailure('Concept does not exist')
    if not o1.conceptExists(c2):
        reportDetail('Correctly checked that concept does not exist')
    else:
        reportDetailFailure('Concept exists')
    try:
        o1.conceptExists('An ill-formed concept')
        reportDetailFailure('Concept is ill-formed')
    except SelfException:
        reportDetail('Correctly denied checking existence of ill-formed concept')

    reportSection('numberOfConcepts')
    o1.addConcept(c2)
    if o1.numberOfConcepts() == 2:
        reportDetail('Correctly reported number of concepts')
    else:
        reportDetailFailure('Number of concepts is wrong')

    reportSection('iterateOverConcepts')
    o1.addConcept(c3)
    o1.iterateOverConcepts(reportConceptName)
    reportDetail('Correctly iterated over concepts')
    o1.iterateOverConcepts(reportConceptName, CONCEPT_NAME_1)
    reportDetail('Correctly iterated over concepts with given name')
    o1.iterateOverConcepts(reportConceptName, None, AnotherConcept)
    reportDetail('Correctly iterated over concepts with given concept class')
    o1.iterateOverConcepts(reportConceptName, CONCEPT_NAME_2, Concept)
    reportDetail('Correctly iterated over concepts with given name and concept class')
    try:
        o1.iterateOverConcepts(reportConceptName, None, SelfException)
        reportDetailFailure('Concept class is ill-formed')
    except SelfException:
        reportDetail('Correctly denied iterating over ill-formed concept class')
    try:
        o1.iterateOverConcepts(reportConceptName, None, 'An ill-formed concept class')
        reportDetailFailure('Concept class is ill-formed')
    except SelfException:
        reportDetail('Correctly denied iterating over ill-formed concept class')

    reportSection('addRelationship')
    o1.addRelationship(r1)
    o1.addRelationship(r2)
    o1.addRelationship(r3)
    if o1.numberOfRelationships() == 3:
        reportDetail('Correctly added relationship')
    else:
        reportDetailFailure('Relationship was not added')
    try:
        o1.addRelationship(r1)
        reportDetailFailure('Relationship already exists')
    except SelfException:
        reportDetail('Correctly denied addding relationship that already exists')
    try:
        o1.addRelationship('An ill-formed relationship')
        reportDetailFailure('Relationship is ill-formed')
    except SelfException:
        reportDetail('Correctly denied adding ill-formed relationship')
    try:
        o1.addRelationship(r4)
        reportDetailFalure('Relationship is not closed')
    except SelfException:
        reportDetail('Correctly denied adding relationship that is not closed')

    reportSection('removeRelationship')
    o1.removeRelationship(r3)
    if not o1.relationshipExists(r3):
        reportDetail('Correctly remove relationship')
    else:
        reportDetailFailure('Relationship was not removed')
    try:
        o1.removeRelationship(r3)
        reportDetailFailure('Relationship exists')
    except SelfException:
        reportDetail('Corectly denied removing relationship that does not exist')
    try:
        o1.removeRelationship('An ill-formed relationship')
        reportDetailFailure('Relationship is ill-formed')
    except SelfException:
        reportDetail('Correctly denied removing ill-formed relationship')

    reportSection('removeAllRelationships')
    o1.removeAllRelationships()
    if o1.numberOfRelationships() == 0:
        reportDetail('Correctly removed all relationships')
    else:
         reportDetailFailure('Relationships were not removed')

    reportSection('relationshipExists')
    o1.addRelationship(r1)
    if o1.relationshipExists(r1):
        reportDetail('Correctly checked that relationship exists')
    else:
        reportDetailFailure('Relationship does not exist')
    if not o1.relationshipExists(r3):
        reportDetail('Correctly checked that relationship does not exist')
    else:
        reportDetailFailure('Relationship exists')
    try:
        o1.relationshipExists('An ill-formed relationship')
        reportDetailFailure('Relationship is ill-formed')
    except SelfException:
        reportDetail('Correctly denied checking existance of ill-formed relationship')

    reportSection('numberOfRelationship')
    o1.addRelationship(r2)
    if o1.numberOfRelationships() == 2:
        reportDetail('Correctly reported number of relationships')
    else:
        reportDetailFailure('Number of relationships is wrong')

    reportSection('iterateOverRelationships')
    o1.addRelationship(r3)
    o1.iterateOverRelationships(reportConceptName)
    reportDetail('Correctly iterated over relationships')
    o1.iterateOverRelationships(reportConceptName, RELATIONSHIP_NAME_1)
    reportDetail('Correctly iterated over relationships with given name')
    o1.iterateOverRelationships(reportConceptName, None, AnotherRelationship)
    reportDetail('Correctly iterated over relationships with given relationship class')
    o1.iterateOverRelationships(reportConceptName, RELATIONSHIP_NAME_2, Relationship)
    reportDetail('Correctly iterated over relationshps with given name and concept class')
    try:
        o1.iterateOverRelationships(reportConceptName, None, SelfException)
        reportDetailFailure('Relationship class is ill-formed')
    except SelfException:
        reportDetail('Correctly denied iterating over ill-formed relationship class')
    try:
        o1.iterateOverRelationships(reportConceptName, None, 'An ill-formed relationship class')
        reportDetailFailure('Relationship class is ill-formed')
    except SelfException:
        reportDetail('Correctly denied iterating over ill-formed relationship class')

    reportSection('conceptIsBound')
    if o1.conceptIsBound(c1):
        reportDetail('Correctly checked that concept is bound')
    else:
        reportDetailFailure('Concept is not bound')
    if not o1.conceptIsBound(c4):
        reportDetail('Correctly checked that concept is not bound')
    else:
        reportDetailFailure('Concept is bound')
    try:
        o1.conceptIsBound('An ill-formed concept')
        reportDetailFailure('Concept is ill-formed')
    except SelfException:
        reportDetail('Correctly denied checking if an ill-formed concept is bound')

    reportSection('numberOfUnboundConcepts')
    o1.addConcept(c4)   
    if o1.numberOfUnboundConcepts() == 1:
        reportDetail('Correctly reported number of unbound concepts')
    else:
        reportDetailFailure('Number of unbound concepts is wrong')

    reportSection('numberOfBoundConcepts')
    if o1.numberOfBoundConcepts() == 3:
        reportDetail('Correctly reported number of bound concepts')
    else:
        reportDetailFailure('Number of bound concepts is wrong')
    
    reportSection('iterateOverUnboundConcepts')
    o1.iterateOverUnboundConcepts(reportConceptName)
    reportDetail('Correctly iterated over unbound concepts')
    o1.iterateOverUnboundConcepts(reportConceptName, CONCEPT_NAME_1)
    reportDetail('Correctly iterated over unbound concepts with given name')
    o1.iterateOverUnboundConcepts(reportConceptName, None, AnotherConcept)
    reportDetail('Correctly iterated over unbound concepts with given concept class')
    o1.iterateOverUnboundConcepts(reportConceptName, CONCEPT_NAME_2, Concept)
    reportDetail('Correctly iterated over unbound concepts with given name and concept class')
    try:
        o1.iterateOverUnboundConcepts(reportConceptName, None, SelfException)
        reportDetailFailure('Concept class is ill-formed')
    except SelfException:
        reportDetail('Correctly denied iterating over ill-formed concept class')
    try:
        o1.iterateOverUnboundConcepts(reportConceptName, None, 'An ill-formed concept class')
        reportDetailFailure('Concept class is ill-formed')
    except SelfException:
        reportDetail('Correctly denied iterating over ill-formed concept class')

    reportSection('iterateOverBoundConcepts')
    o1.iterateOverBoundConcepts(reportConceptName)
    reportDetail('Correctly iterated over bound concepts')
    o1.iterateOverBoundConcepts(reportConceptName, CONCEPT_NAME_1)
    reportDetail('Correctly iterated over bound concepts with given name')
    o1.iterateOverBoundConcepts(reportConceptName, None, AnotherConcept)
    reportDetail('Correctly iterated over bound concepts with given concept class')
    o1.iterateOverBoundConcepts(reportConceptName, CONCEPT_NAME_2, Concept)
    reportDetail('Correctly iterated over bound concepts with given name and concept class')
    try:
        o1.iterateOverBoundConcepts(reportConceptName, None, SelfException)
        reportDetailFailure('Concept class is ill-formed')
    except SelfException:
        reportDetail('Correctly denied iterating over ill-formed concept class')
    try:
        o1.iterateOverBoundConcepts(reportConceptName, None, 'An ill-formed concept class')
        reportDetailFailure('Concept class is ill-formed')
    except SelfException:
        reportDetail('Correctly denied iterating over ill-formed concept class')

# Blackboard unit test

def testBlackboard():

    reportHeader('Blackboard')

    reportSection('attributes')
    if b1.name == BLACKBOARD_NAME_1:
        reportDetail('Correctly set and retrieved name')
    else:
        reportDetailFailure('Name was not set or retrieved')
    try:
        s = b1.concepts
        reportDetailFailure('Concepts were directly accessed')
    except SelfException:
        reportDetail('Correctly denied direct access to concepts')
    try:
        b1.concepts = set()
        reportDetailFailure('Concepts were directly assigned')
    except SelfException:
        reportDetail('Correctly denied direct assignment to concepts')
    try:
        s = b1.conceptClasses
        reportDetailFailure('Concepts classes were directly accessed')
    except SelfException:
        reportDetail('Correctly denied direct access to concept classes')
    try:
        b1.conceptClasses = set()
        reportDetailFailure('Concept classes were directly assigned')
    except SelfException:
        reportDetail('Correctly denied direct assignment to concept classes')
    try:
        s = b1.publications
        reportDetailFailure('Publications were directly accessed')
    except SelfException:
        reportDetail('Correctly denied direct access to publications')
    try:
        b1.publications = set()
        reportDetailFailure('Publications were directly assigned')
    except SelfException:
        reportDetail('Correctly denied direct assignment to publications')
    try:
        s = b1.conceptSubscriptions
        reportDetailFailure('Subscriptions were directly accessed')
    except SelfException:
        reportDetail('Correctly denied direct access to subsubscriptions')
    try:
        b1.conceptSubscriptions = set()
        reportDetailFailure('Subscriptions were directly assigned')
    except SelfException:
        reportDetail('Correctly denied direct assignment to subscriptions')
    try:
        s = b1.classSubscriptions
        reportDetailFailure('Class subscriptions were directly accessed')
    except SelfException:
        reportDetail('Correctly denied direct access to class subscriptions')
    try:
        b1.classSubscriptions = set()
        reportDetailFailure('Class subscriptions were directly assigned')
    except SelfException:
        reportDetail('Correctly denied direct assignment to class subscriptions')

    reportSection('publishConcept')
    b1.publishConcept(a1, c1)
    if b1.conceptExists(c1):
        reportDetail('Correctly published concept')
    else:
        reportDetailFailure('Concept was not published')
    b1.subscribeToConceptClass(a2, AnotherConcept)
    b1.publishConcept(a1, c3)
    if len(b1.subscribers(c3)) == 1:
        reportDetail('Correctly subscribed to concept class instance')
    else:
        reportDetailFailure('Subscription failed')
    try:
        b1.publishConcept(a1, c1)
        reportDetailFailure('Concept already exists')
    except SelfException:
        reportDetail('Correctly denied adding concept that already exists')
    try:
        b1.publishConcept('An ill-formed agent', c1)
        reportDetailFailure('Agent is ill-formed')
    except SelfException:
        reportDetail('Correctly denied publishing ill-formed agent')
    try:
        b1.publishConcept(a1, 'An ill-formed concept')
        reportDetailFailure('Concept is ill-formed')
    except SelfException:
        reportDetail('Correctly denied publishing ill-formed concept')

    reportSection('unpublishConcept')
    b1.unpublishConcept(c1)
    b1.unpublishConcept(c3)
    if not b1.conceptExists(c3):
        reportDetail('Correctly unpublished concept')
    else:
        reportDetailFailure('Concept was not unpublished')
    b1.publishConcept(a1, c1)
    b1.publishConcept(a2, c2)
    b1.publishConcept(a1, c3)
    b1.unpublishConcept()
    if b1.numberOfConcepts() == 0:
        reportDetail('Correctly unpublished all concepts')
    else:
        reportDetailFailure('Concepts were not unpublished')
    try:
        b1.unpublishConcept(c3)
        reportDetailFailure('Concept exists')
    except SelfException:
        reportDetail('Correctly denied unpublishing concept that does not exist')
    try:
        b1.unpublishConcept('An ill-formed concept')
        reportDetailFailure('Concept is ill-formed')
    except SelfException:
        reportDetail('Correctly denied unpublishing ill-formed concept')
    reportSection('publisher')
    b1.publishConcept(a1, c1)
    if b1.publisher(c1) == a1:
        reportDetail('Correctly returned publisher')
    else:
        reportDetailFailure('Publisher was not returned')
    try:
        b1.publisher(c2)
        reportDetailFailure('Concept does not exist')
    except SelfException:
        reportDetail('Correctly denied returning publisher of concept that does not exist')
    try:
        b1.publisher('An ill-formed concept')
        reportDetailFailure('Concept is ill-formed')
    except SelfException:
        reportDetail('Correctly denied returning publisher of ill-formed concept')

    reportSection('signalPublisher')
    b1.signalPublisher(Concept('A well-formed source'), Concept('A well-formed message'), c1)
    reportDetail('Correctly signaled publisher')
    b1.signalPublisher(Concept('A well-formed source'), Concept('A well-formed message'))
    reportDetail('Correctly signaled publishers')
    try:
        b1.signalPublisher(Concept('A well-formed source'), Concept('A well-formed message'), c2)
        reportDetailFailure('Concept does not exist')
    except SelfException:
        reportDetail('Correctly denied signaling a publisher of concept that does not exist')
    try:
        b1.signalPublisher(Concept('A well-formed source'), Concept('A well-formed message'), 'An ill-formed concept')
        reportDetailFailure('Concept is ill-formed')
    except SelfException:
        reportDetail('Correctly denied signaling publisher of ill-formed concept')
    try:
        b1.signalPublisher('An ill-formed source', Concept('A well-formed message'), c1)
        reportDetail('Source is ill-formed')
    except SelfException:
        reportDetail('Correctly denied signaling publisher of ill-formed source')
    try:
        b1.signalPublisher(Concept('A well-formed source'), 'An ill-formed message', c1)
        reportDetailFailure('Message is ill-formed')
    except SelfException:
        reportDetail('Correctly denied signaling publisher of ill-formed message')

    reportSection('conceptExists')
    if b1.conceptExists(c1):
        reportDetail('Correctly checked that concept exists')
    else:
        reportDetailFailure('Concept does not exist')
    if not b1.conceptExists(c2):
        reportDetail('Correctly checked that concept does not exist')
    else:
        reportDetailFailure('Concept exists')
    try:
        b1.conceptExists('An ill-formed concept')
        reportDetailFailure('Concept is ill-formed')
    except SelfException:
        reportDetail('Correctly denied checking of ill-formed concept')

    reportSection('numberOfConcepts')
    b1.publishConcept(a2, c3)
    if b1.numberOfConcepts() == 2:
        reportDetail('Correctly reported number of concepts')
    else:
        reportDetailFailure('Number of concepts is wrong')

    reportSection('iterateOverConcepts')
    b1.iterateOverConcepts(reportConceptName)
    reportDetail('Correctly iterated over concepts')
    b1.iterateOverConcepts(reportConceptName, CONCEPT_NAME_1)
    reportDetail('Correctly iterated over concepts with given name')
    b1.iterateOverConcepts(reportConceptName, None, AnotherConcept)
    reportDetail('Correctly iterated over concepts with given concept class')
    b1.iterateOverConcepts(reportConceptName, CONCEPT_NAME_2, Concept)
    reportDetail('Correctly iterated over concepts with given name and concept class')
    try:
        b1.iterateOverConcepts(reportConceptName, None, SelfException)
        reportDetailFailure('Concept class is ill-formed')
    except SelfException:
        reportDetail('Correctly denied iterating over ill-formed concept class')
    try:
        b1.iterateOverConcepts(reportConceptName, None, 'An ill-formed concept class')
        reportDetailFailure('Concept class is ill-formed')
    except SelfException:
        reportDetail('Correctly denied iterating over ill-formed concept class')

    reportSection('subscribeToConcept')
    b1.subscribeToConcept(a3, c3)
    if len(b1.subscribers(c3)) == 2:
        reportDetail('Correctly subscribed to concept')
    else:
        reportDetailFailure('Concept was not subscribed')
    try:
        b1.subscribeToConcept(a3, c3)
        reportDetailFailure('Concept is already subscribed')
    except SelfException:
        reportDetail('Correctly denied subscribing to concept more than once')
    try:
        b1.subscribeToConcept(a3, c4)
        reportDetailFailure('Concept exists')
    except SelfException:
        reportDetail('Correctly denied subscribing to concept that does not exist')
    try:
        b1.subscribeToConcept('An ill-formed agent', c3)
        reportDetailFailure('Agent is ill-formed')
    except SelfException:
        reportDetail('Correctly denied subscribing by ill-formed agent')
    try:
        b1.subscribeToConcept(a2, 'An ill-formed concept')
        reportDetailFailure('Concept is ill-formed')
    except SelfException:
        reportDetail('Correctly denied subscribing to ill-formed concept')

    reportSection('unsubscribeFromConcept')
    b1.unsubscribeFromConcept()
    if len(b1.subscribers()) == 0:
        reportDetail('Correctly unsubscribed by from all concepts by all agents')
    else:
        reportDetailFailure('Concepts were not unsubscribed')
    b1.subscribeToConcept(a1, c1)
    b1.subscribeToConcept(a1, c3)
    b1.subscribeToConcept(a2, c1)
    b1.subscribeToConcept(a2, c3)
    b1.unsubscribeFromConcept(a1)
    if (len(b1.subscribers(c1)) == 1 and len(b1.subscribers(c3)) == 1):
        reportDetail('Correctly unsubscribed from all concepts by agent')
    else:
        reportDetailFailure('Concepts were not unsubscribed')
    b1.subscribeToConcept(a1, c1)
    b1.unsubscribeFromConcept(None, c1)
    if (len(b1.subscribers(c1)) == 0 and len(b1.subscribers(c3)) == 1):
        reportDetail('Correctly unsubscribied from concept by all agents')
    else:
        reportDetailFailure('Concepts were not unsubscribed')
    b1.unsubscribeFromConcept(a2, c3)
    if len(b1.subscribers(c3)) == 0:
        reportDetail('Correctly unsubscribed from concept by agent')
    else:
        reportDetailFailure('Concept was not unsubscribed')
    try:
        b1.unsubscribeFromConcept(None, c2)
        reportDetailFailure('Concept does not exist')
    except SelfException:
        reportDetail('Correctly denied unsubscribing from concept that does not exist')
    try:
        b1.unsubscribeFromConcept('An ill-formed agent', c1)
        reportDetailFailure('Agent is ill-formed')
    except SelfException:
        reportDetail('Correctly denied unsubscibing from ill-formed agent')
    try:
        b1.unsubscribeFromConcept(a1, 'An ill-formed concept')
        reportDetailFailure('Concept is ill-formed')
    except SelfException:
        reportDetail('Correctly denied unsubscrbing from ill-formed concept')

    reportDetail('subscribers')
    b1.subscribeToConcept(a1, c1)
    b1.subscribeToConcept(a2, c1)
    if len(b1.subscribers(c1)) == 2:
        reportDetail('Correctly return subscribers')
    else:
        reportDetailFailure('Subscribers were not returned')
    if len(b1.subscribers(c3)) == 0:
        reportDetail('Correctly returned subscribers')
    else:
        reportDetailFailure('Subscribers were not returned')
    if len(b1.subscribers()) == 2:
        reportDetail('Correctly returned subscribers')
    else:
        reportDetailFailure('Subscribers were not returned')
    try:
        b1.subscribers(c2)
        reportDetailFailure('Concept exists')
    except SelfException:
        reportDetail('Correctly denied returning subscribers from concept that does not exist')
    try:
        b1.subscribers('An ill-formed concept')
        reportDetailFailure('Concept is ill-formed')
    except:
        reportDetail('Correctly denied returning subscribers from ill-formed concept')

    reportDetail('signalSubscribers')
    b1.signalSubscribers(Concept('A well-formed source'), Concept('A well-formed message'), c1)
    reportDetail('Correctly signaled subscribers')
    b1.signalSubscribers(Concept('A well-formed source'), Concept('A well-formed message'))
    reportDetail('Correctly signaled subscribers')
    try:
        b1.signalSubscribers(Concept('A well-formed source'), Concept('A well-formed message'), c2)
        reportDetailFailure('Concept does not exist')
    except SelfException:
        reportDetail('Correctly denied signaling subscribers of concept that does not exist')
    try:
        b1.signalSubscribers(Concept('A well-formed source'), Concept('A well-formed message'), 'An ill-formed concept')
        reportDetailFailure('Concept is ill-formed')
    except SelfException:
        reportDetail('Correctly denied signaling subscribers of ill-formed concept')
    try:
        b1.signalSubscribers('An ill-formed source', Concept('A well-formed message'), c1)
        reportDetail('Source is ill-formed')
    except SelfException:
        reportDetail('Correctly denied signaling subscribers of ill-formed source')
    try:
        b1.signalSubscribers(Concept('A well-formed source'), 'An ill-formed message', c1)
        reportDetailFailure('Message is ill-formed')
    except SelfException:
        reportDetail('Correctly denied signaling subscribers of ill-formed message')

    reportSection('subscribeToConceptClass')
    b1.unsubscribeFromConceptClass()
    b1.subscribeToConceptClass(a1, Concept)
    b1.subscribeToConceptClass(a2, Concept)
    b1.subscribeToConceptClass(a3, AnotherConcept)
    if len(b1.classSubscribers()) == 3:
        reportDetail('Correctly subscribed to concept class')
    else:
        reportDetailFailure('Concept class was not subscribed')
    if len(b1.classSubscribers(Concept)) == 2:
        reportDetail('Correctly subscribed to concept class')
    else:
        reportDetail('Concept class was not subscribed')
    if len(b1.classSubscribers(AnotherConcept)) == 1:
        reportDetail('Correctly subscribed to concept class')
    else:
        reportDetailFailure('CConcept class was not subscribed')
    try:
        b1.subscribeToConceptClass(a1, Concept)
        reportDetailFailure('Concept class is already subscribed')
    except SelfException:
        reportDetail('Correctly denied subscribing to concept class more than once')
    try:
        b1.subscribeToConceptClass('An ill-formed agent', c3)
        reportDetailFailure('Agent is ill-formed')
    except SelfException:
        reportDetail('Correctly denied subscribing by ill-formed agent')
    try:
        b1.subscribeToConceptClass(a2, 'An ill-formed concept')
        reportDetailFailure('Concept is ill-formed')
    except SelfException:
        reportDetail('Correctly denied subscribing to ill-formed concept')
    
    reportSection('unsubscribeFromConceptClass')
    b1.unsubscribeFromConceptClass()
    if len(b1.classSubscribers()) == 0:
        reportDetail('Correctly unsubscribed by from all concept classes by all agents')
    else:
        reportDetailFailure('Concept classes were not unsubscribed')
    b1.subscribeToConceptClass(a1, Concept)
    b1.subscribeToConceptClass(a1, AnotherConcept)
    b1.subscribeToConceptClass(a2, Concept)
    b1.subscribeToConceptClass(a3, AnotherConcept)
    b1.unsubscribeFromConceptClass(a1)
    if (len(b1.classSubscribers(Concept)) == 1 and len(b1.classSubscribers(AnotherConcept)) == 1):
        reportDetail('Correctly unsubcribed from all concept classes by agent')
    else:
        reportDetailFailure('Concept classes were not unsubscribed')
    b1.subscribeToConceptClass(a1, Concept)
    b1.unsubscribeFromConceptClass(None, Concept)
    if len(b1.classSubscribers(AnotherConcept)) == 1:
        reportDetail('Correctly unsubscribied from concept class by all agents')
    else:
        reportDetailFailure('Concept class was not unsubscribed')
    b1.unsubscribeFromConceptClass(a3, AnotherConcept)
    if len(b1.classSubscribers()) == 0:
        reportDetail('Correctly unsubscribed from concept class by agent')
    else:
        reportDetailFailure('Concept class was not unsubscribed')
    try:
        b1.unsubscribeFromConceptClass(None, c2)
        reportDetailFailure('Concept class does not exist')
    except SelfException:
        reportDetail('Correctly denied unsubscribing from concept class that does not exist')
    try:
        b1.unsubscribeFromConceptClass('An ill-formed agent', c1)
        reportDetailFailure('Agent is ill-formed')
    except SelfException:
        reportDetail('Correctly denied unsubscibing from ill-formed agent')
    try:
        b1.unsubscribeFromConceptClass(a1, 'An ill-formed concept class')
        reportDetailFailure('Concept is ill-formed')
    except SelfException:
        reportDetail('Correctly denied unsubscrbing from ill-formed concept class')

    reportSection('classSubscribers')
    b1.subscribeToConceptClass(a1, Concept)
    b1.subscribeToConceptClass(a2, Concept)
    if len(b1.classSubscribers(Concept)) == 2:
        reportDetail('Correctly return subscribers')
    else:
        reportDetailFailure('Subscribers were not returned')
    if len(b1.classSubscribers()) == 2:
        reportDetail('Correctly returned subscribers')
    else:
        reportDetailFailure('Subscribers were not returned')
    try:
        b1.classSubscribers(AnotherConcept)
        reportDetailFailure('Concept class exists')
    except SelfException:
        reportDetail('Correctly denied returning subscribers from concept class that does not exist')
    try:
        b1.classSubscribers('An ill-formed concept class')
        reportDetailFailure('Concept class is ill-formed')
    except:
        reportDetail('Correctly denied returning subscribers from ill-formed concept class')

    reportSection('signalConceptClassSubscribers')
    b1.subscribeToConceptClass(a3, AnotherConcept)
    b1.signalClassSubscribers(Concept('A well-formed source'), Concept('A well-formed message'), Concept)
    reportDetail('Correctly signaled subscribers')
    b1.signalClassSubscribers(Concept('A well-formed source'), Concept('A well-formed message'))
    reportDetail('Correctly signaled subscribers')
    try:
        b1.signalClassSubscribers(Concept('A well-formed source'), Concept('A well-formed message'), SelfException)
        reportDetailFailure('Concept class does not exist')
    except SelfException:
        reportDetail('Correctly denied signaling subscribers of concept class that does not exist')
    try:
        b1.signalClassSubscribers(Concept('A well-formed source'),
                                  Concept('A well-formed message'),
                                  'An ill-formed concept class')
        reportDetailFailure('Concept class is ill-formed')
    except SelfException:
        reportDetail('Correctly denied signaling subscribers of ill-formed concept class')
    try:
        b1.signalClassSubscribers('An ill-formed source', Concept('A well-formed message'), Concept)
        reportDetail('Source is ill-formed')
    except SelfException:
        reportDetail('Correctly denied signaling subscribers of ill-formed source')
    try:
        b1.signalClassSubscribers(Concept('A well-formed source'), 'An ill-formed message', Concept)
        reportDetailFailure('Message is ill-formed')
    except SelfException:
        reportDetail('Correctly denied signaling subscribers of ill-formed message')

# Agent unit test

def testAgent():

    reportHeader('Agent')

    reportSection('activity')
    a1.activity()
    reportDetail('Correctly carried out the activity')
    a1.activity(Concept('A well-formed parameter'))
    reportDetail('Correctly carried out the activity')
    try:
        a1.activity('An ill-formed parameter')
        reportDetailFailure('Parameters are ill-formed')
    except SelfException:
        reportDetail('Correctly denied carrying out activity with ill-formed parameters')
    
    reportSection('start')
    a1.start()
    reportDetail('Correctly started the agent activity')
    a1.start(Concept('A well-formed parameter'))
    reportDetail('Correctly started the agent activity')
    try:
        a1.start('An ill-formed parameter')
        reportDetailFailure('Parameters are ill-formed')
    except SelfException:
        reportDetail('Correctly denied starting activity with ill-formed parameters')

    reportSection('stop')
    a1.stop()
    reportDetail('Correctly stopped the agent activity')
    a1.stop(Concept('A well-formed parameter'))
    reportDetail('Correctly stopped the agent activity')
    try:
        a1.start('An ill-formed parameter')
        reportDetailFailure('Parameters are ill-formed')
    except SelfException:
        reportDetail('Correctly denied starting activity with ill-formed parameters')

    reportSection('pause')
    a1.pause()
    reportDetail('Correctly paused the agent activity')
    a1.pause(Concept('A well-formed parameter'))
    reportDetail('Correctly paused the agent activity')
    try:
        a1.start('An ill-formed parameter')
        reportDetailFailure('Parameters are ill-formed')
    except SelfException:
        reportDetail('Correctly denied starting activity with ill-formed parameters')

    reportSection('isAlive')
    if a1.isAlive():
        reportDetail('Correctly checked that agent is alive')
    else:
        reportDetailFailure('Agent is not alive')

    reportSection('status')
    if a1.status().name == 'Status':
        reportDetail('Correctly checked agent status')
    else:
        reportDetailFailure('Agent status is wrong')

    reportSection('signal')
    a1.signal(Concept('A well-defined source'), Concept('A well-defined message'))
    reportDetail('Correctly signaled the agent')
    a1.signal(Concept('A well-defined source'), Concept('A well-defined message'), Concept('A well-defined parameter'))
    reportDetail('Correctly signaled the agent')
    try:
        a1.signal('An ill-defined source', Concept('A well-defined message'), Concept('A well-defined parameter'))
        reportDetailFailure('Source is ill-defined')
    except SelfException:
        reportDetail('Correctly denied connecting with ill-defined source')
    try:
        a1.signal(Concept('A well-defined source'), 'An ill-defined message', Concept('A well-defined parameter'))
        reportDetailFailure('Message is ill-defined')
    except SelfException:
        reportDetail('Correctly denied connecting with ill-defined message')
    try:
        a1.signal(Concept('A well-defined source'), Concept('A well-defined message'), 'An ill-defined parameter')
        reportDetailFailure('Parameters are ill-defined')
    except SelfException:
        reportDetail('Correctly denied connecting with ill-defined parameters')

    reportSection('connect')
    a1.connect(Relationship('A well-defined relationship', a1, a2))
    reportDetail('Correctly connected the agent')
    a1.connect(Relationship('A well-defined relationship', a1, a2), Concept('A well-formed parameter'))
    reportDetail('Correctly connected the agent')
    try:
        a1.connect('An ill-formed relationship', Concept('A well-formed parameter'))
        reportDetailFailure('Channel is ill-formed')
    except SelfException:
        reportDetail('Correctly denied connecting with ill-formed channel')
    try:
        a1.connect(Relationship('A well-formed relationship', a1, a2), 'An ill-formed parameter')
        reportDetailFailure('Parameters are ill-defined')
    except SelfException:
        reportDetail('Correctly denied connecting wiht ill-formed parameters')

# Test all of Self's foundational classes

arguments = parseArguments()

testConcept()
testProperty()
testRelationship()
testOntology()
testBlackboard()
testAgent()

# Clean up the output stream if reporting concisely

if arguments.concise == True:
  print()
