from lr_2 import Daemon
import sys
import time
import subprocess
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify


class MyDaemon(Daemon):
    def run(self):

        Notify.init("MyDaemon")

        while True:
            subprocess.run(['cd', '~/projects/pythops/lr_2/testing2'])
            subprocess.run(['git', 'fetch'])
            result = subprocess.run(['git', 'log', '--graph', '--pretty=format:%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset', '--abbrev-commit', '--date=relative', 'master..origin/master'], capture_output=True, text=True)
            output = result.stdout

            if output:
                Notify.Notification.new(output).show()
                
            time.sleep(5)


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




