import os
from crewai import Crew, Task, Agent, Process
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from dotenv import load_dotenv

load_dotenv()

# LLMs no formato do CrewAI (usa LiteLLM por baixo)  
llm_flash = "gemini/gemini-2.5-flash"
llm_pro = "gemini/gemini-2.5-pro"
llm_preview = "gemini/gemini-3-pro-preview"

llm_map = {
    "gemini-2.5-flash": llm_flash,
    "gemini-2.5-pro": llm_pro,
    "gemini-3-pro-preview": llm_preview
}

@CrewBase
class MultiAgentsIA():
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def gerente(self) -> Agent:
        return Agent(
            config=self.agents_config["gerente"],
            llm=llm_map["gemini-3-pro-preview"]
        )

    @agent
    def pesquisador(self) -> Agent:
        return Agent(
            config=self.agents_config["pesquisador"],
            name="Pesquisador",
            tools=[
                SerperDevTool(),
                ScrapeWebsiteTool(),
            ],
            llm=llm_map["gemini-2.5-flash"]

        )

    @agent
    def analista(self) -> Agent:
        return Agent(
            config=self.agents_config["analista"],
            name="Analista",
            llm=llm_map["gemini-2.5-pro"]

        )

    @agent
    def escritor(self) -> Agent:
        return Agent(
            config=self.agents_config["escritor"],
            name="Escritor",
            llm=llm_map["gemini-2.5-flash"]
        )

    @agent
    def revisor(self) -> Agent:
        return Agent(
            config=self.agents_config["revisor"],
            name="Revisor",
            llm=llm_map["gemini-2.5-pro"]
        )

    @task
    def gerente_task(self) -> Task:
        return Task(
            config=self.tasks_config["gerente_task"],
        )

    @task
    def pesquisador_task(self) -> Task:
        return Task(
            config=self.tasks_config["pesquisador_task"],
        )

    @task
    def analista_task(self) -> Task:
        return Task(
            config=self.tasks_config["analista_task"],
            context=[self.pesquisador_task()],
        )

    @task
    def escritor_task(self) -> Task:
        return Task(
            config=self.tasks_config["escritor_task"],
            context=[self.analista_task()],
            output_file="output/escritor_task.md"
        )

    @task
    def revisor_task(self) -> Task:
        return Task(
            config=self.tasks_config["revisor_task"],
            context=[self.escritor_task()],
            output_file="output/revisor_task.md"
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )