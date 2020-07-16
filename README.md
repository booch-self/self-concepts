# self-concepts
Self's foundational abstractions.

<a href="https://github.com/booch-self">Self</a> is a hybrid neuro/symbolic architecture for AGI. At its foundation are seven abstractions upon which all of Self's structure and behavior are built: Concept, Property, Relationship, Ontology, Blackboard, and Agent (plus one more meta abstraction, SelfException). Together with these abstractions are a set of inherent concepts, each of which builds on the foundational abstractions and collectively which provide a common vocabulary at a slightly higher level of abstraction for the purpose of making various important systemic patterns manifest. All of these abstractions are implemented in several different programming languages (<a href="https://github.com/booch-self/self-concepts/tree/master/source/python">Python</a>, <a href="https://github.com/booch-self/self-concepts/tree/master/source/java">Java</a>, and <a href="https://github.com/booch-self/self-concepts/tree/master/source/c++">C++</a>) as well as a set of <a href="https://github.com/booch-self/self-concepts/tree/master/microservices">microservices</a> (which may be deployed to any containerized platform that runs in the cloud as well as on the edge, all orchestrated by Kubernetes). Unit tests for these abstractions may be found <a href="https://github.com/booch-self/self-concepts/tree/master/tests">here</a>.
  
A Slack channel for this project resides at <a href="https://booch-self.slack.com">https://booch-self.slack.com</a>
  
## Architectural Principles
  
There several design decisions that shape the architecture of Self's foundational abstractions.

* Self is a platform for embodied cognition.

* Self serves to orchestrate symbolic and neural models of computation.

* Self builds upon Minsky's concept of a society of mind.

* Self builds on Brooks' concept of intelligence without representation.

* Self balances the explicit repersentation of information with the implicit behavior of stateless and stateful agency, while at the same time, within a system, assuming that information may be incomplete, inconsistent, multi-representational, and even sometimes wrong, and that agency may be deterministic, opportunistic, and even sometimes random.

* Self is designed with abstractions that fold back into themselves, permiting the explicit design of strange loops.

* Self is design for scale, with a clear separation of concerns between logical and physical mechanisms.

