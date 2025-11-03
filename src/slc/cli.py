import typer
from slc.core import reporter, scanner, resolver, analyzer

app = typer.Typer(help="Analyze your dependencies' licenses and compliance obligations.")

@app.command()
def scan(path: str = ".", format: str = "markdown", output: str = "license_report.md"):
    """Scan a project directory for dependency licenses."""
    typer.echo(f"🔍 Scanning {path}...")
    deps = scanner.extract_dependencies(path)
    licenses = resolver.resolve_licenses(deps)
    issues = analyzer.check_compliance(licenses)
    reporter.generate(licenses, issues, format, output)
    typer.echo(f"Report saved to {output}")

if __name__ == "__main__":
    app()