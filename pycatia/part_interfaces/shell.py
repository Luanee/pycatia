#! usr/bin/python3.6
"""
    Module initially auto generated using V5Automation files from CATIA V5 R28 on 2020-06-11 12:40:47.360445

    .. warning::
        The notes denoted "CAA V5 Visual Basic Help" are to be used as reference only.
        They are there as a guide as to how the visual basic / catscript functions work
        and thus help debugging in pycatia.
        
"""
from pycatia.in_interfaces.reference import Reference
from pycatia.in_interfaces.references import References
from pycatia.knowledge_interfaces.length import Length
from pycatia.part_interfaces.dress_up_shape import DressUpShape


class Shell(DressUpShape):
    """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-06-11 12:40:47.360445)

                | System.IUnknown
                |     System.IDispatch
                |         System.CATBaseUnknown
                |             System.CATBaseDispatch
                |                 System.AnyObject
                |                     MecModInterfaces.Shape
                |                         PartInterfaces.DressUpShape
                |                             Shell
                | 
                | Represents the shell shape.
                | A shell shape is made up of a list of faces to process and two thickness
                | parameters.
    
    """

    def __init__(self, com_object):
        super().__init__(com_object)
        self.shell = com_object

    @property
    def external_thickness(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property ExternalThickness() As Length (Read Only)
                | 
                |     Returns the shell external thickness.
                | 
                |     Example:
                |         The following example returns in extThick the external thickness of the
                |         shell firstShell:
                | 
                |          Set extThick = firstShell.ExternalThickness

        :return: Length
        :rtype: Length
        """

        return Length(self.shell.ExternalThickness)

    @property
    def faces_to_remove(self) -> References:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property FacesToRemove() As References (Read Only)
                | 
                |     Returns the collection of faces to be removed by the shell
                |     process.
                | 
                |     Example:
                |         The following example returns in list the faces to be removed from the
                |         shell firstShell:
                | 
                |          Set list = firstShell.FacesToRemove

        :return: References
        :rtype: References
        """

        return References(self.shell.FacesToRemove)

    @property
    def internal_thickness(self) -> Length:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384)
                | o Property InternalThickness() As Length (Read Only)
                | 
                |     Returns the shell internal thickness.
                | 
                |     Example:
                |         The following example returns in intThick the internal thickness of the
                |         shell firstShell:
                | 
                |          Set intThick = firstShell.InternalThickness

        :return: Length
        :rtype: Length
        """

        return Length(self.shell.InternalThickness)

    def add_face_to_remove(self, i_face_to_remove: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddFaceToRemove(Reference iFaceToRemove)
                | 
                |     Adds a new face to those to be removed by the shell
                |     process.
                | 
                |     Parameters:
                | 
                |         iFaceToRemove
                |             The face to be removed
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                | 
                | Example:
                |     The following example adds the new face face to be removed in the shell
                |     firstShell:
                | 
                |      call firstShell.AddFaceToRemove(face)

        :param Reference i_face_to_remove:
        :return: None
        :rtype: None
        """
        return self.shell.AddFaceToRemove(i_face_to_remove.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_face_to_remove'
        # # vba_code = """
        # # Public Function add_face_to_remove(shell)
        # #     Dim iFaceToRemove (2)
        # #     shell.AddFaceToRemove iFaceToRemove
        # #     add_face_to_remove = iFaceToRemove
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def add_face_with_different_thickness(self, i_face_to_thicken: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub AddFaceWithDifferentThickness(Reference
                | iFaceToThicken)
                | 
                |     Adds a new face to be thicken with different offset
                |     values.
                | 
                |     Parameters:
                | 
                |         iFaceToThicken
                |             The face to be thicken with different offset
                |             values
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                | 
                | Example:
                |     The following example adds the new face face to be thicken with different
                |     offset values in the shell firstShell:
                | 
                |      call firstShell.AddFaceWithDifferentThickness(face)

        :param Reference i_face_to_thicken:
        :return: None
        :rtype: None
        """
        return self.shell.AddFaceWithDifferentThickness(i_face_to_thicken.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'add_face_with_different_thickness'
        # # vba_code = """
        # # Public Function add_face_with_different_thickness(shell)
        # #     Dim iFaceToThicken (2)
        # #     shell.AddFaceWithDifferentThickness iFaceToThicken
        # #     add_face_with_different_thickness = iFaceToThicken
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def remove_face_with_different_thickness(self, i_face_to_remove: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub RemoveFaceWithDifferentThickness(Reference
                | iFaceToRemove)
                | 
                |     Removes an existing face from those to be thicken with different offset
                |     values by the shell process.
                | 
                |     Parameters:
                | 
                |         iFaceToRemove
                |             The face to be removed from the shell
                |             specifications
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                | 
                | Example:
                |     The following example removes the face face from the list of faces in the
                |     shell firstShell:
                | 
                |      call firstShell.RemoveFaceWithDifferentThickness(face)

        :param Reference i_face_to_remove:
        :return: None
        :rtype: None
        """
        return self.shell.RemoveFaceWithDifferentThickness(i_face_to_remove.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'remove_face_with_different_thickness'
        # # vba_code = """
        # # Public Function remove_face_with_different_thickness(shell)
        # #     Dim iFaceToRemove (2)
        # #     shell.RemoveFaceWithDifferentThickness iFaceToRemove
        # #     remove_face_with_different_thickness = iFaceToRemove
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def set_volume_support(self, i_volume_support: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub SetVolumeSupport(Reference iVolumeSupport)
                | 
                |     Set the Support Volume of the faces to modify during Shell operation.

        :param Reference i_volume_support:
        :return: None
        :rtype: None
        """
        return self.shell.SetVolumeSupport(i_volume_support.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'set_volume_support'
        # # vba_code = """
        # # Public Function set_volume_support(shell)
        # #     Dim iVolumeSupport (2)
        # #     shell.SetVolumeSupport iVolumeSupport
        # #     set_volume_support = iVolumeSupport
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def withdraw_face_to_remove(self, i_face_to_withdraw: Reference) -> None:
        """
        .. note::
            :class: toggle

            CAA V5 Visual Basic Help (2020-07-06 14:02:20.222384))
                | o Sub WithdrawFaceToRemove(Reference iFaceToWithdraw)
                | 
                |     Withdraws an existing face from those to be removed by the shell
                |     process.
                | 
                |     Parameters:
                | 
                |         iFaceToWithdraw
                |             The face to be withdrawn from the shell
                |             The following 
                | 
                |         Boundary object is supported: Face. 
                | 
                | Example:
                |     The following example removes the face face from the list of faces in the
                |     shell firstShell:
                | 
                |      call firstShell.WithdrawFaceToRemove(face)

        :param Reference i_face_to_withdraw:
        :return: None
        :rtype: None
        """
        return self.shell.WithdrawFaceToRemove(i_face_to_withdraw.com_object)
        # # # # Autogenerated comment: 
        # # some methods require a system service call as the methods expects a vb array object
        # # passed to it and there is no way to do this directly with python. In those cases the following code
        # # should be uncommented and edited accordingly. Otherwise completely remove all this.
        # # vba_function_name = 'withdraw_face_to_remove'
        # # vba_code = """
        # # Public Function withdraw_face_to_remove(shell)
        # #     Dim iFaceToWithdraw (2)
        # #     shell.WithdrawFaceToRemove iFaceToWithdraw
        # #     withdraw_face_to_remove = iFaceToWithdraw
        # # End Function
        # # """

        # # system_service = self.application.system_service
        # # return system_service.evaluate(vba_code, 0, vba_function_name, [self.com_object])

    def __repr__(self):
        return f'Shell(name="{self.name}")'