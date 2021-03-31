# These functions need to be implemented
from ipaddress import IPv4Network,NetmaskValueError
import socket
import struct


class CidrMaskConvert:

    def cidr_to_mask(self, val):
        host_bits = 32 - int(val)
        try:
            netmask = socket.inet_ntoa(struct.pack('!I', (1 << 32) - (1 << host_bits)))
        except:
            return 'Invalid'
        if netmask == '0.0.0.0':
            return 'Invalid'
        return str(netmask)

    def mask_to_cidr(self, val):
        try:
            cidr = IPv4Network((0, val)).prefixlen
        except NetmaskValueError:
            return 'Invalid'
        if cidr == 0:
            return 'Invalid'
        return str(cidr)


