import logging
from datetime import date

from dotenv import load_dotenv
from langchain.tools import tool

from deep_eval_agent.data import users_data
from deep_eval_agent.objects import Purchase

load_dotenv()


@tool
def get_user_purchase(user: str) -> dict:
    """this tool takes the user username and return a dict of what the user purchase history if the user exists"""
    logging.info(f"using get_user_purchase tool on user : {user}")

    if users_data.get(user):
        return users_data[user]
    return {"status": "there was no username found"}


@tool
def calculate_right_refund(user: str, items: list[Purchase]) -> str:
    """this tool takes a list of items to be returned by the user and username will return how much the items are worth"""
    logging.info(f"using calculate_refund tool to get users : {user}, refund")

    if not users_data.get(user):
        return "there was no username found"

    total_refund = 0
    for item in items:
        if users_data[user].get(item.name):
            total_refund += users_data[user][item.name]["price"]
    return f"the total refund is : {total_refund}"


@tool
def issue_refund_ticket(user : str,refund_amount : int) -> str : 
    """this tool will sent the ticket to the teams to return the refund"""
    
    logging.info(f"using the issue_refun_ticket tool for user :{user}")
    return f"issue ticket has been issued succesfilly with refund{refund_amount}"

@tool
def get_today_date(user:str) -> str:
    """this tool will return todays data"""
    logging.info(f"using the date tool")
    return date.today()

