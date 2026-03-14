import os
import json
from typing import List, Dict, Any, Callable
from openai import OpenAI

class AstraeusAgent:
    \"\"\"
    Autonomous agent core implementing the ReAct (Reasoning + Acting) pattern.
    Designed for complex task orchestration and tool integration.
    \"\"\"
    def __init__(self, api_key: str, model: str = "gpt-4-turbo-preview"):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.tools: Dict[str, Callable] = {}
        self.history: List[Dict[str, str]] = []

    def register_tool(self, name: str, func: Callable):
        self.tools[name] = func

    def _generate_system_prompt(self) -> str:
        tool_desc = "\n".join([f"- {name}: {func.__doc__}" for name, func in self.tools.items()])
        return f\"\"\"
        You are Astraeus, an advanced autonomous agent. 
        You operate in a Think-Action-Observe loop.
        
        Available Tools:
        {tool_desc}
        
        Guidelines:
        1. Think: Analyze the current state and plan the next step.
        2. Action: Call a tool if necessary. Use JSON format: {{\"tool\": \"name\", \"input\": \"args\"}}.
        3. Observe: Process the tool output and refine your strategy.
        \"\"\"

    def execute(self, task: str, max_iterations: int = 5):
        print(f"[ASTRAEUS] Starting task: {task}")
        self.history.append({"role": "system", "content": self._generate_system_prompt()})
        self.history.append({"role": "user", "content": task})

        for i in range(max_iterations):
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.history,
                response_format={"type": "json_object"} if "gpt-4" in self.model else None
            )
            
            content = response.choices[0].message.content
            print(f"\n[THOUGHT] Iteration {i+1}:\n{content}")
            self.history.append({"role": "assistant", "content": content})

            try:
                action = json.loads(content)
                if "tool" in action and action["tool"] in self.tools:
                    result = self.tools[action["tool"]](action["input"])
                    print(f"[OBSERVATION] {result}")
                    self.history.append({"role": "system", "content": f"Observation: {result}"})
                else:
                    print("[FINAL] Task completed or no further action needed.")
                    break
            except Exception as e:
                print(f"[ERROR] Failed to parse action: {e}")
                break

if __name__ == "__main__":
    # Example initialization
    agent = AstraeusAgent(api_key="sk-...")
    print("Astraeus Intelligence Core Initialized.")