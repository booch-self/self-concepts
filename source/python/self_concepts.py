'''
self_concepts

This module declares Self's foundational abstractions:

    Concept
    Property
    Relationship
    Ontology
    Blackboard
    Agent

    SelfException
'''

import inspect

# Concept

class Concept:
    '''Concept is Self's central abstraction. Everything is a Concept (and were Python to
    permit self-referential inheritance as does Smalltalk-80, even a Concept would be declared
    as a kind of Concept). The primary responsibilities of a Concept are to name an
    abstraction and to define its characteristics.

    attributes:

        name
        properties

    methods:

        addProperty
        removeProperty
        removeAllProperties

        propertyExists
        numberOfProperties

        iterateOverProperties

    Attributes are protected and are declared using Python's @property mechanism so as to
    ensure a proper separation of concerns between interface and implementation. Type
    checking of names is not enforced; type checking of properties and property classes are
    strictly enforced.
    '''

    # Class constructor

    def __init__(self,
                 name: 'str'):
        '''Initialize the concept's name and properties.'''

        self._name = name
        self._properties = set()

    # Class attributes

    @property
    def name(self):
        '''Return the concept's name.'''

        return self._name

    @name.setter
    def name(self,
             name: 'str'):
        '''Set the concept's name.'''

        self._name = name

    @property
    def properties(self):
        '''Prohibit direct access to the concept's properties.'''

        raise SelfException('Property may not be directly accessed')
    
    @properties.setter
    def properties(self,
                   properties: 'Property set'):
        '''Prohibit direct assignment to the concept's properties.'''

        raise SelfException('Property may not be directly assigned')

    # Class methods

    def addProperty(self,
                    property: 'Property'):
        '''Add a property to the concept. A concept may have properties that have the same
        name (but distinguished by being different property instances); a concept may have
        properties that are instances of different property classes. An exception is raised
        if the property already exists or if the property is not well-formed.'''

        if isinstance(property, Property):
            if not property in self._properties:
                self._properties.add(property)
            else:
                raise SelfException('Property already exists')
        else:
            raise SelfException('Property is not well-formed')

    def removeProperty(self,
                       property: 'Property'):
        '''Remove a property from the concept. An exception is raised if the property is not
        already part of the concept or if the property is not well-formed.'''

        if isinstance(property, Property):
            try:
                self._properties.remove(property)
            except KeyError:
                raise SelfException('Property does not exist')
        else:
            raise SelfException('Property is not well-formed')
        
    def removeAllProperties(self):
        '''Remove all properties from the concept.'''

        self._properties.clear()

    def propertyExists(self,
                       property: 'Property') -> bool:
        '''Return True if the property is part of the concept. An exception is raised if the
        property is not well-formed.'''

        if isinstance(property, Property):
            return property in self._properties
        else:
            raise SelfException('Property is not well-formed')

    def numberOfProperties(self) -> int:
        '''Return the number of properties that are part of the concept.'''
        
        return len(self._properties)

    def iterateOverProperties(self,
                              function: 'function(Property)',
                              name: 'str' = None,
                              propertyClass: 'Property class' = None):
        '''Apply function to every property that matches the name and property class arguments.
        If neither a name nor a property class are given, iteration will take place over all
        of the concept's properties; if a name is given but a property class is not, iteration
        will take place over all of the concept's properties that have that name, regardless
        of their class; if a name is not given but a property class is, iteration will take
        place across every property that is an instance of that class or its subclass; if both
        a name and a property class are given, iteration will take place across all of the
        concept's properties that have that name and that are an instance of that class or its
        subclass. During iteration, modifying the state of an individual property is safe;
        adding or deleting a property may lead to unexpected results. An exception is raised
        if the property class is not well-formed.'''

        if propertyClass is None:
            if name is None:
                for property in self._properties:
                    function(property)
            else:
                for property in self._properties:
                    if property.name == name:
                        function(property)
        else:
            try:
                if issubclass(propertyClass, Property):
                    if name is None:
                        for property in self._properties:
                            if isinstance(property, propertyClass):
                                function(property)
                    else:
                        for property in self._properties:
                            if (property.name == name
                                and isinstance(property, propertyClass)):
                                function(property)
                else:
                    raise SelfException('Property class is not well-formed')
            except TypeError:
                raise SelfException('Property class is not well-formed')

# Property

class Property(Concept):
    '''Property is a Concept defining a name/value pair. Dictionaries are the pythonic way of
    representing key/value pairs, but Property is a subtly different abstraction: a Property
    reifies a name/value relationship, making it possible to define different Property classes
    and to manipulate individual Property instances. The primary responsibility of a Property
    is to define some characteristic of another Concept.

    attributes:

        value

    The attribute is protected and is declared using Python's @property mechanism so as to
    ensure a proper separation of concerns between interface and implementation. Type checking
    of value is not enforced.
    '''

    # Class constructor

    def __init__(self,
                 name: 'str',
                 value: 'literal or Concept'):
        '''Initialize the property's name and value.'''

        Concept.__init__(self, name)
        self._value = value

    # Class attributes

    @property
    def value(self):
        '''Return the property's value.'''

        return self._value

    @value.setter
    def value(self,
              value: 'literal or Concept'):
        '''Set the property's value.'''
        
        self._value = value

# Relationship

