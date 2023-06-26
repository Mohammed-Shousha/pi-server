# sap-pi-backend

FastAPI server for controlling Smart Automatic Pharmacy (SAP). It provides a RESTful API for managing medicines, prescriptions, and performing various actions related to SAP.

## Features

- **List Medicines**: Retrieve a list of available medicines in SAP.
- **List OTC Medicines**: Retrieve a list of over-the-counter medicines in SAP.
- **Show Medicine**: Get details of a specific medicine in SAP by ID.
- **List Prescriptions**: Retrieve a list of prescriptions in SAP.
- **Show Prescription**: Get details of a specific prescription in SAP by ID.
- **Verify Prescription Medicines Availability**: Check the availability of medicines for a given prescription in SAP.
- **Process Prescription**: Process a prescription by dispensing available medicines from SAP.
- **Order Medicines**: Order medicines directly from SAP.
- **Shelf Action**: Perform actions to open or close a specific shelf of SAP.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python.
- **MongoDB**: A NoSQL document database for storing medicines and prescriptions.
- **Motor**: An asynchronous driver for MongoDB that integrates with asyncio.
- **gpiozero**: A library for controlling GPIO pins on a Raspberry Pi to interface with SAP hardware.
