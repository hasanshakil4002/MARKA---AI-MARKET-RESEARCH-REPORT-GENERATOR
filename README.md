# BuisnessResearchAiAssistant Crew

Welcome to the BuisnessResearchAiAssistant Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/buisness_research_ai_assistant/config/agents.yaml` to define your agents
- Modify `src/buisness_research_ai_assistant/config/tasks.yaml` to define your tasks
- Modify `src/buisness_research_ai_assistant/crew.py` to add your own logic, tools and specific args
- Modify `src/buisness_research_ai_assistant/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the Buisness_Research_AI_Assistant Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The Buisness_Research_AI_Assistant Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the BuisnessResearchAiAssistant Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.






ধাপ ১: প্রজেক্ট ফোল্ডারে যান
powershell
cd "D:\Agent Projects\Crewai\buisness_research_ai_assistant"

(ফোল্ডারের নামে স্পেস থাকলে " " দিয়ে লিখুন।)

ধাপ ২: Ollama চালু আছে কিনা দেখুন
powershell
ollama list

llama3.1:8b তালিকায় থাকতে হবে। না থাকলে:

powershell
ollama pull llama3.1:8b

Ollama বন্ধ থাকলে অন্য একটি টার্মিনালে:

powershell
ollama serve
ধাপ ৩: .env ফাইল ঠিক করুন

প্রজেক্টের রুটে .env:

SERPER_API_KEY=your_serper_key
OPENAI_API_KEY=NA
ধাপ ৪: ডিপেন্ডেন্সি ইনস্টল (প্রতি প্রজেক্টে একবার)
powershell
crewai install

শেষ হলে প্রজেক্টের ভেতরে .venv ফোল্ডার তৈরি হবে। এটা আবার চালানোর দরকার নেই, শুধু নতুন প্যাকেজ যোগ করলে বা pyproject.toml বদলালে লাগবে।

ধাপ ৫: main.py এ inputs ঠিক করুন

src/buisness_research_ai_assistant/main.py খুলে run() ফাংশনে আপনার প্রজেক্টের placeholder অনুযায়ী মান দিন। উদাহরণ:

python
def run():
    inputs = {
        'topic': 'Electric Vehicles',
        'country': 'Bangladesh',
        'current_year': str(datetime.now().year)
    }
    BuisnessResearchAiAssistant().crew().kickoff(inputs=inputs)

agents.yaml ও tasks.yaml এ যেসব {placeholder} লিখেছেন, সবগুলোর মান এখানে থাকতে হবে। একটাও বাদ গেলে error আসবে।

ধাপ ৬: চালান
powershell
crewai run










Windows PowerShell

```
C:\envs\crewenv\Scripts\Activate.ps1

```


uvicorn main:app --reload






for the crew_venv venv command 

New-Item -ItemType Directory -Force D:\venvs

py -3.12 -m venv D:\venvs\Crew_venv

D:\venvs\Crew_venv\Scripts\Activate.ps1

python -m pip install --upgrade pip

# Core
pip install crewai crewai-tools python-dotenv

# Common extras for full projects
pip install requests beautifulsoup4 pandas

# Save the installed versions
pip freeze > D:\venvs\Crew_venv\requirements.txt


D:\venvs\Crew_venv\Scripts\Activate.ps1
pip install -r D:\venvs\Crew_venv\requirements.txt


pip install -r requirements.txt
