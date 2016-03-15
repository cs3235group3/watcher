class Packet(object):

    def __init__(self, sender_ip, sender_mac,
            dst_ip, dst_mac):
        self.sender_ip = sender_ip
        self.sender_mac = sender_mac
        self.dst_ip = dst_ip
        self.dst_mac = dst_mac

    def getSenderIp(self):
        return self.sender_ip

    def getSenderMac(self):
        return self.sender_mac

    def getDstIp(self):
        return self.dst_ip

    def getDstMac(self):
        return self.dst_mac
