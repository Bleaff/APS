import csv
from fastapi import FastAPI
from sqlalchemy import create_engine


db_name = 'quest_db'
db_user = 'check'
db_pass = '1111'
db_host = 'db'
db_port = '5432'

# Connecto to the database
db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)

def add_new_row(text, created_date, rubrics):
    global db
    # Insert a new number into the 'numbers' table.
    with db.connect() as conn:
        insert_string = 'INSERT INTO quest(rubrics, text, created_date)' +  f' VALUES (ARRAY{rubrics}' + ', %s, TIMESTAMP %s);'
        result = conn.execute(insert_string,text, created_date)
        return result

def check_in_table(text):
    result = db.execute(
        f"select exists(select 1 from quest where text='{text}')"
    )
    for (r) in result:  
        return r[0]


def parse_data():
    with open('code/app/posts.csv', mode='r') as csv_file:
        reader = csv.reader(csv_file)
        line_count = 0
        for row in reader:
            if line_count == 0:
                line_count += 1
                continue
            if (check_in_table(row[0])):
                return
            add_new_row(row[0], row[1], row[2])
            line_count += 1
    print(f'Processed {line_count} lines.')
#Just parse data to table
parse_data()


app = FastAPI()
@app.get("/search")
async def get_model(text : str):
    with db.connect() as conn:
        result = conn.execute("SELECT * FROM quest WHERE text LIKE %s order by created_date DESC limit 20;", f"%{text}%")
        res_list = list()
        if type(result) != type(dict):
            for it in result:
                res_list.append(it)
        else:
            return result
    return res_list


@app.get("/query")
async def get_query(query_to_quest : str):
    try:
        with db.connect() as conn:
            result = conn.execution_options(stream_results=True).execute(query_to_quest)
            res_list = list()
            for it in result:
                res_list.append(it)
        return res_list
    except:
        return "Query couldn't be resolved"


@app.get("/selected")
async def get_table_info():
    try:
        with db.connect() as conn:
            result = conn.execution_options(stream_results=True).execute(str("select * from quest order by created_date DESC limit 20;"))
            res_list = list()
            for it in result:
                res_list.append(it)
        return res_list
    except:
        return "Query couldn't be resolved"

@app.get("/drop_by_id")
async def drop_by_id(id : int):
    try:
        with db.connect() as conn:
            conn.execute("DELETE FROM quest where id=%s;", id)
        return f"Id = {id} was successfuly deleted!"
    except:
        return "Query couldn't be resolved"