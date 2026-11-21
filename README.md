::: {align="center"}
🚗 Vehicle Insurance MLOps Platform
End-to-end machine learning pipeline --- from raw data to cloud deployment
A production-oriented MLOps project that automates the complete machine
learning lifecycle for a vehicle insurance prediction system. It brings
together data ingestion, validation, transformation, model training,
evaluation, model registry, prediction serving, and CI/CD deployment on
AWS.
![Python](https://img.shields.io/badge/Python-3.10-3776AB?logo=python&logoColor=white)
![ML](https://img.shields.io/badge/Machine%20Learning-Scikit--learn-orange)
![MongoDB](https://img.shields.io/badge/Database-MongoDB%20Atlas-47A248?logo=mongodb&logoColor=white)
![AWS](https://img.shields.io/badge/Cloud-AWS-232F3E?logo=amazonaws&logoColor=white)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker&logoColor=white)
![GitHub](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-2088FF?logo=githubactions&logoColor=white)
:::
---
📌 Project Overview
This project demonstrates how a machine learning application can be
structured and deployed using practical MLOps principles. Instead of
treating model training as a standalone notebook exercise, the project
organizes the workflow into reusable components and connects them to
cloud infrastructure.
The pipeline covers:
Collecting and storing data in MongoDB Atlas
Validating incoming data against a defined schema
Transforming data and preparing features for model training
Training and evaluating machine learning models
Comparing model performance against a configured threshold
Pushing approved models to AWS S3
Serving predictions through a web application
Building and deploying the application using Docker, Amazon ECR,
EC2, and GitHub Actions
✨ Key Features
---
Feature                             What it does
---
Modular project architecture        Separates configuration, entities,
components, pipelines, and
utilities for maintainability
Reusable local package              Uses `setup.py` and
`pyproject.toml` to make project
modules importable
Centralized logging                 Captures pipeline execution details
for easier debugging and
traceability
Custom exception handling           Provides clearer error messages
with useful traceback information
MongoDB integration                 Reads source data from MongoDB
Atlas
Data validation                     Checks incoming data against a
YAML-defined schema
Data transformation                 Prepares and transforms features
for model training
Model training                      Trains the configured machine
learning estimator
Model evaluation                    Evaluates the newly trained model
against the existing production
model
Model registry/storage              Stores and retrieves model
artifacts using AWS S3
Prediction application              Exposes the trained model through a
web interface
Containerization                    Packages the application and
dependencies into a Docker image
CI/CD automation                    Automates image build and
deployment through GitHub Actions
and a self-hosted runner
🧰 Technology Stack
Area                         Tools / Services
---
Language                     Python 3.10
Data handling                Pandas, NumPy
Machine learning             Scikit-learn
Development & EDA            Jupyter Notebook, Matplotlib, Seaborn
Database                     MongoDB Atlas
Configuration & packaging    YAML, `setup.py`, `pyproject.toml`
Code quality / diagnostics   Logging, custom exception handling
Cloud storage                AWS S3
Containerization             Docker
Image registry               Amazon Elastic Container Registry (ECR)
Compute / deployment         Amazon EC2 (Ubuntu)
Automation                   GitHub Actions, self-hosted GitHub Actions runner
---
🏗️ MLOps Workflow
``` mermaid
flowchart TD
    A\[Source Dataset] --> B\[MongoDB Atlas]
    B --> C\[Data Ingestion]
    C --> D\[Data Validation]
    D --> E\[Data Transformation]
    E --> F\[Model Training]
    F --> G\[Model Evaluation]
    G --> H{Performance threshold met?}
    H -- Yes --> I\[Model Pusher]
    H -- No --> J\[Keep existing model / review]
    I --> K\[AWS S3 Model Registry]
    K --> L\[Prediction Pipeline]
    L --> M\[Web Application]

    N\[Git Push] --> O\[GitHub Actions CI/CD]
    O --> P\[Build Docker Image]
    P --> Q\[Amazon ECR]
    Q --> R\[EC2 Deployment]
    R --> M
```
Pipeline stages
Data ingestion --- Connects to MongoDB Atlas, retrieves records,
and converts them into a structured DataFrame.
Data validation --- Uses the dataset schema to verify that
incoming data meets the expected structure and requirements.
Data transformation --- Applies the required preprocessing and
feature-engineering steps.
Model training --- Trains the estimator using the transformed
training data.
Model evaluation --- Compares the newly trained model with the
currently available model using the configured evaluation logic.
Model pushing --- Pushes the approved model artifact to the
configured S3 bucket.
Prediction pipeline --- Loads the model artifact and generates
predictions from application inputs.
CI/CD deployment --- Builds a Docker image, publishes it to ECR,
and deploys the application to EC2.
---
📂 Project Structure
The project follows a modular, component-based structure. The tree below
illustrates the main responsibilities; exact filenames may vary as the
implementation evolves.
``` text
.
├── .github/
│   └── workflows/
│       └── aws.yaml                 # CI/CD workflow
├── artifact/                        # Generated pipeline artifacts (not committed)
├── config/
│   └── schema.yaml                  # Dataset schema for validation
├── notebook/
│   ├── mongoDB\_demo.ipynb           # MongoDB connection and data upload
│   └── ...                          # EDA and feature engineering notebooks
├── src/
│   ├── components/
│   │   ├── data\_ingestion.py
│   │   ├── data\_validation.py
│   │   ├── data\_transformation.py
│   │   ├── model\_trainer.py
│   │   ├── model\_evaluation.py
│   │   └── model\_pusher.py
│   ├── configuration/
│   │   ├── mongo\_db\_connections.py
│   │   └── aws\_connection.py
│   ├── constants/
│   ├── data\_access/
│   ├── entity/
│   │   ├── config\_entity.py
│   │   ├── artifact\_entity.py
│   │   ├── estimator.py
│   │   └── s3\_estimator.py
│   ├── pipeline/
│   │   └── training\_pipeline.py
│   ├── aws\_storage/
│   ├── exception/
│   ├── logger/
│   └── utils/
│       └── main\_utils.py
├── static/                           # Frontend static assets
├── templates/                        # Web application templates
├── app.py                            # Prediction web application
├── demo.py                           # Training pipeline entry point
├── Dockerfile
├── .dockerignore
├── .gitignore
├── pyproject.toml
├── setup.py
└── requirements.txt
```
🚀 Getting Started
1. Clone the repository
``` bash
git clone <YOUR\_REPOSITORY\_URL>
cd <YOUR\_PROJECT\_DIRECTORY>
```
2. Create and activate the environment
``` bash
conda create -n vehicle python=3.10 -y
conda activate vehicle
```
3. Install dependencies
Add the required libraries to `requirements.txt`, then run:
``` bash
pip install -r requirements.txt
```
4. Install the project as a local package
Configure `setup.py` and `pyproject.toml` so that the source package can
be imported throughout the project.
``` bash
pip install -e .
```
Verify the installation:
``` bash
pip list
```
> \*\*Why editable installation?\*\* It makes the local source package
> importable while allowing code changes to take effect without
> reinstalling the package.
---
🗄️ Database Configuration --- MongoDB Atlas
MongoDB Atlas is used as the source database for the pipeline.
Create a MongoDB Atlas account and a project.
Create a cluster. The project setup uses the free M0 tier where
available.
Create a database user with a strong password.
Configure network access. For development, use your current IP
address where possible.
Select Connect → Drivers, choose Python, and copy the connection
string.
Replace the password placeholder with the database user's password.
Upload the dataset to the database using the notebook in
`notebook/`.
Verify the uploaded records under Database → Browse Collections.
Set the connection string as an environment variable.
Bash / macOS / Linux
``` bash
export MONGODB\_URL="mongodb+srv://<username>:<password>@<cluster>/<database>"
echo "$MONGODB\_URL"
```
PowerShell
``` powershell
$env:MONGODB\_URL = "mongodb+srv://<username>:<password>@<cluster>/<database>"
echo $env:MONGODB\_URL
```
Windows Command Prompt
``` cmd
set "MONGODB\_URL=mongodb+srv://<username>:<password>@<cluster>/<database>"
echo %MONGODB\_URL%
```
For persistent configuration on Windows, add `MONGODB\_URL` through the
Windows Environment Variables settings.
> 🔐 \*\*Security note:\*\* Do not commit database credentials or connection
> strings. Avoid allowing `0.0.0.0/0` in MongoDB network access for a
> production deployment; restrict access to trusted IP addresses or use
> an appropriate private networking setup.
---
☁️ AWS Configuration
AWS services are used for model artifact storage and application
deployment.
Services used
Amazon S3 --- Stores model artifacts.
Amazon ECR --- Stores Docker images.
Amazon EC2 --- Hosts the deployed application.
IAM --- Manages access permissions for AWS resources.
The original project configuration uses the `us-east-1` region. Update
the region and resource names if you deploy elsewhere.
Configure AWS credentials
Create an IAM identity for deployment and grant only the permissions
required by the workflow. Configure its access credentials as
environment variables.
Bash / macOS / Linux
``` bash
export AWS\_ACCESS\_KEY\_ID="<your-access-key>"
export AWS\_SECRET\_ACCESS\_KEY="<your-secret-key>"
export AWS\_DEFAULT\_REGION="us-east-1"
```
PowerShell
``` powershell
$env:AWS\_ACCESS\_KEY\_ID = "<your-access-key>"
$env:AWS\_SECRET\_ACCESS\_KEY = "<your-secret-key>"
$env:AWS\_DEFAULT\_REGION = "us-east-1"
```
Windows Command Prompt
``` cmd
set "AWS\_ACCESS\_KEY\_ID=<your-access-key>"
set "AWS\_SECRET\_ACCESS\_KEY=<your-secret-key>"
set "AWS\_DEFAULT\_REGION=us-east-1"
```
The project configuration includes these model-storage settings:
``` python
MODEL\_EVALUATION\_CHANGED\_THRESHOLD\_SCORE = 0.02
MODEL\_BUCKET\_NAME = "my-model-mlopsproj"
MODEL\_PUSHER\_S3\_KEY = "model-registry"
```
Create the S3 bucket with the configured name in the selected region.
The application uses its AWS storage layer and S3 estimator utilities to
upload and retrieve model artifacts.
> 🔐 \*\*Security note:\*\* Keep S3 Block Public Access enabled unless
> public access is explicitly required and has been carefully reviewed.
> Use IAM roles or narrowly scoped IAM policies instead of broad
> administrator permissions. Never put AWS access keys in source code,
> notebooks, Docker images, or Git history.
---
🔄 CI/CD & Cloud Deployment
The deployment workflow uses GitHub Actions, Docker, Amazon ECR, and an
EC2 Ubuntu instance.
Deployment flow
``` mermaid
flowchart LR
    A\[Code change] --> B\[Git push]
    B --> C\[GitHub Actions]
    C --> D\[Self-hosted runner on EC2]
    D --> E\[Build Docker image]
    E --> F\[Push image to Amazon ECR]
    F --> G\[Deploy container]
    G --> H\[Live application]
```
Setup summary
Add a `Dockerfile` and `.dockerignore` to the repository.
Create an ECR repository (the example repository name is
`vehicleproj`) in the selected AWS region.
Launch an Ubuntu EC2 instance and install Docker.
Register the EC2 machine as a self-hosted GitHub Actions runner
by following the runner setup commands shown in the repository's
GitHub settings.
Add the required repository secrets under Settings → Secrets and
variables → Actions.
Configure these GitHub repository secrets:
Secret                    Purpose
---
`AWS\_ACCESS\_KEY\_ID`       IAM access key used by the deployment workflow
`AWS\_SECRET\_ACCESS\_KEY`   Corresponding secret key
`AWS\_DEFAULT\_REGION`      AWS deployment region
`ECR\_REPO`                ECR repository URI
Configure `.github/workflows/aws.yaml` to build and publish the
image and deploy the application.
Commit and push changes to trigger the workflow.
EC2 application access
Configure the EC2 security group to allow inbound traffic on the port
used by the application. Then open:
``` text
http://<EC2\_PUBLIC\_IP>:<APPLICATION\_PORT>
```
The project notes use port `5080` for external access. Ensure the
application, Docker port mapping, CI/CD deployment command, and EC2
security-group rule all use the same port.
The training pipeline can also be triggered through the application's
`/training` route, as implemented in the project.
> \*\*Deployment security:\*\* Restrict inbound access to trusted IP ranges
> where possible. For a public production application, use HTTPS through
> a reverse proxy or load balancer rather than exposing an application
> port directly.
---
⚙️ Running the Project Locally
After configuring the required environment variables and installing
dependencies:
Run the training pipeline
``` bash
python demo.py
```
Start the web application
``` bash
python app.py
```
Open the local URL and port printed by the application. The exact routes
and request formats are defined by the implementation in `app.py`.
🧪 Experimentation & Development
The `notebook/` directory contains the notebooks used during
development, including:
MongoDB connection and dataset upload
Exploratory Data Analysis (EDA)
Feature engineering
The modular pipeline components move the workflow beyond notebook-only
experimentation and make the process easier to test, maintain, and
execute consistently.
🔐 Configuration & Security
Before deploying or sharing this project, make sure that:
`.env` files, credentials, private keys, and AWS CSV key downloads
are excluded from Git.
`MONGODB\_URL`, AWS credentials, and other secrets are supplied
through environment variables or a secrets manager.
The generated `artifact/` directory is ignored by Git unless
selected artifacts are intentionally versioned.
MongoDB network access is restricted to trusted sources.
S3 buckets remain private unless public access is a deliberate
requirement.
IAM permissions follow least-privilege principles.
EC2 inbound rules expose only the ports and source IP ranges
required.
GitHub Actions secrets are used for deployment credentials.
👩‍💻 Author
Anjali Barnwal
GitHub ·
LinkedIn
---
::: {align="center"}
Built to demonstrate the complete journey from data to a deployed
machine learning application.
⭐ If you find this project interesting, consider giving the repository
a star!
:::