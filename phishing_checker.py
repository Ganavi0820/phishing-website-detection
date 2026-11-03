

import ipaddress
from urllib.parse import urlparse


def inspect_url(raw_url):
    warnings = []

    if not raw_url or not raw_url.strip():
        return ["Empty URL entered."]

    raw_url = raw_url.strip()

    # Check URL length
    if len(raw_url) > 100:
        warnings.append("URL is longer than 100 characters.")

    # Check @ symbol
    if "@" in raw_url:
        warnings.append("URL contains an @ symbol.")

    # Add scheme if missing
    url_to_check = raw_url
    if "://" not in url_to_check:
        url_to_check = "http://" + url_to_check

    try:
        parsed_url = urlparse(url_to_check)
        hostname = parsed_url.hostname

        if not hostname:
            return warnings + ["Invalid URL: hostname not found."]

        # Check IP address
        try:
            ipaddress.ip_address(hostname)
            warnings.append("URL uses an IP address as its hostname.")
        except ValueError:
            pass

        # Check hostname segments
        if len(hostname.split(".")) >= 5:
            warnings.append("Hostname contains five or more segments.")

        # Check punycode
        if "xn--" in hostname.lower():
            warnings.append("Hostname contains a punycode marker (xn--).")

        # Check HTTP scheme
        if parsed_url.scheme.lower() == "http":
            warnings.append("URL uses HTTP instead of HTTPS.")

    except ValueError:
        warnings.append("Malformed URL: unable to parse the address.")

    return warnings


def main():
    print("=" * 45)
    print("       PHISHING URL AWARENESS CHECKER")
    print("=" * 45)
    print("This tool checks URL text only.")
    print("It does not open or visit websites.")
    print("Type 'quit' to exit.\n")

    while True:
        url = input("Enter a URL: ").strip()

        if url.lower() == "quit":
            print("Thank you for using the checker!")
            break

        warnings = inspect_url(url)

        print("\n--- Scan Results ---")

        if warnings:
            for warning in warnings:
                print("[WARNING]", warning)

                if "@ symbol" in warning:
                    print("  Explanation: The @ symbol can hide the actual website address.")

                elif "HTTP" in warning:
                    print("  Explanation: HTTP does not provide encrypted communication.")

                elif "IP address" in warning:
                    print("  Explanation: An IP address as a hostname may need extra checking.")

                elif "segments" in warning:
                    print("  Explanation: An unusually long hostname may be suspicious.")

                elif "punycode" in warning:
                    print("  Explanation: Punycode can represent international characters that resemble other characters.")

                elif "100 characters" in warning:
                    print("  Explanation: Very long URLs can make the destination harder to recognize.")

                elif "Malformed URL" in warning:
                    print("  Explanation: The entered URL has an invalid format.")

            print("\nReview carefully: this URL has warning signs.")

        else:
            print("No warning signs detected.")
            print("This does NOT guarantee that the URL is safe.")

        print("-" * 45)


if __name__ == "__main__":
    main()
