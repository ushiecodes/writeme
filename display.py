from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich.table import Table
from rich.rule import Rule
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
AUTHOR = "ushiecodes"
GITHUB = "https://github.com/ushiecodes/writeme"


def print_banner():
    logo_text = Text(ASCII_LOGO, style="bold cyan", justify="left", no_wrap=True, overflow="crop")
    tagline_text = Text(f"{TAGLINE}  {VERSION}", style="italic white", justify="left")
    meta = Text.assemble(
        ("by ", "dim white"),
        (AUTHOR, "bold cyan"),
        ("   ", ""),
        (GITHUB, f"link {GITHUB} cyan"),
    )

    content = Table.grid(expand=True)
    content.add_column(justify="left")
    content.add_row(logo_text)
    content.add_row(tagline_text)
    content.add_row(meta)

    console.print(Panel(content, border_style="cyan", padding=(0, 2), width=80))


def print_info_box(cwd: str, api_key_loaded: bool):
    content = Table.grid(expand=True)
    content.add_column()

    content.add_row(Text("  How it works", style="bold white"))
    content.add_row(Text.assemble(("  1  ", "bold cyan"), ("Answer questions about your project", "white")))
    content.add_row(Text.assemble(("  2  ", "bold cyan"), ("WriteMe scans your codebase", "white")))
    content.add_row(Text.assemble(("  3  ", "bold cyan"), ("Gemini AI generates a README.md", "white")))
    content.add_row(Rule(style="dim white"))
    content.add_row(Text.assemble(("  Tip  ", "bold cyan"), ("Type ", "dim white"), ("RTFM", "bold cyan"), (" on any question for help", "dim white")))
    content.add_row(Rule(style="dim white"))
    content.add_row(Text.assemble(("  Running in  ", "dim white"), (cwd, "cyan")))

    if api_key_loaded:
        content.add_row(Text.assemble(("  ", ""), ("✔", "bold green"), ("  API key loaded", "white")))
    else:
        content.add_row(Text.assemble(("  ", ""), ("→", "bold blue"), ("  No API key found — you will be prompted", "dim white")))

    content.add_row(Text(""))

    console.print(Panel(content, border_style="white", padding=(0, 1), width=80))
    console.print("")


def print_phase_controls(phase_title: str):
    content = Table.grid(expand=True)
    content.add_column()
    content.add_row(Text(f"  {phase_title}", style="bold white"))
    content.add_row(Rule(style="dim white"))
    content.add_row(
        Text.assemble(
            ("  SKIP ", "bold cyan"), ("skip   ", "dim white"),
            ("TLDR ", "bold cyan"), ("generic   ", "dim white"),
            ("RTFM ", "bold cyan"), ("help   ", "dim white"),
            ("QUIT ", "bold cyan"), ("exit", "dim white"),
        )
    )
    console.print(Panel(content, border_style="white", padding=(0, 1), width=80))

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
            width=80,
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
