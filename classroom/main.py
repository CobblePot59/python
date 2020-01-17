import socket
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("You can access on this server by " + str(s.getsockname()[0]) + ":4269")
s.close()

command='gunicorn --worker-class eventlet -w 1 --log-level info --bind 0.0.0.0:4269 app'
#command='gunicorn -w 1 --log-level info --bind 0.0.0.0:4269 app'
process=subprocess.Popen(command, shell=True)
process.communicate()
