"""
ESP32 Motor Controller

This module provides a controller for ESP32-based motor control over HTTP.
It handles communication with an ESP32 web server to control motor movements.
"""

import requests
from time import sleep
from typing import Optional


class ESPController:
    """Controller for ESP32-based motor control.
    
    Args:
        base_url (str): Base URL of the ESP32 web server (e.g., "http://192.168.1.56/")
        direction (str): Initial direction setting (e.g., "forward", "backward")
        timeout (int, optional): Request timeout in seconds. Defaults to 5.
    """
    
    def __init__(self, base_url: str, direction: str, timeout: int = 5):
        if not base_url.endswith('/'):
            base_url += '/'
        self.base_url = base_url
        self.direction = direction
        self.timeout = timeout

    def _make_request(self, endpoint: str) -> Optional[str]:
        """Make an HTTP GET request to the ESP32 server.
        
        Args:
            endpoint (str): API endpoint to call
            
        Returns:
            Optional[str]: Response text if successful, None otherwise
        """
        try:
            response = requests.get(f"{self.base_url}{endpoint}", timeout=self.timeout)
            response.raise_for_status()
            return response.text.strip()
        except requests.exceptions.RequestException as e:
            print(f"Error making request to {endpoint}: {e}")
            return None

    def disable(self) -> str:
        """Disable the motor.
        
        Returns:
            str: Status message
        """
        if self._make_request("off") is not None:
            return "Motor disabled"
        return "Error disabling motor"

    def enable(self) -> str:
        """Enable the motor.
        
        Returns:
            str: Status message
        """
        if self._make_request("on") is not None:
            return "Motor enabled"
        return "Error enabling motor"

    def step(self, steps: int) -> str:
        """Move the motor a specified number of steps.
        
        Args:
            steps (int): Number of steps to move
            
        Returns:
            str: Status message
        """
        if self._make_request(f"step/{steps}") is not None:
            return f"Moved {steps} steps {self.direction}"
        return "Error moving motor"

    def status(self) -> str:
        """Get the current status of the motor.
        
        Returns:
            str: Status message
        """
        status = self._make_request("status")
        return f"Motor status: {status}" if status else "Error getting motor status"

    def check_limit_switch(self) -> Optional[bool]:
        """Check the state of the limit switch.
        
        Returns:
            Optional[bool]: True if limit switch is triggered, False if not, None on error
        """
        response = self._make_request("limitSwitch")
        if response:
            try:
                state = response.split(":")[1].strip().lower()
                return state == "true"
            except (IndexError, ValueError):
                pass
        return None


def create_esp_controller(ip_address: str = "192.168.1.56", direction: str = "forward") -> ESPController:
    """Create a new ESPController instance with the specified configuration.
    
    Args:
        ip_address (str): IP address of the ESP32 device
        direction (str): Initial direction setting
        
    Returns:
        ESPController: Configured ESPController instance
    """
    base_url = f"http://{ip_address}/"
    return ESPController(base_url=base_url, direction=direction)


# Example usage
if __name__ == "__main__":
    # Example usage
    controller = create_esp_controller("192.168.1.56", "forward")
    
    try:
        print(controller.enable())
        print(controller.step(100))
        print(controller.check_limit_switch())
        print(controller.status())
        print(controller.disable())
    except KeyboardInterrupt:
        print("\nExiting...")
        controller.disable()
