def detect_thread_sleep(file_path, file_content):
    findings = []

    if "Thread.sleep" in file_content:
        findings.append({
            "type": "Flaky Risk",
            "severity": "High",
            "file": file_path,
            "issue": "Thread.sleep detected",
            "recommendation": "Replace fixed waits with explicit waits."
        })

    return findings