from os import pipe
import subprocess
import sys
import os

class CuemsDeploy():

    def __init__(self, library_path=None, address=None, log_file=None):
        
        if not address:
            self.address = 'rsync://cuems_library_rsync@master.local/cuems'
        else:
            self.address = address
        
        if not library_path:
            self.library_path = '/opt/cuems_library/'
        else:
            self.library_path = library_path

        if not log_file:
            self.log_file = '/tmp/cuems_rsync.log'
        else:
            self.log_file = log_file

        self.errors = None

        

        


    def sync(self, path):
        #rsync -rv --files-from=/opt/cuems_library/files.tmp --log-file=/tmp/cuems_rsync.log rsync://master.local/cuems /opt/cuems_library/
        try:
            result = subprocess.run(['rsync', '-rq', '--stats', f'--files-from={path}', f'--log-file={self.log_file}', self.address, self.library_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=dict(os.environ, RSYNC_PASSWORD="f48t5eL2kLHw2Wfw"))
            result.check_returncode()
            self.errors = None
            return True
        except subprocess.CalledProcessError as e:
            #print('exit code: {}'.format(e.returncode))
            #print('stdout: {}'.format(e.output.decode(sys.getfilesystemencoding())))
            #print('stderr: {}'.format(e.stderr.decode(sys.getfilesystemencoding())))
            
            errors_string = e.stderr.decode(sys.getfilesystemencoding())
            
            #convert lines to list and remove last line (final error menssage)
            errors_list = errors_string.splitlines()
            errors_list.pop()
            self.errors = errors_list
            return False

