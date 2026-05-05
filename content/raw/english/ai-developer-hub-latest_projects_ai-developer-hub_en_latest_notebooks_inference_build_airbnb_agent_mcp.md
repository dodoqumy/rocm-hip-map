---
title: "AI agent with MCPs using vLLM and PydanticAI &#8212; Tutorials for AI developers 12.0"
source_url: "https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/inference/build_airbnb_agent_mcp.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:25:37.259535+00:00
content_hash: "e4e1381106c95535"
---

# AI agent with MCPs using vLLM and PydanticAI[#](#ai-agent-with-mcps-using-vllm-and-pydanticai)

**Author**: Mahdi Ghodsi

**Knowledge level**: Beginner

This tutorial leverages AMD GPUs and **Model Context Protocol (MCP)**, an open standard for exposing LLM tools using an API, to deploy powerful language models like Qwen3. The key components for this tutorial are:

🖥️

**vLLM**for GPU-optimized inference🛠️

**PydanticAI**for agent and tool management🔌

**MCP Servers**for prebuilt tool integration

You’ll learn how to set up your environment, deploy large language models like Qwen3, connect them to real-world tools using MCP, and build a conversational agent capable of reasoning and taking actions.

By the end of this workshop, you’ll have built an AI-powered Airbnb assistant agent that can find a place to stay based on preferences like location, budget, and travel dates.

This tutorial includes the following sections:

## Prerequisites[#](#prerequisites)

This tutorial was developed and tested using the following setup.

### Operating system[#](#operating-system)

**Ubuntu 22.04/24.04**: Ensure your system is running Ubuntu version 22.04 or 24.04.

### Hardware[#](#hardware)

**AMD Instinct™ GPUs**: This tutorial was tested on an AMD Instinct MI300X GPU. Ensure you are using an AMD Instinct GPU or compatible hardware with ROCm support and that your system meets the[official requirements](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html).

### Software[#](#software)

**ROCm 6.3 or 6.4**: Install and verify ROCm by following the[ROCm install guide](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html). After installation, confirm your setup using:This command lists your AMD GPUs with relevant details.

**Note**: For ROCm 6.4 and earlier, use the`rocm-smi`

command instead.**Docker**: Ensure Docker is installed and configured correctly. Follow the Docker installation guide for your operating system.**Note**: Ensure the Docker permissions are correctly configured. To configure permissions to allow non-root access, run the following commands:usermod -aG docker $USER newgrp docker

Verify Docker is working correctly:

run hello-world


## Prepare the training environment[#](#prepare-the-training-environment)

Follow these steps to configure your tutorial environment:

### 1. Pull the Docker image[#](#pull-the-docker-image)

Ensure your system meets the [system requirements](https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html).

Pull the Docker image required for this tutorial:

```
pull rocm/vllm:latest
```

### 2. Launch the Docker container[#](#launch-the-docker-container)

Launch the Docker container and map the necessary directories.

```
run -it --rm \
--network=host \
--device=/dev/kfd \
--device=/dev/dri \
--group-add=video \
--ipc=host \
--cap-add=SYS_PTRACE \
--security-opt seccomp=unconfined \
--shm-size 8G \
-v $(pwd):/workspace \
-w /workspace/notebooks \
rocm/vllm:latest
```

**Note**: This command mounts the current directory to the `/workspace`

