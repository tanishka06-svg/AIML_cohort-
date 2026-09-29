# Local System Health Monitor MCP

A simple MCP server that lets Claude check information from the local computer. It uses Python and `psutil`(Python System and Process Utilities) python library.

## MCP Components

### Tools

**1. `check_system_health()`**  
Checks CPU, RAM, disk and battery usage. It also gives warnings when CPU or RAM reaches 80% or more, or disk usage reaches 85% or more.

**2. `get_system_info()`**  
Shows basic computer details such as operating system, processor, CPU cores, RAM and Python version.

**3. `get_top_processes()`**  
Shows the top 10 running processes based on CPU usage, along with their PID and memory usage.

### Resource

**`system://info`**  
Provides read-only information about the current computer, including system, RAM, disk and battery details.

### Prompt

**`system_diagnosis`**  
Gives Claude instructions to check the system information and explain possible problems in simple language.

## How It Works

```text
Computer → psutil → MCP Server → Claude
```

The server gets live information from the computer and passes it to Claude through MCP.

## Technologies

- Python
- MCP / FastMCP
- psutil

