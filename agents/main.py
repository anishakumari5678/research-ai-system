from agents.online_gatherer import OnlineGatherer
from agents.research_collector import ResearchCollector
from agents.answer_drafter import AnswerDrafter
from main_graph import create_workflow

def main():
    # Initialize agents
    gatherer = OnlineGatherer()
    researcher = ResearchCollector()
    drafter = AnswerDrafter()
    
    # Create workflow
    workflow = create_workflow(gatherer, researcher, drafter)
    
    # Run research
    query = "Latest breakthroughs in quantum computing error correction"
    result = workflow.invoke({
        "query": query,
        "iterations": 0
    })
    
    print("Final Answer:\n", result["draft"])

if __name__ == "__main__":
    main()
