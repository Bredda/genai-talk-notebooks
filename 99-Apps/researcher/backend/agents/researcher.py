from . import Task, ResearchState
import streamlit as st





class ResercherAgent:
    def __init__(self, log):
        pass

    async def run_initial_research(self, research_state: ResearchState):
        task = research_state.get("task")
        query = task.query
        source = "web"
        st.write("Running initial research on the following query: {query}")
        return {"task": task, "initial_research": await self.research(query=query, verbose=task.verbose,
                                                                      source=source, tone=self.tone, headers=self.headers)}
    
    async def research(self, query: str, research_report: str = "research_report",
                       parent_query: str = "", verbose=True, source="web", tone=None, headers=None):
        
      pass