# Vulnerability research

Ali Firas / `thesmartshadow`

This is my published work, indexed by project and identifier. The brief descriptions tell you where the check failed

The table contains 39 CVE records from the current research ledger. It is not a live counter, and it should not be read as a claim that I wrote every vendor fix.
## 2026

| CVE | Project | Specific failure mode | Source / attribution trail |
| --- | --- | --- | --- |
| [CVE-2026-10722](https://www.cve.org/CVERecord?id=CVE-2026-10722) | cilium/ebpf | Malformed BTF parsing / panic | [Source](https://github.com/cilium/ebpf/issues/2019) |
| [CVE-2026-25500](https://www.cve.org/CVERecord?id=CVE-2026-25500) | Rack | Stored XSS in Rack::Directory | [Source](https://ubuntu.com/security/notices/USN-8066-1) |
| [CVE-2026-28435](https://www.cve.org/CVERecord?id=CVE-2026-28435) | cpp-httplib | Decompression budget bypass / DoS | [Source](https://github.com/yhirose/cpp-httplib/security/advisories/GHSA-xvfx-w463-6fpp) |
| [CVE-2026-32808](https://www.cve.org/CVERecord?id=CVE-2026-32808) | pyLoad | Path traversal and deletion (co-reported) | [Source](https://github.com/pyload/pyload/security/advisories/GHSA-7g4m-8hx2-4qh3) |
| [CVE-2026-32936](https://www.cve.org/CVERecord?id=CVE-2026-32936) | CoreDNS | Unauthenticated DoH resource amplification | [Source](https://github.com/coredns/coredns/security/advisories/GHSA-63cw-r7xf-jmwr) |
| [CVE-2026-33491](https://www.cve.org/CVERecord?id=CVE-2026-33491) | Zen C | Stack overflow in identifier mangling | [Source](https://github.com/zenc-lang/zenc/security/advisories/GHSA-rv74-w6q7-h8xr) |
| [CVE-2026-34601](https://www.cve.org/CVERecord?id=CVE-2026-34601) | xmldom | CDATA serialization and XML structure injection | [Source](https://github.com/xmldom/xmldom/security/advisories/GHSA-wh4c-j3r5-mjhp) |
| [CVE-2026-35191](https://www.cve.org/CVERecord?id=CVE-2026-35191) | OpenSSL | QUIC unvalidated anti-amplification accounting (independent reports) | [Source](https://openssl-library.org/news/secadv/20260929.txt) |
| [CVE-2026-39360](https://www.cve.org/CVERecord?id=CVE-2026-39360) | RustFS | Missing source authorization for multipart copy | [Source](https://github.com/advisories/GHSA-mx42-j6wv-px98) |
| [CVE-2026-43895](https://www.cve.org/CVERecord?id=CVE-2026-43895) | jq | Import-path NUL trust boundary | [Source](https://github.com/jqlang/jq/security/advisories/GHSA-7q7g-mrq3-phxr) |
| [CVE-2026-44240](https://www.cve.org/CVERecord?id=CVE-2026-44240) | basic-ftp | Unbounded multiline FTP response buffering | [Source](https://github.com/advisories/GHSA-rpmf-866q-6p89) |
| [CVE-2026-44724](https://www.cve.org/CVERecord?id=CVE-2026-44724) | systeminformation | Command injection in NetworkManager names | [Source](https://github.com/sebhildebrandt/systeminformation/security/advisories/GHSA-hvx9-hwr7-wjj9) |
| [CVE-2026-45539](https://www.cve.org/CVERecord?id=CVE-2026-45539) | Microsoft APM | Symlink disclosure during remote package installation | [Source](https://github.com/microsoft/apm/security/advisories/GHSA-q5pp-gvjg-h7v4) |
| [CVE-2026-45784](https://www.cve.org/CVERecord?id=CVE-2026-45784) | rust-openssl | Heap out-of-bounds write in AES-KW-PAD binding | [Source](https://github.com/advisories/GHSA-phqj-4mhp-q6mq) |
| [CVE-2026-48525](https://www.cve.org/CVERecord?id=CVE-2026-48525) | PyJWT | Detached JWS resource amplification | [Source](https://github.com/jpadilla/pyjwt/security/advisories/GHSA-w7vc-732c-9m39) |
| [CVE-2026-54568](https://www.cve.org/CVERecord?id=CVE-2026-54568) | Microsoft UFO | Device-system-information authorization bypass | [Source](https://github.com/microsoft/UFO/security/advisories/GHSA-hc27-j4p9-qm2x) |
| [CVE-2026-59896](https://www.cve.org/CVERecord?id=CVE-2026-59896) | Hono | Shared JSX context / request-state leakage | [Source](https://github.com/honojs/hono/security/advisories/GHSA-hvrm-45r6-mjfj) |
| [CVE-2026-61371](https://www.cve.org/CVERecord?id=CVE-2026-61371) | Microsoft AVML | Symlink-following output and truncation | [Source](https://github.com/microsoft/avml/pull/754) |
| [CVE-2026-62291](https://www.cve.org/CVERecord?id=CVE-2026-62291) | libheif | Out-of-bounds heap write in uncompressed encoder | [Source](https://ubuntu.com/security/notices/USN-8683-1) |
| [CVE-2026-67320](https://www.cve.org/CVERecord?id=CVE-2026-67320) | Axios | Proxy behavior inherited via prototype chain | [Source](https://github.com/advisories/GHSA-gcfj-64vw-6mp9) |
| [CVE-2026-68930](https://www.cve.org/CVERecord?id=CVE-2026-68930) | Russh | Expired channel lifecycle / authorization-state error | [Source](https://github.com/advisories/GHSA-m65r-rprj-r5rg) |
| [CVE-2026-70622](https://www.cve.org/CVERecord?id=CVE-2026-70622) | tar-rs | Archive path/symlink escape | [Source](https://www.cve.org/CVERecord?id=CVE-2026-70622) |
| [CVE-2026-82457](https://www.cve.org/CVERecord?id=CVE-2026-82457) | su-exec | UID number truncation / privilege boundary | [Source](https://www.vulncheck.com/advisories/su-exec-through-0.3-privilege-escalation-via-numeric-user-id) |
| [CVE-2026-85091](https://www.cve.org/CVERecord?id=CVE-2026-85091) | zlib | gz_vacate heap out-of-bounds write | [Source](https://ubuntu.com/security/notices/USN-8954-1) |
| [CVE-2026-85092](https://www.cve.org/CVERecord?id=CVE-2026-85092) | LiME | Symlink overwrite at output creation | [Source](https://www.vulncheck.com/advisories/lime-through-1.12.0-arbitrary-file-overwrite-via-symlink-following) |
| [CVE-2026-89146](https://www.cve.org/CVERecord?id=CVE-2026-89146) | rust-libp2p rendezvous | Timer/TTL overflow denial of service | [Source](https://github.com/advisories/GHSA-gh9c-4324-26cm) |
| [CVE-2026-89147](https://www.cve.org/CVERecord?id=CVE-2026-89147) | Net-SNMP | SMUX unauthenticated blocking read / DoS | [Source](https://github.com/net-snmp/net-snmp/issues/1134) |
| [CVE-2026-92956](https://www.cve.org/CVERecord?id=CVE-2026-92956) | vm2 | Host-realm Promise sandbox escape (co-reported) | [Source](https://github.com/advisories/GHSA-wjwh-qqvp-g4p4) |
| [CVE-2026-93657](https://www.cve.org/CVERecord?id=CVE-2026-93657) | Hickory DNS | DNSSEC bogus state suppressed in resolver API | [Source](https://github.com/advisories/GHSA-5j98-2g5x-46v6) |
| [CVE-2026-93658](https://www.cve.org/CVERecord?id=CVE-2026-93658) | uutils coreutils | setuid install sequencing and ownership failure | [Source](https://github.com/uutils/coreutils/security/advisories/GHSA-cgg3-923w-v53m) |
| [CVE-2026-100394](https://www.cve.org/CVERecord?id=CVE-2026-100394) | Nezha | Authenticated member-triggered instance-wide DoS | [Source](https://github.com/advisories/GHSA-qjpp-gffx-2wm9) |
| [CVE-2026-105299](https://www.cve.org/CVERecord?id=CVE-2026-105299) | Cloudflare Pingora | Hop-by-hop header trust boundary | [Source](https://github.com/cloudflare/pingora/security/advisories/GHSA-vx4q-2c55-cvmg) |
| [CVE-2026-106484](https://www.cve.org/CVERecord?id=CVE-2026-106484) | Chrome DevTools MCP | Path rewrite after MCP roots validation | [Source](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/106xxx/CVE-2026-106484.json) |

## 2025

| CVE | Project | Specific failure mode | Source / attribution trail |
| --- | --- | --- | --- |
| [CVE-2025-13437](https://www.cve.org/CVERecord?id=CVE-2025-13437) | Google zx | External node_modules deletion via cleanup alias | [Source](https://github.com/google/zx/pull/1349) |
| [CVE-2025-59716](https://www.cve.org/CVERecord?id=CVE-2025-59716) | ownCloud Guests | Unauthenticated pending-guest enumeration | [Source](https://www.cve.org/CVERecord?id=CVE-2025-59716) |
| [CVE-2025-59717](https://www.cve.org/CVERecord?id=CVE-2025-59717) | DigitalOcean do-markdownit | Allowed classes type confusion | [Source](https://github.com/thesmartshadow/writeup) |
| [CVE-2025-63095](https://www.cve.org/CVERecord?id=CVE-2025-63095) | Tempus Ex hello-video-codec | BitstreamWriter input-triggered denial of service | [Source](https://www.cve.org/CVERecord?id=CVE-2025-63095) |
| [CVE-2025-67124](https://www.cve.org/CVERecord?id=CVE-2025-67124) | miniserve | Symlink race in upload finalization | [Source](https://www.cve.org/CVERecord?id=CVE-2025-67124) |
| [CVE-2025-67125](https://www.cve.org/CVERecord?id=CVE-2025-67125) | docopt.cpp | Signed counter overflow | [Source](https://github.com/docopt/docopt.cpp/pull/168) |

## Reports published without a CVE

| Record | Project | Evidence / counting rule |
| --- | --- | --- |
| [GO-2026-4950](https://pkg.go.dev/vuln/GO-2026-4950) | fasthttp | Official Go Vulnerability Database credit to Ali Firas, with upstream fix in 1.70.0; **not a CVE**. |
| [GHSA-hfq4-89cf-8p8j](https://github.com/cisagov/manage.get.gov/security/advisories/GHSA-hfq4-89cf-8p8j) | CISA manage.get.gov | Security advisory and authorization fix; **not counted as a CVE**. |

## Withdrawn identifier

[CVE-2026-82455](https://www.cve.org/CVERecord?id=CVE-2026-82455) was rejected after RubyGems maintainers declined the security classification. The code change in [RubyGems #9493](https://github.com/ruby/rubygems/pull/9493) was merged. I'm not counting the withdrawn identifier as a published vulnerability.

## Notes on credit

OpenSSL [CVE-2026-35191](https://openssl-library.org/news/secadv/20260929.txt) records my report and a later independent report by Nikolas Gauder. Neil Horman wrote the fix. I did not write the upstream OpenSSL patch.

The Linux [`599d0e97610f`](https://github.com/torvalds/linux/commit/599d0e97610f09162d84c4ede4164628c066921e) change is my authored, merged patch. The rest of the related seven-patch series has a different status.

For [fasthttp GO-2026-4950](https://pkg.go.dev/vuln/GO-2026-4950), I reported the issue. The maintainer authored [PR #2163](https://github.com/valyala/fasthttp/pull/2163).

vm2 and pyLoad were co-discoveries. Ubuntu's two libheif notices cover the same CVE. Chrome DevTools MCP's [CVE-2026-106484](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/106xxx/CVE-2026-106484.json) was assigned by Chrome CNA.

## lldpd

The [lldpd out-of-bounds read advisory](https://github.com/lldpd/lldpd/security/advisories/GHSA-jmrh-hxvj-p42g) is referenced by [Debian's 1.0.23-1 upload](https://tracker.debian.org/news/1815479/accepted-lldpd-1023-1-source-into-unstable/). I have not confirmed the reporter field from the original advisory in this audit, so this stays outside the attributed CVE list.
