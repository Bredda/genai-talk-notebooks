from .workflow import ResearchState
from datetime import date, datetime, timezone
from pydantic import BaseModel, Field
from backend.llm import get_llm_model
from langchain.prompts import PromptTemplate


max_iterations: int = 3,
context_prompt = """
You are a seasoned research assistant tasked with generating search queries to find relevant information for the following task: "{task}".

Write {max_iterations} google search queries to search online that form an objective opinion for the task"

Assume the current date is {date} if required.
"""
class ResearchSubQueries(BaseModel):
    """List of internet search queries"""
    queries: list[str] = Field(description="List of the generated internet search queries")


class EditorAgent:
    def __init__(self, log):
        self.log = log


    async def plan_research_outline(self, research_state: ResearchState):
        task = research_state.get("task")
        date = datetime.now(timezone.utc).strftime('%B %d, %Y')
        llm = get_llm_model(structured_output=ResearchSubQueries)
        chain = PromptTemplate.from_template(context_prompt) | llm
        self.log("Running initial research on the following query: {query}")
        response = await chain.ainvoke({"task":task.query, "max_iterations":max_iterations, "date":date})
        return {"sub_queries": response['queries']}