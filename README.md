# flask sqlalchemy with graphql

## how to install 

Clone this repo 

## how to run

`python ./app.py`


### go to browser 

http://localhost:5000/graphql


### paste this query

```
{
  allEmployees {
    edges {
      node {
        id
        name
        department {
          name
        }
      }
    }
  }
}

```

then click on Run icon.

