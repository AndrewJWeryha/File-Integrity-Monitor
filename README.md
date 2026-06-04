# File-Integrity-Monitor

## Project Overview
This project is a beginner, host-based File Integrity Monitor (FIM) written in Python. It establishes a cryptographic baseline of a target file using the SHA-256 algorithm and continuously monitors it for unauthorized modifications or deletions. When a change is detected, the script generates a real-time alert with an explicit timestamp and writes the event to a persistent security log for incident response analysis.


Bash

python simple_fim.py


