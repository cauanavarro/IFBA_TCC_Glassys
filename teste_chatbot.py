import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from langchain_ollama import ChatOllama
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit


load_dotenv()

usuario = "postgres"
senha = ""
host = "localhost"
porta = "5432"
banco = "glassys"

url_conexao = (
    f"postgresql+psycopg2://"
    f"{usuario}:{senha}@{host}:{porta}/{banco}"
)

# Banco de dados
engine = create_engine(url_conexao)

db = SQLDatabase(engine)


# LLM local
llm = ChatOllama(
    model="llama3.1:8b",
    validate_model_on_init=True,
    temperature=0.0
)


# Toolkit SQL
toolkit = SQLDatabaseToolkit(
    db=db,
    llm=llm
)


SQL_AGENT_PREFIX = """
You are an SQL assistant for an optical store management system.

You interact with a PostgreSQL database to answer questions about the
business data.

Given a user's question:

1. Identify the relevant tables.
2. Inspect their schemas when necessary.
3. Create a syntactically correct PostgreSQL query.
4. Execute the query using the available SQL tools.
5. Analyze the returned data.
6. Provide a direct natural-language answer to the user.

Rules:

- You MUST execute the SQL query before giving the final answer.
- NEVER return only the SQL query as the final answer.
- The final answer MUST be based on the actual result returned by the database.
- Never invent data that was not returned by the database.
- DO NOT execute INSERT, UPDATE, DELETE, DROP, ALTER or other commands
  that modify the database.
- Query only columns relevant to the user's question.
- Unless otherwise requested, limit queries to at most 5 results.
- Do not identify customers, products, employees or other entities by
  their database IDs in the final answer.
- Use their names whenever possible.
- Do not explain SQL queries, tools, internal steps or reasoning.
- Answer the user's question directly and clearly.
- Always write the final answer in Brazilian Portuguese.
- Do NOT use the table "usuarios" to answer questions about customers, products, employees or other entities.
"""


agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    prefix=SQL_AGENT_PREFIX,
    handle_parsing_errors=True,
    verbose=True
)


def chat(pergunta):
    try:
        resposta = agent_executor.invoke({
            "input": pergunta
        })

        return resposta["output"]

    except Exception as e:
        return f"Ocorreu um erro: {e}. Tente novamente."


if __name__ == "__main__":

    while True:

        pergunta = input("Você: ")

        if pergunta.lower() in [
            "sair",
            "encerrar",
            "tchau"
        ]:
            break

        resposta = chat(pergunta)

        print("Chatbot:", resposta)