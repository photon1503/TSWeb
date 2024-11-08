
# NINA Target Scheduler Web

View and update Target Schedule plans.

Currently implemented:
* Toggle status of a project (active / inactive)
* Change number of desired and accepted images for existing exposure plans

![](image.png)

# Install

1. Install or update Python from https://www.python.org/downloads
2. start a Terminal session
3. change into your favorite directory
   i.e. ```cd \scripts```
4. clone repository
   ```git clone https://github.com/photon1503/TSWeb.git```
5. change to new directory
   ```cd TSWeb```
6. Install requirements
    ```pip install -r requirements.txt```
    If you get some error while building astropy library, you might need to download VS Build Tools from https://visualstudio.microsoft.com/de/visual-cpp-build-tools/ or install this astropy manually using   ```pip install astropy[recommended] --upgrade```


# Run

## Development mode
```py tsweb.py```
Go to http://localhost:5000

## Production mode
```py tsweb_server.py```
The port can be modified in tsweb_server.py,

Go to http://localhost:8081
or ```http://<ip of your observatory pc>:8081```

# Known issues

* No support for multiple profiles
