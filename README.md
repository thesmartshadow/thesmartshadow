# Ali Firas

**Linux Kernel Development & Networking | Zero-Day Vulnerability Research | Low-Level Systems & Security Engineering | Binary Exploitation**

`thesmartshadow`

C/C++ · Rust · Go · kernel networking · Netlink / VXLAN · eBPF / XDP · resource accounting · reverse engineering · memory safety · exploit validation · protocol security · sandboxing · filesystem and privilege boundaries · upstream patches · regression tests

I work on the implementation details behind security failures: state transitions, memory ownership, validation order, and boundaries that break when data changes representation or crosses into another subsystem. My work spans the Linux network stack, userspace protocol implementations, runtimes, package managers, and security-sensitive tooling.

[Kernel commits](https://github.com/torvalds/linux/commit/599d0e97610f09162d84c4ede4164628c066921e) · [Research](RESEARCH.md) · [Upstream work](UPSTREAM.md) · [Advisories](https://github.com/advisories?query=credit%3Athesmartshadow) · [thesmartshadow.dev](https://thesmartshadow.dev)

---

## Linux kernel

**[vxlan: vnifilter: validate the VXLAN_VNIFILTER_ENTRY nest](https://github.com/torvalds/linux/commit/599d0e97610f09162d84c4ede4164628c066921e)**  
`599d0e97610f` · `net-next` · merged into `torvalds/linux`

`vxlan_vnifilter_process()` processed entries while their nested attributes were still being validated individually. A malformed later entry could reject the request after an earlier entry had already been installed and an `RTM_NEWTUNNEL` notification sent. The change binds `VXLAN_VNIFILTER_ENTRY` to `vni_filter_entry_policy` using `NLA_POLICY_NESTED()`, validating the message's entry attributes before dispatch.

The [VXLAN VNIFILTER patch series](https://lore.kernel.org/netdev/20261014123814.388557-1-alishmery18@gmail.com/) extends into VNI range limits, netlink dump semantics, per-message bounds, allocation accounting, and forwarding selftests. The work involves `GFP_KERNEL_ACCOUNT`, `GFP_ATOMIC`, memcg behavior, rhashtable and FDB lifetime, and the practical constraints of memory allocation inside kernel locking paths.

[Mainline commit](https://github.com/torvalds/linux/commit/599d0e97610f09162d84c4ede4164628c066921e) · [Netdev series](https://lore.kernel.org/netdev/20261014123814.388557-1-alishmery18@gmail.com/) · [Upstream changes](UPSTREAM.md)

## Vulnerability research

**[OpenSSL - CVE-2026-35191](https://openssl-library.org/news/secadv/20260929.txt)**  
QUIC amplification accounting. With address validation disabled, a coalesced datagram could contribute its full length to the unvalidated-send budget more than once. This broke the RFC 9000 amplification bound in the affected server configuration. [OpenSSL security record](https://openssl-library.org/news/vulnerabilities/).

**[Cloudflare Pingora - CVE-2026-105299](https://github.com/cloudflare/pingora/security/advisories/GHSA-vx4q-2c55-cvmg)**  
An HTTP/1 proxy chain could carry client-controlled `Connection` header nominations across a trust boundary. A later intermediary could remove a header used by the origin for access control. The issue lies in hop-by-hop header processing and the assumptions made between proxies. [RustSec](https://rustsec.org/advisories/RUSTSEC-2026-0390.html).

**[zlib - CVE-2026-85091](https://www.cve.org/CVERecord?id=CVE-2026-85091)**  
Heap corruption in the gzip write path after a nonblocking output stall. Buffer state retained by `gz_vacate()` could make a later formatted write reach an out-of-bounds `memmove`. [Technical report](https://gist.github.com/thesmartshadow/e0b9481792afb7c31e86fee1ff084490) · [Ubuntu security update](https://ubuntu.com/security/notices/USN-8954-1).

**[vm2 - CVE-2026-92956](https://github.com/advisories/GHSA-wjwh-qqvp-g4p4)**  
Sandbox escape involving host-realm Promise behavior exposed through WebAssembly streaming on Node.js 26. The `Promise.prototype.finally` and `Symbol.species` path allowed sandbox code to recover capabilities outside the intended realm.

**[Chrome DevTools MCP - CVE-2026-106484](https://github.com/ChromeDevTools/chrome-devtools-mcp/security/advisories/GHSA-5hw5-4q87-m6x9)**  
MCP root restrictions were applied before an output path was rewritten. The final write could follow a symlink outside the approved roots because the transformed destination was not checked again. [Chrome CNA record](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/106xxx/CVE-2026-106484.json).

**[Gitea - CVE-2026-89430](https://github.com/go-gitea/gitea/security/advisories/GHSA-hcgw-r9gf-8mph)**  
Push-mirror destinations were checked against host policy at configuration time but not at synchronization. DNS changes between those points could redirect `git push` to internal Git services and enable forced reference updates where the destination allowed writes. [Release notes](https://blog.gitea.com/release-of-28.0.0/).

**[rust-openssl - CVE-2026-45784](https://github.com/rust-openssl/rust-openssl/security/advisories/GHSA-phqj-4mhp-q6mq)**  
An incomplete buffer-sizing fix in `CipherCtxRef::cipher_update_inplace` left an out-of-bounds write reachable with AES key-wrap-with-padding and non-aligned input. The flaw is in the Rust bindings, separate from the OpenSSL QUIC issue.

**[libheif - CVE-2026-62291](https://github.com/strukturag/libheif/security/advisories/GHSA-xpw3-9rhw-482x)**  
An encoder allocation derived from primary-image dimensions was used while copying an auxiliary image plane with different dimensions. The inconsistency produced a heap out-of-bounds write. [Ubuntu USN-8683-1](https://ubuntu.com/security/notices/USN-8683-1) · [USN-8774-1](https://ubuntu.com/security/notices/USN-8774-1).

**[Hickory DNS - CVE-2026-93657](https://github.com/advisories/GHSA-5j98-2g5x-46v6)**  
DNSSEC verification failures could be lost across resolver lookup interfaces, allowing a failed authentication result to be returned as ordinary resolved data.

**[CoreDNS - CVE-2026-32936](https://github.com/coredns/coredns/security/advisories/GHSA-63cw-r7xf-jmwr)**  
The DoH GET path spent CPU and memory decoding and parsing attacker-controlled inputs before enforcing request limits. The order of operations made unauthenticated work amplification possible.

**[cpp-httplib - CVE-2026-28435](https://github.com/yhirose/cpp-httplib/security/advisories/GHSA-xvfx-w463-6fpp)**  
Streaming request readers checked compressed input against `set_payload_max_length()` without applying that limit to decompressed output. Small gzip bodies could expand beyond the configured cap.

**[fasthttp - GO-2026-4950](https://pkg.go.dev/vuln/GO-2026-4950)**  
A second path-decoding step in file-serving helpers changed the path after application authorization checks. Double-encoded filenames could resolve to resources the application had already denied. [Upstream fix](https://github.com/valyala/fasthttp/pull/2163).

**[uutils coreutils - CVE-2026-93658](https://github.com/uutils/coreutils/security/advisories/GHSA-cgg3-923w-v53m)**  
The `install` path could leave privileged mode bits on a file when ownership changes failed. The security-sensitive order is ownership first, then mode; reversing it crosses a privilege boundary in filesystem metadata.

**[cilium/ebpf - CVE-2026-10722](https://www.cve.org/CVERecord?id=CVE-2026-10722)**  
Integer overflow in BTF collection parsing could trigger excessive allocation or failure while loading a crafted eBPF spec. The relevant boundary is the parser's allocation arithmetic before a trusted program representation exists.

**[RustFS - CVE-2026-39360](https://github.com/advisories/GHSA-mx42-j6wv-px98)**  
A multipart copy authorized the destination-side operation without consistently checking access to the source object. The gap exposed data across bucket or tenant boundaries.

**[CISA manage.get.gov - GHSA-hfq4-89cf-8p8j](https://github.com/cisagov/manage.get.gov/security/advisories/GHSA-hfq4-89cf-8p8j)**  
A view-only organization member could reach privileged member-management operations through an authorization gap in the application workflow. [Remediation](https://github.com/cisagov/manage.get.gov/pull/5049).

**[xmldom - CVE-2026-34601](https://github.com/xmldom/xmldom/security/advisories/GHSA-wh4c-j3r5-mjhp)**  
CDATA serialization failed to preserve the text boundary when supplied content contained a terminator. The output could change the structure of the resulting XML document, with downstream exposure in IBM products using the affected dependency.

[Full research index](RESEARCH.md)

## Upstream patches

- [RubyGems #9493](https://github.com/ruby/rubygems/pull/9493) - prevent archive extraction from following pre-existing symlinks outside `destination_dir`; regression coverage.
- [Google zx #1349](https://github.com/google/zx/pull/1349) - fix `--prefer-local` cleanup so an external `node_modules` target is not removed.
- [CEL-Go #1302](https://github.com/cel-expr/cel-go/pull/1302) - enforce expression-size limits before constructing the source buffer.
- [Akamai CLI #227](https://github.com/akamai/cli/pull/227) - validate command names before deriving filesystem output paths.
- [Ruby JSON #948](https://github.com/ruby/json/pull/948) - reject negative nesting depth in the native generator.
- [Google HumanIO #4](https://github.com/google/humanio/pull/4) - prevent server-source exposure and remove embedded service credentials.

[Patch details](UPSTREAM.md)

## Downstream security response

Selected distribution advisories, released package fixes, and vendor security assessments:

- **OpenSSL** - [OpenSSL advisory](https://openssl-library.org/news/secadv/20260929.txt), [Ubuntu](https://ubuntu.com/security/notices/USN-8847-1), [Debian](https://lists.debian.org/debian-security-announce/2026/msg00444.html), [SUSE](https://www.suse.com/support/update/announcement/2026/suse-su-202624245-1/).
- **zlib** - [Ubuntu USN-8954-1](https://ubuntu.com/security/notices/USN-8954-1), [Debian](https://security-tracker.debian.org/tracker/CVE-2026-85091).
- **libheif** - [Ubuntu USN-8683-1](https://ubuntu.com/security/notices/USN-8683-1), [USN-8774-1](https://ubuntu.com/security/notices/USN-8774-1).
- **Rack** - [Ubuntu USN-8066-1](https://ubuntu.com/security/notices/USN-8066-1), [Debian DSA-6180-1](https://lists.debian.org/debian-security-announce/2026/msg00089.html).
- **xmldom** - [IBM Cloud Pak for Integration](https://www.ibm.com/support/pages/security-bulletin-automation-assets-ibm-cloud-pak-integration-vulnerable-vulnerability-xmldom), [IBM Maximo Application Suite](https://www.ibm.com/support/pages/security-bulletin-ibm-maximo-application-suite-visual-inspection-component-uses-xmldom-which-vulnerable-cve-2026-34601), [Red Hat](https://access.redhat.com/security/cve/cve-2026-34601).
- **rust-openssl** - [Red Hat](https://access.redhat.com/security/cve/cve-2026-45784), [SUSE](https://www.suse.com/security/cve/CVE-2026-45784.html).

[Research](RESEARCH.md) · [Upstream](UPSTREAM.md) · [HackerOne](https://hackerone.com/thesmartshadow) · [Website](https://thesmartshadow.dev)
