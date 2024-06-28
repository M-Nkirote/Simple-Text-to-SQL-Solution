import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.utilities import SQLDatabase
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.chat_models import ChatOllama
import re

load_dotenv()

# 1. Establish connection to ClickHouse

db_host = os.getenv("CLICKHOUSE_HOST")
db_user = os.getenv("CLICKHOUSE_USER")
db_password = os.getenv("CLICKHOUSE_PASSWORD")
db_name = os.getenv("CLICKHOUSE_DATABASE")

connection_url = f'clickhouse://{db_user}:{db_password}@{db_host}:8123/{db_name}'

db = SQLDatabase.from_uri(connection_url)


def get_schema(_):
    return db.get_table_info()

# print("\n ------------------------- \n This is my schema : ", get_schema(None))


# 2. Interact with the LLM

# 2.1. Define the LLM
llm = ChatOllama(model='llama3')

# 2.1. Define the user question
user_question = "Which items have Bob Johnson ever bought?"

# 2.2. Generate the SQL query
generate_sql_query_prompt_template = """Based on the table schema below, write a SQL query that would answer the user's question:
{schema}

Question: {question}
SQL Query:
"""
generate_sql_query_prompt = ChatPromptTemplate.from_template(generate_sql_query_prompt_template)

# print("Simple starter prompt to ask how many users are there : ", prompt.format(schema="simple_text_to_sql",
# question="how many users are there?"))


sql_chain = (
        RunnablePassthrough.assign(schema=get_schema)
        | generate_sql_query_prompt
        | llm
        | StrOutputParser()
)

sql_chain_query = sql_chain.invoke({"question": user_question})

# 2.2. Extract the 'sql' from the sql_chain response
match = re.search(r'```sql(.*?)```', sql_chain_query, re.DOTALL)
extracted_sql = match.group(1).strip()

# 2.3. Generate response using the LLM
template = """
Based on the table schema below, question, sql query, and sql response, write a natural language response:
{schema}

Question: {question}
SQL Query: {query}
SQL Response: {response}

Do not have a statement like "Here's a natural language response:" in the response
"""

prompt = ChatPromptTemplate.from_template(template)


def run_query(query):
    # print("\n ************ Running query is ****: ", query, "******")
    return db.run(query)


full_chain = (
        RunnablePassthrough.assign(query=sql_chain).assign(
            schema=get_schema,
            response=lambda variables: run_query(extracted_sql)
        )
        | prompt
        | llm
)
full_chain_response = full_chain.invoke({"question": user_question})

full_chain_answer = full_chain_response.content

print("Question : ", user_question, "\n")
print("Answer : ", full_chain_answer)
