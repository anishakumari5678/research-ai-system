from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic

class AnswerDrafter:
    def __init__(self):
        self.llm = ChatAnthropic(model="claude-3-haiku-20240307")
        self.prompt = ChatPromptTemplate.from_template(
            """Draft comprehensive answer based on research:
            Query: {query}
            Research: {research_analysis}
            
            Guidelines:
            - Maintain academic tone
            - Cite sources numerically
            - Include statistics
            - Highlight controversies
            - Limit to 1000 words"""
        )
    
    def draft_answer(self, query, research_analysis):
        chain = self.prompt | self.llm
        return chain.invoke({
            "query": query,
            "research_analysis": research_analysis
        })
