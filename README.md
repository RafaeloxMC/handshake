# Verify integrity in Python

This tool can test if a hash was created on a specific server

# Usage

Start your server using `py Server.py` (elevated) or on Linux `sudo python3 Server.py`

(If you want to change ports or IPs, do this in the Server.py at the very top. The variables are called `host` and `port` and their defaults are `localhost` or `0.0.0.0` (you probably shouldn't change the host, if you don't know, what you're doing) and `9999` for the port.

As you can see, a file called `secret` will be created on the server. __DO NOT SHARE THIS__ or people will be able to clone your server's integrity keys!

Now simply run the file called Client.py (for commands check the server part above) and everything should work perfectly fine. If you changed variables for the server, you need to do this here as well.
