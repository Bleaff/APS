
FROM python:latest
# 
WORKDIR /code
# 
COPY requirements.txt code/requirements.txt
COPY posts.csv code/app/posts.csv
# 
RUN pip install --no-cache-dir --upgrade -r code/requirements.txt
# 
COPY main.py /code/app/main.py
# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]