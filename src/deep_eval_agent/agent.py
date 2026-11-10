from uuid import uuid4

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver

from deep_eval_agent.models import get_groq_model
from deep_eval_agent.objects import Answer
from deep_eval_agent.prompts import agent_system_prompt
from deep_eval_agent.tools import (
    calculate_right_refund,
    get_today_date,
    get_user_purchase,
    issue_refund_ticket,
)

load_dotenv()

model = get_groq_model()

tools = [
    get_user_purchase,
    calculate_right_refund,
    issue_refund_ticket,
    get_today_date,
]


agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=agent_system_prompt,
    response_format=Answer,
    checkpointer=InMemorySaver()
)

def run_conversation() :
    config = {"configurable" : {"thread_id" : str(uuid4())}}
    question = HumanMessage(content="I would like to refund")
    conversation = True
    
    while conversation : 
        response = agent.invoke({"messages" : question}, config= config)
        structured_response = response["structured_response"]
        print(structured_response)
        
        conversation = structured_response.conversation
        
        if conversation :
            user_input = input("reply :/n")
            question = HumanMessage(content=user_input)
    print("the job is done")