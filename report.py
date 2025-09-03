import csv

def generate():
    with open("sample_report.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Status"])
        writer.writerow(["2025-09-01", "OK"])
        writer.writerow(["2025-09-02", "FAIL"])

if __name__ == "__main__":
    generate()
