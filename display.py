from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align

console = Console()

ASCII_LOGO = """
██╗    ██╗██████╗ ██╗████████╗███████╗    ███╗   ███╗███████╗
██║    ██║██╔══██╗██║╚══██╔══╝██╔════╝    ████╗ ████║██╔════╝
██║ █╗ ██║██████╔╝██║   ██║   █████╗      ██╔████╔██║█████╗  
██║███╗██║██╔══██╗██║   ██║   ██╔══╝      ██║╚██╔╝██║██╔══╝  
╚███╔███╔╝██║  ██║██║   ██║   ███████╗    ██║ ╚═╝ ██║███████╗
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝    ╚═╝     ╚═╝╚══════╝
"""

TAGLINE = "AI-powered README generator"
VERSION = "v0.1.0"


def print_banner():
    combined = Text()
    combined.append(ASCII_LOGO, style="bold cyan")
    combined.append(f"\n  {TAGLINE}", style="italic white")
    combined.append(f"  {VERSION}\n", style="dim white")

    console.print(
        Panel(
            Align.center(combined),
            border_style="cyan",
            padding=(1, 4),
        )
    )


def print_phase_header(title: str):
    console.print(
        Panel(
            f"[bold white]{title}[/bold white]",
            border_style="blue",
            padding=(0, 2),
        )
    )


def print_controls():
    console.print(
        Panel(
            "  [bold cyan]SKIP[/bold cyan] [dim]skip entirely[/dim]   "
            "[bold cyan]TLDR[/bold cyan] [dim]generic answer[/dim]   "
            "[bold cyan]RTFM[/bold cyan] [dim]show help[/dim]   "
            "[bold cyan]QUIT[/bold cyan] [dim]exit[/dim]",
            border_style="dim white",
            padding=(0, 1),
        )
    )


def print_question(text: str, hints: list):
    console.print(f"\n[bold white]{text}[/bold white]")
    for hint in hints:
        console.print(f"[dim]{hint}[/dim]")


def print_rtfm(content: str):
    console.print(
        Panel(
            f"[white]{content}[/white]",
            title="[bold cyan] RTFM [/bold cyan]",
            border_style="cyan",
            padding=(1, 2),
        )
    )


def print_layer_prompt():
    console.print(
        Panel(
            "[bold white]Your README draft is ready and publishable as-is.[/bold white]\n\n"
            "  [bold cyan]Layer 2[/bold cyan] [dim]— usage guide, configuration reference, architecture[/dim]\n"
            "  [bold cyan]Layer 3[/bold cyan] [dim]— security, deployment, changelog, contributing guide[/dim]\n\n"
            "[dim]Type [/dim][bold white]more[/bold white][dim] for both · "
            "[/dim][bold white]layer 2[/bold white][dim] or [/dim][bold white]layer 3[/bold white]"
            "[dim] for one · [/dim][bold white]done[/bold white][dim] to finish[/dim]",
            border_style="cyan",
            padding=(1, 2),
        )
    )


def print_success(message: str):
    console.print(f"\n[bold green]✔[/bold green]  [white]{message}[/white]")


def print_warning(message: str):
    console.print(f"\n[bold yellow]⚠[/bold yellow]  [yellow]{message}[/yellow]")


def print_error(message: str):
    console.print(f"\n[bold red]✘[/bold red]  [red]{message}[/red]")


def print_info(message: str):
    console.print(f"\n[bold blue]→[/bold blue]  [dim]{message}[/dim]")


def print_audit_report(lines: list):
    content = "\n".join(lines)
    console.print(
        Panel(
            content,
            title="[bold white] README Audit [/bold white]",
            border_style="blue",
            padding=(1, 2),
        )
    )
