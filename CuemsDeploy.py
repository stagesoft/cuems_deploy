import subprocess

class CuemsDeploy():

    def __init__(self):
        self.log_file = './cuems_rsync.log'
        self.address = 'rsync://master.local/cuems'
        self.library_path = '/opt/cuems_library/'

    def sync(self, path):
        #rsync -rv --files-from=/opt/cuems_library/files.tmp --log-file=/tmp/cuems_rsync.log rsync://master.local/cuems /opt/cuems_library/
        result = subprocess.run(['rsync', '-rv', f'--files-from={path}', f'--log-file={self.log_file}', self.address, self.library_path])
        print(result)

d = CuemsDeploy()
d.sync('/opt/cuems_library/files.tmp')
