import random
from faker import Faker
from datetime import datetime, timedelta
import json

# Initialize the Faker instance
fake = Faker()


def generate_random_user():
    date_fmt = "%Y-%m-%d"

    # Generate a random username
    random_username = fake.user_name()

    # Generate a random birthday date within the past 50 years

    random_birthday = fake.date_of_birth(minimum_age=18, maximum_age=70, tzinfo=None).strftime(date_fmt)

    # print(f"Username: {random_username}")
    # print(f"Birthday Date: {random_birthday}")

    return random_username, random_birthday,


def get_random_id_from_existing_ids(ids: list):
    random_index = random.randint(0, len(ids) - 1)
    return ids[random_index]


def generate_random_post(accounts_ids_array: list):
    datetime_fmt = "%Y-%m-%d %H:%M:%S"
    # Generate a random datetime for the creation of the post within the past year
    random_post_datetime = fake.date_time_this_decade().strftime(datetime_fmt)

    # Generate random text content for the post
    random_text_content = fake.text(max_nb_chars=200)

    random_account_id = get_random_id_from_existing_ids(accounts_ids_array)

    # print(f"Post Creation Datetime: {random_post_datetime}")
    # print(f"Post Content: {random_text_content}")
    # print(f"Author id: {random_account_id}")

    return random_account_id, random_post_datetime, random_text_content


def generate_random_like(accounts_ids_array: list, posts_ids_array: list):
    random_account_id = get_random_id_from_existing_ids(accounts_ids_array)
    random_post_id = get_random_id_from_existing_ids(posts_ids_array)

    # print(f"Author id: {random_account_id}")
    # print(f"Post id: {random_post_id}")

    return random_account_id, random_post_id

def generate_data(accounts_num, posts_num, like_post_num):
    account = {"id": [], "username": [], "birthday": []}
    post = {"id": [], "account_id": [], "created_on": [], "content": []}
    like_post = {"id": [], "account_id": [], "post_id": []}

    account_ids = []
    post_ids = []

    n = 10

    for id_ in range(accounts_num):
        username, birthday = generate_random_user()
        account["id"].append(id_)
        account_ids.append(id_)
        account["username"].append(username)
        account["birthday"].append(birthday)

    for id_ in range(posts_num):
        account_id, post_datetime, text_content = generate_random_post(account_ids)
        post["id"].append(id_)
        post_ids.append(id_)
        post["account_id"].append(account_id)
        post["created_on"].append(post_datetime)
        post["content"].append(text_content)

    for id_ in range(like_post_num):
        account_id, post_id = generate_random_like(account_ids, post_ids)
        like_post["id"].append(id_)
        like_post["account_id"].append(account_id)
        like_post["post_id"].append(post_id)

    return account, post, like_post


if __name__ == "__main__":
    accounts_number = 100000
    posts_number = 1000000
    likes_number = 10000000
    account, post, like_post = generate_data(accounts_number, posts_number, likes_number)
    with open("static/account.json", "w") as f:
        json.dump(account, f)
    with open("static/post.json", "w") as f:
        json.dump(post, f)
    with open("static/like_post.json", "w") as f:
        json.dump(like_post, f)

