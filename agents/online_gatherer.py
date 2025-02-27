from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

class OnlineGatherer:
    def __init__(self):
        self.search_tool = TavilySearchResults(max_results=5)
        self.prompt = ChatPromptTemplate.from_template(
            "Gather relevant information about: {query}\n"
            "Focus on:\n"
            "- Recent developments (last 2 years)\n"
            "- Authoritative sources\n"
            "- Statistical data\n"
            "- Multiple perspectives"
        )
    
    def gather_information(self, query):
        raw_results = self.search_tool.invoke({"query": query})
        processed = self.prompt | RunnablePassthrough()
        return processed.invoke({"query": query, "raw_data": raw_results})
