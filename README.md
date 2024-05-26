# Cupet - Flask Application Development and Deployment





<img width="1492" alt="image" src="https://github.com/SKDS2020/Cupet/assets/74349598/e19a8ab7-81db-4b5b-9343-bb8435f6eaf9">

<img width="1381" alt="image" src="https://github.com/SKDS2020/Cupet/assets/74349598/b2beafa9-929e-4d44-b9b1-5b9f8c165748">

<img width="1337" alt="image" src="https://github.com/SKDS2020/Cupet/assets/74349598/4b30ce98-c77d-4025-9df2-6ade4776aa5b">

## Overview

This repository contains the source code and necessary files for a basic Flask web application that allows users to enter their name and email. The application saves these details in a database and provides a personalized greeting. Additionally, the application displays an image or video hosted on an S3 bucket. The project includes steps for containerizing the application using Docker and deploying it to an EC2 instance with auto-scaling and load balancing capabilities.

## Features

1. **Flask Application**:
    - A form to collect user name and email.
    - Saves user details to a database.
    - Greets the user with a personalized message.
    - Displays an image from an S3 bucket.
      <img width="25" alt="image" src="https://github.com/SKDS2020/Cupet/assets/74349598/50d8ec87-bb37-49f1-af09-89b2f4d89e73">


2. **Containerization**:
    - Dockerfile to containerize the Flask application.
    - Configuration for dependencies, port exposure, volume, and network setup.

3. **Deployment**:
    - Steps to deploy the application on an EC2 instance.
    - Auto-scaling and load balancing setup.
    - Secure access to a private S3 bucket using IAM roles.


## Create S3 Bucket
<img width="1405" alt="image" src="https://github.com/SKDS2020/Cupet/assets/74349598/e0d42d68-cd6f-4bad-a2df-3cb12369cbf2">


## Create Template:
<img width="794" alt="image" src="https://github.com/SKDS2020/Cupet/assets/74349598/fe85242a-a83e-4cdb-949b-aa359ad4ccc2">

## Create Load Balancer:
<img width="1203" alt="image" src="https://github.com/SKDS2020/Cupet/assets/74349598/2e39f32c-e3c2-4d2b-926d-cbb93696f0a0">
testing the Load Balancer (By checking the DNS name):
<img width="771" alt="image" src="https://github.com/SKDS2020/Cupet/assets/74349598/b3eb4187-0ca4-4ed6-bda5-6c043e9c0901">

## Create Auto-scaling (Application :
<img width="941" alt="image" src="https://github.com/SKDS2020/Cupet/assets/74349598/9fbe2033-113a-4f84-b096-ef59acee3866">
testing the Auto-scaling (By checking if another instances upload or remove by Application load balancer request count per target):
<img width="966" alt="image" src="https://github.com/SKDS2020/Cupet/assets/74349598/3fc5f20e-c104-4f0a-af33-be1843cc8bd7">




## Conclusion

By following the steps outlined in this README, you can develop, containerize, and deploy a Flask web application on AWS EC2. This setup includes auto-scaling, load balancing, and secure access to an S3 bucket.


## Prerequisites

- Python 3.x
- Docker
- AWS Account
- AWS CLI
- Git
- 
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Flask documentation
- Docker documentation
- AWS documentation
