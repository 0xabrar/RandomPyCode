from twisted.internet import protocol, reactor

transports = set()


class Chat(protocol.Protocol):

    def dataReceived(self, data):
        transports.add(self.transport)

        if ":" not in data:
            return

        use, msg = data.split(":", 1)

        for t in transports:
            if t is not self.transport:
                t.write("{0} says: {1}".format(user, msg))


class ChatFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return Chat()

reactor.listenTCP(9096, ChatFactory())
reactor.run()
