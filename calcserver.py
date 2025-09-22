from mcp.server.fastmcp import FastMCP



mcp = FastMCP("MathServerAgent", host="127.0.0.1", port=8001)

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    if b == 0:
        return float('inf')  # Handle division by zero
    return a / b

if __name__ == "__main__":
    print("Starting MCP Math server...")
    # Start the MCP server on port 8013
    mcp.run(transport="streamable-http")

    #mcp.run(transport="streamable-http", host="127.0.0.1", port=8013)