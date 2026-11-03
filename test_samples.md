
# Phishing URL Awareness Checker - Test Results

## Test 1: Normal HTTPS URL
**Input:** https://www.example.com/login

**Expected result:** No warning signs detected.

**Actual result:** Passed.

## Test 2: IP Address URL
**Input:** http://192.0.2.10/account

**Expected warnings:**
- IP address hostname.
- HTTP scheme.

**Actual result:** Passed.

## Test 3: URL with @ Symbol
**Input:** http://example.com@sample.invalid/login

**Expected warnings:**
- @ symbol.
- HTTP scheme.

**Actual result:** Passed.

## Test 4: Long Hostname
**Input:** https://a.b.c.d.e.example.invalid/path

**Expected warning:**
- Hostname contains five or more segments.

**Actual result:** Passed.

## Test 5: Punycode URL
**Input:** https://xn--example.invalid/

**Expected warning:**
- Punycode marker (xn--).

**Actual result:** Passed.

## Additional Test: Malformed URL
**Input:** http://[bad

**Expected warning:**
- Malformed URL.

**Actual result:** Passed.
