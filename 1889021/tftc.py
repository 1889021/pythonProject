import socket
import argparse
from struct import pack

DEFAULT_PORT = 69
BLOCK_SIZE = 512
DEFAULT_TRANSFER_MODE = 'netascii'

OPCODE = {'RRQ': 1, 'WRQ': 2, 'DATA': 3, 'ACK': 4, 'ERROR': 5}
MODE = {'netascii': 1,'octet': 2, 'mail': 3}

ERROR_CODE = {
    0: "Not defined, see error message (if any).",
    1: "File not found.",
    2: "Access violation.",
    3: "Disk full or allocation exceeded.",
    4: "Illegal TFTP operation.",
    5: "Unknown transfer ID.",
    6: "File already exists.",
    7: "No such user."
}

def send_wrq(filename, mode):
    format = f'>h{len(filename)}sB{len(mode)}sB'
    wrq_message = pack(format, OPCODE['WRQ'], bytes(filename, 'utf-8'), 0, bytes(mode, 'utf-8'), 0)
    sock.sendto(wrq_message, server_address)

def send_rrq(filename, mode):
    format = f'>h{len(filename)}sB{len(mode)}sB'
    rrq_message = pack(format, OPCODE['RRQ'], bytes(filename, 'utf-8'), 0, bytes(mode, 'utf-8'), 0)
    sock.sendto(rrq_message, server_address)

def send_ack(seq_num, server):
    format = f'>hh'
    ack_message = pack(format, OPCODE['ACK'], seq_num)
    sock.sendto(ack_message, server)

# parse command line arguments
parser = argparse.ArgumentParser(description='TFTP client program')
parser.add_argument(dest="host", help="Server IP address", type=str)
parser.add_argument(dest="action", help="get or put a file", type=str)
parser.add_argument(dest="filename", help="name of file to transfer", type=str)
parser.add_argument("-p", "--port", dest="port", action="store", type=int)
args = parser.parse_args()

server_ip = args.host
server_port = DEFAULT_PORT
server_address = (server_ip, server_port)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

if args.action == 'put':
    mode = DEFAULT_TRANSFER_MODE
    filename = args.filename
    send_wrq(filename, mode)
    file = open(filename, "rb")
    seq_number = 0
    while True:
        # Read data from the file
        file_block = file.read(BLOCK_SIZE)
        if not file_block:
            break

        # Prepare DATA message
        format = f'>hh{len(file_block)}s'
        data_message = pack(format, OPCODE['DATA'], seq_number, file_block)
        sock.sendto(data_message, server_address)

        # Wait for ACK from the server
        ack_received = False
        while not ack_received:
            try:
                ack_data, server = sock.recvfrom(4)
                ack_opcode = int.from_bytes(ack_data[:2], 'big')
                ack_seq_number = int.from_bytes(ack_data[2:], 'big')
                if ack_opcode == OPCODE['ACK'] and ack_seq_number == seq_number:
                    ack_received = True
            except socket.timeout:
                # Resend the data if timeout occurs
                sock.sendto(data_message, server_address)

        seq_number += 1

    file.close()
    sock.close()
    print("File transfer complete.")
else:
    # Send RRQ message for get action
    mode = DEFAULT_TRANSFER_MODE
    filename = args.filename
    send_rrq(filename, mode)

    # Open a file with the same name to save data from the server
    file = open(filename, "wb")
    seq_number = 0

    while True:
        # Receive data from the server
        data, server = sock.recvfrom(516)
        opcode = int.from_bytes(data[:2], 'big')

        if opcode == OPCODE['DATA']:
            seq_number = int.from_bytes(data[2:4], 'big')
            send_ack(seq_number, server)

            file_block = data[4:]
            file.write(file_block)

            if len(file_block) < BLOCK_SIZE:
                file.close()
                break

    sock.close()
    print("File received and saved.")

