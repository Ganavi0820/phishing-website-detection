
# Phishing URL Awareness Checker

## 1. Project Overview

The Phishing URL Awareness Checker is a beginner-friendly Python cybersecurity project.

It examines URL text and identifies common warning signs that may be associated with phishing URLs.

The program does not open websites, send network requests, or use online reputation services.

## 2. Objectives

- Understand common phishing URL warning signs.
- Identify suspicious URL patterns.
- Improve awareness of phishing attacks.
- Provide simple explanations for detected warnings.

## 3. Features

The program checks for six warning signs:

1. Presence of the @ symbol.
2. URL length greater than 100 characters.
3. IP address used as the hostname.
4. Five or more hostname segments.
5. Punycode marker (xn--).
6. HTTP instead of HTTPS.

## 4. Additional Improvements

- Multiple URL checking using a loop.
- Explanations for detected warning signs.
- Handling malformed URLs without crashing.
- Clear and user-friendly output.
- Cautious message when no warning signs are detected.

## 5. Technologies Used

- Python 3
- Visual Studio Code
- Python standard libraries:
  - ipaddress
  - urllib.parse

## 6. How to Run the Project

1. Install Python 3.10 or later.
2. Open the project folder in Visual Studio Code.
3. Open the integrated terminal.
4. Run the following command:

   python phishing_checker.py

5. Enter a URL when prompted.
6. Type quit to exit the program.

## 7. Sample Output

Input:

https://www.example.com/login

Output:

No warning signs detected.
This does NOT guarantee that the URL is safe.

## 8. Testing

The program was tested using five required sample URLs:

| Test | Description | Result |
|---|---|---|
| 1 | Normal HTTPS URL | Passed |
| 2 | IP address hostname | Passed |
| 3 | URL containing @ symbol | Passed |
| 4 | Hostname with five or more segments | Passed |
| 5 | Punycode hostname | Passed |

An additional malformed URL test was also completed successfully.

## 9. Project Structure

phishing website detection/
- phishing_checker.py
- README.md
- requirements.txt
- tests/test_samples.md
- screenshots/sample_run.png
- screenshots/test_results.png

## 10. Limitations

- The program checks URL text only.
- It does not confirm whether a website is genuinely malicious.
- Absence of warning signs does not guarantee safety.
- It does not visit websites or check online reputation.

## 11. Conclusion

This project demonstrates how Python can be used to identify common phishing-related URL warning signs.

It helps users become more aware of suspicious URL patterns and encourages careful browsing.
