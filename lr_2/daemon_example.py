from lr_2 import Daemon
import sys
import time
import subprocess
# from gi.repository import Notify


class MyDaemon(Daemon):
    def run(self):
        # Notify.init("MyDaemon")
        # Notify.Notification.new("Test notification!").show()
        while True:
            time.sleep(1)

daemon = MyDaemon('/tmp/daemon-example.pid')

arg = None

try:
    arg = sys.argv[1]
except:
    print('ERROR: No arguments were given!')


if arg == 'start': 
    daemon.start()
elif arg == 'stop': 
    daemon.stop()
elif arg == 'restart': 
    daemon.restart()
else:
    print('ERROR: Daemon not launched!')


subprocess.run('git fetch')
subprocess.run("git log --graph --pretty=format:'%Cred%h%Creset-%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset' --abbrev-commit --date=relative master..origin/master")
