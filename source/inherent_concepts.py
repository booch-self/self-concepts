'''
This module declares Self's inherent concepts.
'''

import self_concepts

# Inherent concepts

NULL = self_concepts.Concept("NULL")

# Inherent properties

PARENT = self_concepts.Parent("PARENT", NULL)
CHILD = self_concepts.Parent("CHILD", NULL)

DIRECTED = self_concepts.Parent("DIRECTED", True)
UNDIRECTED = self_concepts.Parent("DIRECTED", False)

WEIGHT = self_concepts.Parent("WEIGHT", 0)


# Inherent relationships


