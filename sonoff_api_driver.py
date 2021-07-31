import requests
from abstracts import PowerSwitch
from logger import Logger
from time import sleep

logger = Logger()

class SonoffConnection(PowerSwitch):

    def __init__(self, device_id, device_IP):
        """

        :param device_id: [description]
        :type device_id: [type]
        :param device_IP: [description]
        :type device_IP: [type]
        """

        self.device_id = device_id
        self.device_IP = device_IP

    def build_request(self, command):

        commands_to_data_map = {"turn_on": {"switch": "on"},
                                "turn_off": {"switch": "off"}, "get_info": {}}

        request_body = {
            "deviceid": self.device_id,
            "data": commands_to_data_map[command]
        }

        return request_body

    def send_command(self, command):

        request_body = self.build_request(command)
        paths_for_commands = {"turn_on": "switch",
                              "turn_off": "switch", "get_info": "info"}
        path = paths_for_commands[command]
        try:
            response = requests.post(
                f"http://{self.device_IP}:8081/zeroconf/{path}", json=request_body)
        except requests.exceptions.ConnectionError as ex:
            logger.error(
                f"Attempt to connect to {self.device_id} was unsuccesfull. Error:= {ex}")
            return
        return response.json()

    def is_on(self):
        instance_info = self.send_command("get_info")
        try:
            if instance_info["data"]["switch"] == "on":
                return True
            else:
                return False
        except:
            return False

    def turn_on(self, max_retry_attmeps=5):
        for _ in range(max_retry_attmeps):
            if not self.is_on():
                self.send_command("turn_on")
                sleep(2)
            else:
                break

    def turn_off(self, max_retry_attmeps=5):
        for _ in range(max_retry_attmeps):
            if self.is_on():
                self.send_command("turn_off")
                sleep(2)
            else:
                break
