import re
import csv

log_file = "logs/auth.log"
report_file = "reports/report.txt"
csv_file = "reports/report.csv"

failed_ips = {}

with open(log_file, "r") as file:
    for line in file:

        if "Failed password" in line:

            ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

            if ip_match:

                ip = ip_match.group(1)

                if ip in failed_ips:
                    failed_ips[ip] += 1
                else:
                    failed_ips[ip] = 1


# Display results in terminal
print("\nFailed Login Summary")
print("----------------------")

for ip, count in failed_ips.items():

    print(f"{ip} : {count} failed attempts")

    if count >= 3:
        print(f"ALERT! Possible brute-force attack from {ip}")


# Generate report file
with open(report_file, "w") as report:

    report.write("Security Log Analyzer Report\n")
    report.write("=============================\n\n")

    for ip, count in failed_ips.items():

        report.write(f"{ip} : {count} failed attempts\n")

        if count >= 3:
            report.write(
                f"ALERT! Possible brute-force attack from {ip}\n"
            )

print("\nReport generated successfully!")
print("Location: reports/report.txt")
with open(csv_file, "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow(["IP Address", "Failed Attempts", "Status"])

    for ip, count in failed_ips.items():

        if count >= 3:
            status = "Brute-force Suspected"
        else:
            status = "Normal"

        writer.writerow([ip, count, status])

print("CSV report generated successfully!")
print("Location: reports/report.csv")