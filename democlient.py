import asyncio
import os
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import AzureChatOpenAI

load_dotenv()


async def main(prompt: str):
    print("Starting MCP Client...")
    
    # Define all possible servers
    servers = {
        "MathServerAgent": {
            "url": "http://127.0.0.1:8001/mcp",
            "transport": "streamable_http"
        }
    }

    
    # Create client with only working servers
    try:
        client = MultiServerMCPClient(servers)
        tools = await client.get_tools()
        print(f"Loaded {len(tools)} tools from available servers")
    except Exception as e:
        error_msg = f"Failed to initialize MCP client: {e}"
        print(error_msg)
        return error_msg

    llm = AzureChatOpenAI(
        azure_endpoint="https://sparkapi.spglobal.com/v1/sparkassist",
        azure_deployment="gpt-4o-mini",
        openai_api_version="2024-02-01",
        api_key=os.getenv("SPARK_API_TOKEN")
    )
    
    agent = create_react_agent(
        llm,
        tools
    )

    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": prompt}]}
    )

    content = response['messages'][-1].content
    print(content)

asyncio.run(main("What is 25 multiplied by 6 and what is Open AI?"))

# Sample prompts
# What is 25 multiplied by 6 and what is Open AI?
# Explain Model Context Protocol in less than 50 words and also calculate 40 multiplied by 8?