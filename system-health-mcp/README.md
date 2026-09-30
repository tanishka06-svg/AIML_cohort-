# Local System Health Monitor MCP

A small, local **Model Context Protocol (MCP)** server made to understand the basic ideas of MCP by connecting Claude with live information from a computer.

> **The main idea:** I wanted to make a simple MCP server that can check my computer's current condition and give that information to an AI assistant.

Instead of using sample data, the server reads actual system information such as CPU, RAM, disk, battery, and running processes.

---

# Overview

The Local System Health Monitor gives an MCP-compatible client access to information from the local computer.

The server includes:

- **Tools** — check and collect system information
- **Resource** — provide readable system details
- **Prompt** — give Claude instructions for system diagnosis

The AI can:

- Check current system health
- View basic computer information
- Find processes using more CPU
- Read general system information
- Explain possible system problems

The basic flow is:

```text
┌──────────────────────────┐
│      Claude Desktop      │
│                          │
│    AI reasoning          │
│    Tool calling          │
└────────────┬─────────────┘
             │
             │ MCP / stdio
             ▼
┌──────────────────────────┐
│ Local System Health MCP  │
│                          │
│ Tools                    │
│ Resource                 │
│ Prompt                   │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│       Local Computer     │
│                          │
│ CPU / RAM / Disk / etc.  │
└──────────────────────────┘
```

---

# MCP Components

## Tools

### `check_system_health`

Checks the current CPU, RAM, disk, and battery usage.

The tool also gives a warning when:

- CPU usage is 80% or more
- RAM usage is 80% or more
- Disk usage is 85% or more

Example:

```text
CPU Usage: 88%
Memory Usage: 61%
Disk Usage: 72%

Warnings:
- High CPU usage
```

This is useful when the computer feels slow and I want a quick check of the current system load.

---

### `get_system_info`

Returns basic information about the computer.

It includes:

- Operating system
- Processor
- Physical and logical CPU cores
- Total RAM
- Available RAM

For example, Claude can use this tool when asked:

```text
What are the basic specifications of my computer?
```

---

### `get_top_processes`

Shows the top 10 processes based on CPU usage.

For each process, it provides:

- Process name
- PID
- CPU usage
- Memory usage

For example:

```text
1. chrome.exe
   PID: 1234
   CPU: 24.5%
   Memory: 8.20%
```

This can help find which programs are using a lot of system resources.

---

# Resource

## `system://info`

This resource provides general information about the current computer.

It includes details such as:

- Operating system
- Processor
- CPU cores
- RAM
- Disk space
- Battery status

The resource is read-only. It does not change anything on the computer.

---

# Prompt

## `system_diagnosis`

This is a reusable prompt that tells Claude how to look at the system information.

It asks Claude to check:

- CPU usage
- Memory usage
- Disk usage
- Battery status
- Heavy processes
- Unusual system conditions

It also asks Claude to explain the result in simple language and separate the observed information from possible causes and suggestions.

---

# Example AI Interactions

### Check system health

```text
Is my computer currently under heavy load?
```

Claude can use:

```text
check_system_health
```

### Check computer details

```text
Show me my system information.
```

Claude can use:

```text
get_system_info
```

### Find heavy processes

```text
Which programs are using the most CPU?
```

Claude can use:

```text
get_top_processes
```

### Diagnose the system

```text
Can you check my system and explain if there is anything unusual?
```

The `system_diagnosis` prompt can be used to guide the analysis.

---

# How It Works

The project uses `psutil` to read information directly from the operating system.

```text
Local Computer
      ↓
    psutil
      ↓
   MCP Server
      ↓
  Claude Desktop
```

For example:

```python
psutil.cpu_percent()
```

gets CPU usage, while:

```python
psutil.virtual_memory()
```

gets RAM information.

No database or external API is needed.

---

# Tech Stack

- **Python** — server implementation
- **MCP / FastMCP** — MCP server
- **psutil** — system and process information
- **uv** — Python project and dependency management
- **Claude Desktop** — MCP client
- **MCP Inspector** — testing the server

---

# Project Structure

```text
system-health-mcp/
│
├── server.py
├── pyproject.toml
├── uv.lock
└── README.md
```

The main MCP code is inside:

```text
server.py
```

---

# Getting Started

## Install dependencies

```powershell
uv add "mcp==1.30.0"
uv add psutil
```

## Run the server

```powershell
uv run mcp dev server.py
```
The Inspector should show:

### Tools

```text
check_system_health
get_system_info
get_top_processes
```

### Resource

```text
system://info
```

### Prompt

```text
system_diagnosis
```

# Conclusion

The Local System Health Monitor is a small practical project for learning MCP.

It shows how Claude can use tools, resources, and prompts to work with information from a real computer instead of only using information already available to the model.
