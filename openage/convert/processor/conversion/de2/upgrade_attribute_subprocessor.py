# Copyright 2020-2022 the openage authors. See copying.md for legal info.
#
# pylint: disable=too-few-public-methods
#
# TODO: Remove when all methods are implemented
# pylint: disable=unused-argument

"""
Creates upgrade patches for attribute modification effects in DE2.
"""
from __future__ import annotations
import typing


if typing.TYPE_CHECKING:
    from openage.convert.entity_object.conversion.converter_object import ConverterObjectGroup
    from openage.convert.entity_object.conversion.aoc.genie_unit import GenieGameEntityGroup
    from openage.nyan.nyan_structs import MemberOperator
    from openage.convert.value_object.conversion.forward_ref import ForwardRef


class DE2UpgradeAttributeSubprocessor:
    """
    Creates raw API objects for attribute upgrade effects in DE2.
    """

    @staticmethod
    def regeneration_rate_upgrade(
        converter_group: ConverterObjectGroup,
        line: GenieGameEntityGroup,
        value: typing.Union[int, float],
        operator: MemberOperator,
        team: bool = False
    ) -> list[ForwardRef]:
        """
        Creates a patch for the regeneration rate modify effect (ID: 109).

        TODO: Move into AK processor.

        :param converter_group: Tech/Civ that gets the patch.
        :type converter_group: ...dataformat.converter_object.ConverterObjectGroup
        :param line: Unit/Building line that has the ability.
        :type line: ...dataformat.converter_object.ConverterObjectGroup
        :param value: Value used for patching the member.
        :type value: int, float
        :param operator: Operator used for patching the member.
        :type operator: MemberOperator
        :returns: The forward references for the generated patches.
        :rtype: list
        """
        patches = []

        # TODO: Implement

        return patches
