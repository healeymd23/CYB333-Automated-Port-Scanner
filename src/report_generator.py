# Report generation functions for CYB333

def save_report(results):
    with open("reports/sample_scan.txt", "w") as report:
        report.write(results)
