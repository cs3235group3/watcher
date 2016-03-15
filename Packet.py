class Packet(object):

    def __init__(self, sender_ip, sender_mac,
            dst_ip, dst_mac):
        self.sender_ip = sender_ip
        self.sender_mac = sender_mac
        self.dst_ip = dst_ip
        self.dst_mac = dst_mac

    def getSenderIP():
        return self.sender_ip

    def getSenderMac():
        return self.sender_mac

    def getDstIp():
        return self.dst_ip

    def getDstMac():
        return self.dst_mac