class Relationship(Concept):
    '''A Relationship is a Concept defining the connection between two other Concepts or
    Concept classes, each edge of which may have its own Properties. The primary responsibility
    of a Relationship is to define the meaning of how two Concepts or Concept classes are
    connected to one another.

    attributes:

        edge1
        edge2
        edge1Properties
        edge2Properties

    methods:

        addPropertyToEdge
        removePropertyFromEdge
        removeAllEdgeProperties

        edgePropertyExists
        numberOfEdgeProperties

        iterateOverEdgeProperties

    Attributes are protected and are declared using Python's @property mechanism so as to
    ensure a proper separation of concerns between interface and implementation. Type
    checking of edges, properties, and property classes are strictly enforced.
    '''

    # Class constants
    
    EDGE1 = True
    EDGE2 = False

    # Class constructor

    def __init__(self,
                 name: 'str',
                 edge1: 'Concept or Concept class',
                 edge2: 'Concept or Concept class'):
        '''Initialize the relationship's name, edges, and edge properties.'''

        Concept.__init__(self, name)
        try:
            if (isinstance(edge1, Concept)
                or issubclass(edge1, Concept)):
                self._edge1 = edge1
                self._edge1Properties = set()
            else:
                raise SelfException('Edge is not well-formed')
        except TypeError:
            raise SelfException('Edge is not well-formed')
        try:
            if (isinstance(edge2, Concept)
                or issubclass(edge2, Concept)):
                self._edge2 = edge2
                self._edge2Properties = set()
            else:
                raise SelfException('Edge is not well-formed')
        except TypeError:
            raise SelfException('Edge is not well-formed')

    # Class attributes

    @property
    def edge1(self):
        '''Return edge1.'''

        return self._edge1

    @edge1.setter
    def edge1(self, edge: 'Concept or Concept class'):
        '''Set edge1.'''

        try:
            if (isinstance(edge, Concept)
                or issubclass(edge, Concept)):
                self._edge1 = edge
            else:
                raise SelfException('Edge is not well-formed')
        except TypeError:
            raise SelfException('Edge is not well-formed')

    @property
    def edge2(self):
        '''Return edge2.'''

        return self._edge2

    @edge2.setter
    def edge2(self,
              edge: 'Concept or Concept Class'):
        '''Set edge2.'''

        try:
            if (isinstance(edge, Concept)
                or issubclass(edge, Concept)):
                self._edge2 = edge
            else:
                raise SelfException('Edge is not well-formed')
        except TypeError:
            raise SelfException('Edge is not well-formed')

    @property
    def edge1Properties(self):
        '''Prohibit direct access to the edge's properties.'''

        raise SelfException('Edge properties may not be directly accessed')
    
    @edge1Properties.setter
    def edge1Properties(self,
                        properties: 'Property set'):
        '''Prohibit direct assignement to the edge's properties.'''

        raise SelfException('Edge properties may not be assigned directly')

    @property
    def edge2Properties(self):
        '''Prohibit direct access to the edge's properties.'''
        
        raise SelfException('Edge properties may not be accessed directly')
    
    @edge2Properties.setter
    def edge2Properties(self,
                        properties: 'Property set'):
        '''Prohibit direct assignemtn to the edges' properties.'''
        
        raise SelfException('Edge properties may not be assigned directly')

    # Class methods

    def addEdgeProperty(self,
                        edge: 'bool',
                        property: 'Property'):
        '''Add a property to the given edge. An edge may have properties that have the same
        name (but distinguished by being different property instances); an edge may have
        properties that are instances of different property classes. An exception is raised
        if the property already exists or if the property is not well-formed.'''

        if isinstance(property, Property):
            if edge == Relationship.EDGE1:
                if not property in self._edge1Properties:
                    self._edge1Properties.add(property)
                else:
                    raise SelfException('Edge property already exists')
            else:
                if not property in self._edge2Properties:
                    self._edge2Properties.add(property)
                else:
                    raise SelfException('Edge property already exists')
        else:
            raise SelfException('Edge property is not well-formed')

    def removeEdgeProperty(self,
                           edge: 'bool',
                           property: 'Property'):
        '''Remove a property from the given edge. An exception is raised if the property
        is not already part of the edge or if the property is not well-formed.'''

        if isinstance(property, Property):
            if edge == Relationship.EDGE1:
                try:
                    self._edge1Properties.remove(property)
                except KeyError:
                    raise SelfException('Edge property does not exist')
            else:
                try:
                    self._edge2Properties.remove(property)
                except KeyError:
                    raise SelfException('Edge property does not exist')
        else:
            raise SelfException('Edge property is not well-formed')
        
    def removeAllEdgeProperties(self,
                                edge: 'bool'):
        '''Remove all properties from the given edge'''

        if edge == Relationship.EDGE1:
            self._edge1Properties.clear()
        else:
            self._edge2Properties.clear()

    def edgePropertyExists(self, edge: 'bool',
                           property: 'Property') -> bool:
        '''Return True if the property is part of the given edge. An exception is raised if
        the property is not well-formed.'''

        if isinstance(property, Property):
            if edge == Relationship.EDGE1:
                return property in self._edge1Properties
            else:
                return property in self._edge2Properties
        else:
            raise SelfException('Edge property is not well-formed')

    def numberOfEdgeProperties(self,
                               edge: 'bool') -> int:
        '''Return the number of properties that are part of the given edge.'''

        if edge == Relationship.EDGE1:
            return len(self._edge1Properties)
        else:
            return len(self._edge2Properties)

    def iterateOverEdgeProperties(self,
                                  edge: 'bool',
                                  function: 'function(Property)',
                                  name: 'str' = None,
                                  propertyClass: 'Property class' = None):
        '''Apply function to every property in the given edge that matches the name and
        property class arguments. If neither a name nor a property class are given, iteration
        will take place over all of that edges's properties; if a name is given but a property
        class is not, iteration will take place over all of that edges's properties that have
        that name, regardless of their class; if a name is not given but a property class is,
        iteration will take place across every property of that edge that is an instance of
        that class or its subclass; if both a name and a property class are given, iteration
        will take place across all of the edge's properties that have that name and that are
        an instance of that class or its subclass. During iteration, modifying the state of an
        individual property is safe; adding or deleting a property may lead to unexpected
        results. An exception is raised if the property class is not well-formed.'''

        if propertyClass is None:
            if name is None:
                if edge == Relationship.EDGE1:
                    for property in self._edge1Properties:
                        function(property)
                else:
                    for property in self._edge2Properties:
                        function(property)
            else:
                if edge == Relationship.EDGE1:
                    for property in self._edge1Properties:
                        if property.name == name:
                            function(property)
                else:
                    for property in self._edge2Properties:
                        if property.name == name:
                            function(property)
        else:
            try:
                if issubclass(propertyClass, Property):
                    if name is None:
                        if edge == Relationship.EDGE1:
                            for property in self._edge1Properties:
                                if isinstance(property, propertyClass):
                                    function(property)
                        else:
                            for property in self._edge2Properties:
                                if isinstance(property, propertyClass):
                                    function(property)
                    else:
                        if edge == Relationship.EDGE1:
                            for property in self._edge1Properties:
                                if (property.name == name
                                    and isinstance(property, propertyClass)):
                                    function(property)
                        else:
                            for property in self._edge2Properties:
                                if (property.name == name
                                    and isinstance(property, propertyClass)):
                                    function(property)
                else:
                    raise SelfException('Property class is not well-formed')
            except TypeError:
                raise SelfException('Property class is not well-formed')

# Ontology

