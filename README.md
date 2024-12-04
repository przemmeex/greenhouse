# Greenhouse Monitoring System

## Overview
The Greenhouse Monitoring System is designed to help you keep track of the environmental conditions in your greenhouse. It monitors temperature, humidity, and light levels, alerting you when conditions fall outside optimal ranges.

## Features
- **Temperature Monitoring**: Keeps track of the temperature inside the greenhouse.
- **Humidity Monitoring**: Measures the humidity levels to ensure they are within the desired range.
- **Light Monitoring**: Monitors the light levels to ensure plants receive adequate light.
- **Alerts**: Sends alerts when conditions are not optimal.

## Technologies Used
- **ESP32**: Microcontroller used for data collection and processing.
- **DHT22 Sensor**: Measures temperature and humidity.
- **Photoresistor (LDR)**: Measures light intensity.
- **MQTT**: Protocol used for sending data to a dashboard.
- **Adafruit IO**: Platform used for visualizing data.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/przemmeex/greenhouse.git
    ```
2. Navigate to the project directory:
    ```bash
    cd greenhouse
    ```
3. Install the required libraries:
    - ESP32 board support
    - DHT sensor library
    - Adafruit IO library

## Usage
1. Connect the sensors to the ESP32 as per the circuit diagram.
2. Upload the code to the ESP32 using the Arduino IDE.
3. Open the serial monitor to check the sensor readings.
4. View the data on the Adafruit IO dashboard.

## Circuit Diagram
!Circuit Diagram

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any questions or suggestions, please open an issue or contact the repository owner.
