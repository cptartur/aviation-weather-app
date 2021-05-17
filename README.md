# Aviation weather app

Simple website built using flask, allowing for checking aviation weather for airports around the world. Uses weather data from [NOAA Aviation Weather Center](https://www.aviationweather.gov/).

## Installation

1. Clone this repository
2. Install required dependencies

    ```
    pip install -r requirements.txt
    ```
    and install
    [metar.py](https://github.com/cptartur/metar-py)

3. Setup elasticsearch
   1. [Download and install elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)
   2. Download `airports.csv` from [this link](https://ourairports.com/data/) and [import  it into Elasticsearch](https://www.elastic.co/blog/importing-csv-and-log-data-into-elasticsearch-with-file-data-visualizer), set `ident`, `municipality` and `name` field types to `text` or the search functionality will not work correctly
   3. Set `ELASTICSEARCH_URL` environmental variable
   4. Set `SEARCH_INDEX_NAME` to the name of the index you created while importing `airports.csv`
4. Set `FLASK_APP` environmental variable to `avw`  
    using linux

    ```bash
    export FLASK_APP="avw"
    ```  

    using windows (powershell)  

    ```powershell
    $env:FLASK_APP="avw"
    ```

5. Set `SQLALCHEMY_DATABASE_URI` environmental variable to correct SQLite database URI (use `sqlite://` for in memory database)
6. Set `SECRET_KEY` environmental variable to a randomly generated string. For generation, may use

    ```bash
    python -c 'import os; print(os.urandom(16))'
    ```
    
7. Generate necessary tables in the database  
    Open flask shell with

    ```
    flask shell
    ```

    and run

    ```python
    from avw import db
    from avw.models import User

    db.create_all()
    ```

## Usage

Run the app with

```
flask run
```

## Testing

Run tests with

```
pytest
```
