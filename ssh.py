import paramiko

host = '***'
port = ***
user = '***'
password = '***'

connect = paramiko.SSHClient()
connect.set_missing_host_key_policy(paramiko.AutoAddPolicy())
connect.connect(hostname=host, username=user, password=password, port=port)

download = connect.open_sftp()
download.chdir('***')
fileList = download.listdir()
currentDir = download.getcwd()
download.put('***','***')
connect.close()
