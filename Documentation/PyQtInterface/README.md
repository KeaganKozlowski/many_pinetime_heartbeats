# PyQtInterface Documentation
## 1. Introduction
### What is the PyQtInterface Folder?
The folder contains a collection of scripts which makeup the GUI (Graphical User Interface) for the application.

However, this does not mean all the scripts are used, as some feature code snippet examples. Which proves useful when debugging the Main_UI script.

## 2. External Libraries and Modules
### PyQt6
* **Purpose**: Enables Python to be used as an alternative application development language to C++ on all supported platforms including iOS and Android. 
* **Documentation**: [PyQt6](https://www.riverbankcomputing.com/static/Docs/PyQt6/)<br>
#### **Why PyQt6?**
* PyQt6 is the most current version of PyQt which means it has the most up-to date features and bug fixes compared to older versions.
* PyQt has been around longer than PySide which means the community is more active allowing for questions to be answered quicker or the answer already exists online.
* PyQt gets the latest Qt features faster and often in a more stable state than PySide.
* PyQt has more extensive documentation than that of PySide.
### Numpy
* **Purpose**: Numpy is utilized for numerical operations and data manipulation within scripts.
* **Documentation**: [Numpy Documentation](https://numpy.org/doc/1.26/)<br>
### bleak - Bluetooth Low Energy platform Agnostic Klient
* **Purpose**: Bleak handles Bluetooth Low Energy (BLE) connections across different platforms.
* **Documentation**: [bleak Documentation](https://bleak.readthedocs.io/en/latest/index.html)<br>
### Async - Asynchronous
* **Purpose**: Asyncio is used for writing concurrent code, allowing the scripts to manage multiple connections and tasks asynchronously.
* **Documentation**: [asyncio Documentation](https://docs.python.org/3/library/asyncio.html)<br>


## 3. Internal Libraries and Modules
### Sys
* **Purpose**: Provides functions and variables which are used to manipulate different parts of the Python Runtime Enviroment.
* **Documentation**: [sys](https://docs.python.org/3/library/sys.html)<br>
### asyncio
* **Purpose**: Asyncio is used for writing concurrent code, allowing the scripts to manage multiple connections and tasks asynchronously.
* **Documentation**: [asyncio Documentation](https://docs.python.org/3/library/asyncio.html)<br>

## 4. Error Handling
### 1. bleak threading error
* **Issue**: Just getting an error message through terminal saying unable to complete action cause of threading error.
* **Possible cause**: 
  * One of the modules/libraries that bleak imports from hasn't been properly setup or included at all.
  * The logic of the code being implemented not properly being implemented leading to logic errors.
* **Possible solutions**: 
  * Importing the required libraries
  * Fixing the logic of the function that hasn't properly been implemented
* **Actual solution**:
### 2. InfinitTime device error
* **Issue**: When pressing the "Scan for devices" button sometimes the InfiniTime watches just don't get scanned or not all of the watches will get scanned.
* **Potential cause**:
  * The watches having a weak bluetooth emitter, which is flaky and isn't always picked up from computer's bluetooth scan.
  * An error in my function for discovering devices and receiving their device information.
* **Potential solutions**:
* **Actual solution**:
### If any other error are found please create an issue

## 5. File Breakdown
### [Basic UI](https://github.com/KeaganKozlowski/many_pinetime_heartbeats/blob/main/PyQtInterface/basic_ui.py)
* This file was my inital attempt at trying to use PyQt6.
* As for a while I was struggling to use the library and need a place to mess around and try stuff out.
* That's why compared to other files in this folder, the code is very simple and has little to no comments.
### [Functionality UI](https://github.com/KeaganKozlowski/many_pinetime_heartbeats/blob/main/PyQtInterface/functionality_UI.txt)
* This file contains a checklist for what I had originally wanted on my inital attempt at creating the GUI.
* However, since starting this project and becoming more confident with PyQt6, it no longer has purpose
### [Main UI](https://github.com/KeaganKozlowski/many_pinetime_heartbeats/blob/main/PyQtInterface/main_ui.py)
* This file contains my inital attempt at creating a centralized GUI using PyQt.
* However, this file is no longer being work on and instead is being used to show how not to code a GUI in PyQt.
* This is mainly due to the way I was implementing changing between layouts and the relationship between QWidgets just wasn't working.
### [Main UI 2](https://github.com/KeaganKozlowski/many_pinetime_heartbeats/blob/main/PyQtInterface/main_ui_2.py)
* This is the new main file for the UI.
* As compared to the previous Main UI file it uses QStackWidgets, which allows only one Widget to be visible at a time but there are multiple in the same place which aren't visible.
* The file only contains one class for all the code as changing layout is just done through functions.
* Finally compared to the previous file this file features alot more comments and the code is layout in a way that is easier to read.
#### Class and Function breakdown
Worker Class + Asyncio + Threading 

## 6. Why PyQt6 is no longer being used
This boiled down to several errors which I could not find a fix for, my fix did not work or the libraries being used work fully compatible with each other.
