from twisted.internet import reactor, protocol

class ChatClientFactory(protocol.ClientFactory):
	protocol = ChatClient

	def __init__(self, app):
		self.app = app

class ChatClient(protocol.Protocol):
	def connectionMade(self):
		self.transport.write("CONNECT")
		self.factor.app.on_connect(self.transport)

	def dataReceived(self, data):
		self.factory.app.on_message(data)