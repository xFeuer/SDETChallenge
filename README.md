# SDET Coding Challenge

## Project Overview
This project aims to test a state-of-the-art calculator built to perform basic arithmetic operations. The objective is to identify and report any bugs or issues using various testing strategies.

## Setup Environment

### Prerequisites
- Docker
- Python 3.x

### Install Docker
Follow the instructions to install Docker on your platform:

- **macOS**: https://docs.docker.com/docker-for-mac/install/
- **Linux**: https://docs.docker.com/engine/install/
- **Windows**: https://docs.docker.com/docker-for-windows/install/

### Install Python
If Python is not already installed, download and install it from:
https://www.python.org/downloads/

### Pull the Docker Image
Pull the calculator Docker image using the following command:
```bash
docker pull public.ecr.aws/l4q9w4c5/loanpro-calculator-cli:latest
```

### Running the Calculator
Run the calculator with the following command format:
```bash
docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli <operation> <num1> <num2>
```

Available operations:

* add
* subtract
* multiply
* divide

Example:
```bash
docker run --rm public.ecr.aws/l4q9w4c5/loanpro-calculator-cli add 8 5
```

### Running the Tests
### Clone the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/xFeuer/SDETChallenge.git
cd SDETChallenge
```

### Test Script
The test_calculator.py script automates the testing of the calculator and generates a report file.

### Run the Test Script
Execute the test script using Python:
```bash
python test_calculator.py
```

This script will run a series of test cases against the calculator and generate a report file with the results. The report file will be named test_report_<timestamp>.txt.

### Report
The report will include:

* Test cases with results (passed/failed)
* Expected vs. actual outcomes
* Error information for failed tests