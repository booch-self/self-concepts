# self-concepts
Self's foundational abstractions.

<img src="/Documentation/Images/self_concepts.png" alt="self_concepts">

<a href="https://github.com/booch-self">Self</a> is a hybrid neuro/symbolic architecture for AGI. At its foundation are seven abstractions upon which all of Self's structure and behavior are built: Concept, Property, Relationship, Ontology, Blackboard, and Agent (plus one more meta abstraction, SelfException). Together with these abstractions are a set of inherent concepts, each of which builds on these seven foundational abstractions and collectively which provide a common vocabulary at a slightly higher level of abstraction for the purpose of making various important systemic patterns manifest. All of these abstractions are implemented in several different programming languages (<a href="https://github.com/booch-self/self-concepts/tree/master/source/python">Python</a>, <a href="https://github.com/booch-self/self-concepts/tree/master/source/java'>Java</a>, and <a href="https://github.com/booch-self/self-concepts/tree/master/source/c++">C++</a>) as well as a set of <a href="https://github.com/booch-self/self-concepts/tree/master/microservices">microservices</a> (which may be deployed to any containerized platform that runs in the cloud as well as on the edge, all orchestrated by Kubernetes). Unit tests for these abstractions may be found <a href="https://github.com/booch-self/self-concepts/tree/master/tests">here</a>.
  
A Slack channel for this project resides at <a href="https://booch-self.slack.com">https://booch-self.slack.com</a>
  
## Architectural Principles
  
TBD
  
## Self Concepts
  
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

TBD

## Inherent Concepts
