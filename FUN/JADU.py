import time
msg = "REDBUNNY IS A HACKER"
for i in range(len(msg)+1):
    print(msg[:i] + "█")
    time.sleep(0.15)