# ${\textsf{\color{#C25A7C}Simple Text-to-SQL Project}}$ 📊🧠

Welcome to the Text-to-SQL project! This repository demonstrates a simple yet powerful way to translate natural language queries into SQL statements using an LLM (Large Language Model). Let's dive into the details of this project and how you can get it up and running. 🚀

## ${\textsf{\color{#C25A7C}Project Overview}}$ 📋
Text-to-SQL is a Natural Language Processing (NLP) technique that translates human language queries into structured SQL (Structured Query Language) statements. This project leverages sample data on Customers and Purchases, which are stored in ClickHouse tables, and utilizes the clickhouse-migrations Python library for managing database migrations.

For the LLM, I used Ollama, which helps generate SQL queries based on user questions and returns natural language responses based on the SQL results.

## ${\textsf{\color{#C25A7C}Project Structure}}$ 🗂️

    .
    ├── data  
    │   ├── Customers.csv
    │   ├── Purschases.csv 
    ├── src  
    │   ├── data 
    │   |   ├── run_migrations.py  
    │   ├── migrations
    │   |   ├── 001_create_customers_tbl.sql
    │   |   ├── 001_create_purchases_tbl.sql
    │   ├── text_to_sql
    │   |   ├── main.py
    │   ├── __init__.py
    ├── .env                     
    ├── .gitignore                    
    ├── README.md        
    └── requirements.txt

## ${\textsf{\color{#C25A7C}Set Up}}$ 🛠️
### ${\textsf{\color{#FFC0CB}Clone the Repo}}$
> `git clone git@github.com:M-Nkirote/Simple-Text-to-SQL-Solution.git`
>
> `cd Simple-Text-to-SQL-Solution` 

### ${\textsf{\color{#FFC0CB}Set up virtual environment}}$
> `python -m venv venv`
> 
> `source venv/bin/activate`

### ${\textsf{\color{#FFC0CB}Install dependencies}}$
> `pip install -r requirements.txt`

### ${\textsf{\color{#FFC0CB}Install ClickHouse}}$
Refer to [Clickhouse Installation Steps](https://clickhouse.com/docs/en/install).

### ${\textsf{\color{#FFC0CB}Run migrations}}$
> `cd src/data`
> 
> `python3 run_migrations.py`

### ${\textsf{\color{#FFC0CB}To insert csv data into the ClickHouse table, you can run the following commands on terminal}}$
> `tail -n +2 /Users/nkirote/Simple-Text-to-SQL-Solution/data/Customers.csv | ./clickhouse client --query="INSERT INTO simple_text_to_sql.Customers FORMAT CSV"` 
> 
> `tail -n +2 /Users/nkirote/Simple-Text-to-SQL-Solution/data/Customers.csv | ./clickhouse client --query="INSERT INTO simple_text_to_sql.Customers FORMAT CSV"` 

### ${\textsf{\color{#FFC0CB}To run the text-to-sql script}}$
> `cd src/text_to_sql`
> 
> `python3 main.py`

## ${\textsf{\color{#C25A7C}Sample Questions and Answers}}$ 🗂️ 💬
> ${\textsf{\color{#C25A7C}Question}}$ :  How many people are from Kiambu?
> 
> ${\textsf{\color{#E7A1B0}Answer}}$ :  Based on our customer database, it appears that there are two individuals who hail from Kiambu. These individuals are John Doe and Bob Johnson. They can be found in the Customers table with a city of "Kiambu" and corresponding zip codes of 62701 and 62703 respectively.

> ${\textsf{\color{#C25A7C}Question}}$ :  How much has John Doe spent so far?
> 
> ${\textsf{\color{#E7A1B0}Answer}}$ :  John Doe has spent a total of $1,520 so far.

> ${\textsf{\color{#C25A7C}Question}}$ :  Which items have Bob Johnson ever bought? 
>
> ${\textsf{\color{#E7A1B0}Answer}}$ :  Bob Johnson has purchased a Tablet and a Laptop.

