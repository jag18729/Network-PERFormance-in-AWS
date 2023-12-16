import subprocess
import threading
import datetime

# Server IPs
server_ips = ['44.214.93.244', '3.235.16.122', '44.201.3.152']
# Replace with actual IPs

def run_iperf3(server_ip):
    try:
        # iPerf3 command with reverse testing and interval set to 1 second
        command = ['iperf3', '-c', server_ip, '-R', '-i', '1', '-t', '60']  # 60 seconds duration
        result = subprocess.run(command, capture_output=True, text=True, timeout=70)
        return result.stdout
    except subprocess.TimeoutExpired:
        return f"iperf3 test timed out for server {server_ip}\n"
    except Exception as e:
        return f"Error: {e}\n"

def main():
    threads = []
    results = []

    for server_ip in server_ips:
        thread = threading.Thread(target=lambda: results.append(run_iperf3(server_ip)))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    # Save results to a file
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"iperf_results_{timestamp}.txt"
    with open(filename, 'w') as file:
        for result in results:
            file.write(result)

    return filename

if __name__ == '__main__':
    result_file = main()
    print(f"Results saved in {result_file}")

