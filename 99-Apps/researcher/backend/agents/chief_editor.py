from .workflow import Task, ResearchState
import time
from . import WriterAgent, EditorAgent, ResercherAgent, PublisherAgent, HumanAgent
from langgraph.graph import StateGraph, END
import streamlit as st

class ChiefEditorAgent:


    def __init__(self, task: Task):
        self.task = task
        self.task_id = int(time.time())


    def _initialize_agents(self):
        self.writer = WriterAgent()
        self.editor = EditorAgent()
        self.researcher = ResercherAgent()
        self.publisher = PublisherAgent()
        self.human = HumanAgent()

    def _create_workflow(self):
        workflow = StateGraph(ResearchState)

        # Add nodes for each agent
        #workflow.add_node("browser", self.researcher.run_initial_research)
        workflow.add_node("planner", self.editor.plan_research_outline)
        #workflow.add_node("researcher", self.editor.run_parallel_research)
        #workflow.add_node("writer", self.writer.run)
        #workflow.add_node("publisher", self.publisher.run)
        #workflow.add_node("human", self.human.review_plan)

        # Add edges
        # workflow.set_entry_point("planner")
        # workflow.add_edge('browser', 'planner')
        # workflow.add_edge('planner', 'human')
        # workflow.add_edge('researcher', 'writer')
       #  workflow.add_edge('writer', 'publisher')

        workflow.add_edge('planner', END)

        # Add human in the loop
         #workflow.add_conditional_edges(
         #    'human',
         #    lambda review: "accept" if review['human_feedback'] is None else "revise",
         #    {"accept": "researcher", "revise": "planner"}
         #)

        return workflow
    
    def init_research_team(self):
        """Initialize and create a workflow for the research team."""
        self._initialize_agents()
        return self._create_workflow()