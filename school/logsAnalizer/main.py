def loadlogs(filename):
    logs = []
    with open(filename, 'r') as file:
        for line in file:
            logs.append(line.strip())
    return logs
def filterlogs(logs, keyword):
    return [log for log in logs if keyword in log]
def displaylogs(logs):
    replacelogs = [log.replace(';', ' |') for log in logs]
    print("ID | TIME                | IP            | EVENT         | INT")
    print("--------------------------------------------------------------")
    for log in replacelogs:
        print(log)
def incidents(logs):
    suspectlogs = []
    loginfail_count = {}
    portscan_count = {}
    incident_keywords = ['LOGIN_FAIL', 'PORT_SCAN', 'MALWARE_ALERT']

    for log in logs:
        fields = log.split(';')
        if len(fields) < 4:
            print(f"Skipping malformed log entry: {log}")
            continue
        timestamp, ip, event, interface = fields
        if event == incident_keywords[0]:
            if ip not in loginfail_count:
                loginfail_count[ip] = []
            loginfail_count[ip].append(timestamp)
        elif event == incident_keywords[1]:
            if ip not in portscan_count:
                portscan_count[ip] = []
            portscan_count[ip].append(timestamp)
        elif event == incident_keywords[2]:
            suspectlogs.append(log)
            print("Malware Alert")

    for ip, times in loginfail_count.items():
        times.sort()
        fail_count = 1
        for i in range(1, len(times)):
            if (parse_time(times[i]) - parse_time(times[i - 1])).total_seconds() <= 5 * 60:
                fail_count += 1
                if fail_count > 3:
                    print("Brute force login")
                    suspectlogs.append(ip)
                    break
            else:
                fail_count = 1

    for ip, times in portscan_count.items():
        times.sort()
        scan_count = 1
        for i in range(1, len(times)):
            if (parse_time(times[i]) - parse_time(times[i - 1])).total_seconds() <= 3 * 60:
                scan_count += 1
                if scan_count > 1:
                    print("Port scan alert")
                    suspectlogs.append(ip)
                    break
            else:
                scan_count = 1

    return suspectlogs

def parse_time(timestamp):
    from datetime import datetime
    return datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

def main():
    logs = loadlogs('logs.txt')
    displaylogs(logs)
    suspi =incidents(logs)
    print("Suspect logs/IPs:")
    for item in suspi:
        print(item)
main()