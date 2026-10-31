# Ali Firas

`thesmartshadow` | Linux kernel contributor | Security research

I work on Linux networking and vulnerability research in open-source software. Most of the bugs I spend time on are in the details: netlink attributes applied before validation finishes, paths checked before they are rewritten, counters that stop meaning what their callers think they mean, or parsers doing expensive work before enforcing a limit.

I also write fixes. The [VXLAN change below](https://github.com/torvalds/linux/commit/599d0e97610f09162d84c4ede4164628c066921e) is in the mainline kernel; other work has landed in RubyGems, CEL-Go, zx, Akamai CLI and several smaller projects.

[Kernel commits](https://github.com/torvalds/linux/commit/599d0e97610f09162d84c4ede4164628c066921e) / [Advisories](https://github.com/advisories?query=credit%3Athesmartshadow) / [Research notes](https://thesmartshadow.dev/) / [HackerOne](https://hackerone.com/thesmartshadow)

## Linux networking

**VXLAN VNI filter validation**, merged into [`torvalds/linux`](https://github.com/torvalds/linux/commit/599d0e97610f09162d84c4ede4164628c066921e) as `599d0e97610f`.

`vxlan_vnifilter_process()` parsed the outer netlink message, then validated nested VNI entries as it dispatched them. That ordering matters. If the first entry was valid and the next was malformed, the first could already have been installed and its `RTM_NEWTUNNEL` notification sent by the time the request failed.

The merged patch wires `VXLAN_VNIFILTER_ENTRY` to `vni_filter_entry_policy` through `NLA_POLICY_NESTED()`. Policy-invalid entries are rejected before dispatch. It does not attempt to roll back later device or handler failures.

I authored the change; Jakub Kicinski applied it to `net-next` on 21 October 2026. It reached the [mainline Linux tree](https://github.com/torvalds/linux/commit/599d0e97610f09162d84c4ede4164628c066921e).

The work started as a [seven-patch vnifilter series](https://patchew.org/linux/20261014123814.388557-1-alishmery18%40gmail.com/) covering range validation, request bounds, dump behavior, per-VNI accounting and selftests. The [netdev application notice](https://lists.openwall.net/linux-kernel/2026/10/21/37) identifies patch 1/7 as merged. I have not labelled the remaining six as merged.

## Security work

These are a few of the issues I can point to with maintainer records, not a list of everything I've reported.

**OpenSSL, QUIC anti-amplification accounting.** [CVE-2026-35191](https://openssl-library.org/news/vulnerabilities/)

With address validation disabled, a QUIC server could overcount the unvalidated credit earned from a UDP datagram carrying multiple packets. That makes the RFC 9000 3x amplification limit unreliable under the affected configuration. [OpenSSL's advisory](https://openssl-library.org/news/secadv/20260929.txt) credits my report of 13 June 2026 and an independent report from Nikolas Gauder in August. Neil Horman wrote the fix. This is a protocol accounting bug, not a TLS primitive break.

**Chrome DevTools MCP, path validation after an incomplete fix.** [CVE-2026-106484](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/106xxx/CVE-2026-106484.json) / [GHSA-5hw5-4q87-m6x9](https://github.com/ChromeDevTools/chrome-devtools-mcp/security/advisories/GHSA-5hw5-4q87-m6x9)

The server checked an output path against MCP roots, changed the file extension, then wrote to the new path without checking where it resolved. A symlink on the rewritten path could take the write outside the permitted roots. The reproducer exercised the real MCP path, not just an isolated helper. Chrome CNA published the CVE; the fix shipped in `chrome-devtools-mcp` 1.5.0.

**zlib, gzip write buffer handling.** [CVE-2026-85091](https://ubuntu.com/security/notices/USN-8954-1)

A stalled write could leave stale buffer state in the gzip output path. A later formatted write could reach an out-of-bounds `memmove` in `gz_vacate()`. [Ubuntu's security notice](https://ubuntu.com/security/notices/USN-8954-1) credits the discovery and records affected distribution packages. My [proposed upstream patch](https://github.com/madler/zlib/pull/1317) was closed without merge.

**Cloudflare Pingora, `Connection` header handling.** [CVE-2026-105299](https://github.com/cloudflare/pingora/security/advisories/GHSA-vx4q-2c55-cvmg)

In a particular chained HTTP/1 proxy arrangement, client-nominated hop-by-hop headers could strip a header the downstream service relied on for authorization. The issue depends on that deployment and trust relationship. Cloudflare's [advisory](https://github.com/cloudflare/pingora/security/advisories/GHSA-vx4q-2c55-cvmg)

**vm2, Node.js sandbox escape.** [CVE-2026-92956](https://github.com/advisories/GHSA-wjwh-qqvp-g4p4)

A host-realm Promise exposed by a WebAssembly streaming path could cross vm2's sandbox boundary through `finally` and `Symbol.species` handling. Reproduced under the affected Node.js 26
**Memory safety in rust-openssl and libheif.** [CVE-2026-45784](https://github.com/advisories/GHSA-phqj-4mhp-q6mq) / [CVE-2026-62291](https://github.com/strukturag/libheif/security/advisories/GHSA-xpw3-9rhw-482x)

The first is an out-of-bounds write in the Rust OpenSSL binding's `CipherCtxRef::cipher_update_inplace` path for AES-KW-PAD. It is separate from the OpenSSL QUIC report. The second is a heap out-of-bounds write in libheif's uncompressed encoder caused by inconsistent component-plane dimensions. Ubuntu credits my libheif report in [USN-8683-1](https://ubuntu.com/security/notices/USN-8683-1) and [USN-8774-1](https://ubuntu.com/security/notices/USN-8774-1).

Other reports include [CoreDNS](https://github.com/coredns/coredns/security/advisories/GHSA-63cw-r7xf-jmwr) (DoH resource amplification), [cpp-httplib](https://github.com/yhirose/cpp-httplib/security/advisories/GHSA-xvfx-w463-6fpp) (gzip payload limit bypass), [CISA manage.get.gov](https://github.com/cisagov/manage.get.gov/security/advisories/GHSA-hfq4-89cf-8p8j) (organization-member authorization), [xmldom](https://github.com/xmldom/xmldom/security/advisories/GHSA-wh4c-j3r5-mjhp) (CDATA serialization), and [fasthttp](https://pkg.go.dev/vuln/GO-2026-4950) (double-decoded file paths). The fasthttp report has a Go vulnerability ID and a maintainer fix

The rest is in the [research index](RESEARCH-INDEX.md).

## Upstream changes

Code or documentation I authored that was merged, with the change itself linked:

| Upstream | Change |
| --- | --- |
| [Linux, `599d0e97610f`](https://github.com/torvalds/linux/commit/599d0e97610f09162d84c4ede4164628c066921e) | Validate nested VXLAN VNI entries before dispatch |
| [RubyGems #9493](https://github.com/ruby/rubygems/pull/9493) | Keep extraction inside its destination when existing symlinks are present |
| [CEL-Go #1302](https://github.com/cel-expr/cel-go/pull/1302) | Check source expression size before constructing the source |
| [Google zx #1349](https://github.com/google/zx/pull/1349) | Stop `--prefer-local` cleanup from deleting an external `node_modules` directory |
| [Akamai CLI #227](https://github.com/akamai/cli/pull/227) | Validate command names before using them in output paths |
| [Ruby JSON #948](https://github.com/ruby/json/pull/948) | Reject negative generator depth |
| [Google HumanIO #4](https://github.com/google/humanio/pull/4) | Remove source exposure and hard-coded token handling |
| [httparse #217](https://github.com/seanmonstar/httparse/pull/217) | Document repeated `Partial` parsing hazards (documentation) |

## Distribution and vendor response

Some of the reports have reached security updates for systems people actually run:

- **Ubuntu:** [OpenSSL, USN-8847-1](https://ubuntu.com/security/notices/USN-8847-1); [zlib, USN-8954-1](https://ubuntu.com/security/notices/USN-8954-1); [libheif, USN-8683-1](https://ubuntu.com/security/notices/USN-8683-1) and [USN-8774-1](https://ubuntu.com/security/notices/USN-8774-1); [Rack, USN-8066-1](https://ubuntu.com/security/notices/USN-8066-1).
- **Debian:** [OpenSSL, DSA-6531-1](https://lists.debian.org/debian-security-announce/2026/msg00444.html) and [Rack, DSA-6180-1](https://lists.debian.org/debian-security-announce/2026/msg00089.html).
- **SUSE:** [OpenSSL security update](https://www.suse.com/support/update/announcement/2026/suse-su-202624245-1/). Other findings also appear in SUSE's product-specific CVE records.
- **IBM / Red Hat:** IBM issued [Cloud Pak](https://www.ibm.com/support/pages/security-bulletin-automation-assets-ibm-cloud-pak-integration-vulnerable-vulnerability-xmldom) and [Maximo](https://www.ibm.com/support/pages/security-bulletin-ibm-maximo-application-suite-visual-inspection-component-uses-xmldom-which-vulnerable-cve-2026-34601) bulletins for the xmldom issue; [Red Hat tracks the CVE](https://access.redhat.com/security/cve/cve-2026-34601).

I keep the [source record](EVIDENCE-REGISTER.md) separate because a distribution notice, a CVE tracker entry and a merged upstream patch are different things.

## Contact

[GitHub](https://github.com/thesmartshadow) / [HackerOne](https://hackerone.com/thesmartshadow) / [LinkedIn](https://www.linkedin.com/in/ali-shmery/) / [Research site](https://thesmartshadow.dev/)
