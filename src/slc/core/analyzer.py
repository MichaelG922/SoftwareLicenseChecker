import json
from importlib.resources import files

RULES_FILEPATH = files('slc').joinpath('core/rules/default.json')
with open(RULES_FILEPATH, 'r') as rulesFile:
    RULES = json.load(rulesFile)

def classify(license_name):
    for category, licenses in RULES.items():
        if license_name in licenses:
            return category
    return "Unknown"

def check_compliance(licenses):
    issues = []
    for dep in licenses:
        category = classify(dep["license"])
        if category == "Copyleft":
            issues.append({
                "name": dep["name"],
                "license": dep["license"],
                "issue": "Copyleft license may restrict proprietary use"
            })
    return issues
