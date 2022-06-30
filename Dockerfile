# 
FROM  tadeorubio/pyodbc-msodbcsql17:latest

# RUN apt update -y  &&  apt upgrade -y && apt-get update 

# # Add SQL Server ODBC Driver 17 for Ubuntu 18.04
# RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
# RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
# RUN apt-get update
# RUN apt-get install direnv
# RUN ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated msodbcsql17
# RUN ACCEPT_EULA=Y apt-get install -y --allow-unauthenticated mssql-tools
# RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
# RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

# 
WORKDIR /code

# 
COPY . /code

# RUN direnv allow
RUN python3 -m pip install --upgrade pip

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./sql_app /code/sql_app

# 
CMD ["uvicorn", "sql_app.main:app", "--reload"]
