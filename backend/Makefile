# backend/Makefile
SHELL=/bin/bash

currwd = $(shell pwd)
inv_test = https://drive.usercontent.google.com/download?id=1hO-oWX-ecnHOTl8xF2imkY7WGYoF1nL0&confirm=ABC
inv_errr = https://drive.usercontent.google.com/download?id=16-VH9CM9hTQvMPqixY41yD3H201kZNsT&confirm=ABC

setup:
	@echo "Downloading required assets for testing..."
	@echo "Test Excel files..."
	@echo ""
	curl --output ${currwd}/inputs/inventario-test.xlsx --location "${inv_test}"
	curl --output ${currwd}/inputs/inventario-test-erroneo.xlsx --location "${inv_errr}"
	@echo ""
	@echo "Checking downloaded files..."
	ls -la ${currwd}/inputs | grep xlsx
