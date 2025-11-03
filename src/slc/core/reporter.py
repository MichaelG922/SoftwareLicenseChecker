def generate(licenses, issues, format, output):
    lines = ["# License Report\n"]
    lines.append("| Dependency | Ecosystem | License |")
    lines.append("|-------------|------------|----------|")
    for d in licenses:
        lines.append(f"| {d['name']} | {d['ecosystem']} | {d['license']} |")
    lines.append("\n## Potential Issues\n")
    if issues:
        for i in issues:
            lines.append(f"- ⚠️ {i['name']}: {i['issue']} ({i['license']})")
    else:
        lines.append("No major issues found.")
    open(output, "w").write("\n".join(lines))
