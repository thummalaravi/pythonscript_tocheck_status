import subprocess
import json
import socket
import time

services = ["httpd", "rabbitmq-server", "postgresql"]
for service in services:
  p =  subprocess.Popen(["systemctl", "is-active",  service], stdout=subprocess.PIPE)
  (output, err) = p.communicate()
  output = output.decode('utf-8').rstrip()
  if output == "active":
    status = "UP"
  else:
    status = "DOWN"
  service_info = {
    "service_name": service,
    "service_status": status,
    "host_name": socket.gethostname()
  }
  named_tuple = time.localtime() # get struct_time
  time_stamp = time.strftime("%m%d%Y-%H%M%S", named_tuple)
  my_file=open("%s-status-%s.json" %(service, time_stamp), "w")
  json_data = json.dumps(service_info)
  print(json_data)
  my_file.write(json_data+'\n')
