# Ali Firas (thesmartshadow)

**Linux kernel contributor | Vulnerability researcher | Systems engineer**

My work is in Linux networking and the security boundaries of widely used software. I investigate bugs in parsers, file operations, protocol implementations, authorization paths, and resource accounting. Some reports end in advisories; others end in patches and tests that upstream maintainers can carry.

I prefer to keep the evidence close to the claim: original commits, maintainer advisories, release notes, and distribution security notices.

[Kernel commit](https://github.com/torvalds/linux/commit/599d0e97610f09162d84c4ede4164628c066921e) | [OpenSSL advisory](https://openssl-library.org/news/secadv/20260929.txt) | [Chrome CNA record](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/106xxx/CVE-2026-106484.json) | [GitHub advisories](https://github.com/advisories?query=credit%3Athesmartshadow) | [Upstream PRs](https://github.com/pulls?q=is%3Apr+author%3Athesmartshadow) | [Research site](https://thesmartshadow.dev/)

The complete [research index](RESEARCH-INDEX.md) covers the other published findings. [Source and patch notes](EVIDENCE-REGISTER.md) distinguish credited discoveries from fixes I authored, upstream merges, and vendor or distribution response.

## Linux kernel

I contributed [`599d0e97610f`](https://github.com/torvalds/linux/commit/599d0e97610f09162d84c4ede4164628c066921e), **`vxlan: vnifilter: validate the VXLAN_VNIFILTER_ENTRY nest`**, to the Linux networking code. The patch was merged through `net-next` and is present in [`torvalds/linux`](https://github.com/torvalds/linux). It is authored and signed off by Ali Firas and was committed by Jakub Kicinski on 21 October 2026.

The problem was in the netlink validation boundary. VXLAN VNI filter entries were parsed and applied one at a time. A message containing a valid entry followed by a policy-invalid entry could change state and emit an `RTM_NEWTUNNEL` notification before the kernel rejected the rest of the message. I connected the outer nest to the entry policy with `NLA_POLICY_NESTED()`, moving that validation ahead of dispatch. The change closes the policy-validation case; it does not make all later device or handler failures atomic.

The commit came out of a [seven-patch VXLAN vnifilter series](https://patchew.org/linux/20261014123814.388557-1-alishmery18%40gmail.com/) involving VNI range checks, bounded requests, dump consistency, memory accounting, and selftests. [Patch 1 was accepted](https://lists.openwall.net/linux-kernel/2026/10/21/37). I keep the remaining submitted patches separate from the merged record.

## Vulnerability research

### OpenSSL: QUIC amplification accounting

[CVE-2026-35191](https://www.cve.org/CVERecord?id=CVE-2026-35191) | [OpenSSL security advisory](https://openssl-library.org/news/secadv/20260929.txt) | [OpenSSL vulnerability record](https://openssl-library.org/news/vulnerabilities-4.0/)

In the affected OpenSSL QUIC server configuration, an incoming UDP datagram containing multiple QUIC packets could be counted more than once toward unvalidated amplification credit. That broke the intended three-times amplification bound in RFC 9000. The condition depends on the server's address-validation configuration; it is not a general TLS or cryptographic primitive flaw.

OpenSSL records my report on 13 June 2026 and an independent report from Nikolas Gauder of NVIDIA on 22 August. Neil Horman wrote the fix, released in OpenSSL 3.5.9, 3.6.5, and 4.0.3. The advisory is unusually useful here because it records the reporting chronology, technical impact, and remediation in one place.

### Chrome DevTools MCP: checking a path before changing it

[CVE-2026-106484](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/106xxx/CVE-2026-106484.json) | [GHSA-5hw5-4q87-m6x9](https://github.com/ChromeDevTools/chrome-devtools-mcp/security/advisories/GHSA-5hw5-4q87-m6x9)

The MCP server checked the caller-supplied path against its permitted roots, then rewrote the file extension before writing. The final path was not subjected to the same canonical-path check. Under the documented symlink conditions, this allowed a write outside the intended roots.

The finding was an incomplete-fix variant, not a new class of unrestricted browser execution. The maintainer advisory credits `thesmartshadow`, and **Chrome CNA** assigned and published CVE-2026-106484 on 28 October 2026. The affected package was `chrome-devtools-mcp` before 1.5.0.

### zlib: stale buffer state across a write stall

[CVE-2026-85091](https://www.cve.org/CVERecord?id=CVE-2026-85091) | [Research](https://gist.github.com/thesmartshadow/e0b9481792afb7c31e86fee1ff084490) | [Ubuntu USN-8954-1](https://ubuntu.com/security/notices/USN-8954-1)

A non-blocking write stall could leave stale external-buffer state in the gzip write path. A subsequent formatted write could then reach an out-of-bounds `memmove` in `gz_vacate()`. Ubuntu's security notice identifies Ali Firas as the discoverer and records patched distribution packages. I also submitted [zlib PR #1317](https://github.com/madler/zlib/pull/1317); it was closed without merge and is not listed as an accepted patch.

### vm2: a host-realm Promise escaping the sandbox

[CVE-2026-92956](https://github.com/advisories/GHSA-wjwh-qqvp-g4p4) | Critical | Co-reported with `zolbooo`

On affected Node.js 26 configurations, a `WebAssembly` streaming path exposed a host-realm Promise through a default vm2 sandbox. The interaction with `Promise.prototype.finally` and `Symbol.species` could recover host capabilities. The result is a sandbox escape under the affected conditions, not an assertion that every vm2 deployment is remotely exploitable.

### Cloudflare Pingora: hop-by-hop headers and downstream authorization

[CVE-2026-105299](https://www.cve.org/CVERecord?id=CVE-2026-105299) | [Cloudflare advisory](https://github.com/cloudflare/pingora/security/advisories/GHSA-vx4q-2c55-cvmg) | [RustSec](https://rustsec.org/advisories/RUSTSEC-2026-0390.html)

In chained HTTP/1 proxy deployments, attacker-controlled `Connection` header tokens could cause an intermediary to remove a header trusted by the origin. The authorization consequence depended on the proxy chain and how the origin used that header. Cloudflare credits my report and notes that its CDN customers were not affected.

### Memory safety: rust-openssl and libheif

[CVE-2026-45784](https://github.com/advisories/GHSA-phqj-4mhp-q6mq) involved an out-of-bounds write in the Rust `openssl` crate's `CipherCtxRef::cipher_update_inplace` for AES key-wrap-with-padding. The operation was missed by an earlier fix; the correction shipped in crate version 0.10.80. This is **separate** from my QUIC finding in OpenSSL's C codebase.

[CVE-2026-62291](https://github.com/strukturag/libheif/security/advisories/GHSA-xpw3-9rhw-482x) was a heap out-of-bounds write in libheif's uncompressed encoder when component-plane dimensions did not match the primary image. Ubuntu issued [USN-8683-1](https://ubuntu.com/security/notices/USN-8683-1) and [USN-8774-1](https://ubuntu.com/security/notices/USN-8774-1). Both name Ali Firas and cover the affected releases separately.

### Resource limits, parsing, and authorization

A few examples where the security assumption failed before the final validation point:

- [CoreDNS CVE-2026-32936](https://github.com/coredns/coredns/security/advisories/GHSA-63cw-r7xf-jmwr): oversized DNS-over-HTTPS GET input could consume resources before the request was rejected. Fixed in CoreDNS 1.14.3.
- [cpp-httplib CVE-2026-28435](https://github.com/yhirose/cpp-httplib/security/advisories/GHSA-xvfx-w463-6fpp): streaming gzip decompression bypassed the configured payload budget. Fixed in 0.35.0.
- [fasthttp GO-2026-4950](https://pkg.go.dev/vuln/GO-2026-4950): double-encoded paths could be interpreted differently by authorization logic and file-serving code. [Upstream fix #2163](https://github.com/valyala/fasthttp/pull/2163) was written by the maintainer and released in 1.70.0, with credit to my report. This record is not a CVE.
- [CISA manage.get.gov GHSA-hfq4-89cf-8p8j](https://github.com/cisagov/manage.get.gov/security/advisories/GHSA-hfq4-89cf-8p8j): a view-only organization member could reach privileged member-management operations. [Maintainer fix #5049](https://github.com/cisagov/manage.get.gov/pull/5049).
- [xmldom CVE-2026-34601](https://github.com/xmldom/xmldom/security/advisories/GHSA-wh4c-j3r5-mjhp): CDATA serialization failed to preserve the intended XML structure boundary. The issue subsequently appeared in vendor and distribution security notices.

## Patches accepted upstream

These are changes I wrote that were merged into repositories outside my account. The list is separate from vulnerabilities I reported but did not patch.

| Project | Change |
| --- | --- |
| [Linux kernel, 599d0e97610f](https://github.com/torvalds/linux/commit/599d0e97610f09162d84c4ede4164628c066921e) | Validate nested VXLAN VNI filter attributes before dispatch. |
| [RubyGems #9493](https://github.com/ruby/rubygems/pull/9493) | Keep extraction within its destination when pre-existing symlinks are present; add regression coverage. |
| [CEL-Go #1302](https://github.com/cel-expr/cel-go/pull/1302) | Enforce source expression size limits before allocation. |
| [Google zx #1349](https://github.com/google/zx/pull/1349) | Prevent cleanup through `--prefer-local` from deleting an external `node_modules` target. |
| [Akamai CLI #227](https://github.com/akamai/cli/pull/227) | Validate package command names before deriving output paths. |
| [Ruby JSON #948](https://github.com/ruby/json/pull/948) | Reject negative generator depth before entering unsafe native behavior. |
| [Google HumanIO #4](https://github.com/google/humanio/pull/4) | Remove server source exposure and move a hard-coded token into configuration. |
| [httparse #217](https://github.com/seanmonstar/httparse/pull/217) | Document resource limits for repeated partial-buffer parsing. This was a documentation change. |

## Security notices and downstream handling

I follow findings beyond the initial advisory, but I distinguish a package tracker from a security update that a distribution has actually shipped.

| Research | Published response |
| --- | --- |
| **zlib, CVE-2026-85091** | [Ubuntu USN-8954-1](https://ubuntu.com/security/notices/USN-8954-1) credits my discovery and lists fixed packages; [Debian](https://security-tracker.debian.org/tracker/CVE-2026-85091) tracks affected versions. |
| **OpenSSL, CVE-2026-35191** | [Ubuntu USN-8847-1](https://ubuntu.com/security/notices/USN-8847-1), [Debian DSA-6531-1](https://lists.debian.org/debian-security-announce/2026/msg00444.html), and [SUSE](https://www.suse.com/support/update/announcement/2026/suse-su-202624245-1/) published security updates for their applicable packages. |
| **libheif, CVE-2026-62291** | [Ubuntu USN-8683-1](https://ubuntu.com/security/notices/USN-8683-1) and [USN-8774-1](https://ubuntu.com/security/notices/USN-8774-1) credit Ali Firas directly. |
| **Rack, CVE-2026-25500** | [Ubuntu USN-8066-1](https://ubuntu.com/security/notices/USN-8066-1) names me; [Debian DSA-6180-1](https://lists.debian.org/debian-security-announce/2026/msg00089.html) and [SUSE](https://www.suse.com/security/cve/CVE-2026-25500.html) document downstream response. |
| **xmldom, CVE-2026-34601** | [IBM Cloud Pak](https://www.ibm.com/support/pages/security-bulletin-automation-assets-ibm-cloud-pak-integration-vulnerable-vulnerability-xmldom), [IBM Maximo](https://www.ibm.com/support/pages/security-bulletin-ibm-maximo-application-suite-visual-inspection-component-uses-xmldom-which-vulnerable-cve-2026-34601), and [Red Hat](https://access.redhat.com/security/cve/cve-2026-34601) document product impact or assessment. |

The presence of a CVE in a vendor tracker does not establish exploitability in every downstream product.

## Other published investigations

My public record also includes:

- **Privilege boundaries:** [uutils coreutils CVE-2026-93658](https://www.cve.org/CVERecord?id=CVE-2026-93658), [su-exec CVE-2026-82457](https://www.cve.org/CVERecord?id=CVE-2026-82457), [Microsoft AVML CVE-2026-61371](https://www.cve.org/CVERecord?id=CVE-2026-61371), [LiME CVE-2026-85092](https://www.cve.org/CVERecord?id=CVE-2026-85092).
- **Authorization and trust boundaries:** [RustFS CVE-2026-39360](https://github.com/advisories/GHSA-mx42-j6wv-px98), [Microsoft APM CVE-2026-45539](https://github.com/microsoft/apm/security/advisories/GHSA-q5pp-gvjg-h7v4), [Microsoft UFO CVE-2026-54568](https://github.com/microsoft/UFO/security/advisories/GHSA-hc27-j4p9-qm2x), [Russh CVE-2026-68930](https://github.com/advisories/GHSA-m65r-rprj-r5rg), [Axios CVE-2026-67320](https://github.com/advisories/GHSA-gcfj-64vw-6mp9), [ownCloud Guests CVE-2025-59716](https://www.cve.org/CVERecord?id=CVE-2025-59716).
- **Parsers and state handling:** [Hickory DNS CVE-2026-93657](https://github.com/advisories/GHSA-5j98-2g5x-46v6), [cilium/ebpf CVE-2026-10722](https://github.com/cilium/ebpf/issues/2019), [Net-SNMP CVE-2026-89147](https://www.cve.org/CVERecord?id=CVE-2026-89147), [libp2p rendezvous CVE-2026-89146](https://www.cve.org/CVERecord?id=CVE-2026-89146), [Nezha CVE-2026-100394](https://github.com/advisories/GHSA-qjpp-gffx-2wm9), [Hono CVE-2026-59896](https://github.com/advisories/GHSA-hvrm-45r6-mjfj).
- **File handling and resource consumption:** [pyLoad CVE-2026-32808](https://github.com/pyload/pyload/security/advisories/GHSA-7g4m-8hx2-4qh3) (co-discovered with Ali Al-Akbar), [PyJWT CVE-2026-48525](https://github.com/advisories/GHSA-w7vc-732c-9m39), [basic-ftp CVE-2026-44240](https://github.com/advisories/GHSA-rpmf-866q-6p89), [systeminformation CVE-2026-44724](https://github.com/advisories/GHSA-hvx9-hwr7-wjj9), [jq CVE-2026-43895](https://github.com/advisories/GHSA-7q7g-mrq3-phxr), [tar-rs CVE-2026-70622](https://www.cve.org/CVERecord?id=CVE-2026-70622), [miniserve CVE-2025-67124](https://www.cve.org/CVERecord?id=CVE-2025-67124).

I do not count proposed fixes as merged patches, or advisories without a CVE as additional CVEs.

## Contact

[GitHub](https://github.com/thesmartshadow) | [HackerOne](https://hackerone.com/thesmartshadow) | [Research site](https://thesmartshadow.dev/) | [LinkedIn](https://www.linkedin.com/in/ali-shmery/)

For coordinated disclosure or work on an upstream fix, GitHub or HackerOne are the best starting points.
