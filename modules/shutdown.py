import subprocess

class Addon():
    service = 'shutdown'
    name = 'Shutdown'
    icon = 'mdi:power'
    unit = 'json'

    def startControl(self, topic, data):
        print(topic, data)
        subprocess.call(["shutdown", "now"])
