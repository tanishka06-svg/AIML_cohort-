from mcp.server.fastmcp import FastMCP
import psutil
import platform
import sys

#defining an mcp serevr

mcp = FastMCP("Local System Health Monitor")

#Tool-1 for checking system health
@mcp.tool()
def check_system_health() -> str:
    """
    Check current CPU, memory, disk and battery usage.
    """

    cpu_usage = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()
    memory_usage = memory.percent

    disk = psutil.disk_usage("/")
    disk_usage = disk.percent

    battery = psutil.sensors_battery()

    if battery:
        battery_status = f"{battery.percent}%"
        charging = "Yes" if battery.power_plugged else "No"
    else:
        battery_status = "Not available"
        charging = "Not available"

    warnings = []

    if cpu_usage >= 80:
        warnings.append("High CPU usage")

    if memory_usage >= 80:
        warnings.append("High memory usage")

    if disk_usage >= 85:
        warnings.append("High disk usage")

    if warnings:
        overall_status = "Attention Required"
        warning_text = "\n".join(
            f"- {warning}" for warning in warnings
        )
    else:
        overall_status = "Normal"
        warning_text = "No major resource warnings detected."

    return f"""
SYSTEM HEALTH REPORT

Overall Status:
{overall_status}

CPU Usage:
{cpu_usage}%

Memory Usage:
{memory_usage}%

Disk Usage:
{disk_usage}%

Battery:
{battery_status}

Charging:
{charging}

Warnings:
{warning_text}
"""
# Tool-2 Getting System Information

@mcp.tool()
def get_system_info() -> str:
    """
    Get basic information about the local computer.
    """

    memory = psutil.virtual_memory()

    physical_cores = psutil.cpu_count(logical=False)
    logical_cores = psutil.cpu_count(logical=True)

    return f"""
SYSTEM INFORMATION

Operating System:
{platform.system()} {platform.release()}

Machine:
{platform.machine()}

Processor:
{platform.processor()}

Physical CPU Cores:
{physical_cores}

Logical CPU Cores:
{logical_cores}

Total RAM:
{memory.total / (1024 ** 3):.2f} GB

Available RAM:
{memory.available / (1024 ** 3):.2f} GB

Python Version:
{sys.version.split()[0]}
"""

#Tool-3: Get Top Processes
@mcp.tool()
def get_top_processes() -> str:
    """
    Get the processes currently using the most CPU.
    """

    processes = []

    for process in psutil.process_iter(
        ["pid", "name", "cpu_percent", "memory_percent"]
    ):
        try:
            info = process.info

            processes.append({
                "pid": info["pid"],
                "name": info["name"],
                "cpu": info["cpu_percent"],
                "memory": info["memory_percent"]
            })

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            continue

    processes.sort(
        key=lambda x: x["cpu"],
        reverse=True
    )

    top_processes = processes[:10]

    result = []

    for index, process in enumerate(
        top_processes,
        start=1
    ):
        result.append(
            f"{index}. {process['name']}\n"
            f"   PID: {process['pid']}\n"
            f"   CPU: {process['cpu']}%\n"
            f"   Memory: {process['memory']:.2f}%"
        )

    return "TOP PROCESSES\n\n" + "\n\n".join(result)

# Resource: System Information

@mcp.resource("system://info")
def system_info() -> str:
    """
    Provide read-only information about the local computer.
    """

    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    battery = psutil.sensors_battery()

    if battery:
        battery_info = (
            f"{battery.percent}% "
            f"(Charging: "
            f"{'Yes' if battery.power_plugged else 'No'})"
        )
    else:
        battery_info = "Not available"

    return f"""
LOCAL SYSTEM INFORMATION

Operating System:
{platform.system()} {platform.release()}

Machine:
{platform.machine()}

Processor:
{platform.processor()}

Physical CPU Cores:
{psutil.cpu_count(logical=False)}

Logical CPU Cores:
{psutil.cpu_count(logical=True)}

Total RAM:
{memory.total / (1024 ** 3):.2f} GB

Available RAM:
{memory.available / (1024 ** 3):.2f} GB

Disk Total:
{disk.total / (1024 ** 3):.2f} GB

Disk Free:
{disk.free / (1024 ** 3):.2f} GB

Battery:
{battery_info}
"""

# Prompt: System Diagnosis
# ============================================================

@mcp.prompt()
def system_diagnosis() -> str:
    """
    Provide a reusable instruction for diagnosing system health.
    """

    return """
Analyze the current computer system information.

Focus on:

1. CPU usage
2. Memory usage
3. Disk usage
4. Battery status
5. Resource-heavy processes
6. Any unusual system conditions

Explain the findings in simple language.

If a resource is unusually high, suggest safe
and practical troubleshooting steps.

Do not recommend deleting files, changing system
settings, or terminating processes unless the user
explicitly asks.

Clearly separate:
- Observed information
- Possible causes
- Suggested actions
"""

if __name__ == "__main__":
    mcp.run()