# PySpark and DynamoDB Connectivity Project

Welcome to the PySpark and DynamoDB connectivity project. This repository demonstrates how to use Apache PySpark to interact with DynamoDB, a managed NoSQL database service by AWS. The project is organized into three main folders: `terraform`, `python`, and `notebook`. Each folder contains different components of the project.

## Project Structure

### 1. `terraform/`

This folder contains Terraform scripts used to create and manage DynamoDB tables on AWS. Terraform is an Infrastructure as Code (IaC) tool that allows you to define and provision infrastructure using a declarative configuration language.

**Usage:**
1. Ensure you have Terraform installed.
2. Navigate to the `terraform` directory.
3. Run `terraform init` to initialize the Terraform configuration.
4. Run `terraform apply` to create the DynamoDB tables.

### 2. `python/`

This folder contains the Python application that generates sample data representing entities in an E-Commerce system. The key entities are:
- **Customer**: Represents a customer in the system.
- **Product**: Represents a product available for purchase.
- **Order**: Represents an order placed by a customer.

**Usage:**
1. Ensure you have Python installed.
2. Install the required Python packages by running `pip install -r requirements.txt` in the `python` directory.
3. Run the sample data generation script by executing `python app/producer.py`.

### 3. `notebook/`

This folder contains Jupyter notebooks with sample PySpark code. The notebooks demonstrate how to read data from DynamoDB and generate sample reports using PySpark.

**Usage:**
1. Ensure you have Jupyter Notebook installed.
2. Install the necessary PySpark and AWS dependencies.
3. Start Jupyter Notebook by running `jupyter notebook` in the `notebook` directory.
4. Open and run the notebooks to see how to read data from DynamoDB and process it using PySpark.

## Prerequisites

- AWS account with appropriate permissions.
- Terraform installed.
- Python 3.x installed.
- PySpark installed.
- Jupyter Notebook installed.

## Setup

1. **DynamoDB Tables Setup:**
   - Navigate to the `terraform` directory.
   - Run `terraform init` to set up Terraform.
   - Execute `terraform apply` to provision the DynamoDB tables.

2. **Data Generation:**
   - Navigate to the `python` directory.
   - Install dependencies: `pip install -r requirements.txt`.
   - Run the data generation script: `python app/producer.py`.

3. **Data Analysis with PySpark:**
   - Navigate to the `notebook` directory.
   - Install PySpark and AWS dependencies.
   - Start Jupyter Notebook: `jupyter notebook`.
   - Open the notebooks and execute the cells to analyze data.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. 

## Contact

For any questions or feedback, feel free to open an issue on GitHub.

---

Happy coding!
