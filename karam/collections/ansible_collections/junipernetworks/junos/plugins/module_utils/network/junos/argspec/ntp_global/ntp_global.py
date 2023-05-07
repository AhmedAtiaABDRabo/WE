#
# -*- coding: utf-8 -*-
# Copyright 2021 Red Hat
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
The arg spec for the junos_ntp_global module
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type


class Ntp_globalArgs(object):  # pylint: disable=R0903
    """The arg spec for the junos_ntp_global module"""

    def __init__(self, **kwargs):
        pass

    argument_spec = {
        "config": {
            "options": {
                "authentication_keys": {
                    "elements": "dict",
                    "no_log": False,
                    "options": {
                        "algorithm": {
                            "choices": ["md5", "sha1", "sha256"],
                            "type": "str",
                        },
                        "id": {"type": "int"},
                        "key": {"type": "str", "no_log": True},
                    },
                    "type": "list",
                },
                "boot_server": {"type": "str"},
                "broadcast_client": {"type": "bool"},
                "broadcasts": {
                    "elements": "dict",
                    "options": {
                        "address": {"type": "str"},
                        "key": {"type": "str", "no_log": False},
                        "routing_instance_name": {"type": "str"},
                        "ttl": {"type": "int"},
                        "version": {"type": "int"},
                    },
                    "type": "list",
                },
                "interval_range": {"type": "int"},
                "multicast_client": {"type": "str"},
                "peers": {
                    "elements": "dict",
                    "options": {
                        "key_id": {"type": "int", "no_log": False},
                        "peer": {"type": "str"},
                        "prefer": {"type": "bool"},
                        "version": {"type": "int"},
                    },
                    "type": "list",
                },
                "servers": {
                    "elements": "dict",
                    "options": {
                        "key_id": {"type": "int"},
                        "prefer": {"type": "bool"},
                        "routing_instance": {"type": "str"},
                        "server": {"type": "str"},
                        "version": {"type": "int"},
                    },
                    "type": "list",
                },
                "source_addresses": {
                    "elements": "dict",
                    "options": {
                        "routing_instance": {"type": "str"},
                        "source_address": {"type": "str"},
                    },
                    "type": "list",
                },
                "threshold": {
                    "options": {
                        "action": {
                            "choices": ["accept", "reject"],
                            "type": "str",
                        },
                        "value": {"type": "int"},
                    },
                    "type": "dict",
                },
                "trusted_keys": {
                    "type": "list",
                    "elements": "dict",
                    "no_log": False,
                    "options": {"key_id": {"type": "int"}},
                },
            },
            "type": "dict",
        },
        "running_config": {"type": "str"},
        "state": {
            "choices": [
                "merged",
                "replaced",
                "deleted",
                "overridden",
                "parsed",
                "gathered",
                "rendered",
            ],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
