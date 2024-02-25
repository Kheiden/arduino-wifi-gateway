from os import environ as env
from dotenv import find_dotenv, load_dotenv

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

SECRET_SSID = env.get('SECRET_SSID')
SECRET_PASS = env.get('SECRET_PASS')

with open(f'output_source/ArduinoCode/ArduinoCode.ino', 'w') as f:
  # Add Header
  with open('create_source/header.txt', 'r') as header:
    f.write(header.read())
  # Add index
  with open(f'create_source/index.html', 'r') as index:
  # Write custom code here
    f.write('\n')
    for line in index.readlines():
      line = line.replace("\\", '\\\\')
      line = line.replace('"', '\\"')
      line = line.replace('\n', '')
      line = f'            client.print("{line}");\n'
      f.writelines([line])
  # Add Footer
  with open('create_source/footer.txt', 'r') as footer:
    f.write(footer.read())
  
with open(f'output_source/ArduinoCode/arduino_secrets.h', 'w') as f:
  secrets_list = [
    f'#define SECRET_SSID "{SECRET_SSID}"',
    '\n',
    f'#define SECRET_PASS "{SECRET_PASS}"'
  ]
  f.writelines(secrets_list)