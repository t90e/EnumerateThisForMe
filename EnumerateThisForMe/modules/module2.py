import sys, subprocess

def f(domain, common, extensive):

    if extensive == "True":
        wordlist = "modules/wordlists/extensive.txt" 
    else:
       wordlist = "modules/wordlists/common.txt"
    cmd = [sys.executable, "-m", "dirsearch", "-u", domain, "-w", wordlist, "-q"]

    result = subprocess.run(cmd, capture_output=True, text=True)

    print(result.stdout)

if __name__ == "__main__":
    f(sys.argv[1], sys.argv[2], sys.argv[3])