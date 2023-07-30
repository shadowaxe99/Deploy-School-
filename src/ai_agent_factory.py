```python
from openai import OpenAI

class AIAgentFactory:
    def __init__(self, whisper_api_key):
        self.whisper_api_key = whisper_api_key
        self.openai = OpenAI(self.whisper_api_key)

    def create_agent(self):
        return self.openai.create_agent()

    def delete_agent(self, agent_id):
        return self.openai.delete_agent(agent_id)

    def get_agent(self, agent_id):
        return self.openai.get_agent(agent_id)

    def list_agents(self):
        return self.openai.list_agents()

    def update_agent(self, agent_id, **kwargs):
        return self.openai.update_agent(agent_id, **kwargs)
```