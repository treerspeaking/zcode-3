import threading
import subprocess

def ping(ip, results):
  """Pings an IP address and stores the result in a list.

  Args:
    ip: The IP address to ping.
    results: A list to store the ping results.
  """
  try:
    # Use "ping -c 1" to send only one ping request
    completed = subprocess.run(["ping", ip, "-s", "8000", "-c", "1"], capture_output=True)
    output = completed.stdout.decode("utf-8")
    if "bytes from" in output:
      results.append(f"{ip} is reachable")
    else:
      results.append(f"{ip} is unreachable")
  except subprocess.CalledProcessError:
    results.append(f"Error pinging {ip}")

def main():
  """Main function that gets user input, creates threads, and stores results."""
  # Get the IP address from the user
  ip_address = "192.168.1.1"

  results = []
  num_threads = 3  # Since it's just one IP, use a single thread

  # Create and start the thread
  while num_threads > 0:
    thread = threading.Thread(target=ping, args=(ip_address, results))
    print(f"Starting thread {num_threads}")
    thread.start()
    num_threads -= 1

  # Wait for the thread to finish
  thread.join()

  # Print the results
  for result in results:
    print(result)

if __name__ == "__main__":
  main()
