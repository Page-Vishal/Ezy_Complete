import ast
import asyncio
from typing import List, Dict
from prisma import Prisma
from prisma.models import Post

from Code.client.client import client

schema = {
    "id": "id of the post",
    "title": "the title of the post",
    "price": "The price defined of the room",
    "images": "The list of link for the room",
    "address": "The major full address for the rented rooms",
    "city": "the city of the room",
    "bedroom": "Number of available bedrooms",
    "bathroom": "Number of available bathrooms",
    "latitude": "The latitude of the location",
    "longitude": "The longitude of the location",
}

def create_query(question):
    schemaz = repr(schema)
    questionz = repr(question)
    code = f"""
        You are given a task to create a Prisma Client query code. The schema of the database you refer to is given as:
        {schemaz}. But you only consider price, address ,city, bedroom, bathroom. You return the where part of the code

        Example:
            query: Find me the rooms available at Chitwan:
            result:     
                posts = await db.post.find_many(
                    where={{'address' : "Chitwan"}},
                )
            BUT response:
                {{'address' : "Chitwan"}},
            query: Find me 2 bedroom rooms at rent in kathmandu:
            result:
                posts = await db.post.find_many(
                    where={{
                        'AND': [
                            {{'address' : "kathmandu"}},
                            {{'bedroom' : 2 }},
                        ]
                    }}
                )
            BUT response:
                {{'AND': [{{'address' : "kathmandu"}},{{'bedroom' : 2 }},]}}
        You don't have to be so much specific about user's question. Just answer by generalizing the question and not making too complex query or assumptions. Take a <pause> to evaluate the query.
        You only generate one and specific code that will be most suited. You do not generate and respond with unnecessary texts not even backticks.

        The question is : {questionz}

        Your Turn:
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a helpful Prisma Client Python assistant."},
            {"role": "user", "content": code},
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
    )
    query = completion.choices[0].message.content
    return query

def format_post(post:Post):
    return {
        "id": post.id,
        "title": post.title,
        "price": post.price,
        "images": post.images,
        "address": post.address,
        "city": post.city,
        "bedroom": post.bedroom,
        "bathroom": post.bathroom,
        "latitude": post.latitude,
        "longitude": post.longitude,
        "type": post.type, #'enums.Type'
        "property": post.property,
        "createdAt": post.createdAt.isoformat()
        # "user": Optional['models.User'] = None
        # "userId": post.userId,
        # "postDetail": Optional['models.PostDetail'] = None
        # savedPosts: Optional[List['models.SavedPost']] = None
    }

async def exec_query(code):
    db = Prisma()
    query = create_query(code)

    await db.connect()
    where_dict =  ast.literal_eval(query)
    posts = await db.post.find_many(where=where_dict)
    try:
        posts_list = list(posts)
    except Exception as e:
        print(f"Error while converting posts to list: {e}")
        posts_list = []

    list_posts = []
    if posts_list:
        for post in posts_list:
            post = format_post(post)
            list_posts.append(post)
            # for field,value in post.items():
            #     if type(value) is list:
            #         print(f"{field} :")
            #         for link in value:
            #             print(f"\t{link}")
            #     else:
            #         print(f"{field} : {value}")
    else:
        print("The post is empty: ",posts)
    await db.disconnect()

    return list_posts

async def mongo_query(user_input:str) -> List[Dict]:
    """
    Processes user input and returns a list of MongoDB query results.

    Args:
        user_input (str): The input string containing user's natural language question.

    Returns:
        List[Dict]: A list of dictionaries representing MongoDB documents.
    """
    return await exec_query(user_input) #asyncio.run(  )

if __name__ == "__main__":
    msg = "Find me a room with 1 bedroom minimum"
    ans = create_query(question=msg)
    print("The code is:",ans)
    # ans = f"""{{'AND': [{{'address' : "kathmandu"}},{{'bedroom' : 2 }}]}}"""
    response = mongo_query(msg)
    print(response)
