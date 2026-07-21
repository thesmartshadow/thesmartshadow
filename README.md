<div align="center">

# Ali Firas

### Open Source Security Researcher

I audit open source software, reproduce security flaws, work with maintainers on remediation, and follow issues through fixes, regression coverage, advisories, and downstream releases.

[GitHub Advisories](https://github.com/advisories?query=credit%3Athesmartshadow) · [HackerOne](https://hackerone.com/thesmartshadow) · [LinkedIn](https://www.linkedin.com/in/ali-shmery/) · [MSRC Special Recognition](https://msrc.microsoft.com/special-mention)

</div>

## What I work on

My work is centered on source code auditing and open source vulnerability research. I am most interested in flaws that cross trust boundaries quietly: authorization mistakes, unsafe file handling, parser failures, shared state, archive extraction, command construction, and resource limits that are enforced too late.

A useful report should leave a project with more than a finding. I try to provide a small reproducible case, affected version analysis, a clear root cause, and a practical fix. When it makes sense, I also write the patch and regression tests myself.

## Selected ecosystem impact

### CISA manage.get.gov

Reported a high impact authorization flaw that allowed a view only organization member to perform privileged member management actions. The report was validated with a real application flow and led to an upstream fix and a GitHub Security Advisory rated 8.1 High.

[GHSA-hfq4-89cf-8p8j](https://github.com/cisagov/manage.get.gov/security/advisories/GHSA-hfq4-89cf-8p8j) · [Fix PR #5049](https://github.com/cisagov/manage.get.gov/pull/5049)

### PyJWT

Reported an unauthenticated resource consumption issue in detached JWS verification. PyJWT decoded an attacker controlled payload segment before signature rejection even though the segment was unused when `b64=false`. The fix shipped in the PyJWT 2.13.0 security release, which credits `@thesmartshadow` as the reporter.

[CVE-2026-48525](https://nvd.nist.gov/vuln/detail/CVE-2026-48525) · [GHSA-w7vc-732c-9m39](https://github.com/jpadilla/pyjwt/security/advisories/GHSA-w7vc-732c-9m39) · [PyJWT changelog](https://github.com/jpadilla/pyjwt/blob/master/CHANGELOG.rst)

### RubyGems

Authored and shipped a symlink aware extraction boundary fix for RubyGems. The patch prevents a pre-existing symlink inside the destination tree from redirecting extracted files outside the intended directory and includes regression coverage. It was released in RubyGems 4.0.13 with credit to `thesmartshadow`.

[PR #9493](https://github.com/ruby/rubygems/pull/9493) · [RubyGems 4.0.13 release](https://blog.rubygems.org/2026/06/03/4.0.13-released.html)

### Rack

Discovered a stored XSS condition in `Rack::Directory` caused by unsafe handling of attacker controlled file names. The fix was released across supported Rack branches and later reached Ubuntu, Debian, and SUSE security updates. Ubuntu credited me by name in its security notice.

[CVE-2026-25500](https://nvd.nist.gov/vuln/detail/CVE-2026-25500) · [GHSA-whrj-4476-wvmp](https://github.com/rack/rack/security/advisories/GHSA-whrj-4476-wvmp) · [Ubuntu USN-8066-1](https://ubuntu.com/security/notices/USN-8066-1) · [Debian DSA-6180-1](https://lists.debian.org/debian-security-announce/2026/msg00089.html) · [SUSE](https://www.suse.com/security/cve/CVE-2026-25500.html)

### Google zx

Discovered and fixed a cleanup bug in `--prefer-local` that could delete an external `node_modules` directory. I provided the reproduction, root cause, patch, and regression tests. The change was merged upstream and later published as CVE-2025-13437.

[CVE-2025-13437](https://nvd.nist.gov/vuln/detail/CVE-2025-13437) · [PR #1349](https://github.com/google/zx/pull/1349)

### Hono

Reported a cross request context isolation flaw in Hono JSX caused by shared mutable state. The issue could leak request scoped values between concurrent requests. The advisory credits `thesmartshadow` as the reporter and the fix shipped in Hono 4.12.27.

[CVE-2026-59896](https://nvd.nist.gov/vuln/detail/CVE-2026-59896) · [GHSA-hvrm-45r6-mjfj](https://github.com/honojs/hono/security/advisories/GHSA-hvrm-45r6-mjfj)

### xmldom

Reported XML injection through unsafe CDATA serialization. The project fixed the direct creation path and the mutation based serialization path, backported the remediation to two maintained release lines, and thanked `@thesmartshadow` in the official changelog for versions 0.8.12 and 0.9.9.

[CVE-2026-34601](https://nvd.nist.gov/vuln/detail/CVE-2026-34601) · [GHSA-wh4c-j3r5-mjhp](https://github.com/xmldom/xmldom/security/advisories/GHSA-wh4c-j3r5-mjhp) · [Project changelog](https://github.com/xmldom/xmldom/blob/master/CHANGELOG.md)

### CEL-Go

Authored an upstream resource consumption fix that moved `ParserExpressionSizeLimit` enforcement ahead of source buffer allocation. The patch includes regression and allocation tests and was merged into the CEL-Go codebase as a CWE-400 fix.

[PR #1302](https://github.com/cel-expr/cel-go/pull/1302) · [Merged commit](https://github.com/cel-expr/cel-go/commit/2814acd9e1edc48811cbd88c6f60432638334e5a)

### pyLoad

Co-discovered an arbitrary file deletion issue in encrypted 7z password verification. An archive controlled entry name was treated as a filesystem path without being confined to the extraction directory. The vulnerability was fixed in `0.5.0b3.dev97` and published as a High severity advisory.

Co-discovered with [Ali Al-Akbar](https://github.com/ExeC-IQ).

[CVE-2026-32808](https://nvd.nist.gov/vuln/detail/CVE-2026-32808) · [GHSA-7g4m-8hx2-4qh3](https://github.com/pyload/pyload/security/advisories/GHSA-7g4m-8hx2-4qh3)

### Microsoft AVML

Discovered that AVML followed symlinks when opening an output destination with create and truncate semantics. This allowed the symlink target to be truncated or overwritten before later validation completed. Microsoft fixed the issue in AVML 0.17.0 and the case was published as CVE-2026-61371.

[CVE-2026-61371](https://www.cve.org/CVERecord?id=CVE-2026-61371) · [Microsoft fix PR #754](https://github.com/microsoft/avml/pull/754)

## Merged upstream security work

These are patches I authored that were accepted into projects outside my own account:

- [RubyGems #9493](https://github.com/ruby/rubygems/pull/9493), confine extraction when destination paths contain symlinks
- [CEL-Go #1302](https://github.com/cel-expr/cel-go/pull/1302), enforce expression limits before source allocation
- [Google zx #1349](https://github.com/google/zx/pull/1349), prevent deletion of an external `node_modules` directory
- [Ruby JSON #948](https://github.com/ruby/json/pull/948), reject negative generator depth before native hangs or crashes
- [Google HumanIO #4](https://github.com/google/humanio/pull/4), harden serving and secret handling boundaries
- [httparse #217](https://github.com/seanmonstar/httparse/pull/217), document limits for repeated parsing of growing partial buffers

## Published advisories

My public record currently includes 13 or more published CVEs plus additional GitHub Security Advisories. The number is less important to me than whether the report produced a useful outcome for maintainers and downstream users.

- [CVE-2026-61371](https://www.cve.org/CVERecord?id=CVE-2026-61371), Microsoft AVML
- [CVE-2026-59896](https://nvd.nist.gov/vuln/detail/CVE-2026-59896), Hono
- [CVE-2026-48525](https://nvd.nist.gov/vuln/detail/CVE-2026-48525), PyJWT
- [CVE-2026-34601](https://nvd.nist.gov/vuln/detail/CVE-2026-34601), xmldom
- [CVE-2026-32808](https://nvd.nist.gov/vuln/detail/CVE-2026-32808), pyLoad
- [CVE-2026-25500](https://nvd.nist.gov/vuln/detail/CVE-2026-25500), Rack
- [CVE-2026-10722](https://nvd.nist.gov/vuln/detail/CVE-2026-10722), cilium/ebpf
- [CVE-2025-67125](https://nvd.nist.gov/vuln/detail/CVE-2025-67125), docopt.cpp
- [CVE-2025-67124](https://nvd.nist.gov/vuln/detail/CVE-2025-67124)
- [CVE-2025-63095](https://nvd.nist.gov/vuln/detail/CVE-2025-63095)
- [CVE-2025-59717](https://nvd.nist.gov/vuln/detail/CVE-2025-59717), DigitalOcean do-markdownit
- [CVE-2025-59716](https://nvd.nist.gov/vuln/detail/CVE-2025-59716), ownCloud Guests
- [CVE-2025-13437](https://nvd.nist.gov/vuln/detail/CVE-2025-13437), Google zx

Additional advisory:

- [GHSA-hfq4-89cf-8p8j](https://github.com/cisagov/manage.get.gov/security/advisories/GHSA-hfq4-89cf-8p8j), CISA manage.get.gov authorization bypass

## How I approach a project

I start with the trust boundary, not a scanner result. I trace how external data reaches file operations, parsers, authorization checks, process execution, shared state, or resource allocation. When something looks wrong, I reduce it to the smallest realistic reproduction I can build and test it against clean versions.

I also try to keep severity separate from technical validity. Some findings are vulnerabilities, some are hardening opportunities, and some should remain ordinary bugs. The goal is to give maintainers evidence they can act on without forcing a security label where it does not belong.

## Current interests

- Package managers and archive extraction
- Parsers and malformed input handling
- Authorization and multi tenant isolation
- Developer tools and CI workflows
- Linux and systems software
- Supply chain security
- Patch analysis and incomplete fixes

## Contact

For coordinated disclosure or open source security collaboration:

- GitHub: [@thesmartshadow](https://github.com/thesmartshadow)
- HackerOne: [thesmartshadow](https://hackerone.com/thesmartshadow)
- LinkedIn: [Ali Firas](https://www.linkedin.com/in/ali-shmery/)
