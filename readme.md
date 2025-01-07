IP Locator Documentation
The IP Locator is a Python program designed to retrieve the geographical location information of IPv4 addresses using the ip-api.com API. This program takes as input a specified number of IPv4 addresses, queries the API for their geographical details, and then provides the country, state, and city information as a response.

Disclaimer
This program is provided as-is, and the developers are not responsible for any misuse or inaccuracies in the location information provided by the ip-api.com API.

Prerequisites
Python 3.x installed on your system.
An active internet connection to access the ip-api.com API.
Installation
Download or clone the IP Locator repository from GitHub.
Navigate to the project directory in your terminal.
Usage
1. Open a terminal window and navigate to the directory where the program is located.
2. Run the program using the following command:

	python ip_locator.py

The program will prompt you to enter the number of IPv4 addresses you want to locate.

3. Enter the IPv4 addresses one by one, and the program will query the ip-api.com API for location information.
4. Once all IP addresses are entered, the program will display the country, state, and city details for each IP address.

Example
	Copy code
	Welcome to IP Locator!
	Please enter the number of IPv4 addresses you want to locate: 2

	Enter IPv4 address 1: 8.8.8.8
	Enter IPv4 address 2: 216.58.206.46


Note
This program is designed to work with IPv4 addresses only.
The program relies on the ip-api.com API to perform IP address location searches.
The accuracy and availability of the location information are subject to the ip-api.com service.
This program does not store or save any of the entered IP addresses or location information.
Credits
This IP Locator program was developed by [Your Name]. You can find the source code and contribute to the project on GitHub.


