from twisted.internet import protocol, reactor
import itertools


transports = set()

colors = itertools.cycle(("7F8C8D", "C0392B", "2C3E50", "8E44AD", "27AE60"))


class Chat(protocol.Protocol):

    def connectionMade(self):
        self.color = colors.next()
        colors.insert(0, self.color)

    def dataReceived(self, data):
        transports.add(self.transport)

        if ":" not in data:
            return

        user, msg = data.split(":", 1)

        for t in transports:
            if t is not self.transport:
                t.write("[b][color={}]{}:[/color][/b]{}"
                        .format(self.color, user, esc_markup(msg)))


class ChatFactory(protocol.Factory):

    def buildProtocol(self, addr):
        return Chat()

reactor.listenTCP(9096, ChatFactory())
reactor.run()
