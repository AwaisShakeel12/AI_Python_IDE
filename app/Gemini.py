from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

from langchain_groq import ChatGroq
# from .views import code

PRODUCT_BOT_TEMPLATE = """
You are an python expert, you goal is to analayze code and find the error and  provide a 
best possible solution in python format. 
provide best optimize answer 
answer should be in python code.
CONTEXT:
{context}

QUESTION: {question}

YOUR ANSWER:
"""

prompt = ChatPromptTemplate.from_template(PRODUCT_BOT_TEMPLATE)

llm = ChatGroq(model='llama-3.1-70b-versatile', groq_api_key='')

# Build the chain
chain = (
    { "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)
