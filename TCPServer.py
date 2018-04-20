import socketserver
import foo_pb2

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024)

        msg = foo_pb2.Person()
        msg.ParseFromString(self.data)
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        msg.name = "server msg"
        encode = msg.SerializeToString()
        print("Message: {}".format(msg.__str__()))
        self.request.sendall(encode)

    # @classmethod
    # def test(cls):
    #     """
    #
    #
    #     :return:
    #     """
    #     pass

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()


# class Session(socketserver.BaseRequestHandler):
#     def handle(self):
#         header = self.request.recv(4)
#         message_length, = unpack('>I', header)
#         print(message_length)
#
#         message = self.request.recv(message_length)
#         pb_message = foo_pb2.Person()
#         pb_message.ParseFromString(message)
#
#         print("Message: " + pb_message.cont)
#
# if __name__ == "__main__":
#     HOST, PORT = "localhost", 9999
#     server = socketserver.TCPServer((HOST, PORT), Session)
#     server.serve_forever()