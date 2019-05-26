import socket
from genetic_tests import *

IP = '64.187.254.184'


class SocketServer:

    def __init__(self, ip, port=8888, max_connections=10):

        self.ip = ip

        self.port = port

        self.server = socket.socket()

        self.comm_codes = {'begin file transfer': b'[/beftran/]', 'end file transfer': b'[/enftran/]',
                           'stay connected': b'[/staycon/]', 'terminate connection': b'[/termcon/]'}

        self.clients = []

        self.max_connections = max_connections

        self.server.settimeout(0)

        self.setup()

    def command(self, command_name, server_id):

        self.clients[server_id].send(self.comm_codes[command_name])

    def recieve(self, id):

        self.command('begin file transfer', id)  # signal to the host that the client is waiting for the data

        received = b''

        while True:

            data = self.try_recv(4096, id)  # try to get 4096 bytes of data

            if data is not None:

                if data.endswith(self.comm_codes['end file transfer']):

                    received += data[:-len(self.comm_codes['end file transfer'])]

                    break

                else:

                    received += data

        return received

    def send(self, obj, id):

        self.command('begin file transfer', id)

        while True:

            data = self.try_recv(4096, id)  # try to grab data from host

            if data is not None:  # if receiving data then continue

                if data.startswith(self.comm_codes['begin file transfer']):  # if host tells the client to send data

                    self.clients[id].send(obj)  # send data

                    self.command('end file transfer', id)  # tell host the data transfer is finished

                    break

    def close_all(self):

        for id in range(len(self.clients)):

            self.close(id)

    def __del__(self):

        self.close_all()

    def setup(self):

        self.server.bind((self.ip, self.port))

        self.server.listen(self.max_connections)

    def close(self, id):

        self.command('terminate connection', id)

        while True:

            data = self.try_recv(4096, id)  # try to grab data from host

            if data is not None:  # if receiving data then continue

                if data.startswith(self.comm_codes['terminate connection']):

                    del self.clients[id]

    def update(self):

        received = {}

        for id in range(len(self.clients)):

            data = self.try_recv(4096, id)

            if data == self.comm_codes['begin file transfer']:

                received[id] = self.recieve(id)

            elif data == self.comm_codes['terminate connection']:

                self.command('terminate connection', id)

            else:

                received[id] = None

        return received

    def try_accept(self):

        if len(self.clients) < self.max_connections:

            try:

                conn, details = self.server.accept()

                self.clients.append(conn)

                return True

            except:

                return False

        else:

            return False

    def try_recv(self, buffsize, id):

        try:

            return self.clients[id].recv(buffsize)

        except:

            return None


server = SocketServer(IP, max_connections=10, port=9006)


while True:

    if server.try_accept():

        print('Testing...')

    client_info = server.update()

    for id in client_info:

        info = client_info[id]

        if info is not None:

            print('Receiving data...')

            with open('temp.png', 'wb') as f:

                f.write(info)

            image = load_image('temp.png')

            results = fonconi_anemia_test(image)

            if results:

                server.send(b'You may suffer from Foconi Anemia :(', id)

            else:

                server.send(b'You are fine :)', id)

            image.show()

            time.sleep(5)

            end()



