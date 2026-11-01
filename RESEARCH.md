# Research

Ali Firas - `thesmartshadow`

## Selected technical notes

### [OpenSSL - CVE-2026-35191](https://openssl-library.org/news/secadv/20260929.txt)

The QUIC server's unvalidated-send budget could be increased once per packet using the *whole datagram length*. When a datagram contained several coalesced packets, accounting recorded more bytes received than actually arrived. Under the affected configuration with address validation disabled, that error defeated the 3x limit in RFC 9000. The correction is in the QUIC receive/accounting path rather than the TLS cryptography. [OpenSSL vulnerability record](https://openssl-library.org/news/vulnerabilities/).

### [zlib - CVE-2026-85091](https://www.cve.org/CVERecord?id=CVE-2026-85091)

After a nonblocking `gzwrite()` stall, `gz_vacate()` could retain external-buffer state that was no longer valid for subsequent formatted writes. `gzprintf()` or `gzvprintf()` could then reach an unchecked `memmove` beyond the internal input buffer. The investigation followed the failure state through the write path, with a reproducer and version analysis rather than relying on a single crash trace. [Research report](https://gist.github.com/thesmartshadow/e0b9481792afb7c31e86fee1ff084490) · [Ubuntu USN-8954-1](https://ubuntu.com/security/notices/USN-8954-1).

### [vm2 - CVE-2026-92956](https://github.com/advisories/GHSA-wjwh-qqvp-g4p4)

A Node.js 26 WebAssembly streaming path exposed a host-realm Promise/error object to code running inside a default VM sandbox. The `finally`/`Symbol.species` behavior permitted a transition back into host capabilities without directly obtaining a normal global constructor. Cross-version tests and negative controls isolate the realm boundary involved in the escape.

### [Chrome DevTools MCP - CVE-2026-106484](https://github.com/ChromeDevTools/chrome-devtools-mcp/security/advisories/GHSA-5hw5-4q87-m6x9)

A destination path was checked against MCP roots before the tool changed its extension. The write operation used the transformed path, and a symlink at that final location could redirect output beyond the allowed roots. The fix belongs at the final canonical pathname, after all path transformations. [Chrome CNA record](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/106xxx/CVE-2026-106484.json).

### [Cloudflare Pingora - CVE-2026-105299](https://github.com/cloudflare/pingora/security/advisories/GHSA-vx4q-2c55-cvmg)

In affected HTTP/1 chained-proxy deployments, the downstream client's `Connection` nominations reached the upstream side without the hop-by-hop stripping required at a forwarding boundary. A later intermediary could remove a trusted header inserted by the proxy, with an access-control consequence when an origin relied on that header. This is an intermediary protocol-state failure, not a generic authorization bug in the origin. [RustSec](https://rustsec.org/advisories/RUSTSEC-2026-0390.html).

### [Gitea - CVE-2026-89430](https://github.com/go-gitea/gitea/security/advisories/GHSA-hcgw-r9gf-8mph)

Push-mirror egress policy applied when the mirror was created. Synchronization subsequently used the stored hostname directly; DNS resolution could change between the policy check and the `git push`. An allowed name could therefore point at an internal Git service at use time. Where that destination accepted writes, forced reference updates became possible. The same address must be checked at the operation that uses it. [Release](https://blog.gitea.com/release-of-28.0.0/).

### [rust-openssl - CVE-2026-45784](https://github.com/rust-openssl/rust-openssl/security/advisories/GHSA-phqj-4mhp-q6mq)

`CipherCtxRef::cipher_update_inplace` did not reserve enough output capacity for AES key-wrap-with-padding operations on non-aligned input. The called library could write beyond the end of the caller's `Vec` or buffer. This was an incomplete memory-safety correction in the Rust binding layer, fixed in the `openssl` crate 0.10.80.

## Other published findings

## Protocol processing and resource accounting

- [Hickory DNS - CVE-2026-93657](https://github.com/advisories/GHSA-5j98-2g5x-46v6) - bogus DNSSEC validation state lost across resolver lookup interfaces.
- [CoreDNS - CVE-2026-32936](https://github.com/coredns/coredns/security/advisories/GHSA-63cw-r7xf-jmwr) - expensive DoH GET processing occurred before request-limit enforcement.
- [cpp-httplib - CVE-2026-28435](https://github.com/yhirose/cpp-httplib/security/advisories/GHSA-xvfx-w463-6fpp) - streaming gzip decompression bypassed configured payload-length limits.
- [fasthttp - GO-2026-4950](https://pkg.go.dev/vuln/GO-2026-4950) - double-decoded paths bypassed application authorization in file serving.
- [Net-SNMP - CVE-2026-89147](https://www.cve.org/CVERecord?id=CVE-2026-89147) - unauthenticated SMUX read path could block service progress.
- [rust-libp2p rendezvous - CVE-2026-89146](https://github.com/advisories/GHSA-gh9c-4324-26cm) - TTL handling reached an overflowing timer path.
- [basic-ftp - CVE-2026-44240](https://github.com/advisories/GHSA-rpmf-866q-6p89) - unbounded multiline FTP responses exhausted client memory.
- [PyJWT - CVE-2026-48525](https://github.com/jpadilla/pyjwt/security/advisories/GHSA-w7vc-732c-9m39) - detached JWS processing amplified resource use before authentication.

## Memory safety and execution boundaries

- [libheif - CVE-2026-62291](https://github.com/strukturag/libheif/security/advisories/GHSA-xpw3-9rhw-482x) - auxiliary-plane dimensions exceeded the allocation used in uncompressed encoding.
- [Zen C - CVE-2026-33491](https://github.com/zenc-lang/zenc/security/advisories/GHSA-rv74-w6q7-h8xr) - fixed-size identifier mangling buffer overflow.
- [cilium/ebpf - CVE-2026-10722](https://www.cve.org/CVERecord?id=CVE-2026-10722) - malformed BTF data crossed parser bounds and caused a panic.
- [Tempus Ex hello-video-codec - CVE-2025-63095](https://www.cve.org/CVERecord?id=CVE-2025-63095) - malformed bitstream input exhausted or crashed the encoder path.
- [docopt.cpp - CVE-2025-67125](https://www.cve.org/CVERecord?id=CVE-2025-67125) - signed counter overflow in option handling.
- [Hono - CVE-2026-59896](https://github.com/honojs/hono/security/advisories/GHSA-hvrm-45r6-mjfj) - cross-request state could leak through shared JSX context.

## Authorization and filesystem boundaries

- [CISA manage.get.gov - GHSA-hfq4-89cf-8p8j](https://github.com/cisagov/manage.get.gov/security/advisories/GHSA-hfq4-89cf-8p8j) - read-only organization access reached privileged membership operations.
- [RustFS - CVE-2026-39360](https://github.com/advisories/GHSA-mx42-j6wv-px98) - missing source-object authorization in multipart copy.
- [Microsoft APM - CVE-2026-45539](https://github.com/microsoft/apm/security/advisories/GHSA-q5pp-gvjg-h7v4) - symlink-controlled paths disclosed local files during package installation.
- [Microsoft AVML - CVE-2026-61371](https://www.cve.org/CVERecord?id=CVE-2026-61371) - output-file symlink resolution and truncation occurred before safe destination handling.
- [Microsoft UFO - CVE-2026-54568](https://github.com/microsoft/UFO/security/advisories/GHSA-hc27-j4p9-qm2x) - device-information access crossed an authorization boundary.
- [Russh - CVE-2026-68930](https://github.com/advisories/GHSA-m65r-rprj-r5rg) - SSH channel state did not preserve authorization constraints.
- [uutils coreutils - CVE-2026-93658](https://github.com/uutils/coreutils/security/advisories/GHSA-cgg3-923w-v53m) - `install` applied privileged mode bits before ownership had been finalized.
- [su-exec - CVE-2026-82457](https://www.cve.org/CVERecord?id=CVE-2026-82457) - numeric UID truncation affected privilege selection.
- [tar-rs - CVE-2026-70622](https://www.cve.org/CVERecord?id=CVE-2026-70622) - symlinked archive paths crossed extraction boundaries.
- [LiME - CVE-2026-85092](https://www.cve.org/CVERecord?id=CVE-2026-85092) - symlink following at the acquisition output path.
- [miniserve - CVE-2025-67124](https://www.cve.org/CVERecord?id=CVE-2025-67124) - upload finalization raced with symlink replacement.
- [ownCloud Guests - CVE-2025-59716](https://www.cve.org/CVERecord?id=CVE-2025-59716) - pending guest information exposed through unauthenticated enumeration.
- [Nezha - CVE-2026-100394](https://github.com/advisories/GHSA-qjpp-gffx-2wm9) - synchronization race crashed the monitoring service.

## Parsing and data integrity

- [xmldom - CVE-2026-34601](https://github.com/xmldom/xmldom/security/advisories/GHSA-wh4c-j3r5-mjhp) - CDATA terminators escaped the intended serialization boundary.
- [Rack - CVE-2026-25500](https://github.com/rack/rack/security/advisories/GHSA-whrj-4476-wvmp) - unsafe filename handling in `Rack::Directory`.
- [Axios - CVE-2026-67320](https://github.com/advisories/GHSA-gcfj-64vw-6mp9) - proxy settings inherited through the prototype chain after configuration cloning.
- [systeminformation - CVE-2026-44724](https://github.com/sebhildebrandt/systeminformation/security/advisories/GHSA-hvx9-hwr7-wjj9) - NetworkManager profile names reached shell execution.
- [pyLoad - CVE-2026-32808](https://github.com/pyload/pyload/security/advisories/GHSA-7g4m-8hx2-4qh3) - path traversal allowed unintended file deletion through archive handling.
- [jq - CVE-2026-43895](https://github.com/jqlang/jq/security/advisories/GHSA-7q7g-mrq3-phxr) - embedded-NUL path interpretation broke an import boundary.
- [DigitalOcean do-markdownit - CVE-2025-59717](https://www.cve.org/CVERecord?id=CVE-2025-59717) - allow-list type confusion in Markdown handling.
- [Google zx - CVE-2025-13437](https://github.com/google/zx/pull/1349) - cleanup logic could remove an external `node_modules` target.

## Distribution security updates

**OpenSSL** - [Ubuntu USN-8847-1](https://ubuntu.com/security/notices/USN-8847-1) · [Debian DSA-6531-1](https://lists.debian.org/debian-security-announce/2026/msg00444.html) · [SUSE](https://www.suse.com/support/update/announcement/2026/suse-su-202624245-1/)

**zlib** - [Ubuntu USN-8954-1](https://ubuntu.com/security/notices/USN-8954-1) · [Debian](https://security-tracker.debian.org/tracker/CVE-2026-85091)

**libheif** - [Ubuntu USN-8683-1](https://ubuntu.com/security/notices/USN-8683-1) · [Ubuntu USN-8774-1](https://ubuntu.com/security/notices/USN-8774-1)

**Rack** - [Ubuntu USN-8066-1](https://ubuntu.com/security/notices/USN-8066-1) · [Debian DSA-6180-1](https://lists.debian.org/debian-security-announce/2026/msg00089.html)

**xmldom** - [IBM Cloud Pak for Integration](https://www.ibm.com/support/pages/security-bulletin-automation-assets-ibm-cloud-pak-integration-vulnerable-vulnerability-xmldom) · [IBM Maximo Application Suite](https://www.ibm.com/support/pages/security-bulletin-ibm-maximo-application-suite-visual-inspection-component-uses-xmldom-which-vulnerable-cve-2026-34601) · [Red Hat](https://access.redhat.com/security/cve/cve-2026-34601)

**rust-openssl** - [Red Hat](https://access.redhat.com/security/cve/cve-2026-45784) · [SUSE](https://www.suse.com/security/cve/CVE-2026-45784.html)

[Main profile](README.md) · [Upstream patches](UPSTREAM.md)