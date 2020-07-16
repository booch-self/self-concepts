# self-concepts
Self's foundational abstractions.

<a href="https://github.com/booch-self">Self</a> is a hybrid neuro/symbolic architecture for AGI. At its foundation are seven abstractions upon which all of Self's structure and behavior are built: Concept, Property, Relationship, Ontology, Blackboard, and Agent (plus one more meta abstraction, SelfException). Together with these abstractions are a set of inherent concepts, each of which builds on these seven foundational abstractions and collectively which provide a common vocabulary at a slightly higher level of abstraction for the purpose of making various important systemic patterns manifest. All of these abstractions are implemented in several different programming languages (<a href="https://github.com/booch-self/self-concepts/tree/master/source/python">Python</a>, <a href="https://github.com/booch-self/self-concepts/tree/master/source/java'>Java</a>, and <a href="https://github.com/booch-self/self-concepts/tree/master/source/c++">C++</a>) as well as a set of <a href="https://github.com/booch-self/self-concepts/tree/master/microservices">microservices</a> (which may be deployed to any containerized platform that runs in the cloud as well as on the edge, all orchestrated by Kubernetes). Unit tests for these abstractions may be found <a href="https://github.com/booch-self/self-concepts/tree/master/tests">here</a>.
  
A Slack channel for this project resides at <a href="https://booch-self.slack.com">https://booch-self.slack.com</a>
  
## Architectural Principles
  
TBD
  
## Self Concepts

There are seven abstractions upon which all of Self's structure and behavior are built.

    Concept
    Property
    Relationship
    Ontology
    Blackboard
    Agent
    
    SelfException
    
<img src="/Documentation/Images/self_concepts.png" alt="self_concepts">

### Concept
  
Concept is Self's central abstraction. Everything is a Concept (and a Concept is conidered to be a kind of Concept). The primary responsibilities of a Concept are to name an abstraction and to define its characteristics.

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

Attributes are protected so as to ensure a proper separation of concerns between interface and implementation. Type checking of names is not enforced; type checking of properties and property classes are strictly enforced.

### Property

Property is a Concept defining a name/value pair. Dictionaries are a common way of representing key/value pairs, but Property is a subtly different abstraction: a Property reifies a name/value relationship, making it possible to define different Property classes and to manipulate individual Property instances. The primary responsibility of a Property is to define some characteristic of another Concept

   attributes:

        value

 The attribute is protected so as to ensure a proper separation of concerns between interface and implementation. Type checking of value is not enforced.

### Relationship

Relationship is a Concept defining the connection between two other Concepts or Concept classes, each edge of which may have its own Properties. The primary responsibility of a Relationship is to define the meaning of how two Concepts or Concept classes are connected to one another.

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

Attributes are protected so as to ensure a proper separation of concerns between interface and implementation. Type checking of edges, properties, and property classes are strictly enforced.

### Ontology

Ontology is a Concept defining a collection of Concepts together with their Relationships. An Ontology is guaranteed to be closed (a Relationship can only refer to a Concept that is part of that Ontology) and complete (a Relationship cannot have a dangling edge). An Ontology is sometimes ephemeral (meaning that its state persists only for the lifetime of its parent) but most often is meant to define a more permanant artifact (one whose state persists across time). The primary responsiblities of an Ontology are to define the vocabulary, the meaning, and/or the state of particular domain.

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

Attributes are protected so as to ensure a proper separation of concerns between interface and implementation. Type checking of concepts, relationships, concept classes, and relationship classes is strictly enforced.
    '''

### Blackboard

Blackboard is a Concept defining a collection of Concepts, each of which is published by an Actor and each to which an Actor may subscribe, such that the publisher and/or the subscriber can be signaled about interesting events concerning that Concept. An Actor may subscribe to a Concept class, such that when an instance of that Concept class is published by some Actor, a subscription to that Concept is made manifest. A Blackboard is guaranteed to be closed subscriptions can only refer to a Concept or a Concept class that is part of the Blackboard). A Blackboard is generally ephemeral (meaning that its state persists only for the lifetime of its parent). The primary responsibility of a Blackboard is to define a bounded context for a society of Actors who wish to collaborate around the state space of a shared collection of Concepts.

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

Attributes are protected so as to ensure a proper separation of concerns between interface and implementation. Type checking of concepts, concept classes, publications, and subscriptions are strictly enforced.

### Agent

Agent is a Concept defining a self-directed locus of activity. An Agent is an actor that has identify (it can be distinguished among all other Agents), agency (within its bounded context, it exhibits independent activity), concurrency (it carries out its activity in parallel with all other Agents), and state (it can act and react to as well as alter the state of its contex and/or its internal condition). Agents are typically organized into societies that collaborate with one another around the state space of a shared collection of Concepts as defined by a Blackboard; those societies of agents are typically further organized into nearly independent, hierarchical layers. Agents may communicate directly with one another via synchronous and/or asynchronous channels. An Agent is partly emphemeral (meaning that its state is vibrantly active during its lifetime) and partly permanant (meaning that some internal state may be preserved across invocations of the Agent). The concurrent behavior of an Agent is made manifest at deployment; at the logical level, an Agent neither assumes nor provides any intrinsic mechanisms for threading or for synchronization. The primary responsibility of an Agent is to reify an independent activity.

        methods:

            activity

            start
            stop
            pause

            isAlive
            status

            signal
            connect

This base class serves to define the essence of every well-formed Agent. As such, its specification is minimal; it is expected to have subclasses that provide attributes, implementations of these base methods, and additional methods. Type checking of parameters, sources, messages, and channels are strictly enforced.

## Inherent Concepts

There are sixty-three abstractions organized in eleven categories that build on Self's foundational abstractions and collectively which provide a common vocabulary at a slightly higher level of abstraction for the purpose of making various important systemic patterns manifest.

    Meta Organizational
    Identification
    Classification
    Role
    Compositional
    Spatial
    Temporal
    Causal
    Relational
    Blackboard
    Agent

<img src="/Documentation/Images/self_concepts.png" alt="self_concepts">

### Meta Organizational

    Model
    Society
    Layer
    Subsystem
    System

Model is a collection of (typically permanant) ontologies.

Society is a collection of collaborating agents.

Layer is a collection of societies, all at the same level of abstraction

Subsystem is a collection of ontologies, agents, and blackboards.

System is a collection of subsystems that form a whole.

### Identification

    Identity
    
    AliasFor
    IsA
    
### Classification

    AKindOf
    SimilarTo
    UnlikeA
    
### Role

    Event/Action/Occurrence
    State/Condition
    Operator
    Instrument
    Operand
    Resource
    Input/Sensor
    Output/Acutator
    InputOutput

### Compositional

    ComponentOf/PartOf
    ElementOf
    MaterialOf
    MemberOf
    PortionOf

### Spatial

    Location
    Position
    Orientation
        
    Location
    HasContactWith
    HasNoContactWith
    InteractsWith
    NoInteractionWith
    EnclosesA
    PlacementIn
    PlacementWith

### Temporal

    Date
    Time
    DateTime

    Before
    After
    CoOccurs

### Causal

    Goal/Aim/Purpose/Reason
    Cause/Stimuli/Factor
    Consequence/Result/Response/Effect

    PreconditionOf
    ConstraintOn

### Relational

    Weight
    Directed
        
    Describes/Represents/Specifies
    Realizes
    Satisfies
    Delivers
    Influences
    Encourages
    Inhibits

### Blackboard

    Publication
    Subscription

### Agent

    Source
    Message
    Parameters
    Channel
    Status
