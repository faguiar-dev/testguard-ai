from pathlib import Path
from rules.flaky_rules import detect_thread_sleep


def analyze_file(file_path):
    content = file_path.read_text(encoding="utf-8")
    findings = []

    findings.extend(detect_thread_sleep(str(file_path), content))

    return findings


def analyze_project(project_path):
    findings = []

    for file_path in Path(project_path).rglob("*.java"):
        findings.extend(analyze_file(file_path))

    return findings


if __name__ == "__main__":
    results = analyze_project("examples")

    for finding in results:
        print(f"[{finding['severity']}] {finding['type']} - {finding['file']}")
        print(f"Issue: {finding['issue']}")
        print(f"Recommendation: {finding['recommendation']}")
        print()