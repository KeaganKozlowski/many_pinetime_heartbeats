# Breakdowns of the files in Legacy and their libraries

## Context
### What is the Legacy Folder?
The point of this folder is that it contains multiple scripting to assist with connecting pinetime watches to the other series of scripts that is the many_pinetime_heartbeats project. 

### External Libraries
#### Numpy
[Numpy Documentation](https://numpy.org/doc/1.26/)<br>
#### bleak - Bluetooth Low Energy platform Agnostic Klient
[bleak Documentation](https://bleak.readthedocs.io/en/latest/index.html)<br>
### Internal functions and modules
#### asyncio
[asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
#### typing
[typing Documentation](https://docs.python.org/3/library/typing.html)<br>
[typing Cheat Sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)
### Errors in this folder
* bleak
  * bleak library is "randomly" disconnecting
  * There are two possibilities I can think of for this error
    * One of the files which handles connection to the watches has a logic error
    * The library is behaving in a way we weren't expecting
  * Two solutions to above
    * Implementing try and catch statement to understand the logic error
    * Look through library documentation/potentially talk to library developer and ask them for a technical explaination

## Files
### Main

### Many devices

### Multiple devices
The purpose of this file is to:
* Connect to a watch based on address given as input
  * If cannot connect to device output error to user
  * Else 
### new
The purpose of this file is to:
* Connect to a watch based on a address given to it
* Wait for the watch to generate data such as
  * Heartrate
  * Step count
  * Raw data (Not 100% what this entails)
* Output the data it has collected back to the user
* Or if the device address does not link to a devices gives a device not found error back to the User
Used to check that the software can communicate with the watch and ot the user.

