#!/usr/bin/env python3
"""Check exact .com availability against the Verisign RDAP registry.

Usage:
  python3 rdap.py a.com b.com ...
  python3 rdap.py --file domains.txt [more.com ...]

The file holds one domain per line; blank lines and lines starting with # are skipped.

Output, one line per domain:
  name.com               AVAILABLE
  name.com               TAKEN  reg YYYY-MM-DD  exp YYYY-MM-DD  Registrar  status
  name.com               ? http CODE            (000 = no response; retry once)
"""
import sys, json, subprocess


def check(d):
    r = subprocess.run(["curl", "-sS", "-m", "30", "-w", "\n%{http_code}",
                        f"https://rdap.verisign.com/com/v1/domain/{d}"],
                       capture_output=True, text=True)
    body, code = r.stdout.rsplit("\n", 1) if "\n" in r.stdout else ("", r.stdout or "000")
    if code.strip() == "404": return f"{d:<22} AVAILABLE"
    if code.strip() != "200": return f"{d:<22} ? http {code.strip()}"
    j = json.loads(body); reg = ""
    for e in j.get("entities", []):
        if "registrar" in e.get("roles", []):
            for v in e.get("vcardArray", [[], []])[1]:
                if v[0] == "fn": reg = v[3]
    ev = {x["eventAction"]: x["eventDate"][:10] for x in j.get("events", [])}
    st = ",".join(s for s in j.get("status", []) if "prohibited" not in s)
    return f"{d:<22} TAKEN  reg {ev.get('registration','?')}  exp {ev.get('expiration','?')}  {reg[:28]:<28} {st}"


def domains(argv):
    out, args = [], iter(argv)
    for a in args:
        if a == "--file":
            path = next(args, None)
            if path is None: sys.exit("--file needs a path")
            with open(path) as f:
                out += [l.strip() for l in f if l.strip() and not l.lstrip().startswith("#")]
        elif a.startswith("--file="):
            with open(a.split("=", 1)[1]) as f:
                out += [l.strip() for l in f if l.strip() and not l.lstrip().startswith("#")]
        else:
            out.append(a)
    return [d.lower() for d in dict.fromkeys(out)]


if __name__ == "__main__":
    ds = domains(sys.argv[1:])
    if not ds: sys.exit(__doc__)
    for d in ds: print(check(d), flush=True)