class Ontology(Concept):
    '''An Ontology is a Concept defining a collection of Concepts together with their
    Relationships. An Ontology is guaranteed to be closed (a Relationship can only refer to a
    Concept that is part of that Ontology) and complete (a Relationship cannot have a dangling
    edge). An Ontology is sometimes ephemeral (meaning that its state persists only for the
    lifetime of its parent) but most often is meant to define a more permanant artifact
    (one whose state persists across time). The primary responsiblities of an Ontology are to
    define the vocabulary, the meaning, and/or the state of particular domain.

    attributes:

        concepts
        relationships

    methods:

        addConcept
        removeConcept
        removeAllConcepts

        conceptExists
        numberOfConcepts

        iterateOverConcepts

        addRelationship
        removeRelationship
        removeAllRelationships

        relationshipExists
 
        numberOfRelationships

        iterateOverRelationships

        conceptIsBound
        numberOfUnboundConcepts
        numberOfBoundConcepts

        iterateOverUnboundConcepts
        iterateOverBoundConcepts

    Attributes are protected and are declared using Python's @property mechanism so as to
    ensure a proper separation of concerns between interface and implementation. Type
    checking of concepts, relationships, concept classes, and relationship classes is
    strictly enforced.
    '''

    # Class constructor

    def __init__(self,
            name: 'str'):
        ''' Initialize the ontology's name, concepts, and relationships.'''

        Concept.__init__(self, name)
        self._concepts = set()
        self._relationships = set()

    # Class attributes

    @property
    def concepts(self):
        '''Prohibit direct access to the ontology's concepts.'''

        raise SelfException('Concepts may not be accessed directly')

    @concepts.setter
    def concepts(self,
                 concepts: 'Concept set'):
        '''Prohibit direct assignment to the ontology's concepts.'''

        raise SelfException('Concepts may not be assigned directly')

    @property
    def relationships(self):
        '''Prohibit direct access to the ontology's relationships.'''

        raise SelfException('Relationships may not be accessed directly')
    
    @relationships.setter
    def relationships(self,
                      relationships: 'Relationship set'):
        '''Prohibit direct assignment to the ontology's relationships.'''
        
        raise SelfException('Relationships may not be assigned directly')

    # Class methods

    def addConcept(self,
                   concept: 'Concept'):
        '''Add a concept to the ontology. An ontology may have concepts that have the same
        name (but distinguished by being of different concept instances); an ontology may have
        concepts that are instances of different concept classes. An exception is raised
        if the concept already exists or if the concept is not well-formed.'''

        if isinstance(concept, Concept):
            if not concept in self._concepts:
                self._concepts.add(concept)
            else:
                raise SelfException('Concept already exists')
        else:
            raise SelfException('Concept is not well-formed')

    def removeConcept(self,
                      concept: 'Concept'):
        '''Remove a concept from the ontology. An exception is raised if the concept is
        bound by a relationship, if the concept is not already part of the ontology, or if
        the concept is not well-formed.'''

        if not self.conceptIsBound(concept):
            try:
                self._concepts.remove(concept)
            except KeyError:
                raise SelfException('Concept does not exist')
        else:
            raise SelfException('Concept is bound')

    def removeAllConcepts(self):
        '''Remove all concepts from the ontology.'''

        for concept in self._concepts:
            if self.conceptIsBound(concept):
                raise SelfException('Concept is bound')
        self._concepts.clear()   

    def conceptExists(self,
                      concept: 'Concept') -> bool:
        '''Return True if the concept is part of the ontology. An exception is raised if the
        concept is not well-formed.'''

        if isinstance(concept, Concept):
            return concept in self._concepts
        else:
            raise SelfException('Concept is not well-formed')

    def numberOfConcepts(self) -> int:
        '''Return the number of concepts that are part of the ontology.'''

        return len(self._concepts)

    def iterateOverConcepts(self,
                            function: 'function(Concept)',
                            name: 'str' = None,
                            conceptClass: 'Concept class' = None):
        '''Apply function to every concept that matches the name and concept class arguments.
        If neither a name nor a concept class are given, iteration will take place over all
        of the ontology's concepts; if a name is given but a concept class is not, iteration
        will take place over all of the ontology's concepts that have that name, regardless
        of their class; if a name is not given but a concept class is, iteration will take
        place across every concept that is an instance of that class or its subclass; if both
        a name and a concept class are given, iteration will take place across all of the
        ontology's concepts that have that name and that are an instance of that class or its
        subclass. During iteration, modifying the state of an individual concept is safe;
        adding or deleting a concept may lead to unexpected results. An exception is raised
        if the concept class is not well-formed.'''

        if conceptClass is None:
            if name is None:
                for concept in self._concepts:
                    function(concept)
            else:
                for concept in self._concepts:
                    if concept.name == name:
                        function(concept)
        else:
            try:
                if issubclass(conceptClass, Concept):
                    if name is None:
                        for concept in self._concepts:
                            if isinstance(concept, conceptClass):
                                function(concept)
                    else:
                        for concept in self._concepts:
                            if (concept.name == name
                                and isinstance(concept, conceptClass)):
                                function(concept)
                else:
                    raise SelfException('Concept class is not well-formed')
            except TypeError:
                raise SelfException('Concept class is not well-formed')

    def addRelationship(self,
                        relationship: 'Relationship'):
        '''Add a relationship to the ontology. An ontology may have relationships that have
        the same name (but distinguished by being of different relationship instances); an
        ontology may have relationships that are instances of different relationship classes.
        An exeption is raised if the relationship already exists, if the relationship is
        not well-formed, or if the relationship is not closed (meaning that its edges do not
        designate concepts that are not already in the ontology).'''

        if isinstance(relationship, Relationship):
            if not relationship in self._relationships:
                if (relationship.edge1 in self._concepts
                    and relationship.edge2 in self._concepts):
                    self._relationships.add(relationship)
                else:
                    raise SelfException('Relationship is not closed')
            else:
                raise SelfException('Relationship already exists')
        else:
            raise SelfException('Relationship is not well-formed')

    def removeRelationship(self,
                           relationship: 'Relationship'):
        '''Remove a relationship from the ontology. An exception is raised if the
        relationship is not already part of the ontology or if the relationship is not
        well-formed.'''

        if isinstance(relationship, Relationship):
            try:
                self._relationships.remove(relationship)
            except KeyError:
                raise SelfException('Relationship does not exist')
        else:
            raise SelfException('Relationship is not well-formed')

    def removeAllRelationships(self):
        '''Remove all relationships from the ontology.'''

        self._relationships.clear()

    def relationshipExists(self,
                           relationship: 'Relationship') -> bool:
        '''Return True if the relationship is part of the ontology. An exception is raised if
        the relationship is not well-formed.'''

        if isinstance(relationship, Relationship):
            return relationship in self._relationships
        else:
            raise SelfException('Relationship is not well-formed')
       
    def numberOfRelationships(self) -> int:
        '''Return the number of relationships that are part of the ontology.'''

        return len(self._relationships)

    def iterateOverRelationships(self,
                                 function: 'function(Concept)',
                                 name: 'str' = None,
                                 relationshipClass: 'Relationship class' = None):
        '''Apply function to every relationshp that matches the name and relationship class
        arguments. If neither a name nor a relationship class are given, iteration will take
        place over all of the ontology's relationships; if a name is given but a relationship
        class is not, iteration will take place over all of the ontology's relationships
        that have that name, regardless of their class; if a name is not given but a
        relationship class is, iteration will take place across every relationship that is an
        instance of that class or its subclass; if both a name and a relationship class are
        given, iteration will take place across all of the ontology's relationships that have
        that name and that are an instance of that class or its subclass. During iteration,
        modifying the state of an individual relationship is safe; adding or deleting a
        relationship may lead to unexpected results. An exception is raised if the
        relationship class is not well-formed.'''
        
        if relationshipClass is None:
            if name is None:
                for relationship in self._relationships:
                    function(relationship)
            else:
                for relationship in self._relationships:
                    if relationship.name == name:
                        function(relationship)
        else:
            try:
                if issubclass(relationshipClass, Relationship):
                    if name is None:
                        for relationship in self._relationships:
                            if isinstance(relationship, relationshipClass):
                                function(relationship)
                    else:
                        for relationship in self._relationships:
                            if (relationship.name == name
                                and isinstance(relationship, relationshipClass)):
                                function(relationship)
                else:
                    raise SelfException('Relationship class is not well-formed')
            except TypeError:
                raise SelfException('Relationship class is not well-formed')

    def conceptIsBound(self,
                       concept: 'Concept') -> bool:
        '''Return True if the concept is bound by one or more edges of relationships that are
        part of the ontology. An exception is raised if the concept is not well-formed.'''

        if isinstance(concept, Concept):
            for relationship in self._relationships:
                if relationship.edge1 == concept:
                 return True
                if relationship.edge2 == concept:
                    return True
            return False
        else:
            raise SelfException('Concept is not well-formed')

    def numberOfUnboundConcepts(self) -> int:
        '''Return the number of concepts that are not bound by an edges of relationships that
        are part of the ontology.'''

        concepts = self._concepts.copy()
        for relationship in self._relationships:
            concepts.discard(relationship.edge1)
            concepts.discard(relationship.edge2)
        return len(concepts)

    def numberOfBoundConcepts(self) -> int:
        '''Return the number of concepts that are bound by one more more edges of
        relationships that are part of the ontology.'''

        concepts = set()
        for relationship in self._relationships:
            concepts.add(relationship.edge1)
            concepts.add(relationship.edge2)
        return len(concepts)

    def iterateOverUnboundConcepts(self,
                                   function: 'function(Concept)',
                                   name: 'str' = None,
                                   conceptClass: 'Concept class' = None):
        '''Apply function to every unbound concept that matches the name and concept class
        arguments. If neither a name nor a concept class are given, iteration will take
        place over all of the ontology's unbound concepts; if a name is given but a
        concept class is not, iteration will take place over all of the ontology's unbound
        concepts that have that name, regardless of their class; if a name is not given but a
        concept class is, iteration will take place across every unbound concept that is an
        instance of that class or its subclass; if both a name and a concept class are
        given, iteration will take place across all of the ontology's unbound concepts that
        have that name and that are an instance of that class or its subclass. During
        iteration, modifying the state of an individual concept is safe; adding or deleting a
        concept may lead to unexpected results. An exception is raised if the
        concept class is not well-formed.'''        

        if conceptClass is None:
            concepts = self._concepts.copy()
            for relationship in self._relationships:
                concepts.discard(relationship.edge1)
                concepts.discard(relationship.edge2)
            if name is None:
                for concept in concepts:
                    function(concept)
            else:
                for concept in concepts:
                    if concept.name == name:
                        function(concept)
        else:
            try:
                if issubclass(conceptClass, Concept):
                    concepts = self._concepts.copy()
                    for relationship in self._relationships:
                        concepts.discard(relationship.edge1)
                        concepts.discard(relationship.edge2)
                    if name is None:
                        for concept in concepts:
                            if isinstance(concept, conceptClass):
                                function(concept)
                    else:
                        for concept in concepts:
                            if (concept.name == name
                                and isinstance(concept, conceptClass)):
                                function(concept) 
                else:
                    raise SelfException('Concept class is not well-formed')
            except TypeError:
                raise SelfException('Concept class is not well-formed')

    def iterateOverBoundConcepts(self,
                                 function: 'function(Concept)',
                                 name: 'str' = None,
                                 conceptClass: 'Concept class' = None):
        '''Apply function to every bound concept that matches the name and concept class
        arguments. If neither a name nor a concept class are given, iteration will take
        place over all of the ontology's bound concepts; if a name is given but a
        concept class is not, iteration will take place over all of the ontology's bound
        concepts that have that name, regardless of their class; if a name is not given but a
        concept class is, iteration will take place across every bound concept that is an
        instance of that class or its subclass; if both a name and a concept class are
        given, iteration will take place across all of the ontology's bound concepts that
        have that name and that are an instance of that class or its subclass. During
        iteration, modifying the state of an individual concept is safe; adding or deleting a
        concept may lead to unexpected results. An exception is raised if the
        concept class is not well-formed.'''        

        if conceptClass is None:
            concepts = set()
            for relationship in self._relationships:
                concepts.add(relationship.edge1)
                concepts.add(relationship.edge2)
            if name is None:
                for concept in concepts:
                    function(concept)
            else:
                for concept in concepts:
                    if concept.name == name:
                        function(concept)
        else:
            try:
                if issubclass(conceptClass, Concept):
                    concepts = set()
                    for relationship in self._relationships:
                        concepts.add(relationship.edge1)
                        concepts.add(relationship.edge2)
                    if name is None:
                        for concept in concepts:
                            if isinstance(concept, conceptClass):
                                function(concept)
                    else:
                        for concept in concepts:
                            if (concept.name == name
                                and isinstance(concept, conceptClass)):
                                function(concept) 
                else:
                    raise SelfException('Concept class is not well-formed')
            except TypeError:
                raise SelfException('Concept class is not well-formed')

