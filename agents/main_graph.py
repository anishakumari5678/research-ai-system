from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Dict, Optional

class ResearchState(TypedDict):
    query: str
    raw_data: Optional[Dict]
    analysis: Optional[Dict]
    draft: Optional[str]
    iterations: int

def create_workflow(gatherer, researcher, drafter):
    workflow = StateGraph(ResearchState)
    
    # Add nodes
    workflow.add_node("gather", gatherer.gather_information)
    workflow.add_node("analyze", researcher.analyze_data)
    workflow.add_node("draft", drafter.draft_answer)
    
    # Set edges
    workflow.set_entry_point("gather")
    workflow.add_edge("gather", "analyze")
    workflow.add_edge("analyze", "draft")
    workflow.add_edge("draft", END)
    
    return workflow.compile()
