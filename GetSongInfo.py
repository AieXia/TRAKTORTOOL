import socket
import re

HOST = 'localhost'
PORT = 8000
connected = False
artist_title_re = re.compile("ARTIST=(.*)TITLE=(.*)vorbis")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr

def response_ok(conn):
    conn.send('HTTP/1.0 200 OK\r\n\r\n')

while 1:
    data = conn.recv(8192)
    if not data: break
    if not connected:
        response_ok(conn)
        connected = True
    at = artist_title_re.search(data)
    if at:
        print at.group(1), at.group(2)

conn.close()
