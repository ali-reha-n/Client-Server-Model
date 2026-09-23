# Client-Server Model

Simple Python examples of client-server communication using TCP and UDP sockets. The client sends a message to the server, and the server sends back the message in uppercase.

## Files

- `TCPServer.py` / `TCPClient.py` — client-server communication over TCP
- `UDPServer.py` / `UDPClient.py` — client-server communication over UDP

## Usage

**TCP**

```bash
python TCPServer.py
python TCPClient.py
```

**UDP**

```bash
python UDPServer.py
python UDPClient.py
```

Run the server first, then the client, in separate terminals. Type a message in the client — the server will respond with the same message in uppercase.
