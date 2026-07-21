<div align="center">

# Ali Firas

### Open-Source Security Researcher

I audit open-source software, reproduce security flaws, work with maintainers on remediation, and follow issues through fixes, regression coverage, advisories, releases, and downstream distribution updates.

[GitHub Advisories](https://github.com/advisories?query=credit%3Athesmartshadow) · [HackerOne](https://hackerone.com/thesmartshadow) · [LinkedIn](https://www.linkedin.com/in/ali-shmery/) · [MSRC Special Recognition](https://msrc.microsoft.com/special-mention)

</div>

## What I work on

My work is centered on source-code auditing and open-source vulnerability research. I am most interested in flaws that cross trust boundaries quietly: authorization mistakes, unsafe file handling, parser failures, shared state, archive extraction, command construction, memory safety, and resource limits that are enforced too late.

A useful report should leave a project with more than a finding. I try to provide a small reproducible case, affected-version analysis, a clear root cause, and a practical fix. When it makes sense, I also write the patch and regression tests myself.

## Selected ecosystem impact

### CISA manage.get.gov

Reported a high-impact authorization flaw that allowed a view-only organization member to perform privileged member-management actions. The report was validated through a real application flow and led to an upstream fix and an official GitHub Security Advisory rated 8.1 High.

[GHSA-hfq4-89cf-8p8j](https://github.com/cisagov/manage.get.gov/security/advisories/GHSA-hfq4-89cf-8p8j) · [Fix PR #5049](https://github.com/cisagov/manage.get.gov/pull/5049)

### CoreDNS

Reported a remote, unauthenticated denial-of-service issue in the DNS-over-HTTPS GET path. Oversized `dns` query values caused expensive parsing, Base64 decoding, and DNS message processing before validation rejected the request. The fix shipped in CoreDNS 1.14.3, and the advisory credits `thesmartshadow` as the reporter.

[CVE-2026-32936](https://www.cve.org/CVERecord?id=CVE-2026-32936) · [GHSA-63cw-r7xf-jmwr](https://github.com/coredns/coredns/security/advisories/GHSA-63cw-r7xf-jmwr) · [GO-2026-5164](https://pkg.go.dev/vuln/GO-2026-5164)

### jq

Reported a path-resolution inconsistency caused by embedded NUL bytes in jq import paths. A policy layer could approve the full logical import name while jq resolved and opened a different local module or data file, breaking trust assumptions around policy loading and redaction. The issue was fixed in jq 1.8.2 and later tracked by major Linux and cloud vendors.

[CVE-2026-43895](https://www.cve.org/CVERecord?id=CVE-2026-43895) · [GHSA-7q7g-mrq3-phxr](https://github.com/jqlang/jq/security/advisories/GHSA-7q7g-mrq3-phxr)

### Microsoft APM

Reported a symlink-handling flaw in the installation of remote APM packages. Package-controlled links inside `.apm/prompts/` or `.apm/agents/` could be followed during installation, copying local file contents into generated assistant directories such as `.claude`, `.codex`, `.cursor`, and `.github`. Microsoft fixed the issue in APM 0.13.0.

[CVE-2026-45539](https://www.cve.org/CVERecord?id=CVE-2026-45539) · [GHSA-q5pp-gvjg-h7v4](https://github.com/microsoft/apm/security/advisories/GHSA-q5pp-gvjg-h7v4)

### libheif

Reported a heap out-of-bounds write in the uncompressed encoder when auxiliary alpha-plane dimensions did not match the primary image. The encoder sized its output using the primary image while copying component data using the component plane's actual size. The project fixed the issue in libheif 1.23.1.

[CVE-2026-62291](https://www.cve.org/CVERecord?id=CVE-2026-62291) · [GHSA-xpw3-9rhw-482x](https://github.com/strukturag/libheif/security/advisories/GHSA-xpw3-9rhw-482x)

### RubyGems

Authored and shipped a symlink-aware extraction boundary fix for RubyGems. The patch prevents a pre-existing symlink inside the destination tree from redirecting extracted files outside the intended directory and includes regression coverage. It was released in RubyGems 4.0.13 with credit to `thesmartshadow`.

[PR #9493](https://github.com/ruby/rubygems/pull/9493) · [RubyGems 4.0.13 release](https://blog.rubygems.org/2026/06/03/4.0.13-released.html)

### rust-openssl

Reported an out-of-bounds write in `CipherCtxRef::cipher_update_inplace` for AES key-wrap-with-padding ciphers. Non-aligned input could cause OpenSSL to write beyond the caller-provided buffer, and the affected method had been missed by an earlier security fix. The issue was fixed in the `openssl` crate 0.10.80.

[CVE-2026-45784](https://www.cve.org/CVERecord?id=CVE-2026-45784) · [GHSA-phqj-4mhp-q6mq](https://github.com/rust-openssl/rust-openssl/security/advisories/GHSA-phqj-4mhp-q6mq)

### systeminformation

Reported command injection in the Linux `networkInterfaces()` path through attacker-controlled NetworkManager connection-profile names. The issue was reproduced with the real `nmcli` flow, where simply calling the API could reach vulnerable shell commands. The project fixed the issue in systeminformation 5.31.6.

[CVE-2026-44724](https://www.cve.org/CVERecord?id=CVE-2026-44724) · [GHSA-hvx9-hwr7-wjj9](https://github.com/sebhildebrandt/systeminformation/security/advisories/GHSA-hvx9-hwr7-wjj9) · [Project security page](https://systeminformation.io/security.html)

### Rack

Discovered a stored XSS condition in `Rack::Directory` through unsafe handling of attacker-controlled file names. The fix was released across supported Rack branches and later reached Ubuntu, Debian, and SUSE security updates. Ubuntu credited me by name in its security notice.

[CVE-2026-25500](https://www.cve.org/CVERecord?id=CVE-2026-25500) · [GHSA-whrj-4476-wvmp](https://github.com/rack/rack/security/advisories/GHSA-whrj-4476-wvmp) · [Ubuntu USN-8066-1](https://ubuntu.com/security/notices/USN-8066-1) · [Debian DSA-6180-1](https://lists.debian.org/debian-security-announce/2026/msg00089.html) · [SUSE](https://www.suse.com/security/cve/CVE-2026-25500.html)

### RustFS

Reported a missing source-authorization check in the multipart copy path. A low-privileged tenant without read access to a private source object could copy it into a multipart upload under their own control and retrieve the completed object. The end-to-end reproduction confirmed cross-bucket data exposure with matching file size and SHA-256.

[CVE-2026-39360](https://www.cve.org/CVERecord?id=CVE-2026-39360) · [GHSA-mx42-j6wv-px98](https://github.com/advisories/GHSA-mx42-j6wv-px98)

## Upstream patches I authored

These are changes I wrote that were accepted into projects outside my own account:

- [RubyGems #9493](https://github.com/ruby/rubygems/pull/9493), confine extraction when destination paths contain pre-existing symlinks; released in RubyGems 4.0.13
- [CEL-Go #1302](https://github.com/cel-expr/cel-go/pull/1302), enforce expression-size limits before source-buffer allocation, with regression and allocation tests
- [Google zx #1349](https://github.com/google/zx/pull/1349), prevent cleanup from deleting an external `node_modules` directory; later published as CVE-2025-13437
- [Ruby JSON #948](https://github.com/ruby/json/pull/948), reject negative generator depth before native hangs or crashes
- [Google HumanIO #4](https://github.com/google/humanio/pull/4), stop source-file exposure and move a hard-coded service token to environment configuration
- [httparse #217](https://github.com/seanmonstar/httparse/pull/217), document strict limits for repeated parsing of growing partial buffers

## Additional published security research

- **PyJWT**, unauthenticated resource-consumption amplification in detached JWS processing; fixed in 2.13.0 with reporter credit in the security release. [CVE-2026-48525](https://www.cve.org/CVERecord?id=CVE-2026-48525) · [GHSA-w7vc-732c-9m39](https://github.com/jpadilla/pyjwt/security/advisories/GHSA-w7vc-732c-9m39)
- **Hono**, cross-request context leakage caused by shared mutable JSX state; fixed in 4.12.27. [CVE-2026-59896](https://www.cve.org/CVERecord?id=CVE-2026-59896) · [GHSA-hvrm-45r6-mjfj](https://github.com/honojs/hono/security/advisories/GHSA-hvrm-45r6-mjfj)
- **xmldom**, XML injection through unsafe CDATA serialization; fixed across two maintained release lines with changelog credit. [CVE-2026-34601](https://www.cve.org/CVERecord?id=CVE-2026-34601) · [GHSA-wh4c-j3r5-mjhp](https://github.com/xmldom/xmldom/security/advisories/GHSA-wh4c-j3r5-mjhp)
- **Zen C**, stack-based buffer overflow in compiler identifier mangling; fixed in 0.4.4, with `thesmartshadow` credited as reporter. [CVE-2026-33491](https://www.cve.org/CVERecord?id=CVE-2026-33491) · [GHSA-rv74-w6q7-h8xr](https://github.com/zenc-lang/zenc/security/advisories/GHSA-rv74-w6q7-h8xr)
- **basic-ftp**, unbounded multiline-response accumulation from a malicious or compromised FTP server; fixed in 5.3.1. [CVE-2026-44240](https://www.cve.org/CVERecord?id=CVE-2026-44240) · [GHSA-rpmf-866q-6p89](https://github.com/advisories/GHSA-rpmf-866q-6p89)
- **Microsoft UFO**, missing authorization allowed an authenticated device client to request another device's stored system information. [CVE-2026-54568](https://www.cve.org/CVERecord?id=CVE-2026-54568) · [GHSA-hc27-j4p9-qm2x](https://github.com/microsoft/UFO/security/advisories/GHSA-hc27-j4p9-qm2x)
- **pyLoad**, arbitrary file deletion during encrypted 7z password verification; co-discovered with [Ali Al-Akbar](https://github.com/ExeC-IQ). [CVE-2026-32808](https://www.cve.org/CVERecord?id=CVE-2026-32808) · [GHSA-7g4m-8hx2-4qh3](https://github.com/pyload/pyload/security/advisories/GHSA-7g4m-8hx2-4qh3)
- **Microsoft AVML**, symlink-following output creation with truncation before validation; fixed in 0.17.0. [CVE-2026-61371](https://www.cve.org/CVERecord?id=CVE-2026-61371) · [Research reference](https://gist.github.com/thesmartshadow/2d099071f847de8db3dc4bbaf4dfa6df) · [Microsoft fix PR #754](https://github.com/microsoft/avml/pull/754)
- **cilium/ebpf**, malformed BTF input could trigger parser panics; the report led to an upstream boundary-check fix. [CVE-2026-10722](https://www.cve.org/CVERecord?id=CVE-2026-10722) · [Issue #2019](https://github.com/cilium/ebpf/issues/2019) · [Fix PR #2021](https://github.com/cilium/ebpf/pull/2021)
- **miniserve**, upload finalization was affected by a TOCTOU and symlink race outside the intended root. [CVE-2025-67124](https://www.cve.org/CVERecord?id=CVE-2025-67124) · [GHSA-mxc8-4jqf-368q](https://github.com/advisories/GHSA-mxc8-4jqf-368q)
- **docopt.cpp**, signed counter overflow in repeated-option occurrence merging. [CVE-2025-67125](https://www.cve.org/CVERecord?id=CVE-2025-67125) · [Research reference](https://gist.github.com/thesmartshadow/672afe8828844c833f46f8ebe2f5f3bd)
- **ownCloud Guests**, unauthenticated pending-guest enumeration through response differences in registration links. [CVE-2025-59716](https://www.cve.org/CVERecord?id=CVE-2025-59716) · [Research reference](https://gist.github.com/thesmartshadow/64ae0449e909174d0479a4f23657147f)
- **DigitalOcean do-markdownit**, allow-list bypass through string-versus-array type confusion. [CVE-2025-59717](https://www.cve.org/CVERecord?id=CVE-2025-59717) · [GHSA-2h8j-8r9p-849f](https://github.com/advisories/GHSA-2h8j-8r9p-849f)
- **Tempus Ex hello-video-codec**, crafted input could trigger denial of service in `BitstreamWriter::write_bits()`. [CVE-2025-63095](https://www.cve.org/CVERecord?id=CVE-2025-63095) · [Research reference](https://gist.github.com/thesmartshadow/b092e2493821491b981a069847a33064)

<details>
<summary><strong>Published CVE record, 23 entries</strong></summary>

### 2026

- [CVE-2026-62291](https://www.cve.org/CVERecord?id=CVE-2026-62291), libheif
- [CVE-2026-61371](https://www.cve.org/CVERecord?id=CVE-2026-61371), Microsoft AVML
- [CVE-2026-59896](https://www.cve.org/CVERecord?id=CVE-2026-59896), Hono
- [CVE-2026-54568](https://www.cve.org/CVERecord?id=CVE-2026-54568), Microsoft UFO
- [CVE-2026-48525](https://www.cve.org/CVERecord?id=CVE-2026-48525), PyJWT
- [CVE-2026-45784](https://www.cve.org/CVERecord?id=CVE-2026-45784), rust-openssl
- [CVE-2026-45539](https://www.cve.org/CVERecord?id=CVE-2026-45539), Microsoft APM
- [CVE-2026-44724](https://www.cve.org/CVERecord?id=CVE-2026-44724), systeminformation
- [CVE-2026-44240](https://www.cve.org/CVERecord?id=CVE-2026-44240), basic-ftp
- [CVE-2026-43895](https://www.cve.org/CVERecord?id=CVE-2026-43895), jq
- [CVE-2026-39360](https://www.cve.org/CVERecord?id=CVE-2026-39360), RustFS
- [CVE-2026-34601](https://www.cve.org/CVERecord?id=CVE-2026-34601), xmldom
- [CVE-2026-33491](https://www.cve.org/CVERecord?id=CVE-2026-33491), Zen C
- [CVE-2026-32936](https://www.cve.org/CVERecord?id=CVE-2026-32936), CoreDNS
- [CVE-2026-32808](https://www.cve.org/CVERecord?id=CVE-2026-32808), pyLoad
- [CVE-2026-25500](https://www.cve.org/CVERecord?id=CVE-2026-25500), Rack
- [CVE-2026-10722](https://www.cve.org/CVERecord?id=CVE-2026-10722), cilium/ebpf

### 2025

- [CVE-2025-67125](https://www.cve.org/CVERecord?id=CVE-2025-67125), docopt.cpp
- [CVE-2025-67124](https://www.cve.org/CVERecord?id=CVE-2025-67124), miniserve
- [CVE-2025-63095](https://www.cve.org/CVERecord?id=CVE-2025-63095), Tempus Ex hello-video-codec
- [CVE-2025-59717](https://www.cve.org/CVERecord?id=CVE-2025-59717), DigitalOcean do-markdownit
- [CVE-2025-59716](https://www.cve.org/CVERecord?id=CVE-2025-59716), ownCloud Guests
- [CVE-2025-13437](https://www.cve.org/CVERecord?id=CVE-2025-13437), Google zx

</details>

<details>
<summary><strong>Downstream distribution and vendor tracking</strong></summary>

### Rack, CVE-2026-25500

- [Ubuntu USN-8066-1](https://ubuntu.com/security/notices/USN-8066-1)
- [Debian DSA-6180-1](https://lists.debian.org/debian-security-announce/2026/msg00089.html)
- [SUSE security tracker](https://www.suse.com/security/cve/CVE-2026-25500.html)
- [GitLab Advisory Database](https://advisories.gitlab.com/gem/rack/CVE-2026-25500/)
- [GitLab EE deployment discussion](https://forum.gitlab.com/t/is-it-possible-to-update-the-rack-ruby-library-of-my-gitlab-ee-installation/132909)

### jq, CVE-2026-43895

- [Red Hat](https://access.redhat.com/security/cve/cve-2026-43895)
- [Amazon Linux](https://explore.alas.aws.amazon.com/CVE-2026-43895.html)
- [Alibaba Cloud Linux](https://alas.aliyuncs.com/cves/detail/CVE-2026-43895)
- [ALT Linux](https://packages.altlinux.org/en/vuln/CVE-2026-43895)
- [Alpine Linux](https://security.alpinelinux.org/vuln/CVE-2026-43895)

### CoreDNS, CVE-2026-32936

- [Go Vulnerability Database](https://pkg.go.dev/vuln/GO-2026-5164)
- [Red Hat](https://access.redhat.com/security/cve/cve-2026-32936)
- [Microsoft Security Response Center](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-32936)
- [Tenable](https://www.tenable.com/plugins/pipeline/issues/222896-0)

### rust-openssl, CVE-2026-45784

- [LWN security update coverage](https://lwn.net/Articles/1083188/)
- [openSUSE advisory coverage](https://linuxsecurity.com/advisories/opensuse/opensuse-2026-0243-1-afterburn)
- [Additional SUSE package coverage](https://www.linuxcompatible.org/story/racut-systemd-pythonmaturin-go-125-and-kerneldevel-updates-for-suse/)
- [Amazon ECS Init openSUSE advisory coverage](https://linuxsecurity.com/advisories/opensuse/opensuse-2026-10871-1-amazon-ecs-init)

### systeminformation, CVE-2026-44724

- [Project security page](https://systeminformation.io/security.html)
- [Ubuntu Launchpad tracking](https://launchpad.net/bugs/cve/CVE-2026-44724)

</details>

## How I approach a project

I start with the trust boundary, not a scanner result. I trace how external data reaches file operations, parsers, authorization checks, process execution, shared state, cryptographic buffers, or resource allocation. When something looks wrong, I reduce it to the smallest realistic reproduction I can build and test it against clean versions.

I also try to keep severity separate from technical validity. Some findings are vulnerabilities, some are hardening opportunities, and some should remain ordinary bugs. The goal is to give maintainers evidence they can act on without forcing a security label where it does not belong.

## Current interests

- Package managers and archive extraction
- Authorization and multi-tenant isolation
- Parsers and malformed-input handling
- Memory safety and cryptographic bindings
- Developer tools, AI tooling, and CI workflows
- Linux and systems software
- Supply-chain security
- Patch analysis and incomplete fixes

## Contact

For coordinated disclosure or open-source security collaboration:

- GitHub: [@thesmartshadow](https://github.com/thesmartshadow)
- HackerOne: [thesmartshadow](https://hackerone.com/thesmartshadow)
- LinkedIn: [Ali Firas](https://www.linkedin.com/in/ali-shmery/)
