import argparse
import sys
import socket
import struct

###########################################################
####################### YOUR CODE #########################
###########################################################


def server(server_ip, server_port):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((server_ip, server_port))
        s.listen()
        while True:
            conn, addr = s.accept()
            size = conn.recv(4)
            size = struct.unpack('<I', size)
            data = conn.recv(size[0])
            if not data:
                break
            print(data.decode())
            conn.close()
        s.close()


###########################################################
##################### END OF YOUR CODE ####################
###########################################################


def get_args():
    parser = argparse.ArgumentParser(description='server ip and port')
    parser.add_argument('server_ip', type=str,
                        help='the server\'s ip')
    parser.add_argument('server_port', type=int,
                        help='the server\'s port')
    return parser.parse_args()


def main():
    '''
    Implementation of CLI and sending data to server.
    '''
    args = get_args()
    try:
        server(args.server_ip, args.server_port)
        print('Done.')
    except Exception as error:
        print(f'ERROR: {error}')
        return 1


if __name__ == '__main__':
    sys.exit(main())