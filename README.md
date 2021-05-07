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
    ```buildoutcfg
    python -m venv venv 
    ```
- Activate the venv -
    ```buildoutcfg
    venv\Scripts\activate
    ```
- Install packages -
    ```buildoutcfg
    pip install -r requirements.txt
    ```

&nbsp;

### Steps for running pytest and generating coverage report

- Run pytest -
    ```buildoutcfg
    pytest
    ```
  
- Browse index.html in directory `htmlcov` to check coverage.


&nbsp;

### Steps for building docker image & deploying on container

- Generate docker image with name `business-database`  by running command from root directory -
    ```buildoutcfg
    docker build --tag business-database .
    ```
  
- Deploy to container with name `business-info` -
    ```buildoutcfg
    docker run --name business-info business-database
    ```

&nbsp; 
 
### Steps for deploying on Kubernetes Cluster 

- Deploy application to Kubernetes by -
  ```buildoutcfg
    kubectl apply -f k8.yml
  ```
  
&nbsp;

### Queries & Mutations List -

- Query to get list of all business - 
```buildoutcfg
query{
  allBusiness{
    name,
    owner,
    address,
    employeeCount
  }
}
```

- Search Query for exact value in address, name and owner fields -
```buildoutcfg
query {
  searchBusiness(name_Iexact: "zomato"){
    edges{
      node{
        name,
        owner,
        address,
        employeeCount
      }
    }
  }
}
```

- Search Query for specific value in address, name and owner fields -
```buildoutcfg
query {
  searchBusiness(name_Icontains: "bank"){
    edges{
      node{
        name,
        owner,
        address,
        employeeCount
      }
    }
  }
}
```

- Search Query with starting keyword in address, name and owner fields -
```buildoutcfg
query {
  searchBusiness(name_Istartswith: "fire"){
    edges{
      node{
        name,
        owner,
        address,
        employeeCount
      }
    }
  }
}
```

- Search Query for less than specific value in employeeCount field -
```buildoutcfg
query {
  searchBusiness(employeeCount_Lt: 500){
    edges{
      node{
        name,
        owner,
        address,
        employeeCount
      }
    }
  }
}
```

- Search Query for greater than specific value in employeeCount field -
```buildoutcfg
query {
  searchBusiness(employeeCount_Gt: 4500){
    edges{
      node{
        name,
        owner,
        address,
        employeeCount
      }
    }
  }
}
```

- Mutation Query to add Business Data -
```buildoutcfg
mutation CreateBusinessMutation{
  createBusiness(name: "Eichiba Inc", owner: "Anweshan Guha", address: "San Jose, California, United States", employeeCount:10){
    business{
      name,
      owner,
      address,
      employeeCount
    }
    message,
    status
  }
}
```

- Mutation Query to update Business Data -
```buildoutcfg
mutation UpdateBusinessMutation{
  updateBusiness(name: "Zomato", owner: "Deepinder Goyal", address: "Gurgaon, Haryana, India", employeeCount:5001){
    business{
      name,
      owner,
      address,
      employeeCount
    }
    message,
    status
  }
```

- Mutation Query to delete Business Data -
```buildoutcfg
mutation DeleteBusinessMutation{
  deleteBusiness(name: "Zomato"){
    message,
    status
  }
}
```