# Blackboard

class Blackboard(Concept):
    '''A Blackboard is a Concept defining a collection of Concepts, each of which is published
    by an Actor and each to which an Actor may subscribe, such that the publisher and/or the
    subscriber can be signaled about interesting events concerning that Concept. An Actor may
    subscribe to a Concept class, such that when an instance of that Concept class is
    published by some Actor, a subscription to that Concept is made manifest. A Blackboard is
    guaranteed to be closed (subscriptions can only refer to a Concept or a Concept class that
    is part of the Blackboard). A Blackboard is generally ephemeral (meaning that its state
    persists only for the lifetime of its parent). The primary responsibility of a Blackboard
    is to define a bounded context for a society of Actors who wish to collaborate around the
    state space of a shared collection of Concepts.

    attributes:

        concepts
        conceptClasses
        publications
        conceptSubscriptions
        classSubcriptions

    methods:

        publishConcept
        unpublishConcept

        publisher
        signalPublisher

        conceptExists
        numberOfConcepts

        iterateOverConcepts

        subscribeToConcept
        unsubscribeFromConcept

        subscribers
        signalSubscribers

        subscribeToConceptClass
        unsubscribeFromConceptClass

        classSubscribers
        signalConceptClassSubscribers

    Attributes are protected and are declared using Python's @property mechanism so as to
    ensure a proper separation of concerns between interface and implementation. Type
    checking of concepts, concept classes, publications, and subscriptions are strictly
    enforced.'''

    # Class constructor

    def __init__(self,
                 name: 'str'):
        '''Initialize the blackboard's name, concept, publications, subscriptions, and class
        subscriptions.'''

        Concept.__init__(self, name)
        self._concepts = set()
        self._publications = set()
        self._conceptSubscriptions = set()
        self._classSubscriptions = set()

    # Class attributes
 
    @property
    def concepts(self):
        '''Prohibit direct access to the blackboard's concepts.'''

        raise SelfException('Concepts may not be directly accessed')

    @concepts.setter
    def concepts(self,
                 concepts: 'Concept set'):
        '''Prohibit direct assignment to the blackboard's concepts.'''

        raise SelfException('Concepts may not be directly assigned')

    @property
    def conceptClasses(self):
        '''Prohibit direct access to the blackboard's concept classes.'''

        raise SelfException('Concepts may not be directly accessed')

    @conceptClasses.setter
    def conceptClasses(self,
                       conceptClasses: 'Concept class set'):
        '''Prohibit direct assignment to the blackboard's concept classes.'''

        raise SelfException('Concept classes may not be directly assigned')

    @property
    def publications(self):
        '''Prohibit direct access to the blackboard's publications.'''

        raise SelfException('Publications may not be directly accessed')

    @publications.setter
    def publications(self,
                     publications: 'Relationship set'):
        '''Prohibit direct assignment to the blackboard's publications.'''

        raise SelfException('Publications may not be directly assigned')
  
    @property
    def conceptSubscriptions(self):
        '''Prohibit direct access to the blackboard's concept subscriptions.'''

        raise SelfException('Subscriptions may not be directly accessed')

    @conceptSubscriptions.setter
    def conceptSubscriptions(self,
                             subscriptions: 'Relationship set'):
        '''Prohibit direct assignment to the blackboard's concept subscriptions.'''

        raise SelfException('Subscriptions may not be directly assigned')

    @property
    def classSubscriptions(self):
        '''Prohibit direct access to the blackboard's concept class subscriptions.'''

        raise SelfException('Class subscriptions may not be directly accessed')

    @classSubscriptions.setter
    def classSubscriptions(self,
                           classSubscriptions: 'Relationship set'):
        '''Prohibit direct assignment to the blackboard's concept class subscriptions.'''

        raise SelfException('Class subscriptions may not be directly assigned')

    # Class methods

    def publishConcept(self,
                       agent: 'Agent',
                       concept: 'Concept'):
        '''Publish a concept to the blackboard. Only an agent can publish a concept; on a
        given blackboard, a concept can only be published by one agent at a time. When a
        concept is published, the publishing agent is signaled that the concept has been
        published; any agent that had previously subscribed to a concept class for which that
        concept is directly or by subclass an instance is subscribed to that instance and is
        signaled that a subscription has been made manifest. A blackboard may have concepts
        that have the same name (but distinguished by being of different concept instances);
        a blackboard may have concepts that are instances of different concept classes. An
        exception is raised if the concept has already been published to the blackboard,
        if the concept is not well-formed, or if the agent is not well-formed.'''

        if isinstance(agent, Agent):
            if isinstance(concept, Concept):
                if not concept in self._concepts:
                    self._concepts.add(concept)
                    publication = Relationship('Published Concept',
                                               agent,
                                               concept)
                    self._publications.add(publication)
                    agent.signal(self, publication)
                    for classSubscription in self._classSubscriptions:
                        if isinstance(concept, classSubscription.edge2):
                            subscription = Relationship('Subscribed To Concept Class Instance',
                                                        classSubscription.edge1,
                                                        concept)
                            self._conceptSubscriptions.add(subscription)
                            classSubscription.edge1.signal(self, subscription)
                else:
                    raise SelfException('Concept already exists')
            else:
                raise SelfException('Concept is not well-formed')
        else:
            raise SelfException('Agent is not well-formed')

    def unpublishConcept(self,
                         concept: 'Concept' = None):
        '''Unpublish a concept from the blackboard. If no concept is given, all of the
        blackboard's concepts are unpublished. When a concept is unpublished, the publishing
        agent is signaled that the concept has been unpublished; any agent that had previously
        subscribed to that concept is unsubscribed and is signaled that the concept has been
        unsubscribed. An exception is raised if the concept does not exist or if the concept
        is not well-formed.'''

        def unpublish(concept: 'Concept'):

            if isinstance(concept, Concept):
                if concept in self._concepts:
                    publicationToRemove = None
                    for publication in self._publications:
                      if publication.edge2 == concept:
                            publicationToRemove = publication
                            break
                    self._concepts.remove(concept)
                    unpublication = Relationship('Unpublished Concept',
                                                publicationToRemove.edge1,
                                                publicationToRemove.edge2)
                    self._publications.remove(publicationToRemove)
                    publicationToRemove.edge1.signal(self, unpublication)
                    subscriptionsToRemove = set()
                    for subscription in self._conceptSubscriptions:
                        if subscription.edge2 == concept:
                            subscriptionsToRemove.add(subscription)
                    for subscription in subscriptionsToRemove:
                        self._conceptSubscriptions.remove(subscription)
                        unsubscription = Relationship('Unsubscribed From Concept',
                                                    subscription.edge1,
                                                    subscription.edge2)
                        subscription.edge1.signal(self, unsubscription)
                else:
                    raise SelfException('Concept does not exist')
            else:
                raise SelfException('Concept is not well-formed')

        if concept == None:
            concepts = self._concepts.copy()
            for concept in concepts:
                unpublish(concept)
        else:
            unpublish(concept)

    def publisher(self,
                  concept: 'Concept') -> Concept:
        '''Return the agent that published the concept. An exception is raised if the
        concept does not exist or if the concept is not well-formed.'''

        if isinstance(concept, Concept):
            if concept in self._concepts:
                for publication in self._publications:
                    if publication.edge2 == concept:
                        return publication.edge1
                raise SelfException('Concept does not exist')
            else:
                raise SelfException('Concept does not exist')
        else:
            raise SelfException('Concept is not well-formed')

    def signalPublisher(self,
                        source: 'Concept',
                        message: 'Concept',
                        concept: 'Concept' = None):
        '''Signal the agent that published the concept. If no concept is given, the
        publishers of every concept currently published to the blackboard are signaled. An
        exception is raised if the given concept does not exist, if the concept is not
        well-formed, if the source is not well-formed, or if the message is not well-formed.'''

        if concept == None:
            if isinstance(source, Concept):
                if isinstance(message, Concept):
                    for publication in self._publications:
                        publication.edge1.signal(source, message)
                else:
                    raise SelfException('Message is not well-formed')
            else:
                raise SelfException('Source is not well-formed')
        else:
            if isinstance(concept, Concept):
                if concept in self._concepts:
                    if isinstance(source, Concept):
                        if isinstance(message, Concept):
                            for publication in self._publications:
                                if publication.edge2 == concept:
                                    publication.edge1.signal(source, message)
                                    return
                        else:
                            raise SelfException('Message is not well-formed')
                    else:
                        raise SelfException('Source is not well-formed')
                else:
                    raise SelfException('Concept does not exist')
            else:
                raise SelfException('Concept is not well-formed')

    def conceptExists(self,
                      concept: 'Concept') -> bool:
        '''Return True if the concept has been published to the blackboard. An exception
        is raised if the concept is not well-formed.'''

        if isinstance(concept, Concept):
            return concept in self._concepts
        else:
            raise SelfException('Concept is not well-formed')

    def numberOfConcepts(self) -> int:
        '''Return the number of concepts that have been published to the blackboard.'''

        return len(self._concepts)

    def iterateOverConcepts(self,
                            function: 'function(Concept)',
                            name: 'str' = None,
                            conceptClass: 'Concept class' = None):
        '''Apply function to every concept that matches the name and concept class
        arguments. If neither a name nor a concept class are given, iteration will take
        place over all of the concepts currently published to the blackboard; if a name is
        given but a concept class is not, iteration will take place over all of the concepts
        currently published to blackboard that have that name, regardless of their class; if
        a name is not given but a concept class is, iteration will take place across every
        concept currently published to the blackboard that is an instance of that class or its
        subclass; if both a name and a concept class are given, iteration will take place
        across every concept currently published to the blackboard that have that name and
        that are an instance of that class or its subclass. During iteration, modifying the
        state of an individual concept is safe; adding or deleting a concept may lead to
        unexpected results. An exception is raised if the concept class is not well-formed.'''

        if conceptClass is None:
            if name is None:
                for concept in self._concepts:
                    function(concept)
            else:
                for concept in self._concepts:
                    if concept.name == name:
                        function(concept)
        else:
            try:
                if issubclass(conceptClass, Concept):
                    if name is None:
                        for concept in self._concepts:
                            if isinstance(concept, conceptClass):
                                function(concept)
                    else:
                        for concept in self._concepts:
                            if (concept.name == name
                                and isinstance(concept, conceptClass)):
                                function(concept)
                else:
                    raise SelfException('Concept class is not well-formed')
            except TypeError:
                raise SelfException('Concept class is not well-formed')

    def subscribeToConcept(self,
                           agent: 'Agent',
                           concept: 'Concept'):
        '''Subscribe to a concept on the blackboard. Only an agent can subscribe to a
        concept; on a given blackboard, a concept can be subscribed to by zero or more agents.
        When a subscription is made manifest, the subscribing agent is signaled that the
        concept has been subscribed to. An exception is raised if the agent has already
        subscribed to the concept, if the concept does not exist, if the agent is not
        well-formed, or if the concept is not well-formed.'''

        if isinstance(agent, Agent):
            if isinstance(concept, Concept):
                if concept in self._concepts:
                    for subscription in self._conceptSubscriptions:
                        if (subscription.edge1 == agent
                            and subscription.edge2 == concept):
                            raise SelfException('Agent is already subscribed')
                    subscription = Relationship('Subscribed To Concept',
                                                agent,
                                                concept)
                    self._conceptSubscriptions.add(subscription)
                    agent.signal(self, subscription)
                else:
                    raise SelfException('Concept does not exist')
            else:
                raise SelfException('Concept is not well-formed')
        else:
            raise SelfException('Agent is not well-formed')

    def unsubscribeFromConcept(self,
                               agent: 'Agent' = None,
                               concept: 'Concept' = None):
        '''Unsubscribe to a concept on the blackboard. If neither an agent nor a concept are
        given, every subscription to every published concept on the blackboard will be
        unsubscribed; if an agent is given but a concept is not, every subscription by that
        agent across every published concept on the blackboard will be unsubscribed; if an
        agent is not given but a concpet is, every subscription to that concept will be
        unsubscribed. When a subscription is withdrawn, the subscribing agent will be signaled
        that the concept has been unsubscribed. An exception is raised if the concept does not
        exist, if the agent is not well-formed, or if the concept is not well-formed.'''
        
        subscriptionsToRemove = set()
        if concept is None:
            if agent is None:
                for subscription in self._conceptSubscriptions:
                    subscriptionsToRemove.add(subscription)
                    unsubscription = Relationship('Unsubscribed From Concept',
                                                  subscription.edge1,
                                                  subscription.edge2)
                    subscription.edge1.signal(self, unsubscription)
            else:
                if isinstance(agent, Agent):
                    for subscription in self._conceptSubscriptions:
                        if subscription.edge1 == agent:
                            subscriptionsToRemove.add(subscription)
                            unsubscription = Relationship('Unsubscribed from Concept',
                                                          subscription.edge1,
                                                          subscription.edge2)
                            subscription.edge1.signal(self, unsubscription)
                else:
                    raise SelfException('Agent is not well-formed')
        else:
            if isinstance(concept, Concept):
                if concept in self._concepts:
                    if agent is None:
                        for subscription in self._conceptSubscriptions:
                            if subscription.edge2 == concept:
                                subscriptionsToRemove.add(subscription)
                                unsubscription = Relationship('Unsubscribed from Concept',
                                                              subscription.edge1,
                                                              subscription.edge2)
                                subscription.edge1.signal(self, unsubscription)
                    else:
                        if isinstance(agent, Agent):
                            for subscription in self._conceptSubscriptions:
                                if (subscription.edge1 == agent
                                    and subscription.edge2 == concept):
                                    subscriptionsToRemove.add(subscription)
                                    unsubscription = Relationship('Unsubscribed From Concept',
                                                                  subscription.edge1,
                                                                  subscription.edge2)
                                    subscription.edge1.signal(self, unsubscription)
                                    break
                        else:
                            raise SelfException('Agent is not well-formed')
                else:
                    raise SelfException('Concept does not exist')
            else:
                raise SelfException('Concept is not well-formed')
        for subscription in subscriptionsToRemove:
            self._conceptSubscriptions.remove(subscription)
                
    def subscribers(self,
                    concept: 'Concept' = None) -> set:
        '''Return the agents that have subscribed to the concept. If no concept is given,
        return the subscribers to every concept currently published to the blackboard. An
        exception is raised if the concept does not exist of if the concept is not
        well-formed.'''

        if concept == None:
            agents = set()
            for subscriber in self._conceptSubscriptions:
                agents.add(subscriber.edge1)
            return agents
        else:
            if isinstance(concept, Concept):
                if concept in self._concepts:
                    agents = set()
                    for subscriber in self._conceptSubscriptions:
                        if subscriber.edge2 == concept:
                            agents.add(subscriber.edge1)
                    return agents
                else:
                    raise SelfException('Concept does not exist')
            else:
                raise SelfException('Concept is not well-formed')

    def signalSubscribers(self,
                          source: 'Concept',
                          message: 'Concept',
                          concept: 'Concept' = None):
        '''Signal the agents that have subscribed to the concept. If no concept is given, the
        subscribers of every concept currently published to the blackboard are signaled. An
        exception is raised if the given concept does not exist, if the concept is not
        well-formed, if the source is not well-formed, or if the message is not well-formed.'''

        if not isinstance(source, Concept):
            raise SelfException('Source is not well-formed')
        if not isinstance(message, Concept):
            raise SelfException('Message is not well-formed')
        if concept == None:
            for subscription in self._conceptSubscriptions:
                subscription.edge1.signal(source, message)
        else:
            if isinstance(concept, Concept):
                if concept in self._concepts:
                    for subscription in self._conceptSubscriptions:
                        if subscription.edge2 == concept:
                            subscription.edge1.signal(source, message)
                else:
                    raise SelfException('Concept does not exist')
            else:
                raise SelfException('Concept is not well-formed')

    def subscribeToConceptClass(self,
                                agent: 'Agent',
                                conceptClass: 'Concept class'):
        '''Subscribe to a concept class. Only an agent can subscribe to a concept class;
        on a given blackboard, a concept class can be subscribed to by one or more agents.
        When an instance of that concept class or its subclasses is published to the
        blackboard, a subscription to that concept class instance is made manifest, and any
        agent that has subscribed to that concept class is signaled that the subscription
        has been made. An exception is raised if the agent is not well-formed or if the
        concept class is not well-formed.'''

        if isinstance(agent, Agent):
            try:
                if issubclass(conceptClass, Concept):
                    for classSubscription in self._classSubscriptions:
                        if (classSubscription.edge1 == agent
                            and classSubscription.edge2 == conceptClass):
                            raise SelfException('Agent is already subscribed')
                    classSubscription = Relationship('Subscribed To Concept Class',
                                                     agent,
                                                     conceptClass)
                    self._classSubscriptions.add(classSubscription)
                    agent.signal(self, classSubscription);
            except TypeError:
                raise SelfException('Concept class is not well-formed')
        else:
            raise SelfException('Agent is not well-formed')

    def unsubscribeFromConceptClass(self,
                                    agent: 'Agent' = None,
                                    conceptClass: 'Concept class' = None):
        '''Unsubscribe from the concept class. If neither an agent nor a concept class are
        given, every subscription to every concept class associated with the blackboard will
        be unsubscribed; if an agent is given but a concept is not, every subscription by that
        agent across every concept class will be unsubscribed; if an agent is not given but a
        concept class is, every subscription to that concept class associated with the
        blackboard will be unsubscribed. When a subscription is withdrawn, the subscribing
        agent will be signaled that the concept class has been unsubscribed. An exception is
        raised if the agent is not well-formed or if the concept class is not well-formed.'''

        subscriptionsToRemove = set()
        if conceptClass is None:
            if agent is None:
                for subscription in self._classSubscriptions:
                    subscriptionsToRemove.add(subscription)
                    unsubscription = Relationship('Unsubscribed From Concept Class',
                                                  subscription.edge1,
                                                  subscription.edge2)
                    subscription.edge1.signal(self, unsubscription)
            else:
                if isinstance(agent, Agent):
                    for subscription in self._classSubscriptions:
                        if subscription.edge1 == agent:
                            subscriptionsToRemove.add(subscription)
                            unsubscription = Relationship('Unsubscribed from Concept Class',
                                                          subscription.edge1,
                                                          subscription.edge2)
                            subscription.edge1.signal(self, unsubscription)
                else:
                    raise SelfException('Agent is not well-formed')
        else:
            try:
                if issubclass(conceptClass, Concept):
                    if agent is None:
                        for subscription in self._classSubscriptions:
                            if subscription.edge2 == conceptClass:
                                subscriptionsToRemove.add(subscription)
                                unsubscription = Relationship(
                                                     'Unsubscribed from concept class',
                                                     subscription.edge1,
                                                     subscription.edge2)
                                subscription.edge1.signal(self, unsubscription)
                    else:
                        if isinstance(agent, Agent):
                            for subscription in self._classSubscriptions:
                                if (subscription.edge1 == agent
                                    and subscription.edge2 == conceptClass):
                                    subscriptionsToRemove.add(subscription)
                                    unsubscription = Relationship(
                                                         'Unsubscribed from concept class',
                                                          subscription.edge1,
                                                          subscription.edge2)
                                    subscription.edge1.signal(self, unsubscription)
                                    break

                        else:
                            raise SelfException('Agent is not well-formed')
                else:
                    raise SelfException('Concept class is not well-formed')
            except:
                raise SelfException('Concept class is not well-formed')
        for subscription in subscriptionsToRemove:
            self._classSubscriptions.remove(subscription)

    def classSubscribers(self,
                         conceptClass: 'ConceptClass' = None):
        '''Return the agents that have subscribed to the concept class. If no concept class is
        given, return the subscribers to every concept class currently associated with the
        blackboard. An exception is raised if the concept class does not exist or if the
        concept class is not well-formed.'''

        if conceptClass == None:
            agents = set()
            for classSubscriber in self._classSubscriptions:
                agents.add(classSubscriber.edge1)
            return agents
        else:
            try:
                if issubclass(conceptClass, Concept):
                    agents = set()
                    for classSubscriber in self._classSubscriptions:
                        if classSubscriber.edge2 == conceptClass:
                            agents.add(classSubscriber.edge1)
                    if len(agents) == 0:
                        raise SelfException('Concept class does not exist')
                    return agents
            except TypeError:
                raise SelfException('Concept class is not well-formed')

    def signalClassSubscribers(self,
                               source: 'Concept',
                               message: 'Concept',
                               conceptClass: 'Concept class' = None):
        '''Signal the agents that have subscribed to the concept class. If no concept class
        is given, the subscribers of every concept class associated with the blackboard are
        signaled. An exception is raised if the given concept class does not exist, if the
        concept class is not well-formed, if the source is not well-formed, or if the
        message is not well-formed.'''

        if not isinstance(source, Concept):
            raise SelfException('Source is not well-formed')
        if not isinstance(message, Concept):
            raise SelfException('Message is not well-formed')
        if conceptClass == None:
            for subscription in self._classSubscriptions:
                subscription.edge1.signal(source, message)
        else:
            try:
                if issubclass(conceptClass, Concept):
                    conceptClassExists = False
                    for subscription in self._classSubscriptions:
                        if subscription.edge2 == conceptClass:
                            conceptClassExists = True
                            subscription.edge1.signal(source, message)  
                    if not conceptClassExists:
                        raise('Concept class does not exist')
                else:
                    raise SelfException('Concept class is not well-formed')
            except TypeError:
                raise SelfException('Concept class is not well-formed')

