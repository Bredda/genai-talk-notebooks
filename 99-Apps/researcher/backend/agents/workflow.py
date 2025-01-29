import operator
from typing import Annotated, Sequence, TypedDict,List
from langchain_core.messages import BaseMessage
from pydantic import BaseModel, Field


class Task(BaseModel):
    query: str = Field(description="The query to be answered")
    verbose: bool = Field(description="Whether to print verbose output")

class ResearchState(TypedDict):
    task: Task
    sub_queries: List[str]
    initial_research: str
    sections: List[str]
    research_data: List[dict]
    human_feedback: str
    # Report layout
    title: str
    headers: dict
    date: str
    table_of_contents: str
    introduction: str
    conclusion: str
    sources: List[str]
    report: str


class ResearchSubQueries(BaseModel):
    """List of internet search queries"""
    queries: list[str] = Field(description="List of the generated internet search queries")