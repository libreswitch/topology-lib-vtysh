# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# WARNING: This is auto-generated, do not manually modify

"""
vtysh library.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division

from .parser import *  # noqa


class ContextManager(object):
    """
    This class defines a context manager object.

    Usage:

    ::

        with ClassName(parameters) as ctx:
            ctx.first_function()
            ctx.second_function()

    This way at the beginning the **pre_commands** will be run and at the end
    the **post_commands** will clean the vtysh terminal. Every implementation
    of this class document their pre_commands and post_commands.

    """


class Configure(ContextManager):
    """
    Configuration terminal

    pre_commands:

    ::

            ['configure terminal']

    post_commands:

    ::

            ['end']
    """
    def __init__(self, enode):
        self.enode = enode

    def __enter__(self):
        commands = """\
            configure terminal
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

        return self

    def __exit__(self, type, value, traceback):
        commands = """\
            end
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

    def no_vlan(self, vlan_id):
        """
        Delete a VLAN

        This function runs the following vtysh command:

        ::

            # no vlan {vlan_id}

        :param vlan_id: VLAN Identifier.
        """

        result = self.enode(
            'no vlan {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_interface_lag(self, lag_id):
        """
        Delete a lag

        This function runs the following vtysh command:

        ::

            # no interface lag {lag_id}

        :param lag_id: link-aggregation identifier.
        """

        result = self.enode(
            'no interface lag {lag_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def ip_route(self, ipv4, next_hop, metric=''):
        """
        Configure static routes

        This function runs the following vtysh command:

        ::

            # ip route {ipv4} {next_hop} {metric}

        :param ipv4: A.B.C.D/M IP destination prefix.
        :param next_hop: Can be an ip address or a interface.
        :param metric: Optional, route address to configure.
        """

        result = self.enode(
            'ip route {ipv4} {next_hop} {metric}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_ip_route(self, ipv4, next_hop, metric=''):
        """
        Un-configure static routes

        This function runs the following vtysh command:

        ::

            # no ip route {ipv4} {next_hop} {metric}

        :param ipv4: A.B.C.D/M IP destination prefix.
        :param next_hop: Can be an ip address or a interface.
        :param metric: Optional, route address to configure.
        """

        result = self.enode(
            'no ip route {ipv4} {next_hop} {metric}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def ip_prefix_list_seq(self, prefix_name, seq, permission, network):
        """
        Configure prefix list

        This function runs the following vtysh command:

        ::

            # ip prefix-list {prefix_name} seq {seq} {permission} {network}

        :param prefix_name: WORD  Name of a prefix list.
        :param seq: <1-4294967295>  Sequence number.
        :param permission: deny    Specify packets to rejectpermit  Specify
            packets to forward
        :param network: A.B.C.D/M  IP prefix <network>/<length>, e.g.,
            35.0.0.0/8 any Any prefix match. Same as "0.0.0.0/0 le 32"
        """

        result = self.enode(
            'ip prefix-list {prefix_name} seq {seq} {permission} {network}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_ip_prefix_list_seq(self, prefix_name, seq, permission, network):
        """
        Un-configure prefix list

        This function runs the following vtysh command:

        ::

            # no ip prefix-list {prefix_name} seq {seq} {permission} {network}

        :param prefix_name: WORD  Name of a prefix list.
        :param seq: <1-4294967295>  Sequence number.
        :param permission: deny    Specify packets to rejectpermit  Specify
            packets to forward
        :param network: A.B.C.D/M  IP prefix <network>/<length>, e.g.,
            35.0.0.0/8 any Any prefix match. Same as "0.0.0.0/0 le 32"
        """

        result = self.enode(
            'no ip prefix-list {prefix_name} seq {seq} {permission} {network}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_route_map(self, routemap_name, permission, seq):
        """
        Route-map configuration

        This function runs the following vtysh command:

        ::

            # no route-map {routemap_name} {permission} {seq}

        :param routemap_name: WORD  Route map tag
        :param permission: deny  Route map denies set operationspermit  Route
            map permits set operations
        :param seq: <1-65535>  Sequence to insert to/delete from existing
            route-map entry
        """

        result = self.enode(
            'no route-map {routemap_name} {permission} {seq}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def ipv6_route(self, ipv6, next_hop, metric=''):
        """
        Configure static routes

        This function runs the following vtysh command:

        ::

            # ipv6 route {ipv6} {next_hop} {metric}

        :param ipv6: X:X::X:X/M IP destination prefix.
        :param next_hop: Can be an ip address or a interface.
        :param metric: Optional, route address to configure.
        """

        result = self.enode(
            'ipv6 route {ipv6} {next_hop} {metric}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_ipv6_route(self, ipv6, next_hop, metric=''):
        """
        Un-configure static routes

        This function runs the following vtysh command:

        ::

            # no ipv6 route {ipv6} {next_hop} {metric}

        :param ipv6: X:X::X:X/M IP destination prefix.
        :param next_hop: Can be an ip address or a interface.
        :param metric: Optional, route address to configure.
        """

        result = self.enode(
            'no ipv6 route {ipv6} {next_hop} {metric}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def lacp_system_priority(self, priority):
        """
        Set LACP system priority.

        This function runs the following vtysh command:

        ::

            # lacp system-priority {priority}

        :param priority: <0-65535>  The range is 0 to 65535.
        """

        result = self.enode(
            'lacp system-priority {priority}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def feature_lldp(self):
        """
        Configure LLDP parameters.

        This function runs the following vtysh command:

        ::

            # feature lldp

        """

        result = self.enode(
            'feature lldp'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_feature_lldp(self):
        """
        Un-configure LLDP parameters.

        This function runs the following vtysh command:

        ::

            # no feature lldp

        """

        result = self.enode(
            'no feature lldp'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result


class RouteMap(ContextManager):
    """
    Route-map configuration

    pre_commands:

    ::

            ['config terminal', 'route-map {routemap_name} {permission} {seq}']

    post_commands:

    ::

            ['end']
    """
    def __init__(self, enode, routemap_name, permission, seq):
        self.enode = enode
        self.routemap_name = routemap_name
        self.permission = permission
        self.seq = seq

    def __enter__(self):
        commands = """\
            config terminal
            route-map {routemap_name} {permission} {seq}
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

        return self

    def __exit__(self, type, value, traceback):
        commands = """\
            end
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

    def description(self, description):
        """
        Set description

        This function runs the following vtysh command:

        ::

            # description {description}

        :param description: LINE  Comment describing this route-map rule
        """

        result = self.enode(
            'description {description}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_description(self, description):
        """
        Unset description

        This function runs the following vtysh command:

        ::

            # no description {description}

        :param description: LINE  Comment describing this route-map rule
        """

        result = self.enode(
            'no description {description}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def match_ip_address_prefix_list(self, prefix_name):
        """
        Set prefix-list

        This function runs the following vtysh command:

        ::

            # match ip address prefix-list {prefix_name}

        :param prefix_name: WORD  IP prefix-list name
        """

        result = self.enode(
            'match ip address prefix-list {prefix_name}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_match_ip_address_prefix_list(self, prefix_name=''):
        """
        Unset prefix-list

        This function runs the following vtysh command:

        ::

            # no match ip address prefix-list {prefix_name}

        :param prefix_name: WORD  IP prefix-list name
        """

        result = self.enode(
            'no match ip address prefix-list {prefix_name}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def set_metric(self, metric):
        """
        Set metric

        This function runs the following vtysh command:

        ::

            # set metric {metric}

        :param metric: <0-4294967295>  Metric value
        """

        result = self.enode(
            'set metric {metric}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_set_metric(self, metric=''):
        """
        Unset metric

        This function runs the following vtysh command:

        ::

            # no set metric {metric}

        :param metric: <0-4294967295>  Metric value
        """

        result = self.enode(
            'no set metric {metric}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def set_community(self, community):
        """
        Set community

        This function runs the following vtysh command:

        ::

            # set community {community}

        :param community: AA:NN  Community number in aa:nn format or local-AS
            \|no-advertise\|no-export\|internet or additive
        """

        result = self.enode(
            'set community {community}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_set_community(self, community=''):
        """
        Unset community

        This function runs the following vtysh command:

        ::

            # no set community {community}

        :param community: AA:NN  Community number in aa:nn format orlocal-AS
            \|no-advertise\|no-export\|internet or additive
        """

        result = self.enode(
            'no set community {community}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result


class ConfigInterface(ContextManager):
    """
    Interface configuration.

    pre_commands:

    ::

            ['config terminal', 'interface {port}']

    post_commands:

    ::

            ['end']
    """
    def __init__(self, enode, portlbl):
        self.enode = enode
        self.port = enode.ports.get(portlbl, portlbl)

    def __enter__(self):
        commands = """\
            config terminal
            interface {port}
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

        return self

    def __exit__(self, type, value, traceback):
        commands = """\
            end
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

    def ip_address(self, ipv4):
        """
        Set IP address

        This function runs the following vtysh command:

        ::

            # ip address {ipv4}

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        result = self.enode(
            'ip address {ipv4}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_ip_address(self, ipv4):
        """
        Unset IP address

        This function runs the following vtysh command:

        ::

            # no ip address {ipv4}

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        result = self.enode(
            'no ip address {ipv4}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def ip_address_secondary(self, ipv4):
        """
        Set secondary IP address

        This function runs the following vtysh command:

        ::

            # ip address {ipv4} secondary

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        result = self.enode(
            'ip address {ipv4} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_ip_address_secondary(self, ipv4):
        """
        Unset secondary IP address

        This function runs the following vtysh command:

        ::

            # no ip address {ipv4} secondary

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        result = self.enode(
            'no ip address {ipv4} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def ipv6_address(self, ipv6):
        """
        Set IPv6 address

        This function runs the following vtysh command:

        ::

            # ipv6 address {ipv6}

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        result = self.enode(
            'ipv6 address {ipv6}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_ipv6_address(self, ipv6):
        """
        Unset IPv6 address

        This function runs the following vtysh command:

        ::

            # no ipv6 address {ipv6}

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        result = self.enode(
            'no ipv6 address {ipv6}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def ipv6_address_secondary(self, ipv6):
        """
        Set secondary IPv6 address

        This function runs the following vtysh command:

        ::

            # ipv6 address {ipv6} secondary

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        result = self.enode(
            'ipv6 address {ipv6} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_ipv6_address_secondary(self, ipv6):
        """
        Unset IPv6 address

        This function runs the following vtysh command:

        ::

            # no ipv6 address {ipv6} secondary

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        result = self.enode(
            'no ipv6 address {ipv6} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def routing(self):
        """
        Configure interface as L3.

        This function runs the following vtysh command:

        ::

            # routing

        """

        result = self.enode(
            'routing'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_routing(self):
        """
        Unconfigure interface as L3.

        This function runs the following vtysh command:

        ::

            # no routing

        """

        result = self.enode(
            'no routing'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def shutdown(self):
        """
        Enable an interface.

        This function runs the following vtysh command:

        ::

            # shutdown

        """

        result = self.enode(
            'shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_shutdown(self):
        """
        Disable an interface.

        This function runs the following vtysh command:

        ::

            # no shutdown

        """

        result = self.enode(
            'no shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def vlan_access(self, vlan_id):
        """
        Access configuration

        This function runs the following vtysh command:

        ::

            # vlan access {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        result = self.enode(
            'vlan access {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_vlan_access(self, vlan_id):
        """
        Remove vlan access

        This function runs the following vtysh command:

        ::

            # no vlan access {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        result = self.enode(
            'no vlan access {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def vlan_trunk_allowed(self, vlan_id):
        """
        Allow VLAN on the trunk port

        This function runs the following vtysh command:

        ::

            # vlan trunk allowed {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        result = self.enode(
            'vlan trunk allowed {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_vlan_trunk_allowed(self, vlan_id):
        """
        Disallow VLAN on the trunk port

        This function runs the following vtysh command:

        ::

            # no vlan trunk allowed {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        result = self.enode(
            'no vlan trunk allowed {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def vlan_trunk_native_tag(self):
        """
        Tag configuration on the trunk port

        This function runs the following vtysh command:

        ::

            # vlan trunk native tag

        """

        result = self.enode(
            'vlan trunk native tag'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_vlan_trunk_native_tag(self):
        """
        Remove tag configuration on the trunk port

        This function runs the following vtysh command:

        ::

            # no vlan trunk native tag

        """

        result = self.enode(
            'no vlan trunk native tag'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def vlan_trunk_native(self, vlan_id):
        """
        Native VLAN on the trunk port

        This function runs the following vtysh command:

        ::

            # vlan trunk native {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        result = self.enode(
            'vlan trunk native {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_vlan_trunk_native(self, vlan_id):
        """
        Remove native VLAN on the trunk port

        This function runs the following vtysh command:

        ::

            # no vlan trunk native {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        result = self.enode(
            'no vlan trunk native {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def lacp_port_id(self, port_id):
        """
        Set port ID used in LACP negotiation.

        This function runs the following vtysh command:

        ::

            # lacp port-id {port_id}

        :param port_id: <1-65535>  .The range is 1 to 65535
        """

        result = self.enode(
            'lacp port-id {port_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def lacp_port_priority(self, port_priority):
        """
        Set port priority is used in LACP negotiation.

        This function runs the following vtysh command:

        ::

            # lacp port-priority {port_priority}

        :param port_priority: <1-65535>  The range is 1 to 65535
        """

        result = self.enode(
            'lacp port-priority {port_priority}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def lag(self, lag_id):
        """
        Add the current interface to link aggregation.

        This function runs the following vtysh command:

        ::

            # lag {lag_id}

        :param lag_id: <1-2000>  LAG number ranges from 1 to 2000
        """

        result = self.enode(
            'lag {lag_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_lag(self, lag_id):
        """
        Remove the current interface to link aggregation.

        This function runs the following vtysh command:

        ::

            # no lag {lag_id}

        :param lag_id: <1-2000>  LAG number ranges from 1 to 2000
        """

        result = self.enode(
            'no lag {lag_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def lldp_transmission(self):
        """
        Set the transmission on lldp.

        This function runs the following vtysh command:

        ::

            # lldp transmission

        """

        result = self.enode(
            'lldp transmission'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_lldp_transmission(self):
        """
        Un-set the transmission on lldp.

        This function runs the following vtysh command:

        ::

            # no lldp transmission

        """

        result = self.enode(
            'no lldp transmission'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def lldp_reception(self):
        """
        Set the reception on lldp.

        This function runs the following vtysh command:

        ::

            # lldp reception

        """

        result = self.enode(
            'lldp reception'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_lldp_reception(self):
        """
        Un-set the reception on lldp.

        This function runs the following vtysh command:

        ::

            # no lldp reception

        """

        result = self.enode(
            'no lldp reception'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result


class ConfigInterfaceVlan(ContextManager):
    """
    VLAN configuration.

    pre_commands:

    ::

            ['config terminal', 'interface vlan {vlan_id}']

    post_commands:

    ::

            ['end']
    """
    def __init__(self, enode, vlan_id):
        self.enode = enode
        self.vlan_id = vlan_id

    def __enter__(self):
        commands = """\
            config terminal
            interface vlan {vlan_id}
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

        return self

    def __exit__(self, type, value, traceback):
        commands = """\
            end
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

    def ip_address(self, ipv4):
        """
        Set IP address

        This function runs the following vtysh command:

        ::

            # ip address {ipv4}

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        result = self.enode(
            'ip address {ipv4}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_ip_address(self, ipv4):
        """
        Unset IP address

        This function runs the following vtysh command:

        ::

            # no ip address {ipv4}

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        result = self.enode(
            'no ip address {ipv4}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def ip_address_secondary(self, ipv4):
        """
        Set secondary IP address

        This function runs the following vtysh command:

        ::

            # ip address {ipv4} secondary

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        result = self.enode(
            'ip address {ipv4} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_ip_address_secondary(self, ipv4):
        """
        Unset secondary IP address

        This function runs the following vtysh command:

        ::

            # no ip address {ipv4} secondary

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        result = self.enode(
            'no ip address {ipv4} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def ipv6_address(self, ipv6):
        """
        Set IPv6 address

        This function runs the following vtysh command:

        ::

            # ipv6 address {ipv6}

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        result = self.enode(
            'ipv6 address {ipv6}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_ipv6_address(self, ipv6):
        """
        Unset IPv6 address

        This function runs the following vtysh command:

        ::

            # no ipv6 address {ipv6}

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        result = self.enode(
            'no ipv6 address {ipv6}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def ipv6_address_secondary(self, ipv6):
        """
        Set secondary IPv6 address

        This function runs the following vtysh command:

        ::

            # ipv6 address {ipv6} secondary

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        result = self.enode(
            'ipv6 address {ipv6} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_ipv6_address_secondary(self, ipv6):
        """
        Unset IPv6 address

        This function runs the following vtysh command:

        ::

            # no ipv6 address {ipv6} secondary

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        result = self.enode(
            'no ipv6 address {ipv6} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def shutdown(self):
        """
        Enable an interface.

        This function runs the following vtysh command:

        ::

            # shutdown

        """

        result = self.enode(
            'shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_shutdown(self):
        """
        Disable an interface.

        This function runs the following vtysh command:

        ::

            # no shutdown

        """

        result = self.enode(
            'no shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result


class ConfigInterfaceLag(ContextManager):
    """
    Configure link-aggregation parameters.

    pre_commands:

    ::

            ['config terminal', 'interface lag {lag}']

    post_commands:

    ::

            ['end']
    """
    def __init__(self, enode, lag):
        self.enode = enode
        self.lag = lag

    def __enter__(self):
        commands = """\
            config terminal
            interface lag {lag}
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

        return self

    def __exit__(self, type, value, traceback):
        commands = """\
            end
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

    def ip_address(self, ipv4):
        """
        Set IP address

        This function runs the following vtysh command:

        ::

            # ip address {ipv4}

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        result = self.enode(
            'ip address {ipv4}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_ip_address(self, ipv4):
        """
        Unset IP address

        This function runs the following vtysh command:

        ::

            # no ip address {ipv4}

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        result = self.enode(
            'no ip address {ipv4}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def ip_address_secondary(self, ipv4):
        """
        Set secondary IP address

        This function runs the following vtysh command:

        ::

            # ip address {ipv4} secondary

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        result = self.enode(
            'ip address {ipv4} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_ip_address_secondary(self, ipv4):
        """
        Unset secondary IP address

        This function runs the following vtysh command:

        ::

            # no ip address {ipv4} secondary

        :param ipv4: A.B.C.D/M Interface IP address.
        """

        result = self.enode(
            'no ip address {ipv4} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def ipv6_address(self, ipv6):
        """
        Set IPv6 address

        This function runs the following vtysh command:

        ::

            # ipv6 address {ipv6}

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        result = self.enode(
            'ipv6 address {ipv6}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_ipv6_address(self, ipv6):
        """
        Unset IPv6 address

        This function runs the following vtysh command:

        ::

            # no ipv6 address {ipv6}

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        result = self.enode(
            'no ipv6 address {ipv6}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def ipv6_address_secondary(self, ipv6):
        """
        Set secondary IPv6 address

        This function runs the following vtysh command:

        ::

            # ipv6 address {ipv6} secondary

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        result = self.enode(
            'ipv6 address {ipv6} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_ipv6_address_secondary(self, ipv6):
        """
        Unset IPv6 address

        This function runs the following vtysh command:

        ::

            # no ipv6 address {ipv6} secondary

        :param ipv6: X:X::X:X/M  Interface IPv6 address
        """

        result = self.enode(
            'no ipv6 address {ipv6} secondary'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def shutdown(self):
        """
        Enable an interface.

        This function runs the following vtysh command:

        ::

            # shutdown

        """

        result = self.enode(
            'shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_shutdown(self):
        """
        Disable an interface.

        This function runs the following vtysh command:

        ::

            # no shutdown

        """

        result = self.enode(
            'no shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def routing(self):
        """
        Configure interface as L3.

        This function runs the following vtysh command:

        ::

            # routing

        """

        result = self.enode(
            'routing'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_routing(self):
        """
        Unconfigure interface as L3.

        This function runs the following vtysh command:

        ::

            # no routing

        """

        result = self.enode(
            'no routing'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def vlan_access(self, vlan_id):
        """
        Access configuration

        This function runs the following vtysh command:

        ::

            # vlan access {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        result = self.enode(
            'vlan access {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_vlan_access(self, vlan_id):
        """
        Remove vlan access

        This function runs the following vtysh command:

        ::

            # no vlan access {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        result = self.enode(
            'no vlan access {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def vlan_trunk_allowed(self, vlan_id):
        """
        Allow VLAN on the trunk port

        This function runs the following vtysh command:

        ::

            # vlan trunk allowed {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        result = self.enode(
            'vlan trunk allowed {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_vlan_trunk_allowed(self, vlan_id):
        """
        Disallow VLAN on the trunk port

        This function runs the following vtysh command:

        ::

            # no vlan trunk allowed {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        result = self.enode(
            'no vlan trunk allowed {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def vlan_trunk_native_tag(self):
        """
        Tag configuration on the trunk port

        This function runs the following vtysh command:

        ::

            # vlan trunk native tag

        """

        result = self.enode(
            'vlan trunk native tag'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_vlan_trunk_native_tag(self):
        """
        Remove tag configuration on the trunk port

        This function runs the following vtysh command:

        ::

            # no vlan trunk native tag

        """

        result = self.enode(
            'no vlan trunk native tag'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def vlan_trunk_native(self, vlan_id):
        """
        Native VLAN on the trunk port

        This function runs the following vtysh command:

        ::

            # vlan trunk native {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        result = self.enode(
            'vlan trunk native {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_vlan_trunk_native(self, vlan_id):
        """
        Remove native VLAN on the trunk port

        This function runs the following vtysh command:

        ::

            # no vlan trunk native {vlan_id}

        :param vlan_id: <1-4094>  VLAN identifier
        """

        result = self.enode(
            'no vlan trunk native {vlan_id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def lacp_mode_passive(self):
        """
        Sets an interface as LACP passive.

        This function runs the following vtysh command:

        ::

            # lacp mode passive

        """

        result = self.enode(
            'lacp mode passive'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_lacp_mode_passive(self):
        """
        Sets an LACP passive interface off.

        This function runs the following vtysh command:

        ::

            # no lacp mode passive

        """

        result = self.enode(
            'no lacp mode passive'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def lacp_mode_active(self):
        """
        Sets an interface as LACP active.

        This function runs the following vtysh command:

        ::

            # lacp mode active

        """

        result = self.enode(
            'lacp mode active'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_lacp_mode_active(self):
        """
        Sets an LACP active interface off.

        This function runs the following vtysh command:

        ::

            # no lacp mode active

        """

        result = self.enode(
            'no lacp mode active'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def lacp_fallback(self):
        """
        Enable LACP fallback mode.

        This function runs the following vtysh command:

        ::

            # lacp fallback

        """

        result = self.enode(
            'lacp fallback'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def hash_l2_src_dst(self):
        """
        Base the hash on l2-src-dst.

        This function runs the following vtysh command:

        ::

            # hash l2-src-dst

        """

        result = self.enode(
            'hash l2-src-dst'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def hash_l3_src_dst(self):
        """
        Base the hash on l3-src-dst.

        This function runs the following vtysh command:

        ::

            # hash l3-src-dst

        """

        result = self.enode(
            'hash l3-src-dst'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def lacp_rate_fast(self):
        """
        Set LACP heartbeats are requested at the rate of one per second.

        This function runs the following vtysh command:

        ::

            # lacp rate fast

        """

        result = self.enode(
            'lacp rate fast'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_lacp_rate_fast(self):
        """
        Set LACP heartbeats slow which is once every  30 seconds.

        This function runs the following vtysh command:

        ::

            # no lacp rate fast

        """

        result = self.enode(
            'no lacp rate fast'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result


class ConfigInterfaceMgmt(ContextManager):
    """
    Configure management interface.

    pre_commands:

    ::

            ['config terminal', 'interface mgmt']

    post_commands:

    ::

            ['end']
    """
    def __init__(self, enode):
        self.enode = enode

    def __enter__(self):
        commands = """\
            config terminal
            interface mgmt
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

        return self

    def __exit__(self, type, value, traceback):
        commands = """\
            end
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

    def ip_static(self, ip):
        """
        Set IP address

        This function runs the following vtysh command:

        ::

            # ip static {ip}

        :param ip: Interface IP (ipv4 or ipv6) address.
        """

        result = self.enode(
            'ip static {ip}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_ip_static(self, ip):
        """
        Unset IP address

        This function runs the following vtysh command:

        ::

            # no ip static {ip}

        :param ip: Interface IP (ipv4 or ipv6) address.
        """

        result = self.enode(
            'no ip static {ip}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def default_gateway(self, gateway):
        """
        Configure the Default gateway address (IPv4 and IPv6)

        This function runs the following vtysh command:

        ::

            # default-gateway {gateway}

        :param gateway: IP (ipv4 or ipv6) address.
        """

        result = self.enode(
            'default-gateway {gateway}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_default_gateway(self, gateway):
        """
        Remove the Default gateway address (IPv4 and IPv6)

        This function runs the following vtysh command:

        ::

            # no default-gateway {gateway}

        :param gateway: IP (ipv4 or ipv6) address.
        """

        result = self.enode(
            'no default-gateway {gateway}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def nameserver(self, primary_nameserver, secondary_nameserver=''):
        """
        Configure the nameserver

        This function runs the following vtysh command:

        ::

            # nameserver {primary_nameserver} {secondary_nameserver}

        :param primary_nameserver: Primary nameserver (ipv4 or ipv6) address.
        :param secondary_nameserver: Secondary nameserver (ipv4 or ipv6)
            address.
        """

        result = self.enode(
            'nameserver {primary_nameserver} {secondary_nameserver}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_nameserver(self, primary_nameserver, secondary_nameserver=''):
        """
        Configure the nameserver

        This function runs the following vtysh command:

        ::

            # no nameserver {primary_nameserver} {secondary_nameserver}

        :param primary_nameserver: Primary nameserver (ipv4 or ipv6) address.
        :param secondary_nameserver: Secondary nameserver (ipv4 or ipv6)
            address.
        """

        result = self.enode(
            'no nameserver {primary_nameserver} {secondary_nameserver}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def ip_dhcp(self):
        """
        Set the mode as dhcp.

        This function runs the following vtysh command:

        ::

            # ip dhcp

        """

        result = self.enode(
            'ip dhcp'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result


class ConfigRouterBgp(ContextManager):
    """
    BGP configuration.

    pre_commands:

    ::

            ['config terminal', 'router bgp {asn}']

    post_commands:

    ::

            ['end']
    """
    def __init__(self, enode, asn):
        self.enode = enode
        self.asn = asn

    def __enter__(self):
        commands = """\
            config terminal
            router bgp {asn}
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

        return self

    def __exit__(self, type, value, traceback):
        commands = """\
            end
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

    def bgp_router_id(self, id):
        """
        Specifies the BGP router-ID for a BGP Router

        This function runs the following vtysh command:

        ::

            # bgp router-id {id}

        :param id: <A.B.C.D> IPv4 address
        """

        result = self.enode(
            'bgp router-id {id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_bgp_router_id(self, id):
        """
        Removes the BGP router-ID for a BGP Router

        This function runs the following vtysh command:

        ::

            # no bgp router-id {id}

        :param id: <A.B.C.D> IPv4 address
        """

        result = self.enode(
            'no bgp router-id {id}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def network(self, network):
        """
        Adds the announcement network for BGP

        This function runs the following vtysh command:

        ::

            # network {network}

        :param network: <A.B.C.D/M> IPv4 address with the prefix len
        """

        result = self.enode(
            'network {network}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_network(self, network):
        """
        Removes the announcement network for BGP

        This function runs the following vtysh command:

        ::

            # no network {network}

        :param network: <A.B.C.D/M> IPv4 address with the prefix length
        """

        result = self.enode(
            'no network {network}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def maximum_paths(self, num):
        """
        Sets the maximum number of paths for a BGP route

        This function runs the following vtysh command:

        ::

            # maximum-paths {num}

        :param num: <1-255> Maximum number of paths. Default is 1
        """

        result = self.enode(
            'maximum-paths {num}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_maximum_paths(self, num):
        """
        Set the max number of paths to the default value of 1

        This function runs the following vtysh command:

        ::

            # no maximum-paths {num}

        :param num: <1-255> Maximum number of paths. Default is 1
        """

        result = self.enode(
            'no maximum-paths {num}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def timers_bgp(self, keepalive, hold):
        """
        Sets the keepalive interval and hold time for a BGP router

        This function runs the following vtysh command:

        ::

            # timers bgp {keepalive} {hold}

        :param keepalive: <0-65535> Keepalive interval in seconds. Default is
            60
        :param hold: <0 - 65535> Hold time in seconds. Default is 180
        """

        result = self.enode(
            'timers bgp {keepalive} {hold}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_timers_bgp(self, keepalive='', hold=''):
        """
        Sets the default values for keepalive interval and hold time for a BGP
        router

        This function runs the following vtysh command:

        ::

            # no timers bgp {keepalive} {hold}

        :param keepalive: <0 - 65535> Keepalive interval in seconds. Default
            is 60
        :param hold: <0 - 65535> Hold time in seconds. Default is 180
        """

        result = self.enode(
            'no timers bgp {keepalive} {hold}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def neighbor_remote_as(self, ip, asn):
        """
        Configures a BGP neighbor

        This function runs the following vtysh command:

        ::

            # neighbor {ip} remote-as {asn}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param asn: <1 - 4294967295> Neighbor AS number. Ranges from 1 to
            4294967295
        """

        result = self.enode(
            'neighbor {ip} remote-as {asn}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_neighbor(self, ip):
        """
        Removes a BGP neighbor

        This function runs the following vtysh command:

        ::

            # no neighbor {ip}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        """

        result = self.enode(
            'no neighbor {ip}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def neighbor_route_map(self, ip, route_name, action):
        """
        Configures a BGP neighbor route-map

        This function runs the following vtysh command:

        ::

            # neighbor {ip} route-map {route_name} {action}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param route_name: WORD  Name of route map
        :param action: export  Apply map to routes coming
            from a Route-Server
            client
            import  Apply map to routes going into
            a Route-Server client's
            table
            in      Apply map to incoming routes
            out     Apply map to
            outbound routes
        """

        result = self.enode(
            'neighbor {ip} route-map {route_name} {action}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_neighbor_route_map(self, ip, route_name, action):
        """
        Unconfigures a BGP neighbor route-map

        This function runs the following vtysh command:

        ::

            # no neighbor {ip} route-map {route_name} {action}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param route_name: WORD  Name of route map
        :param action: export  Apply map to routes coming
            from a Route-Server
            client
            import  Apply map to routes going into
            a Route-Server client's
            table
            in      Apply map to incoming routes
            out     Apply map to
            outbound routes
        """

        result = self.enode(
            'no neighbor {ip} route-map {route_name} {action}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def neighbor_description(self, ip, text):
        """
        Removes a BGP neighbor

        This function runs the following vtysh command:

        ::

            # neighbor {ip} description {text}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param text: Description of the peer router. String of maximum length
            80 chars
        """

        result = self.enode(
            'neighbor {ip} description {text}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_neighbor_description(self, ip, text=''):
        """
        Removes a BGP neighbor

        This function runs the following vtysh command:

        ::

            # no neighbor {ip} description {text}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param text: Description of the peer router.String of maximum length
            80 chars
        """

        result = self.enode(
            'no neighbor {ip} description {text}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def neighbor_password(self, ip, pwd):
        """
        Enables MD5 authentication on a TCP connection between BGP peers.

        This function runs the following vtysh command:

        ::

            # neighbor {ip} password {pwd}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param pwd: Password in plain text.String of maximum length 80 chars
        """

        result = self.enode(
            'neighbor {ip} password {pwd}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_neighbor_password(self, ip):
        """
        Removes MD5 authentication on a TCP connection between BGP peers.

        This function runs the following vtysh command:

        ::

            # no neighbor {ip} password

        :param ip: <A.B.C.D> Neighbor IPv4 address
        """

        result = self.enode(
            'no neighbor {ip} password'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def neighbor_timers(self, ip, keepalive, hold):
        """
        Sets the keepalive interval and hold time for a specific BGP peer

        This function runs the following vtysh command:

        ::

            # neighbor {ip} timers {keepalive} {hold}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param keepalive: <0 - 65535> Keepalive interval in seconds.Default is
            60
        :param hold: <0-65535> Hold time in seconds. Default is 180
        """

        result = self.enode(
            'neighbor {ip} timers {keepalive} {hold}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_neighbor_timers(self, ip, keepalive='', hold=''):
        """
        Sets the default values for keepalive interval and hold time for a
        specific BGP peer

        This function runs the following vtysh command:

        ::

            # no neighbor {ip} timers {keepalive} {hold}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param keepalive: <0 - 65535> Keepalive interval in seconds.Default is
            0
        :param hold: <0 - 65535> Hold time in seconds. Default is 0
        """

        result = self.enode(
            'no neighbor {ip} timers {keepalive} {hold}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def neighbor_allowas_in(self, ip, val=''):
        """
        Specifies an allow-as-in occurrence number for an AS to be in the AS
        path

        This function runs the following vtysh command:

        ::

            # neighbor {ip} allowas-in {val}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param val: <0 - 10> Number of times BGP can allow an instance of AS
            to be in the AS_PATH
        """

        result = self.enode(
            'neighbor {ip} allowas-in {val}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_neighbor_allowas_in(self, ip, val=''):
        """
        Clears the allow-as-in occurrence number for an AS to be in the AS path

        This function runs the following vtysh command:

        ::

            # no neighbor {ip} allowas-in {val}

        :param ip: <A.B.C.D> Neighbor IPv4 address
        :param val: <0 - 10> Number of times BGP can allow aninstance of AS to
            be in the AS_PATH
        """

        result = self.enode(
            'no neighbor {ip} allowas-in {val}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def neighbor_remove_private_as(self, ip):
        """
        Removes private AS numbers from the AS pathin outbound routing updates

        This function runs the following vtysh command:

        ::

            # neighbor {ip} remove-private-AS

        :param ip: <A.B.C.D> Neighbor IPv4 address
        """

        result = self.enode(
            'neighbor {ip} remove-private-AS'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_neighbor_remove_private_as(self, ip):
        """
        Resets to a cleared state (default)

        This function runs the following vtysh command:

        ::

            # no neighbor {ip} remove-private-AS

        :param ip: <A.B.C.D> Neighbor IPv4 address
        """

        result = self.enode(
            'no neighbor {ip} remove-private-AS'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def neighbor_soft_reconfiguration_inbound(self, ip):
        """
        Enables software-based reconfiguration to generate updates from a
        neighbor without clearing the BGP session

        This function runs the following vtysh command:

        ::

            # neighbor {ip} soft-reconfiguration inbound

        :param ip: <A.B.C.D> Neighbor IPv4 address
        """

        result = self.enode(
            'neighbor {ip} soft-reconfiguration inbound'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_neighbor_soft_reconfiguration_inbound(self, ip):
        """
        Resets to a cleared state (default)

        This function runs the following vtysh command:

        ::

            # no neighbor {ip} soft-reconfiguration inbound

        :param ip: <A.B.C.D> Neighbor IPv4 address
        """

        result = self.enode(
            'no neighbor {ip} soft-reconfiguration inbound'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def neighbor_shutdown(self, ip):
        """
        Shuts down the neighbor. This disables the peer routerbut preserves
        neighbor configuration

        This function runs the following vtysh command:

        ::

            # neighbor {ip} shutdown

        :param ip: <A.B.C.D> Neighbor IPv4 address
        """

        result = self.enode(
            'neighbor {ip} shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_neighbor_shutdown(self, ip):
        """
        Re-enables the neighbor

        This function runs the following vtysh command:

        ::

            # no neighbor {ip} shutdown

        :param ip: <A.B.C.D> Neighbor IPv4 address
        """

        result = self.enode(
            'no neighbor {ip} shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def neighbor_peer_group(self, ip_or_group, group=''):
        """
        Assigns a neighbor to a peer-group

        This function runs the following vtysh command:

        ::

            # neighbor {ip_or_group} peer-group {group}

        :param ip_or_group: <A.B.C.D> Neighbor IPv4 address<X:X::X:X> Neighbor
            IPv6 address<WORD> Neighbor group
        :param group: ('Peer-group name.String of maximum length 80 chars',)
        """

        result = self.enode(
            'neighbor {ip_or_group} peer-group {group}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_neighbor_peer_group(self, ip_or_group, group=''):
        """
        Removes the neighbor from the peer-group

        This function runs the following vtysh command:

        ::

            # no neighbor {ip_or_group} peer-group {group}

        :param ip_or_group: <A.B.C.D> Neighbor IPv4 address<X:X::X:X> Neighbor
            IPv6 address<WORD> Neighbor group
        :param group: Peer-group name. String of maximum length 80 chars
        """

        result = self.enode(
            'no neighbor {ip_or_group} peer-group {group}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result


class ConfigVlan(ContextManager):
    """
    VLAN configuration.

    pre_commands:

    ::

            ['config terminal', 'vlan {vlan_id}']

    post_commands:

    ::

            ['end']
    """
    def __init__(self, enode, vlan_id):
        self.enode = enode
        self.vlan_id = vlan_id

    def __enter__(self):
        commands = """\
            config terminal
            vlan {vlan_id}
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

        return self

    def __exit__(self, type, value, traceback):
        commands = """\
            end
        """

        self.enode.libs.common.assert_batch(
            commands,
            replace=self.__dict__,
            shell='vtysh'
        )

    def shutdown(self):
        """
        Enable the VLAN.

        This function runs the following vtysh command:

        ::

            # shutdown

        """

        result = self.enode(
            'shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_shutdown(self):
        """
        Disable the VLAN.

        This function runs the following vtysh command:

        ::

            # no shutdown

        """

        result = self.enode(
            'no shutdown'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def description(self, description):
        """
        Set VLAN description

        This function runs the following vtysh command:

        ::

            # description {description}

        :param description: VLAN description.
        """

        result = self.enode(
            'description {description}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result

    def no_description(self, description):
        """
        Un-set VLAN description

        This function runs the following vtysh command:

        ::

            # no description {description}

        :param description: VLAN description.
        """

        result = self.enode(
            'no description {description}'.format(
                **locals()
            ),
            shell='vtysh'
        )

        assert not result


def show_interface(enode, portlbl):
    """
    Interface infomation.

    This function runs the following vtysh command:

    ::

        # show interface {port}

    :param portlbl: Label that identifies interface.
    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_interface`
    """
    port = enode.ports.get(portlbl, portlbl)

    result = enode(
        'show interface {port}'.format(**locals()),
        shell='vtysh'
    )

    return parse_show_interface(result)


def show_vlan(enode):
    """
    Show VLAN configuration.

    This function runs the following vtysh command:

    ::

        # show vlan

    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_vlan`
    """

    result = enode(
        'show vlan'.format(**locals()),
        shell='vtysh'
    )

    return parse_show_vlan(result)


def show_lacp_interface(enode, portlbl):
    """
    Show LACP interface.

    This function runs the following vtysh command:

    ::

        # show lacp interface {port}

    :param portlbl: Label that identifies interface.
    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_lacp_interface`
    """
    port = enode.ports.get(portlbl, portlbl)

    result = enode(
        'show lacp interface {port}'.format(**locals()),
        shell='vtysh'
    )

    return parse_show_lacp_interface(result)


def show_lacp_aggregates(enode, lag=''):
    """
    Show LACP aggregates.

    This function runs the following vtysh command:

    ::

        # show lacp aggregates {lag}

    :param lag: Link-aggregate name.
    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_lacp_aggregates`
    """

    result = enode(
        'show lacp aggregates {lag}'.format(**locals()),
        shell='vtysh'
    )

    return parse_show_lacp_aggregates(result)


def show_lacp_configuration(enode):
    """
    Show LACP configuration.

    This function runs the following vtysh command:

    ::

        # show lacp configuration

    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_lacp_configuration`
    """

    result = enode(
        'show lacp configuration'.format(**locals()),
        shell='vtysh'
    )

    return parse_show_lacp_configuration(result)


def show_lldp_neighbor_info(enode, portlbl):
    """
    Show global LLDP neighbor information.

    This function runs the following vtysh command:

    ::

        # show lldp neighbor-info {port}

    :param portlbl: Label that identifies interface.
    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_lldp_neighbor_info`
    """
    port = enode.ports.get(portlbl, portlbl)

    result = enode(
        'show lldp neighbor-info {port}'.format(**locals()),
        shell='vtysh'
    )

    return parse_show_lldp_neighbor_info(result)


def show_lldp_statistics(enode):
    """
    Show LLDP statistics.

    This function runs the following vtysh command:

    ::

        # show lldp statistics

    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_lldp_statistics`
    """

    result = enode(
        'show lldp statistics'.format(**locals()),
        shell='vtysh'
    )

    return parse_show_lldp_statistics(result)


def show_ip_bgp_summary(enode):
    """
    Show bgp neighbors information summary.

    This function runs the following vtysh command:

    ::

        # show ip bgp summary

    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_ip_bgp_summary`
    """

    result = enode(
        'show ip bgp summary'.format(**locals()),
        shell='vtysh'
    )

    return parse_show_ip_bgp_summary(result)


def show_ip_bgp_neighbors(enode):
    """
    Show bgp neighbors information.

    This function runs the following vtysh command:

    ::

        # show ip bgp neighbors

    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_ip_bgp_neighbors`
    """

    result = enode(
        'show ip bgp neighbors'.format(**locals()),
        shell='vtysh'
    )

    return parse_show_ip_bgp_neighbors(result)


def show_ip_bgp(enode):
    """
    Show bgp routing information.

    This function runs the following vtysh command:

    ::

        # show ip bgp

    :return: A dictionary as returned by \
        :func:`topology_lib_vtysh.parser.parse_show_ip_bgp`
    """

    result = enode(
        'show ip bgp'.format(**locals()),
        shell='vtysh'
    )

    return parse_show_ip_bgp(result)


__all__ = [
    'ContextManager',
    'Configure',
    'RouteMap',
    'ConfigInterface',
    'ConfigInterfaceVlan',
    'ConfigInterfaceLag',
    'ConfigInterfaceMgmt',
    'ConfigRouterBgp',
    'ConfigVlan',
    'show_interface',
    'show_vlan',
    'show_lacp_interface',
    'show_lacp_aggregates',
    'show_lacp_configuration',
    'show_lldp_neighbor_info',
    'show_lldp_statistics',
    'show_ip_bgp_summary',
    'show_ip_bgp_neighbors',
    'show_ip_bgp'
]
