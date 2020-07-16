'''
inherent_concepts

This module declares Self's inherent concepts:

    Meta Organizational

        Model
        Theory
        Society
        Layer
        Subsystem
        System

    Identification

        Identity
        
        AliasFor
        IsA

    Classification

        AKindOf
        SimilarTo
        UnlikeA
       
    Role

        Event/Action/Occurrence
        State/Condition
        Operator
        Instrument
        Operand
        Resource
        Input/Sensor
        Output/Acutator
        InputOutput/SensorActuator

    Compositional

        ComponentOf/PartOf
        ElementOf
        MaterialOf
        MemberOf
        PortionOf
        
    Spatial

        Location
        Position
        Orientation
        
        Location
        HasContactWith
        HasNoContactWith
        InteractsWith
        NoInteractionWith
        EnclosesA
        IntersectsA
        PlacementIn
        PlacementWith

    Temporal

        Date
        Time
        DateTime

        Before
        After
        CoOccurs
        
    Causal

        Goal/Aim/Purpose/Reason
        Cause/Stimuli/Factor
        Consequence/Result/Response/Effect

        PreconditionOf
        ConstraintOn
        
    Relational

        Weight
        Directed
        
        Describes/Represents/Specifies
        Realizes
        Satisfies
        Delivers
        Influences
        Encourages
        Inhibits
        
    Blackboard

        Publication
        Subscription

    Agent
    
        Source
        Message
        Parameters
        Channel
        Status
'''

from self_concepts import Concept
from self_concepts import Property
from self_concepts import Relationship
from self_concepts import Ontology
from self_concepts import Blackboard
from self_concepts import Agent
from self_concepts import SelfException

# Meta organizational

class Model(Ontology): pass                 # Collection of ontologies capturing past/current state
class Theory(Ontology): pass                # Collection of ontologies capturing potential/future state
class Society(Ontology): pass               # Collection of collaborating agents
class Layer(Ontology): pass                 # Collection of societies, all at the same level of abstraction
class Subsystem(Ontology): pass             # Collection of ontologies, agents, and blackboards
class System(Ontology): pass                # Collection of subsystems that form a whole

# Identification

class Identity(Property): pass              # Internal/secret name for a concept

class AliasFor(Relationship): pass          # Alternate for a concept
class IsA(Relationship): pass               # Concept is an instance of another concept

# Classification

class AKindOf(Relationship): pass           # Concept is a subclass of another concept
class SimilarTo(Relationship): pass         # Concept shares characteristics of another concept
class UnlikeA(Relationship): pass           # Concept has characteristics orthogonal to another concept

# Role

class Event(Concept): pass                  # Instance in time/space, typically demarking state change
Action = Event                              # Alias to Event
Occurrence = Event                          # Alias to Event
class State(Concept): pass                  # Instance or region in landscape of n-dimensional potentials
Condition = State                           # Alias to State
class Operator(Concept): pass               # Instigator of stateless/stateful activity
class Operand(Concept): pass                # Target of stateless/stateful activity
class Instrument(Concept): pass             # Mechanism contributing to stateless/stateful activity
class Resource(Concept): pass               # Finite/infinite material used for stateless/stateful activity
class Input(Concept): pass                  # Signal entering system boundary
Sensor = Input                              # Alias to Input
class Output(Concept): pass                 # Signal leaving system boundary
Actuator = Output                           # Alias to Output
class InputOutput(Concept): pass            # Signal entering and leaving system boundary
SensorActuator = InputOutput                # Alias to InputOutput

# Compositional

class ComponentOf(Relationship): pass       # Concept is structural part of another concept
PartOf = ComponentOf                        # Alias to ComponentOf
class ChildOf(Relationship): pass           # Concept is product of another concept
class ElementOf(Relationship): pass         # Concept is functional part of another concept
class MaterialOf(Relationship): pass        # Concept is elemental part of another concept
class MemberOf(Relationship): pass          # Concept is community member of another concept
class PortionOf(Relationship): pass         # Concept is quantifiable member of another concept

# Spatial

class Location(Property): pass              # Named place in logical or physical space
class Position(Property): pass              # Instance or region in landscape of three-dimensional space
class Orientation(Property): pass           # Absolute or relative direction in three-dimensional space

class HasContactWith(Relationship): pass    # Concept has direct connection to another concept
class HasNoContactWith(Relationship): pass  # Concept has no direct connection to another concept
class InteractsWith(Relationship): pass     # Concept has collaborative connection with another concept
class NoInteractionWith(Relationship): pass # Concept has no collabortive connection with another concept
class EnclosesA(Relationship): pass         # Concept contains another concept
class IntersectsA(Relationship): pass       # Concept intersects another concept
class PlacementIn(Relationship): pass       # Absolute position and/or orientation within another concept
class PlacementWith(Relationship): pass     # Relative postion and/or orientation to another concept

# Temporal

class Date(Property): pass                  # Absolute or relative date
class Time(Property): pass                  # Absolute or relative time
class DateTime(Property): pass              # Date and Time

class Before(Relationship): pass            # Concept precedes another concept in time
class After(Relationship): pass             # Concept follows another concept in time
class CoOccurs(Relationship): pass          # Concept is concurrent with another concept in time

# Causal

class Goal(Concept): pass                   # Desired state
Aim = Goal                                  # Alias to Goal
Purpose = Goal                              # Alias to Goal
Reason = Goal                               # Alias to Goal
class Cause(Concept): pass                  # Precipitating concept
Stimuli = Cause                             # Alias to Cause
Factor = Cause                              # Alias to Cause
class Consequence(Concept): pass            # Outcome of some causal chain
Result = Consequence                        # Alias to Consequence
Response = Consequence                      # Alias to Consequence
Effect = Consequence                        # Alias to Consequence

class PreconditionnOf(Relationship): pass   # Concept depends on another concept in some causal chain
class ConstraintOn(Relationship): pass      # Concept opposes another concept in some causal chain

# Relational

class Weight(Property): pass                # Edge property representing value-based qualification
class Directed(Property): pass              # Edge property representing directionality

class Describes(Relationship): pass         # Concept describes another concept
Represents = Describes                      # Alias to Describes
Specifies = Describes                       # Alias to Describes
class Realizes(Relationship): pass          # Concept makes manifest another concept
class Satisfies(Relationship): pass         # Concept meets the conditions of another concept
class Delivers(Relationship): pass          # Concept makes manifest a concept for another concept
class Influences(Relationship): pass        # Concept encourages or inhibits another concept
class Encourages(Relationship): pass        # Concept promotes activity of another concept
class Inhibits(Relationship): pass          # Concept discourages activity of another concept

# Blackboard concepts

class Publication(Relationship): pass       # Reification of publication or withdrawing
class Subscription(Relationship): pass      # Reification of subscribing or unsubscribing

# Agent-related concepts

class Source(Concept): pass                 # Reification of signal source
class Message(Concept): pass                # Reification of signal message
class Parameters(Concept): pass             # Reification of agent method parameters
class Channel(Concept): pass                # Reification of connection path
class Status(Concept): pass                 # Reification of agent state