directory in the container. Ensure the notebook file is either copied to this directory before running the Docker command or uploaded into the Jupyter Notebook environment after it starts. Save the token or URL provided in the terminal output to access the notebook from your web browser. You can download this notebook from the [AI Developer Hub GitHub repository](https://github.com/ROCm/gpuaidev).

### 3. Install and launch Jupyter[#](#install-and-launch-jupyter)

Inside the Docker container, install Jupyter using the following command:

```
install jupyter
```

Start the Jupyter server:

```
--ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

**Note**: Ensure port `8888`

is not already in use on your system before running the above command. If it is, you can specify a different port by replacing `--port=8888`

with another port number, for example, `--port=8890`

.

## Step 1: Launching the vLLM server[#](#step-1-launching-the-vllm-server)

In this workshop, you’ll use [vLLM](https://github.com/vllm-project/vllm) as your inference serving engine. vLLM provides many benefits, such as fast model execution, an extensive list of supported models, and ease of use. Best of all, it’s open source.

### Deploy the Qwen3-30B-A3B model with vLLM[#](#deploy-the-qwen3-30b-a3b-model-with-vllm)

It’s time to start your vLLM server and create an endpoint for your LLM. First open a terminal using your Jupyter server. Then run the following command in this terminal to start the vLLM server:

```
VLLM_USE_TRITON_FLASH_ATTN=0 \
vllm serve Qwen/Qwen3-30B-A3B \
--served-model-name Qwen3-30B-A3B \
--api-key abc-123 \
--port 8000 \
--enable-auto-tool-choice \
--tool-call-parser hermes \
--trust-remote-code
```

Open another terminal and monitor the GPU utilization by running this command.

**Note**: For ROCm 6.4 and earlier, use the `rocm-smi`

command instead.

```
amd-smi
```

After a successful launch, your server should be accepting incoming traffic through an OpenAI-compatible API. Now set some environment variables for your server to use throughout this tutorial:

```
import os
BASE_URL = f"http://localhost:8000/v1"
os.environ["BASE_URL"] = BASE_URL
os.environ["OPENAI_API_KEY"] = "abc-123"
print("Config set:", BASE_URL)
```

Verify the model is available at the `BASE_URL`

you just set by running the following command.

```
!curl http://localhost:8000/v1/models -H "Authorization: Bearer $OPENAI_API_KEY"
```

Congratulations, you just launched a powerful server that can serve any incoming request, allowing you to build amazing applications.

## Step 2: Installing dependencies[#](#step-2-installing-dependencies)

Install the PydanticAI dependencies using this command:

```
!pip install -q pydantic_ai openai
```

## Step 3: Create a simple instance of a PydanticAI agent[#](#step-3-create-a-simple-instance-of-a-pydanticai-agent)

Start by creating a custom OpenAI-compatible endpoint for your agent.

```
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
provider = OpenAIProvider(
base_url=os.environ["BASE_URL"],
api_key=os.environ["OPENAI_API_KEY"],
)
agent_model = OpenAIModel("Qwen3-30B-A3B", provider=provider)
```

Now create an instance of the `Agent`

class from `pydantic_ai`

.

```
from pydantic_ai import Agent
agent = Agent(
model=agent_model
)
```

It’s time to test the agent. The `pydantic_ai`

framework provides multiple ways to run an `Agent`

instance. To learn more, see the [PydanticAI site](https://ai.pydantic.dev/agents/#running-agents).

In this workshop, you are running the agent in `async`

mode. Define a helper function that allows you to quickly test your agent.

```
import asyncio
from pydantic_ai.mcp import MCPServerStdio
async def run_async(prompt: str) -> str:
async with agent.run_mcp_servers():
result = await agent.run(prompt)
return result.output
```

Test the agent by calling this function.

```
await run_async("What is the capital of France?")
```

Now that you have the basics of an agent instance, connect it to the model you are serving with vLLM.

## Step 4: Write a date/time tool for your agent[#](#step-4-write-a-date-time-tool-for-your-agent)

LLMs rely on their training data to respond to your prompts, so the agent you just defined would fail to answer a factual question that falls outside of its training knowledge. You can show this with an example:

```
await run_async("What’s the date today?")
```

It’s no surprise that the model failed to answer this question. Now it’s time to power-up your LLM by providing the agent with a function that can get the current date. The process by which an LLM triggers a function call is commonly referred to as “Tool Calling” or “Function Calling”. In this workshop, you’re going to take advantage of the `pydantic_ai`

agent `Tool`

package to provide the agent with appropriate tools. First, define a custom tool within this framework using the code sample below.

```
from datetime import datetime
from pydantic_ai import Tool
@Tool
def get_current_date() -> str:
"""Return the current date/time as an ISO-formatted string."""
return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

Next, provide this tool to your agent by adding the function signature of the tool to the `Agent`

constructor. This notifies the LLM that the new tool exists.

```
agent = Agent(
model=agent_model,
tools=[get_current_date],
system_prompt = (
"You have access to:\n"
" 1. get_current_time(params: dict)\n"
"Use this tool for date/time questions."
)
)
```

Now test the agent.

```
await run_async("What’s the date today?")
```

Congratulations on building an agent with access to real-time data.

## Step 5: Replace the date/time tool with an MCP server[#](#step-5-replace-the-date-time-tool-with-an-mcp-server)

Now that you learned how to create a custom tool and let the agent access it, you can enhance this step using the [Model Context Protocol](https://modelcontextprotocol.io/introduction) (MCP). You can replace the custom tool with a simple MCP server that serves the agent and provides similar information.

Why should you use MCP? MCP servers provide:

✅ Standardized API interfaces

🔄 Reusability across projects

📦 Prebuilt functionality


To replace your custom time tool with an official MCP time server, follow these steps:

### Installing an MCP time server[#](#installing-an-mcp-time-server)

Start by installing the MCP server:

```
!pip install -q mcp-server-time
```

Now define the `time_server`

:

```
from pydantic_ai.mcp import MCPServerStdio
time_server = MCPServerStdio(
"python",
args=[
"-m", "mcp_server_time",
"--local-timezone=America/New_York",
],
)
```

Finally, modify your agent by removing the previously defined tool and adding the MCP server instead.

```
agent = Agent(
model=agent_model,
toolsets=[time_server],
system_prompt = (
"You are a helpful agent and you have access to this tool:\n"
" get_current_time(params: dict)\n"
"When the user asks for the current date or time, call get_current_time.\n"
)
)
```

You can now see whether the agent can use MCP to provide the correct time.

```
await run_async("What’s the date today?")
```

You have now used an official MCP server to power up your agent. In the next section, you’ll learn how to turn your ideas into real working projects by using the hundreds of available free or paid MCP servers.

## Step 6: Turn your agent into an Airbnb finder[#](#step-6-turn-your-agent-into-an-airbnb-finder)

As you discovered in the last section, MCP servers are very easy to use. They provide a standard way of providing LLMs with the tools they need. There are already thousands of MCP servers available for you to use. Consult one of the following MCP trackers as a reference to find out about the available servers:

You will use npx to launch your next server. Use the following commands to install the required dependencies:

```
# Install Node.js 20 via NodeSource
!curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
!apt install -y nodejs
```

Verify the `npm`

and `npx`

installations:

```
!node -v && npm -v && npx --version
```

In this part of the workshop, you’re going to build an agent to help browse available Airbnbs listings to book. You can build on top of what you’ve done already and add an open-source Airbnb MCP server to your agent. Start by defining the Airbnb server.

```
airbnb_server = MCPServerStdio(
"npx", args=["-y", "@openbnb/mcp-server-airbnb", "--ignore-robots-txt"]
)
```

Now update your agent.

```
system_prompt = """
You have access to three tools:
1. get_current_time(params: dict)
2. airbnb_search(params: dict)
3. airbnb_listing_details(params: dict)
When the user asks for listings, first call get_current_time, then airbnb_search, etc.
"""
agent = Agent(
model=agent_model,
toolsets=[time_server, airbnb_server],
system_prompt=system_prompt,
)
```

Finally, see if your agent can browse through the Airbnb listings.

```
await run_async("Find a place to stay in Vancouver for next Sunday for 3 nights for 2 adults?")
```

## Step 7: Challenge to expand the agent[#](#step-7-challenge-to-expand-the-agent)

For an additional challenge, add weather integration using the MCP weather server of your choice:

Launch the MCP weather server

Add it to the list of agent tools

Ask the agent to suggest the best travel dates based on the weather
