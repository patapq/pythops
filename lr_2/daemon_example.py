import os, sys
import pathlib
from daemon import Daemon
import time
import subprocess
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify


cwd = pathlib.Path(__file__).parent.resolve()


def fetch_log(folder):
    subprocess.run(['git', f'--git-dir={cwd}/{folder}/.git', 'fetch'])
    result = subprocess.run(['git', f'--git-dir={cwd}/{folder}/.git', 'log', '--graph', "--pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr)%Creset'", '--abbrev-commit', '--date=relative', 'master..origin/master'], text=True, capture_output=True)
    output = result.stdout
    return output



class MyDaemon(Daemon):
    def run(self):

        Notify.init("MyDaemon")
        time.sleep(1)
        folder_names = [name for name in os.listdir(cwd) if os.path.isdir(f'{cwd}/{name}')]

        while True:

            for folder in folder_names:
                output = fetch_log(folder)
            
                if output:
                    Notify.Notification.new(f'FOLDER {folder}', output).show()


            time.sleep(15)


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




