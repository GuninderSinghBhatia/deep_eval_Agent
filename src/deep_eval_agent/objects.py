from pydantic import BaseModel,Field

class Answer(BaseModel) :
    Answer : str = Field(description="the answer that is needed for the question")
    conversation : bool = Field(description = "This is a indicator if a conversation should continue or not, if the agent has made the decision about refuns agent should stop the conversation")
    
class Purchase(BaseModel):
    name : str = Field(description="name of the item purchased")
    