-- link to Minsky paper
-- link to Brook's paper
-- link to ontology paper (https://bib.irb.hr/datoteka/314767.174.pdf)
  
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
  
Concept is Self's central abstraction. Everything is a Concept (and even a Concept is considered to be a kind of Concept). The primary responsibilities of a Concept are to name an abstraction and to define its characteristics.

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

### SelfException

SelfException is a class whose instances are used to report on Concepts that are not well-formed or that behave badly. The primary responsibility of a SelfException is to name the dysfunctional behavior.

    attribute:
    
        errorMessage

The attribute is public. Type checking of the error message is not enforced.


## Inherent Concepts

There are eighty abstractions organized in eleven categories that build on Self's foundational abstractions and collectively which provide a common vocabulary at a slightly higher level of abstraction for the purpose of making various important systemic patterns manifest.

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

<img src="/Documentation/Images/inherent_concepts.png" alt="inherent_concepts">

### Meta Organizational

    Model
    Society
    Layer
    Subsystem
    System

Model is an Ontology representing past/current state.

Theory is an Ontology representing potential/future state.

Society is an Ontology representing a collection of collaborating agents.

Layer is an Ontology representing a collection of societies, all at the same level of abstraction

Subsystem is an Ontology representing a collection of ontologies, agents, and blackboards.

System is an Ontology representing a collection of subsystems that form a whole.

### Identification

    Identity
    
    AliasFor
    IsA

Identity is a Property representing an internal/secret name for a concept.

AliasFor is a Relationship representing an alternate for a concept.

IsA is a Relationship representing that a concept is an instance of another concept.

### Classification

    AKindOf
    SimilarTo
    UnlikeA

AKindOf is a Relationship representing that a concept is a subclass of another concept.

SimilarTo is a Relationship representing that a concept shares characteristics with another concept.

UnlikeA is a Relationship representing that a concept has characteristics orthogonal to another concept.

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

Event is a Concept representing an instance in time/space, typically demarking a state change. Action and Occurrence are alias for Event.

State is a Concept representing an instance or region in a landscape of n-dimentional potentials. Condition is an alias for State.

Operator is a Concept representing an instigator of stateless/stateful activity.

Operand is a Concept representing a target of stateless/stateful activity.

Instrument is a Concept representing a mechanism contributing to stateless/stateful activity.

Resource is a Concept representing finite/invinite material used for stateless/stateful activity.

Input is a Concept representing a Signal entering a system boundary. Sensor is an alias for Input.

Output is a Concept representing a Signal leaving a system boundary. Actuator is an alias for Output.

InputOutput is a Concept representing a Signal entering and leaving system boundary. SensorActuator is an alias for InputOutput.

### Compositional

    ComponentOf/PartOf
    ElementOf
    MaterialOf
    MemberOf
    PortionOf

ComponentOf is a Concept representing a structural part of another concept. PartOf is an alias for ComponentOf.

ChildOf is a Concept representing a product of another concept.

ElementOf is a Concept representing a functional part of another concept.

MaterialOf is a Concept representing an elemental part of another concept.

MemberOf is a Concept representing a community member of another concept.

PortionOf is a Concept representing an quantifiable member of another concept.

### Spatial

    Location
    Position
    Orientation
    
    HasContactWith
    HasNoContactWith
    InteractsWith
    NoInteractionWith
    EnclosesA
    PlacementIn
    PlacementWith

Location is a Property representing a named place in logical or physical space.

Position is a Property representing an instance or region in the landscape of three-dimensional space.

Orientation is a Property representing an absolute or relative dirction in three-dimensional space.

HasContactWith is a Relationship representing a concept has direct connection to another concept.

HasNoContactWith is a Relationship representing a concept has no direct contact to another concept.

InteractsWith is a Relationship representing collaborative connection with another concept.

NoInteractionWith is a Relationship representing no collaborative connection with another concept.

EnclosesAs is a Relationship representing concept contains another concept.

Intersects is a Relationship representing concept intersects another concept.

PlacementIn is a Relationship representing an absolute or relative position and/or orientation within another concept.

PlacementWith is a Relationship representing an absolute or relative position and/or orientation to another concept.

### Temporal

    Date
    Time
    DateTime
    
    Before
    After
    CoOccurs

Date is a Property representing an absolute or relative date.

Time is a Property representing an absolute or relative time.

DateTime is a Property representing a date and time.

Before is a Relationship representing a concept precedes another concept in time.

After is a Relationship representing a concept follows another concept in time.

CoOccurs is a Relationship representing a concept is concurrent with another concept in time.

### Causal

    Goal/Aim/Purpose/Reason
    Cause/Stimuli/Factor
    Consequence/Result/Response/Effect
    
    PreconditionOf
    ConstraintOn

Goal is  a Concept representing a desired state. Aim, Purpose, and Reason are aliases for Goal.

Cause is a Concept representing a precipitating concept. Stimuli and Factor are aliases for Cause.

Consequence is a Concept reprsenting the outcome of some causal chain. Result, Response, and Effect are aliases for Consequence.

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

Weight is a Property of a Relationship edge, representing a value-based qualification.

Directed is a Property of a Relationship edge, representing directionality.

Describes is a Relationship representing a concept that describes another concept. Represents and Specifies are aliases for Describes.

Realizes is a Relationship representing a concept that makes manifest another concept.

Satisfies is a Relationship representing a concept that meets the conditions of another concept.

Delivers is a Relationship representing a concept that makes manifest a concept for another concept.

Influences is a Relationshp representing a concept that encourages or inhibits another concept.

Encourages is a Relationship representing a concept that promotes the activity of another concept.

Inhibits is a Relationshp representing a concept that discourages the activity of another concept.

### Blackboard

    Publication
    Subscription

Publication is a Relationship representing the reification of an agent publishing or withdrawing a concept.

Subscription is a Relationship representing the reification of an agent subscribing or unsubscribing a concept or a concept class.

### Agent

    Source
    Message
    Parameters
    Channel
    Status

Source is a Concept representing the reification of a signal source.

Message is a Concept representing the reification of a signal message.

Parameters is a Concept representing the reification of agent method parameters.

Channel is a Concept representing the reification of a connection path.

Status is a Concept representing the reification of agent state.
