# -*- coding: utf-8 -*-
# Copyright 2020 Red Hat
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

from __future__ import absolute_import, division, print_function


__metaclass__ = type

from ansible_collections.junipernetworks.junos.plugins.modules import junos_prefix_lists
from ansible_collections.junipernetworks.junos.tests.unit.compat.mock import patch
from ansible_collections.junipernetworks.junos.tests.unit.modules.utils import set_module_args

from .junos_module import TestJunosModule, load_fixture


class TestJunosPrefix_listsModule(TestJunosModule):
    module = junos_prefix_lists

    def setUp(self):
        super(TestJunosPrefix_listsModule, self).setUp()
        self.mock_lock_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos.lock_configuration",
        )
        self.lock_configuration = self.mock_lock_configuration.start()
        self.mock_unlock_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.junos.unlock_configuration",
        )
        self.unlock_configuration = self.mock_unlock_configuration.start()
        self.mock_load_config = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.prefix_lists.prefix_lists.load_config",
        )
        self.load_config = self.mock_load_config.start()

        self.mock_commit_configuration = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.config.prefix_lists.prefix_lists.commit_configuration",
        )
        self.mock_commit_configuration = self.mock_commit_configuration.start()

        self.mock_execute_show_command = patch(
            "ansible_collections.junipernetworks.junos.plugins.module_utils.network.junos.facts.prefix_lists.prefix_lists."
            "Prefix_listsFacts.get_device_data",
        )
        self.execute_show_command = self.mock_execute_show_command.start()

    def tearDown(self):
        super(TestJunosPrefix_listsModule, self).tearDown()
        self.mock_load_config.stop()
        self.mock_lock_configuration.stop()
        self.mock_unlock_configuration.stop()
        self.mock_commit_configuration.stop()
        self.mock_execute_show_command.stop()

    def load_fixtures(
        self,
        commands=None,
        format="text",
        changed=False,
        filename=None,
    ):
        def load_from_file(*args, **kwargs):
            if filename:
                output = load_fixture(filename)
            else:
                output = load_fixture("junos_prefix_lists_config.cfg")
            return output

        self.execute_show_command.side_effect = load_from_file

    def test_junos_prefix_lists_merged_01(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="Internal",
                        address_prefixes=["172.16.1.32", "172.16.3.32"],
                    ),
                    dict(name="Test1", dynamic_db=True),
                    dict(
                        name="Test2",
                        address_prefixes=[
                            "172.16.2.32",
                            "172.16.7.32",
                            "172.16.9.32",
                        ],
                    ),
                ],
                state="merged",
            ),
        )
        commands = [
            '<nc:policy-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            "<nc:prefix-list><nc:name>Internal</nc:name><nc:prefix-list-item>"
            "<nc:name>172.16.1.32</nc:name></nc:prefix-list-item>"
            "<nc:prefix-list-item><nc:name>172.16.3.32</nc:name>"
            "</nc:prefix-list-item></nc:prefix-list><nc:prefix-list>"
            "<nc:name>Test1</nc:name><nc:dynamic-db/></nc:prefix-list>"
            "<nc:prefix-list><nc:name>Test2</nc:name><nc:prefix-list-item>"
            "<nc:name>172.16.2.32</nc:name></nc:prefix-list-item>"
            "<nc:prefix-list-item><nc:name>172.16.7.32</nc:name>"
            "</nc:prefix-list-item><nc:prefix-list-item>"
            "<nc:name>172.16.9.32</nc:name></nc:prefix-list-item>"
            "</nc:prefix-list></nc:policy-options>",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_prefix_lists_merged_idempotent_01(self):
        set_module_args(
            dict(
                config=[
                    dict(name="customer_64510"),
                    dict(
                        name="customer_64500",
                        dynamic_db=True,
                        address_prefixes=["172.16.1.16/28", "172.16.1.32/28"],
                    ),
                ],
                state="merged",
            ),
        )
        result = self.execute_module(changed=True)
        self.assertEqual(result["before"], result["after"])

    def test_junos_prefix_lists_replaced_01(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="customer_64510",
                        address_prefixes=["172.16.1.32/28", "172.16.3.32/28"],
                    ),
                    dict(
                        name="customer_64500",
                        address_prefixes=["172.16.2.16/28", "172.16.1.32/28"],
                    ),
                ],
                state="replaced",
            ),
        )
        commands = [
            '<nc:policy-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            '<nc:prefix-list delete="delete"><nc:name>customer_64510</nc:name>'
            '</nc:prefix-list><nc:prefix-list delete="delete">'
            "<nc:name>customer_64500</nc:name></nc:prefix-list>"
            "<nc:prefix-list><nc:name>customer_64510</nc:name>"
            "<nc:prefix-list-item><nc:name>172.16.1.32/28</nc:name>"
            "</nc:prefix-list-item><nc:prefix-list-item>"
            "<nc:name>172.16.3.32/28</nc:name></nc:prefix-list-item>"
            "</nc:prefix-list><nc:prefix-list><nc:name>customer_64500</nc:name>"
            "<nc:prefix-list-item><nc:name>172.16.2.16/28</nc:name>"
            "</nc:prefix-list-item><nc:prefix-list-item><nc:name>172.16.1.32/28</nc:name>"
            "</nc:prefix-list-item></nc:prefix-list></nc:policy-options>",
        ]

        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_prefix_lists_replaced_idempotent_01(self):
        set_module_args(
            dict(
                config=[
                    dict(name="customer_64510"),
                    dict(
                        name="customer_64500",
                        dynamic_db=True,
                        address_prefixes=["172.16.1.16/28", "172.16.1.32/28"],
                    ),
                ],
                state="replaced",
            ),
        )
        result = self.execute_module(changed=True)
        self.assertEqual(result["before"], result["after"])

    def test_junos_prefix_lists_overridden_01(self):
        set_module_args(
            dict(
                config=[
                    dict(
                        name="customer_65500",
                        address_prefixes=["172.16.2.16/28", "172.16.1.32/28"],
                    ),
                ],
                state="overridden",
            ),
        )
        commands = [
            '<nc:policy-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            '<nc:prefix-list delete="delete"><nc:name>customer_64510</nc:name></nc:prefix-list>'
            '<nc:prefix-list delete="delete"><nc:name>customer_64500</nc:name>'
            "</nc:prefix-list><nc:prefix-list><nc:name>customer_65500</nc:name>"
            "<nc:prefix-list-item><nc:name>172.16.2.16/28</nc:name></nc:prefix-list-item>"
            "<nc:prefix-list-item><nc:name>172.16.1.32/28</nc:name></nc:prefix-list-item>"
            "</nc:prefix-list></nc:policy-options>",
        ]
        result = self.execute_module(changed=True)
        self.assertEqual(sorted(result["commands"]), sorted(commands))

    def test_junos_prefix_lists_overridden_idempotent_01(self):
        set_module_args(
            dict(
                config=[
                    dict(name="customer_64510"),
                    dict(
                        name="customer_64500",
                        dynamic_db=True,
                        address_prefixes=["172.16.1.16/28", "172.16.1.32/28"],
                    ),
                ],
                state="overridden",
            ),
        )
        result = self.execute_module(changed=True)
        self.assertEqual(result["before"], result["after"])

    def test_junos_prefix_lists_parsed_01(self):
        parsed_str = """
            <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
                <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
                    <version>18.4R1-S2.4</version>
                    <policy-options>
                    <prefix-list>
                        <name>customer_64510</name>
                    </prefix-list>
                    <prefix-list>
                        <name>customer_64500</name>
                        <dynamic-db/>
                        <prefix-list-item>
                            <name>172.16.1.16/28</name>
                        </prefix-list-item>
                        <prefix-list-item>
                            <name>172.16.1.32/28</name>
                        </prefix-list-item>
                    </prefix-list>
                </policy-options>
                </configuration>
            </rpc-reply>"""
        set_module_args(dict(running_config=parsed_str, state="parsed"))
        result = self.execute_module(changed=False)
        parsed_list = [
            {"name": "customer_64510"},
            {
                "name": "customer_64500",
                "dynamic_db": True,
                "address_prefixes": ["172.16.1.16/28", "172.16.1.32/28"],
            },
        ]
        self.assertEqual(result["parsed"], parsed_list)

    def test_junos_prefix_lists_gathered_01(self):
        """
        :return:
        """
        set_module_args(dict(state="gathered"))
        result = self.execute_module(changed=False)
        gather_list = [
            {"name": "customer_64510"},
            {
                "name": "customer_64500",
                "dynamic_db": True,
                "address_prefixes": ["172.16.1.16/28", "172.16.1.32/28"],
            },
        ]
        self.assertEqual(gather_list, result["gathered"])

    def test_junos_prefix_lists_rendered_01(self):
        """
        :return:
        """
        set_module_args(
            dict(
                config=[
                    dict(
                        name="Internal",
                        address_prefixes=["172.16.1.32", "172.16.3.32"],
                    ),
                    dict(name="Test1", dynamic_db=True),
                    dict(
                        name="Test2",
                        address_prefixes=[
                            "172.16.2.32",
                            "172.16.7.32",
                            "172.16.9.32",
                        ],
                    ),
                ],
                state="rendered",
            ),
        )

        rendered = (
            '<nc:policy-options xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">'
            "<nc:prefix-list><nc:name>Internal</nc:name><nc:prefix-list-item>"
            "<nc:name>172.16.1.32</nc:name></nc:prefix-list-item>"
            "<nc:prefix-list-item><nc:name>172.16.3.32</nc:name>"
            "</nc:prefix-list-item></nc:prefix-list><nc:prefix-list>"
            "<nc:name>Test1</nc:name><nc:dynamic-db/></nc:prefix-list>"
            "<nc:prefix-list><nc:name>Test2</nc:name><nc:prefix-list-item>"
            "<nc:name>172.16.2.32</nc:name></nc:prefix-list-item>"
            "<nc:prefix-list-item><nc:name>172.16.7.32</nc:name>"
            "</nc:prefix-list-item><nc:prefix-list-item>"
            "<nc:name>172.16.9.32</nc:name></nc:prefix-list-item>"
            "</nc:prefix-list></nc:policy-options>"
        )
        result = self.execute_module(changed=False)
        self.assertEqual(sorted(result["rendered"]), sorted(rendered))
