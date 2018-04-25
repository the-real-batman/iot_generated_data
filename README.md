# iot_generated_data
Code to parse and manipulate data from an online JSON file

Data in the form of several JSON objects are available in a website. 
The data is that of the working of several devices in a farm that are operational in a day. 
The task is to parse the data, separate out the objects and then compute for how long a device was active in a day.

The format of the data is:

{ deviceId: Unique Id of a device, previousData: 0 (OFF) / 1 (ON), updatedData: 0 (OFF) / 1 (ON), createdAt: UTC Time }

The output is in the form:

deviceId Total Time (HH:mm:ss)
