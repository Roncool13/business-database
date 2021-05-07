Business Database
----------------------------

- Sample Project using Django and GraphQL.
- Pytest is used for running tests and generating coverage report.
- This sample application stores business information using four fields -
    1. Name - Name of the Business
    2. Owner - Owner name
    3. Address - Business address
    4. EmployeeCount - No of employees
    

- Docker - 
    1. It also has docker configuration in case application needs to be packaged up in Docker. 
    2. Also, Docker Image with name `111369/business_databse` has been pushed to 
       [Docker Hub](https://hub.docker.com/repository/docker/111369/business-database) which is available for public 
       viewing.
    3. It can be used to directly deploy on container/kuubernetes to play around with vanilla application.

    
- Kubernetes -
    1. It also has kubernetes configuration in case if it needs to be directly deployed to Kubernetes Cluster.
    
&nbsp;

### Steps for Creating venv & installing python packages

- After cloning, `cd` to root-directory `business-database` and run below command -
    ```
    python -m venv venv 
    ```
- Activate the venv -
    ```
    venv\Scripts\activate
    ```
- Install packages -
    ```
    pip install -r requirements.txt
    ```

&nbsp;

### Steps for running pytest and generating coverage report

- Run pytest -
    ```
    pytest
    ```
  
- Browse index.html in directory `htmlcov` to check coverage.


&nbsp;

### Steps for building docker image & deploying on container

- Generate docker image with name `business-database`  by running command from root directory -
    ```
    docker build --tag business-database .
    ```
  
- Deploy to container with name `business-info` -
    ```
    docker run --name business-info business-database
    ```

&nbsp; 
 
### Steps for deploying on Kubernetes Cluster 

- Deploy application to Kubernetes by -
  ```
    kubectl apply -f k8.yml
  ```