import psycopg2
import asyncpg
import json
import time

# for async connection
# conn = asyncpg.connect("postgresql://root:root@localhost:5432/db")
# conn.close()

# drop_table_script = '''
#     DROP TABLE IF EXISTS account
# '''

conn = psycopg2.connect("postgresql://root:root@localhost:5432/db")
cur = conn.cursor()


def log(text: str):
    with open("logs.log", "a") as f:
        f.write(text + '\n')


def execute_sql_script(path: str):
    with open(path, 'r') as file:
        sql_commands = file.read()
        cur.execute(sql_commands)
    conn.commit()


def fill_account_table_sync():
    start_time = time.perf_counter()

    with open("../static/account.json", 'r') as file:
        account = json.load(file)
    # keys = ["id", "username", "birthday"]

    for i in range(len(account["id"])):
        id_ = account['id'][i]
        username = account['username'][i]
        birthday = account['birthday'][i]

        cur.execute("INSERT INTO account (id, username, birthday) VALUES (%s, %s, %s)",
                    (id_, username, birthday))

    conn.commit()

    end_time = time.perf_counter() - start_time
    log(f"Sync inserting 100 000 rows into account table took {round(end_time / 60, 3)} minutes")


def fill_post_table_sync():
    start_time = time.perf_counter()
    with open("../static/post.json", 'r') as file:
        post = json.load(file)

    # keys = ["id", "account_id", "created_on", "content"]

    for i in range(len(post["id"])):
        id_ = post['id'][i]
        account_id = post['account_id'][i]
        created_on = post['created_on'][i]
        content = post['content'][i]

        cur.execute("INSERT INTO post (id, account_id, created_on, content) VALUES (%s, %s, %s, %s)",
                    (id_, account_id, created_on, content))

    conn.commit()

    end_time = time.perf_counter() - start_time
    log(f"Sync inserting 1 000 000 rows into posts table took {round(end_time / 60, 3)} minutes")


def fill_like_post_table_sync():
    start_time = time.perf_counter()

    with open("../static/like_post.json", 'r') as file:
        like_post = json.load(file)

    # keys = ["id", "account_id", "post_id"]

    for i in range(len(like_post["id"])):
        id_ = like_post['id'][i]
        account_id = like_post['account_id'][i]
        post_id = like_post['post_id'][i]

        cur.execute("INSERT INTO like_post (id, account_id, post_id) VALUES (%s, %s, %s)",
                    (id_, account_id, post_id))

    conn.commit()

    end_time = time.perf_counter() - start_time
    log(f"Sync inserting 10 000 000 rows into like_posts table took {round(end_time / 60, 3)} minutes")


def create_tables():
    start_time = time.perf_counter()

    execute_sql_script("./sql-scripts/create_tables.sql")

    end_time = time.perf_counter() - start_time
    log(f"Creating account, posts, like_posts tables took {round(end_time / 60, 3)} minutes")


def fill_tables_with_data_sync():
    start_time = time.perf_counter()

    fill_account_table_sync()
    fill_post_table_sync()
    fill_like_post_table_sync()

    end_time = time.perf_counter() - start_time
    log(f"Sync inserting data into account, posts, like_posts tables took {round(end_time / 60, 3)} minutes")


if __name__ == "__main__":
    create_tables()
    fill_tables_with_data_sync()
    conn.close()
