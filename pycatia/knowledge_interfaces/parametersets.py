#! /usr/bin/python3.6
# module initially auto generated using V5Automation.chm from CATIA V5 R25

from pycatia.knowledge_interfaces.parameterset import ParameterSet
from pycatia.system_interfaces.collection import Collection


class ParameterSets(Collection):
    """
        .. note::
            CAA V5 Visual Basic help

                | Represents a collection of parameter sets.The ParameterSet object is a
                | neutral object that contains parameters, like the Parameters node in
                | the specification tree.
                |
                | The following example shows how to retrieve it
                | on a part:
                | Dim CATDocs As Documents
                | Set CATDocs = CATIA.Documents
                | Dim part1 As Document
                | Set part1 = CATDocs.Add("CATPart")
                | Dim parameters1 As Parameters
                | Set parameters1 = part1.Part.Parameters
                | Dim ParameterSet1 As ParameterSet
                | Set ParameterSet1 = parameters1.RootParameterSet
                | Dim parameterSets1 As ParameterSets
                | Set parameterSets1 = parameter.Set1.ParameterSets
                |
                | This collection is not a collection of all parameter sets of a document, but a collection of
                | all parameter sets in the current parameter set.

    """

    def __init__(self, com_object):
        super().__init__(com_object, child_object=ParameterSet)
        self.parameter_sets = com_object

    def create_set(self, i_name):
        """
        .. note::
            CAA V5 Visual Basic help

                | CreateSet
                | o Func CreateSet( CATBSTR iName) As ParameterSet
                |
                | Creates a set of parameters and appends it to the parameter set which
                | corresponds to this collection.

        """
        return self.child_object(self.parameter_sets.CreateSet(i_name))

    def item(self, i_index):
        """
        .. warning::

            The index when not a string must be it's python index (indexes in python start from 0).
            collection. The COM interface index starts at 1.

        .. note::
            CAA V5 Visual Basic help

                | Item
                | o Func Item( CATVariant iIndex) As ParameterSet
                |
                | Returns a parameter set using its index or its name from the
                | ParameterSets collection.
                |
                | Parameters:
                | iIndex
                |    The index or the name of the parameter set to retrieve from
                |    the collection of parameter sets.
                |    As a numeric, this index is the rank of the parameter set
                |    in the collection.
                |    The index of the first parameter set in the collection is 1, and
                |    the index of the last parameter set is Count.
                |    As a string, it is the name you assigned to the parameter set using
                |    the
                |
                |  activateLinkAnchor('AnyObject','Name','AnyObject.Name')  property .
                |
                | Examples:
                | This example retrieves the parameter set named "Parameters.1" in the parameterSets
                | collection:
                |
                | Set theSet = parameterSets.Item("Parameters.1")

        :return: ParameterSet()
        """

        if isinstance(i_index, int):
            i_index += 1

        return self.child_object(self.parameter_sets.Item(i_index))

    def __repr__(self):
        return f'ParameterSets(name="{self.name}")'
