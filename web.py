from http.server import HTTPServer, BaseHTTPRequestHandler
content = """

<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Protocol Suite</title>
    <style>
        body {
            font-family: Arial;
            background-color: #e6f7f2;
            text-align: center;
            padding: 15px;
        }

        h1 {
            color: #14532d;
        }

        .box {
            background: white;
            width: 80%;
            margin: 12px auto;
            padding: 10px;
            border-radius: 8px;
            border: 1px solid #a7d7c5;
        }

        h3 {
            color: #16805d;
            margin: 5px;
        }

        span {
            display: inline-block;
            background: #d1fae5;
            color: #065f46;
            padding: 7px 12px;
            margin: 4px;
            border-radius: 5px;
            font-size: 14px;
        }

        footer {
            color: #14532d;
            margin-top: 18px;
        }
    </style>
</head>

<body>

    <h1>TCP/IP Protocol Suite</h1>
    <p>Understanding the Four Layers of Networking</p>

    <div class="box">
        <h3>01 - Application Layer</h3>
        <span>HTTP</span><span>HTTPS</span><span>FTP</span>
        <span>SMTP</span><span>DNS</span><span>DHCP</span>
    </div>

    <div class="box">
        <h3>02 - Transport Layer</h3>
        <span>TCP</span><span>UDP</span>
    </div>

    <div class="box">
        <h3>03 - Internet Layer</h3>
        <span>IP</span><span>ICMP</span><span>IGMP</span><span>ARP</span>
    </div>

    <div class="box">
        <h3>04 - Network Access Layer</h3>
        <span>Ethernet</span><span>Wi-Fi</span><span>PPP</span>
    </div>

    <footer>
        <b>Learn • Connect • Communicate</b>
    </footer>

</body>
</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',420)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
