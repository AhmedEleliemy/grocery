# Introduction
This project is about providing REST API (HTTP/JSON) for grocery store. It offers two end-points to handle grocery items. 
+ GET /items lists all items that exist in database
+ POST /items adds a grocery item to the database 

In the next sections, I discuss in more details about the solution architecture and system requirement. If one is not interested, (s)he can skip the following part, i.e., One can go directly to [Deployment/Usage](#deployment-usage), [Testing](#testing), [Self-assessment](#self-assessment-of-the-code), and [Reasoning for technological decisions](#reasoning-for-major-selected-toolingframeworklibrary)


# Architecture
**Data Definition**

`Item` has the following attributes: 
+ `id` -> holds a unique integer value (primary key). This attribute is automatically generated and maintained  by the system.
+ `name` -> holds a unique string value of maximum 50 chars. This attribute is given to the system and represents the name of the grocery item.
+ `description` -> holds a none empty string value of maximum 150 chars. This attribute is given to the system and represents the description of the grocery item.
+ `quantity` -> holds an integer value and will be given to the system and represents the available amount of the grocery item.
+ ``price`` ->  holds a float value and will be given to the system and represents the price of the grocery item
  

**End Points (Routes)**
+ `Get /` just returning this README file as HTML
+ `Get /items` (listing  all grocery items) 
  Responses:
  + `STATUS code 200` on success and returns a JSON object that represents list of all available grocery items form the database  
  ```json
  [
    {
        "id": 1,
        "name": "Pasta",
        "description":"Italian Pasta. One packet is 500gm and fits for two persons",
        "price": 2.5,
        "quantity":100
    },
    {
        "id":2,
        "name":  "Coffee beans",
        "description": "Brazilian coffee. One packet is 250gm",
        "price": 5.0,
        "qunatity":200
    }
  ]
  ``` 
+ `Post /items` (adding a new item)
  
  Arguments:

  *name*: none empty string

  *description*: none empty string

  *quantity*: a positive integer

  *price* : a positive  float

  Responses:
    + `STATUS code 201` on success and return the id of the newly added grocery item as JSON object
  ```json
      {
        "id": 3
      }
    ```
    + `STATUS code 409` on failure if item exists with the same name (CONFLICT)
    + `STATUS code 400` on failure if any of the arguments violate the  constraints (BAD REQUEST)

# Software Requirements 
## The solution requires the python packages
+ Flask==2.1.0
+ Flask_SQLAlchemy==2.5.1
+ Markdown==3.4.1
+ marshmallow==3.17.1
+ marshmallow_sqlalchemy==0.28.1
+ SQLAlchemy==1.4.7
+ waitress==2.1.2
+ pytest==6.2.3 (only for running test-cases)

# Deployment (Usage)

## First clone the repository
```shell
git clone https://github.com/AhmedEleliemy/grocery.git
cd grocery
```

## To Run Natively
```shell
python run.py
```

## To Deploy as Containerized app (docker)
+ This requires having docker and docker compose installed on your system. One may check https://docs.docker.com/get-docker/ and https://docs.docker.com/compose/install/

```shell
sudo docker-compose build
sudo docker-compose up
```


# Testing
+ The flask framework provides some integrated testing capabilities which were used with pytest to create some basic functional test cases
+ To execute the available test-cases do the following
```shell
python testcase.py
```

# Self-assessment of the code
I did self-assessment and self-code review, and although I found many things to improve, I did not address them to maintain reasonable time (~3/4 hours) of the task.
#### Comments and Code Documentation
+ The code has certain essential comments.  Most of the functions have multiple lines to describe their functionality and expected behavior. However, some modules miss any comments, e.g., item.py. I also recommend the use the **Docstrings** style to document the code. It helps other developers in the team to deal with modules, classes, and functions as black boxes, i.e., what are the inputs, output, and expected behavior.
#### Code Clarity
+ Variables, functions, and classes follow a naming convention and have meaningful names. But, there is a place for improvements. For instance, some variables could have been named better see the following variables *error* and *result* in the following functions get_all_grocery_items() and add_grocery_item() in (see app/routes/apis.py). Another improvement is **naming consistency**, i.e., the variable name that refers to a grocery item is sometimes named grocery_item, posted_item and item (see app/routes/apis.py)
+ Some cleaning is required where print messages have been left from development. See app/extensions.py 
#### Code Structure and Extendability
+ The design of this project follows as MVC (model-view-control) pattern which supports extendability. The representation of the model class **Item** is independent from the underlying database technology. The APIs do not access the database layer directly they rather use the model class **Item** which inherits ORM (Object Relational Mapper). Furthermore, the APIs delegate data validation to certain database Schema serializer. Thus, changes in the data model would have minimum impact of existing code of the APIs and vice versa.   
  
+ The code structure also reflects the MVC pattern to some extent, i.e., all data models are separated under /app/modules, and all APIs (end-points) are separated under /app/routes. For adding more API's, one may consider separate them in multiple files rather than one file /app/routes/apis.py
     
#### Correctness and BUGs free
+ I could identify one potential problem in /app/routes/apis.py. Some types of exceptions are handled, but still other exceptions may rise, for instance, when **passing a valid grocery item as that has an id**. 

## What is missing and couldn’t be done anymore?
```text
 As per my understanding, "could't be done anymore" refers to "not be able to do it within the excepted time (3~4 hours)".
 ```  

+ Address all the issues in Section [self-assessment](#self-assessment-of-the-code)
+ Implement CRUD fully (create read update delete). The project misses update and delete of grocery  item
+ Adding more test-cases
+ Use a server logging mechanism. This mechanism become extremely essential in production. 

## Which elements should be improved to make it production-ready?
1. The choice of the database backend is crucial and indeed is a function of the business requirement. I would say for small/large grocery businesses, a SQL-,  NOSQL-based databases or a mix of both is recommended. 
2. The application must read its configuration **form a config file** or set of **environment variables**. For instance, the **port number** should not be embedded in the code directly. Another example is **database URI** (path to the sqlite file). 
3. There should be a distinct database for testing and another one for production. 
4. Items 1 and 2 can be seen in a larger context as well, i.e., use some CI/CD frameworks like TravisCI.      
5. Security:
   1.  Currently anyone can add items to the database. Thus, **securing the post endpoint is needed**, e.g., ensuring it is only accessed by **logged in users**
   2.  The string values in the posted json object are not guarded against JS and HTML injections. API's (post and get) are not affected but future services that use them are in risk.   

## Were there any topics you strugged with?
+ The use of waitress and mapping the ports correctly with the docker
# Reasoning for major selected tooling/framework/library
+ For **web development**t in python, there are two frameworks
  + Django
  + Flask
+ I selected **Flask** because it is more simple but yet productive and efficient to meet all the requirements of the task. Also, the project only had to include APIs.
+ For me, having Django for this project is like  driving an airplane to go for daily shopping. 
+ For Object Relational Mapping (ORM), I used **SQLAchemy**. There are other options like, for instance, Peewee. But,**SQLAchemy** supports more databases and have a larger community for online support.
+ I used **Marshmallow-Sqlalchemy** to serializes/deserializes dicts to SQLAlchemy with ensuring some **validation rules** on the input values
+ I used **pytest** to run functional tests. I chose it because it is simple and I am familiar with it.
+ I used SQLite for ease of use, simplicity, and sufficient for the task
+ I used Docker to containerize the application for easy deployment 