# Agent

class Agent(Concept):
    '''An Agent is a Concept defining a self-directed locus of activity. An Agent is an actor
    that has identify (it can be distinguished among all other Agents), agency (within its
    bounded context, it exhibits independent activity), concurrency (it carries out its
    activity in parallel with all other Agents), and state (it can act and react to as well as
    alter the state of its contex and/or its internal condition). Agents are typically
    organized into societies that collaborate with one another around the state space of a
    shared collection of Concepts as defined by a Blackboard; those societies of agents are
    typically further organized into nearly independent, hierarchical layers. Agents may
    communicate directly with one another via synchronous and/or asynchronous channels. An
    Agent is partly emphemeral (meaning that its state is vibrantly active during its lifetime)
    and partly permanant (meaning that some internal state may be preserved across invocations
    of the Agent). The concurrent behavior of an Agent is made manifest at deployment; at the
    logical level, an Agent neither assumes nor provides any intrinsic mechanisms for
    threading or for synchronization. The primary responsibility of an Agent is to reify an
    independent activity.

        methods:

            activity

            start
            stop
            pause

            isAlive
            status

            signal
            connect

    This base class serves to define the essence of every well-formed Agent. As such, its
    specification is minimal; it is expected to have subclasses that provide attributes,
    implementations of these base methods, and additional methods. Type checking of parameters,
    sources, messages, and channels are strictly enforced.'''

    # Class constructor

    def __init__(self,
                 name: 'str'):
        '''Initialize the agent's name and start its activity.'''

        Concept.__init__(self, name)

    def activity(self,
                 parameters: 'Concept' = None):
        '''Carry out the agent's essential activity. An exception is raised if the parameters
        are not well-formed.'''

        if not parameters == None:
            if not isinstance(parameters, Concept):
                raise SelfException('Parameters are not well-formed')

        pass

    def start(self,
              parameters: 'Concept' = None):
        '''Start the agent's essential activity. An exception is raised if the parameters are
        not well-formed.'''

        if not parameters == None:
            if not isinstance(parameters, Concept):
                raise SelfException('Parameters are not well-formed')

        pass

    def stop(self,
             parameters: 'Concept' = None):
        '''Stop the agent's essential activity. An exception is raised if the parameters are
        not well-formed.'''

        if not parameters == None:
            if not isinstance(parameters, Concept):
                raise SelfException('Parameters are not well-formed')

        pass

    def pause(self,
              parameters: 'Concept' = None):
        '''Pause the agent's essential activity. An exception is raised if the parameters are
        not well-formed.'''

        if not parameters == None:
            if not isinstance(parameters, Concept):
                raise SelfException('Parameters are not well-formed')

        pass

    def isAlive(self) -> bool:
        '''Return True if the agent is active.'''

        pass

    def status(self) -> Concept:
        '''Return the agent's status.'''

        pass

    def signal(self,
               source: 'Concept',
               message: 'Concept',
               parameters: 'Concept' = None):
        '''Signal the agent with a message. An exception is raised if the source, the message,
        and the parameters are not well-formed.'''

        if not isinstance(source, Concept):
            raise SelfException('Source is not well-formed')
        if not isinstance(message, Concept):
            raise SelfException('Message is not well-formed')
        if not parameters == None:
            if not isinstance(parameters, Concept):
                raise SelfException('Parameters are not well-formed')

        pass

    def connect(self,
                channel: 'Relationship',
                parameters: 'Concept' = None):
        '''Establish a synchronous or asynthronous channel of communication with one or more
        agents. An exception is raised if the channel or the parameters are not well-formed.'''

        if not isinstance(channel, Relationship):
            raise SelfException('Channel is not well-formed''')
        if not parameters == None:
            if not isinstance(parameters, Concept):
                raise SelfException('Parameters are not well-formed')

        pass

# SelfException

class SelfException(Exception):
    '''SelfException is a class whose instances are used to report on Concepts that are not
    well-formed or that behave badly. The primary responsibility of a SelfException is to name
    the dysfunctional behavior.

    attribute:

        errorMessage

    The attribute is public. Type checking of the error message is not enforced.'''

    # Class constructor

    def __init__(self,
                 errorMessage: 'str'):
        '''Initialize the exception's error message.'''
        
        self.exception = errorMessage
