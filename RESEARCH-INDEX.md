# Security research index - Ali Firas (thesmartshadow)

**Cut-off:** 2026-10-31. This is a curated index assembled from original maintainer advisories, CNA records, distribution notices, and previously archived research. A record is listed by its publicly published identifier; inclusion is not an assertion that the researcher wrote the vendor's patch, or that every listed downstream product is exploitable.

**Do not use this table as a live CVE counter.** A complete published-CVE reconciliation requires regular checks against CVE states PUBLISHED and attribution. This working index contains **39 distinct published CVE leads** from the evidence reviewed, excluding the explicitly rejected RubyGems ID. For externally communicated metrics, verify all 39 records again against their source before displaying an exact total. See [EVIDENCE-REGISTER.md](EVIDENCE-REGISTER.md) for evidence quality and exact update classifications.

## 2026

| CVE | Project | Specific failure mode | Source / attribution trail |
| --- | --- | --- | --- |
| [CVE-2026-10722](https://www.cve.org/CVERecord?id=CVE-2026-10722) | cilium/ebpf | Malformed BTF parsing / panic | [Record](https://github.com/cilium/ebpf/issues/2019) |
| [CVE-2026-25500](https://www.cve.org/CVERecord?id=CVE-2026-25500) | Rack | Stored XSS in Rack::Directory | [Record](https://ubuntu.com/security/notices/USN-8066-1) |
| [CVE-2026-28435](https://www.cve.org/CVERecord?id=CVE-2026-28435) | cpp-httplib | Decompression budget bypass / DoS | [Record](https://github.com/yhirose/cpp-httplib/security/advisories/GHSA-xvfx-w463-6fpp) |
| [CVE-2026-32808](https://www.cve.org/CVERecord?id=CVE-2026-32808) | pyLoad | Path traversal and deletion (co-reported) | [Record](https://github.com/pyload/pyload/security/advisories/GHSA-7g4m-8hx2-4qh3) |
| [CVE-2026-32936](https://www.cve.org/CVERecord?id=CVE-2026-32936) | CoreDNS | Unauthenticated DoH resource amplification | [Record](https://github.com/coredns/coredns/security/advisories/GHSA-63cw-r7xf-jmwr) |
| [CVE-2026-33491](https://www.cve.org/CVERecord?id=CVE-2026-33491) | Zen C | Stack overflow in identifier mangling | [Record](https://github.com/zenc-lang/zenc/security/advisories/GHSA-rv74-w6q7-h8xr) |
| [CVE-2026-34601](https://www.cve.org/CVERecord?id=CVE-2026-34601) | xmldom | CDATA serialization and XML structure injection | [Record](https://github.com/xmldom/xmldom/security/advisories/GHSA-wh4c-j3r5-mjhp) |
| [CVE-2026-35191](https://www.cve.org/CVERecord?id=CVE-2026-35191) | OpenSSL | QUIC unvalidated anti-amplification accounting (independent reports) | [Record](https://openssl-library.org/news/secadv/20260929.txt) |
| [CVE-2026-39360](https://www.cve.org/CVERecord?id=CVE-2026-39360) | RustFS | Missing source authorization for multipart copy | [Record](https://github.com/advisories/GHSA-mx42-j6wv-px98) |
| [CVE-2026-43895](https://www.cve.org/CVERecord?id=CVE-2026-43895) | jq | Import-path NUL trust boundary | [Record](https://github.com/jqlang/jq/security/advisories/GHSA-7q7g-mrq3-phxr) |
| [CVE-2026-44240](https://www.cve.org/CVERecord?id=CVE-2026-44240) | basic-ftp | Unbounded multiline FTP response buffering | [Record](https://github.com/advisories/GHSA-rpmf-866q-6p89) |
| [CVE-2026-44724](https://www.cve.org/CVERecord?id=CVE-2026-44724) | systeminformation | Command injection in NetworkManager names | [Record](https://github.com/sebhildebrandt/systeminformation/security/advisories/GHSA-hvx9-hwr7-wjj9) |
| [CVE-2026-45539](https://www.cve.org/CVERecord?id=CVE-2026-45539) | Microsoft APM | Symlink disclosure during remote package installation | [Record](https://github.com/microsoft/apm/security/advisories/GHSA-q5pp-gvjg-h7v4) |
| [CVE-2026-45784](https://www.cve.org/CVERecord?id=CVE-2026-45784) | rust-openssl | Heap out-of-bounds write in AES-KW-PAD binding | [Record](https://github.com/advisories/GHSA-phqj-4mhp-q6mq) |
| [CVE-2026-48525](https://www.cve.org/CVERecord?id=CVE-2026-48525) | PyJWT | Detached JWS resource amplification | [Record](https://github.com/jpadilla/pyjwt/security/advisories/GHSA-w7vc-732c-9m39) |
| [CVE-2026-54568](https://www.cve.org/CVERecord?id=CVE-2026-54568) | Microsoft UFO | Device-system-information authorization bypass | [Record](https://github.com/microsoft/UFO/security/advisories/GHSA-hc27-j4p9-qm2x) |
| [CVE-2026-59896](https://www.cve.org/CVERecord?id=CVE-2026-59896) | Hono | Shared JSX context / request-state leakage | [Record](https://github.com/honojs/hono/security/advisories/GHSA-hvrm-45r6-mjfj) |
| [CVE-2026-61371](https://www.cve.org/CVERecord?id=CVE-2026-61371) | Microsoft AVML | Symlink-following output and truncation | [Record](https://github.com/microsoft/avml/pull/754) |
| [CVE-2026-62291](https://www.cve.org/CVERecord?id=CVE-2026-62291) | libheif | Out-of-bounds heap write in uncompressed encoder | [Record](https://ubuntu.com/security/notices/USN-8683-1) |
| [CVE-2026-67320](https://www.cve.org/CVERecord?id=CVE-2026-67320) | Axios | Proxy behavior inherited via prototype chain | [Record](https://github.com/advisories/GHSA-gcfj-64vw-6mp9) |
| [CVE-2026-68930](https://www.cve.org/CVERecord?id=CVE-2026-68930) | Russh | Expired channel lifecycle / authorization-state error | [Record](https://github.com/advisories/GHSA-m65r-rprj-r5rg) |
| [CVE-2026-70622](https://www.cve.org/CVERecord?id=CVE-2026-70622) | tar-rs | Archive path/symlink escape | [Record](https://www.cve.org/CVERecord?id=CVE-2026-70622) |
| [CVE-2026-82457](https://www.cve.org/CVERecord?id=CVE-2026-82457) | su-exec | UID number truncation / privilege boundary | [Record](https://www.vulncheck.com/advisories/su-exec-through-0.3-privilege-escalation-via-numeric-user-id) |
| [CVE-2026-85091](https://www.cve.org/CVERecord?id=CVE-2026-85091) | zlib | gz_vacate heap out-of-bounds write | [Record](https://ubuntu.com/security/notices/USN-8954-1) |
| [CVE-2026-85092](https://www.cve.org/CVERecord?id=CVE-2026-85092) | LiME | Symlink overwrite at output creation | [Record](https://www.vulncheck.com/advisories/lime-through-1.12.0-arbitrary-file-overwrite-via-symlink-following) |
| [CVE-2026-89146](https://www.cve.org/CVERecord?id=CVE-2026-89146) | rust-libp2p rendezvous | Timer/TTL overflow denial of service | [Record](https://github.com/advisories/GHSA-gh9c-4324-26cm) |
| [CVE-2026-89147](https://www.cve.org/CVERecord?id=CVE-2026-89147) | Net-SNMP | SMUX unauthenticated blocking read / DoS | [Record](https://github.com/net-snmp/net-snmp/issues/1134) |
| [CVE-2026-92956](https://www.cve.org/CVERecord?id=CVE-2026-92956) | vm2 | Host-realm Promise sandbox escape (co-reported) | [Record](https://github.com/advisories/GHSA-wjwh-qqvp-g4p4) |
| [CVE-2026-93657](https://www.cve.org/CVERecord?id=CVE-2026-93657) | Hickory DNS | DNSSEC bogus state suppressed in resolver API | [Record](https://github.com/advisories/GHSA-5j98-2g5x-46v6) |
| [CVE-2026-93658](https://www.cve.org/CVERecord?id=CVE-2026-93658) | uutils coreutils | setuid install sequencing and ownership failure | [Record](https://github.com/uutils/coreutils/security/advisories/GHSA-cgg3-923w-v53m) |
| [CVE-2026-100394](https://www.cve.org/CVERecord?id=CVE-2026-100394) | Nezha | Authenticated member-triggered instance-wide DoS | [Record](https://github.com/advisories/GHSA-qjpp-gffx-2wm9) |
| [CVE-2026-105299](https://www.cve.org/CVERecord?id=CVE-2026-105299) | Cloudflare Pingora | Hop-by-hop header trust boundary | [Record](https://github.com/cloudflare/pingora/security/advisories/GHSA-vx4q-2c55-cvmg) |
| [CVE-2026-106484](https://www.cve.org/CVERecord?id=CVE-2026-106484) | Chrome DevTools MCP | Path rewrite after MCP roots validation | [Record](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/106xxx/CVE-2026-106484.json) |

## 2025

| CVE | Project | Specific failure mode | Source / attribution trail |
| --- | --- | --- | --- |
| [CVE-2025-13437](https://www.cve.org/CVERecord?id=CVE-2025-13437) | Google zx | External node_modules deletion via cleanup alias | [Record](https://github.com/google/zx/pull/1349) |
| [CVE-2025-59716](https://www.cve.org/CVERecord?id=CVE-2025-59716) | ownCloud Guests | Unauthenticated pending-guest enumeration | [Record](https://www.cve.org/CVERecord?id=CVE-2025-59716) |
| [CVE-2025-59717](https://www.cve.org/CVERecord?id=CVE-2025-59717) | DigitalOcean do-markdownit | Allowed classes type confusion | [Record](https://github.com/thesmartshadow/writeup) |
| [CVE-2025-63095](https://www.cve.org/CVERecord?id=CVE-2025-63095) | Tempus Ex hello-video-codec | BitstreamWriter input-triggered denial of service | [Record](https://www.cve.org/CVERecord?id=CVE-2025-63095) |
| [CVE-2025-67124](https://www.cve.org/CVERecord?id=CVE-2025-67124) | miniserve | Symlink race in upload finalization | [Record](https://www.cve.org/CVERecord?id=CVE-2025-67124) |
| [CVE-2025-67125](https://www.cve.org/CVERecord?id=CVE-2025-67125) | docopt.cpp | Signed counter overflow | [Record](https://github.com/docopt/docopt.cpp/pull/168) |

## Security records without an accepted CVE in this audit

| Record | Project | Evidence / counting rule |
| --- | --- | --- |
| [GO-2026-4950](https://pkg.go.dev/vuln/GO-2026-4950) | fasthttp | Official Go Vulnerability Database credit to Ali Firas, with upstream fix in 1.70.0; **not a CVE**. |
| [GHSA-hfq4-89cf-8p8j](https://github.com/cisagov/manage.get.gov/security/advisories/GHSA-hfq4-89cf-8p8j) | CISA manage.get.gov | Security advisory and authorization fix; **not counted as a CVE**. |

## Explicitly excluded from an active CVE count

- **[CVE-2026-82455](https://www.cve.org/CVERecord?id=CVE-2026-82455)** - RubyGems entry **REJECTED** following maintainers' security classification decision. The actual [authored and merged RubyGems patch #9493](https://github.com/ruby/rubygems/pull/9493) is still valid engineering work; it is not an active CVE.

## Authorship and credit boundaries

- **Linux mainline:** [599d0e97610f](https://github.com/torvalds/linux/commit/599d0e97610f09162d84c4ede4164628c066921e) was authored by Ali Firas and committed by Jakub Kicinski. This proves a merged networking contribution; other patches in the related VXLAN v4 series must be accounted for separately.
- **OpenSSL:** [the vendor's September 2026 bulletin](https://openssl-library.org/news/secadv/20260929.txt) credits Ali Firas and separately credits Nikolas Gauder (independent report) and Neil Horman (fix). Do not imply that Ali authored the OpenSSL fix.
- **fasthttp:** Go DB credits Ali Firas as reporter, but PR #2163 was written by another upstream developer.
- **libheif:** [USN-8683-1](https://ubuntu.com/security/notices/USN-8683-1) and [USN-8774-1](https://ubuntu.com/security/notices/USN-8774-1) are two Ubuntu remediation notices for the same single CVE.
- **vm2** and **pyLoad** were jointly reported as indicated in source advisories; joint discovery should be visible everywhere the work is featured.
- **Chrome DevTools MCP:** [CVE-2026-106484](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/106xxx/CVE-2026-106484.json) was assigned by **Chrome CNA**, rather than a GitHub or VulnCheck CNA.

## Newly surfaced project advisory requiring reporter-credit confirmation

- **lldpd - [GHSA-jmrh-hxvj-p42g](https://github.com/lldpd/lldpd/security/advisories/GHSA-jmrh-hxvj-p42g):** the Debian [1.0.23-1 upload record dated 26 October 2026](https://tracker.debian.org/news/1815479/accepted-lldpd-1023-1-source-into-unstable/) explicitly says the upstream release fixes an out-of-bounds read tracked by this GHSA. The original private-or-restricted GitHub advisory did not expose its reporter field during this audit, so the finding is marked **credit to be verified** rather than silently included in a verified discoverer list. It has **not** been counted as a CVE.
