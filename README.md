# WARNING
The webUI is not finished, some functions may not work.

# deemix
## What is deemix?
deemix is a deezer downloader built from the ashes of Deezloader Remix. The base library (or core) can be used as a stand alone CLI app or implemented in an UI using the API.

## How can I use this?
Currently there are no available builds as it's still in development.<br>
But you can try to run it yourself!<br>

## Running instructions
### Standard way
NOTE: Python 3 is required for this app. Make sure you tick the option to add python to PATH when installing.<br>
NOTE: If `pip3` and `python3` are "not recognized commands" try using `pip` and `python` instead<br>
<br>
After installing python install the dependencies using `pip3 install -r requirements.txt`<br>
Run `python3 -m deemix --help` to see how to use the app<br>
Run `python3 server.py` to start the server and then connect to 127.0.0.1:33333.<br>
Enjoy!<br>

### Easy Windows way
Download `install.bat` file to your PC and place it in the folder where you want Deemix to live<br>
Start the `install.bat` as administrator<br>
Wait for it to finish, then run the `start.bat`<br>

## What's left to do?
Library:
- Add a log system
- Adding whatever is missing for the webUI
- Write the API Documentation

WebUI:
- Stylize and separate the options in the Settings tab
- Home tab
- About Section
- Animations and style polishing
- ?

# License
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
