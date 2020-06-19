'''
self_concepts
This module declares Self's foundational abstractions: Concept, Property, Relationship, and Ontology.
'''

class Concept:
    '''Concept is Self's central abstraction: everything is a Concept (and were Python to permit the self-reference as did Smalltalk-80, even a Concept would be declared as a kind of Concept). A Concept defines a name and a set of Properties.'''

    def __init__(self, name):
        self.name = name
        self.properties = set()

class Property(Concept):
    '''A Property is a Concept defining a name/value pair, where a value is a literal or a Concept.'''

    def __init__(self, name, value):
        Concept.__init__(self, name)
        self.value = value

class Relationship(Concept):
    '''A Relationship is a Concept defining the connection between two other Concepts, each end of which may have its own Properties.'''

    def __init__(self, name):
        Concept.__init__(self, name)
        self.node1 = Concept()
        self.node2 = Concept()
        self.node1Properties = set()
        self.node2Properties = set()

class Ontology(Concept):
    '''An Ontology is a set of Concepts together with their Relationships.'''

    def __init__(self, name):
        Concept.__init__(self, name)
        self.concepts = set()
        self.relationships = set()
