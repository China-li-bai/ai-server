#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null
then
    echo "Python 3 could not be found. Please install Python 3 before running this script."
    exit
fi

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Check if pipreqs is installed, if not, install it
if ! pip show pipreqs &> /dev/null
then
    echo "pipreqs not found. Installing pipreqs..."
    pip install pipreqs
fi

# Generate requirements.txt if it doesn't exist
if [ ! -f requirements.txt ]; then
    echo "requirements.txt not found. Generating requirements.txt using pipreqs..."
    pipreqs . --force
fi

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

echo "Setup complete. Virtual environment is ready to use."

# Deactivate the virtual environment
deactivate 