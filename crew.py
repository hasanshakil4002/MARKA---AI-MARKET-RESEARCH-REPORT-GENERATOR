import os

from crewai import Agent, Crew, Process, Task , LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import (
    SerperDevTool,
    ScrapeWebsiteTool

)

from dotenv import load_dotenv

load_dotenv()
import litellm

search_tool = SerperDevTool()

scrape_tool = ScrapeWebsiteTool()

toolkit=[search_tool,scrape_tool]

@CrewBase
class MarketResearchAi():
    """MarketResearchAi crew"""



    llm = LLM(
    model="openai/gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("API_BASE"),
    temperature=0.3,
    max_tokens=4000,
    )
    
#     llm = LLM(
#     model="gemini/gemini-3.8-flash",
#     api_key=os.getenv("GEMINI_API_KEY"),
#     temperature=0.2,
# )




    # llm = LLM(
    #     model="ollama/llama3.1:8b",
    #     base_url="http://localhost:11434",
    #     temperature=0.2,
    # )

    # llm = LLM(
    # model="openai/gpt-oss-20b",
    # temperature=0.6
    # )



    agents: list[BaseAgent]
    tasks: list[Task]

    agents_config='config/agents.yaml'
    tasks_config='config/tasks.yaml'
    
    # @agent
    # def searcher(self) -> Agent:
    #     return Agent(
    #         config=self.agents_config['searcher'],
    #         tools=toolkit,
    #         llm=self.llm,
    #         verbose=True
    #     )


    # @task
    # def searcher_task(self) -> Task:
    #     return Task(
    #         config=self.tasks_config['searcher_task'], 
    #         output_file='final_report.md'
    #     )





    
    
    
    #======================Agents=======================
    @agent
    def market_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['market_researcher'], 
            tools=toolkit,
            llm = self.llm,
            verbose=True
        )

    @agent
    def country_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['country_researcher'], 
            tools=toolkit,
            llm = self.llm,
            verbose=True
        )
    
    
    @agent
    def competitor_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['competitor_researcher'],
            tools=toolkit, 
            llm = self.llm,
            verbose=True
        )

    
    
    @agent
    def consumer_trend_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['consumer_trend_researcher'], 
            tools=toolkit,
            llm = self.llm,
            verbose=True
        )

    @agent
    def final_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['final_analyst'],
            tools=toolkit,
            llm = self.llm,
            verbose=True
        )



    #=======================Tasks========================
    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['market_research_task'], 
        )

    @task
    def country_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['country_research_task'], 
            context=[self.market_research_task()],
        
        )

    @task
    def competitor_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['competitor_research_task'],
            context=[self.market_research_task(),self.country_research_task()], 
        
        )

    @task
    def consumer_trend_research_task(self) -> Task:
        return Task(
            config=self.tasks_config['consumer_trend_research_task'], 
            context=[self.market_research_task(),self.country_research_task(),self.competitor_research_task()],
    
        )

    @task
    def final_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['final_analysis_task'],
            context=[self.market_research_task(),self.country_research_task(),self.competitor_research_task(),self.consumer_trend_research_task()],
            output_file='output/final_report.md'
        )




    #=======================Crew==========================
    @crew
    def crew(self) -> Crew:
        """Creates the MarketResearchAi crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )


