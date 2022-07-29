# 
FROM  tadeorubio/pyodbc-msodbcsql17:latest

WORKDIR /code
 
COPY . /code

RUN python3 -m pip install --upgrade pip
 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
 
COPY ./sql_app /code/sql_app

CMD ["uvicorn", "sql_app.main:app", "--reload"]
