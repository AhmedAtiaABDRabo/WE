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
The arg spec for the nxos_acls module
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type


class AclsArgs(object):  # pylint: disable=R0903
    """The arg spec for the nxos_acls module"""

    argument_spec = {
        "config": {
            "elements": "dict",
            "options": {
                "acls": {
                    "elements": "dict",
                    "options": {
                        "aces": {
                            "elements": "dict",
                            "mutually_exclusive": [["grant", "remark"]],
                            "options": {
                                "destination": {
                                    "mutually_exclusive": [
                                        ["address", "any", "host", "prefix"],
                                        [
                                            "wildcard_bits",
                                            "any",
                                            "host",
                                            "prefix",
                                        ],
                                    ],
                                    "options": {
                                        "address": {"type": "str"},
                                        "any": {"type": "bool"},
                                        "host": {"type": "str"},
                                        "port_protocol": {
                                            "mutually_exclusive": [
                                                [
                                                    "eq",
                                                    "lt",
                                                    "neq",
                                                    "gt",
                                                    "range",
                                                ],
                                            ],
                                            "options": {
                                                "eq": {"type": "str"},
                                                "gt": {"type": "str"},
                                                "lt": {"type": "str"},
                                                "neq": {"type": "str"},
                                                "range": {
                                                    "options": {
                                                        "end": {"type": "str"},
                                                        "start": {"type": "str"},
                                                    },
                                                    "required_together": [["start", "end"]],
                                                    "type": "dict",
                                                },
                                            },
                                            "type": "dict",
                                        },
                                        "prefix": {"type": "str"},
                                        "wildcard_bits": {"type": "str"},
                                    },
                                    "required_together": [["address", "wildcard_bits"]],
                                    "type": "dict",
                                },
                                "dscp": {"type": "str"},
                                "fragments": {"type": "bool"},
                                "grant": {
                                    "choices": ["permit", "deny"],
                                    "type": "str",
                                },
                                "log": {"type": "bool"},
                                "precedence": {"type": "str"},
                                "protocol": {"type": "str"},
                                "protocol_options": {
                                    "mutually_exclusive": [["icmp", "igmp", "tcp"]],
                                    "options": {
                                        "icmp": {
                                            "options": {
                                                "administratively_prohibited": {"type": "bool"},
                                                "alternate_address": {"type": "bool"},
                                                "conversion_error": {"type": "bool"},
                                                "dod_host_prohibited": {"type": "bool"},
                                                "dod_net_prohibited": {"type": "bool"},
                                                "echo": {"type": "bool"},
                                                "echo_reply": {"type": "bool"},
                                                "echo_request": {"type": "bool"},
                                                "general_parameter_problem": {"type": "bool"},
                                                "host_isolated": {"type": "bool"},
                                                "host_precedence_unreachable": {"type": "bool"},
                                                "host_redirect": {"type": "bool"},
                                                "host_tos_redirect": {"type": "bool"},
                                                "host_tos_unreachable": {"type": "bool"},
                                                "host_unknown": {"type": "bool"},
                                                "host_unreachable": {"type": "bool"},
                                                "information_reply": {"type": "bool"},
                                                "information_request": {"type": "bool"},
                                                "mask_reply": {"type": "bool"},
                                                "mask_request": {"type": "bool"},
                                                "message_code": {"type": "int"},
                                                "message_type": {"type": "int"},
                                                "mobile_redirect": {"type": "bool"},
                                                "net_redirect": {"type": "bool"},
                                                "net_tos_redirect": {"type": "bool"},
                                                "net_tos_unreachable": {"type": "bool"},
                                                "net_unreachable": {"type": "bool"},
                                                "network_unknown": {"type": "bool"},
                                                "no_room_for_option": {"type": "bool"},
                                                "option_missing": {"type": "bool"},
                                                "packet_too_big": {"type": "bool"},
                                                "parameter_problem": {"type": "bool"},
                                                "port_unreachable": {"type": "bool"},
                                                "precedence_unreachable": {"type": "bool"},
                                                "protocol_unreachable": {"type": "bool"},
                                                "reassembly_timeout": {"type": "bool"},
                                                "redirect": {"type": "bool"},
                                                "router_advertisement": {"type": "bool"},
                                                "router_solicitation": {"type": "bool"},
                                                "source_quench": {"type": "bool"},
                                                "source_route_failed": {"type": "bool"},
                                                "time_exceeded": {"type": "bool"},
                                                "timestamp_reply": {"type": "bool"},
                                                "timestamp_request": {"type": "bool"},
                                                "traceroute": {"type": "bool"},
                                                "ttl_exceeded": {"type": "bool"},
                                                "unreachable": {"type": "bool"},
                                            },
                                            "type": "dict",
                                        },
                                        "icmpv6": {
                                            "type": "dict",
                                            "options": {
                                                "beyond_scope": {"type": "bool"},
                                                "destination_unreachable": {
                                                    "type": "bool",
                                                },
                                                "echo_reply": {"type": "bool"},
                                                "echo_request": {"type": "bool"},
                                                "fragments": {"type": "bool"},
                                                "header": {"type": "bool"},
                                                "hop_limit": {"type": "bool"},
                                                "mld_query": {"type": "bool"},
                                                "mld_reduction": {"type": "bool"},
                                                "mld_report": {"type": "bool"},
                                                "mldv2": {"type": "bool"},
                                                "nd_na": {"type": "bool"},
                                                "nd_ns": {"type": "bool"},
                                                "next_header": {"type": "bool"},
                                                "no_admin": {"type": "bool"},
                                                "no_route": {"type": "bool"},
                                                "packet_too_big": {"type": "bool"},
                                                "parameter_option": {
                                                    "type": "bool",
                                                },
                                                "parameter_problem": {
                                                    "type": "bool",
                                                },
                                                "port_unreachable": {
                                                    "type": "bool",
                                                },
                                                "reassembly_timeout": {
                                                    "type": "bool",
                                                },
                                                "renum_command": {"type": "bool"},
                                                "renum_result": {"type": "bool"},
                                                "renum_seq_number": {
                                                    "type": "bool",
                                                },
                                                "router_advertisement": {
                                                    "type": "bool",
                                                },
                                                "router_renumbering": {
                                                    "type": "bool",
                                                },
                                                "router_solicitation": {
                                                    "type": "bool",
                                                },
                                                "time_exceeded": {"type": "bool"},
                                                "unreachable": {"type": "bool"},
                                                "telemetry_path": {"type": "bool"},
                                                "telemetry_queue": {
                                                    "type": "bool",
                                                },
                                            },
                                        },
                                        "igmp": {
                                            "mutually_exclusive": [
                                                [
                                                    "dvmrp",
                                                    "host_query",
                                                    "host_report",
                                                ],
                                            ],
                                            "options": {
                                                "dvmrp": {"type": "bool"},
                                                "host_query": {"type": "bool"},
                                                "host_report": {"type": "bool"},
                                            },
                                            "type": "dict",
                                        },
                                        "tcp": {
                                            "options": {
                                                "ack": {"type": "bool"},
                                                "established": {"type": "bool"},
                                                "fin": {"type": "bool"},
                                                "psh": {"type": "bool"},
                                                "rst": {"type": "bool"},
                                                "syn": {"type": "bool"},
                                                "urg": {"type": "bool"},
                                            },
                                            "type": "dict",
                                        },
                                    },
                                    "type": "dict",
                                },
                                "remark": {"type": "str"},
                                "sequence": {"type": "int"},
                                "source": {
                                    "mutually_exclusive": [
                                        ["address", "any", "host", "prefix"],
                                        [
                                            "wildcard_bits",
                                            "host",
                                            "any",
                                            "prefix",
                                        ],
                                    ],
                                    "options": {
                                        "address": {"type": "str"},
                                        "any": {"type": "bool"},
                                        "host": {"type": "str"},
                                        "port_protocol": {
                                            "mutually_exclusive": [
                                                ["eq", "lt", "neq", "range"],
                                                ["eq", "gt", "neq", "range"],
                                            ],
                                            "options": {
                                                "eq": {"type": "str"},
                                                "gt": {"type": "str"},
                                                "lt": {"type": "str"},
                                                "neq": {"type": "str"},
                                                "range": {
                                                    "options": {
                                                        "end": {"type": "str"},
                                                        "start": {"type": "str"},
                                                    },
                                                    "type": "dict",
                                                },
                                            },
                                            "type": "dict",
                                        },
                                        "prefix": {"type": "str"},
                                        "wildcard_bits": {"type": "str"},
                                    },
                                    "required_together": [["address", "wildcard_bits"]],
                                    "type": "dict",
                                },
                            },
                            "type": "list",
                        },
                        "name": {"required": True, "type": "str"},
                    },
                    "type": "list",
                },
                "afi": {
                    "choices": ["ipv4", "ipv6"],
                    "required": True,
                    "type": "str",
                },
            },
            "type": "list",
        },
        "running_config": {"type": "str"},
        "state": {
            "choices": [
                "deleted",
                "gathered",
                "merged",
                "overridden",
                "rendered",
                "replaced",
                "parsed",
            ],
            "default": "merged",
            "type": "str",
        },
    }  # pylint: disable=C0301
