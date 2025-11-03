import json, re, os

def extract_dependencies(path: str):
    deps = []
    req_file = os.path.join(path, "requirements.txt")
    pkg_file = os.path.join(path, "package.json")

    # Python
    if os.path.exists(req_file):
        with open(req_file) as f:
            for line in f:
                match = re.match(r"([a-zA-Z0-9_\-]+)", line)
                if match:
                    deps.append({"name": match.group(1), "ecosystem": "pypi"})

    # Node
    elif os.path.exists(pkg_file):
        with open(pkg_file) as f:
            pkg = json.load(f)
            for name in pkg.get("dependencies", {}):
                deps.append({"name": name, "ecosystem": "npm"})

    return deps
