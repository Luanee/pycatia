#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""

from pycatia.mec_mod_interfaces.tri_dim_feat_edge import TriDimFeatEdge


class RectilinearTriDimFeatEdge(TriDimFeatEdge):
    """
        .. note::
            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     InfInterfaces.Reference
                |                         MecModInterfaces.Boundary
                |                             MecModInterfaces.Edge
                |                                MecModInterfaces.TriDimFeatEdge
                |                                     RectilinearTriDimFeatEdge
                | 
                | 1-D boundary belonging to a feature whose topological result is three
                | dimensional, the boundary having a rectilinear geometry.
                | Role: This Boundary object may be, for example, the edge of a Pad resulting
                | from the extrusion of a square.
                | You will create a RectilinearTriDimFeatEdge object using the Shapes.GetBoundary
                | , HybridShapes.GetBoundary , Sketches.GetBoundary or Selection.SelectElement2
                | method. Then, you pass it to the operator (such as Hole.SetDirection
                | ).
                | The lifetime of a RectilinearTriDimFeatEdge object is limited, see
                | Boundary.
                | 
                | Example:
                |     This example asks the end user to select a face, a rectilinear edge, and
                |     creates a hole. The rectilinear edge specifies the hole direction. It may be a
                |     RectilinearTriDimFeatEdge, a RectilinearBiDimFeatEdge or a
                |     RectilinearMonoDimFeatEdge.
                | 
                |      Dim EnabledObjectSelection1(0)
                |      Dim EnabledObjectSelection2(2)
                |      Set Document = CATIA.ActiveDocument
                |      Set Selection = Document.Selection
                |      'We propose to the user that he select a face
                |      EnabledObjectSelection1(0)="Face"
                |      Status=Selection.SelectElement2(EnabledObjectSelection1,"Select a
                |      face",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set Face = Selection.Item(1).Value
                |      Selection.Clear
                |      'We propose to the user that he select the hole direction
                |      EnabledObjectSelection2(0)="RectilinearTriDimFeatEdge"
                |      EnabledObjectSelection2(1)="RectilinearBiDimFeatEdge"
                |      EnabledObjectSelection2(2)="RectilinearMonoDimFeatEdge"
                |      Status=Selection.SelectElement2(EnabledObjectSelection2,"Select the hole
                |      direction",true)
                |      if (Status = "cancel") then Exit Sub
                |      Set Hole = ShapeFactory.AddNewHoleFromPoint(20.0,-5.5, 1.07,Face,10.0)
                |      Hole.ThreadingMode = 1
                |      Hole.ThreadSide = 0
                |      Hole.SetDirection Selection.Item(1).Value
                |      Document.Part.Update
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.rectilinear_tri_dim_feat_edge = com_object

    def get_direction(self, o_direction: tuple) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetDirection(CATSafeArrayVariant oDirection)
                | 
                |     Returns the direction of the rectilinear edge
                | 
                |     Parameters:
                | 
                |         oDirection[0]
                |             The X Coordinate of the direction 
                |         oDirection[1]
                |             The Y Coordinate of the direction 
                |         oDirection[2]
                |             The Z Coordinate of the direction

        :param tuple o_direction:
        :return: None
        :rtype: None
        """
        return self.rectilinear_tri_dim_feat_edge.GetDirection(o_direction)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_direction'
        # # vba_code = """
        # # Public Function get_direction(rectilinear_tri_dim_feat_edge)
        # #     Dim oDirection (2)
        # #     rectilinear_tri_dim_feat_edge.GetDirection oDirection
        # #     get_direction = oDirection
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def get_origin(self, o_origin: tuple) -> None:
        """
        .. note::
            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub GetOrigin(CATSafeArrayVariant oOrigin)
                | 
                |     Returns the origin of the the rectilinear edge.
                | 
                |     Parameters:
                | 
                |         oOrigin[0]
                |             The X Coordinate of the rectilinear edge origin 
                |         oOrigin[1]
                |             The Y Coordinate of the rectilinear edge origin 
                |         oOrigin[2]
                |             The Z Coordinate of the rectilinear edge origin

        :param tuple o_origin:
        :return: None
        :rtype: None
        """
        return self.rectilinear_tri_dim_feat_edge.GetOrigin(o_origin)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'get_origin'
        # # vba_code = """
        # # Public Function get_origin(rectilinear_tri_dim_feat_edge)
        # #     Dim oOrigin (2)
        # #     rectilinear_tri_dim_feat_edge.GetOrigin oOrigin
        # #     get_origin = oOrigin
        # # End Function
        # # """

        # # system_service = SystemService(self.application.SystemService)
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'RectilinearTriDimFeatEdge(name="{self.name}")'
