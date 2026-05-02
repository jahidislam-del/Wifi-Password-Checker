import subprocess
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i and len(i.split(":")) > 1]
for profile in profiles:
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        print("{:<30}|  {:<}".format(profile, results[0] if results else ""))
    except subprocess.CalledProcessError:
        print("{:<30}|  {:<}".format(profile, "ERROR"))
print("{:<30}|  {:<}".format("WiFi Name", "Password"))
print("-" * 50)
print("{:<30}|  {:<}".format("------------", "--------"))
    