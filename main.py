import os 
from crew import MultiAgentsIA

def main():
    topic = input("📝 Digite o tema da pesquisa: ")
    
    inputs = {"topic": topic}

    crew_instance = MultiAgentsIA().crew()
    result = crew_instance.kickoff(inputs=inputs)

    print(result)

if __name__ == "__main__":
    main()
