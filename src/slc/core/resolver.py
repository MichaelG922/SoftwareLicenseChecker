import requests

PYPI_URL = "https://pypi.org/pypi"
NPM_URL = "https://registry.npmjs.org"

def resolve_licenses(dependencies):
    results = []
    for dep in dependencies:
        if dep["ecosystem"] == "pypi":
            url = f"{PYPI_URL}/{dep['name']}/json"
            data = requests.get(url).json()
            license_ = data["info"].get("license") or "Unknown"
        elif dep["ecosystem"] == "npm":
            url = f"{NPM_URL}/{dep['name']}"
            data = requests.get(url).json()
            license_ = data.get("license") or data.get("licenses", [{"type":"Unknown"}])[0]["type"]
        else:
            license_ = "Unknown"

        results.append({
            "name": dep["name"],
            "ecosystem": dep["ecosystem"],
            "license": license_
        })
    return results
