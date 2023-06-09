#
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################
"""
The arg spec for the nxos_l2_interfaces module
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type


class L2_interfacesArgs(object):  # pylint: disable=R0903
    """The arg spec for the nxos_l2_interfaces module"""

    argument_spec = {
        "running_config": {"type": "str"},
        "config": {
            "elements": "dict",
            "options": {
                "access": {
                    "options": {"vlan": {"type": "int"}},
                    "type": "dict",
                },
                "mode": {
                    "type": "str",
                    "choices": ["access", "dot1q-tunnel", "trunk", "fex-fabric", "fabricpath"],
                },
                "name": {"required": True, "type": "str"},
                "trunk": {
                    "options": {
                        "allowed_vlans": {"type": "str"},
                        "native_vlan": {"type": "int"},
                    },
                    "type": "dict",
                },
            },
            "type": "list",
        },
        "state": {
            "choices": [
                "merged",
                "replaced",
                "overridden",
                "deleted",
                "rendered",
                "parsed",
                "gathered",
            ],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
