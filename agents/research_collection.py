from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic

class ResearchCollector:
    def __init__(self):
        self.llm = ChatAnthropic(model="claude-3-sonnet-20240229")
        self.prompt = ChatPromptTemplate.from_template(
            """Analyze and organize research data:
            Query: {query}
            Raw Data: {raw_data}
            
            Perform:
            1. Source credibility assessment
            2. Fact validation
            3. Data correlation
            4. Knowledge gap identification"""
        )
    
    def analyze_data(self, query, raw_data):
        chain = self.prompt | self.llm
        return chain.invoke({
            "query": query,
            "raw_data": raw_data
        })
