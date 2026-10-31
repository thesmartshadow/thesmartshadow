# Source and patch record - Ali Firas (thesmartshadow)

**Evidence cut-off:** 2026-10-31. Original notices and upstream identity were rechecked for OpenSSL, cpp-httplib, fasthttp, libheif, Linux, and Chrome. Other rows retain the earlier audit scope. Consult [RESEARCH-INDEX.md](RESEARCH-INDEX.md) for the wider published record; do not infer a global CVE total from the number of notices.

**Interpretation:** `Reporter` means a published record credits the researcher. `Author` means the PR is authored by the researcher. `Merged` is verified separately. `Tracker` means a distro assessed or listed the CVE; it is not necessarily an issued update, a vulnerable product, or a credit to the reporter.

## 1. Kernel source contribution

| Record | Attribution and scope | Status |
| --- | --- | --- |
| [Linux mainline `599d0e97610f`](https://github.com/torvalds/linux/commit/599d0e97610f09162d84c4ede4164628c066921e) · [net-next commit](https://git.kernel.org/netdev/net-next/c/599d0e97610f) | `vxlan: vnifilter: validate the VXLAN_VNIFILTER_ENTRY nest`; commit author **Ali Firas**, committer **Jakub Kicinski**; `NLA_POLICY_NESTED()` prevents partial application of a request containing policy-invalid entries. | **Merged**; verified directly in `torvalds/linux`. Committer timestamp: 2026-10-21 UTC. |
| [net-next v4 0/7 - VXLAN vnifilter](https://patchew.org/linux/20261014123814.388557-1-alishmery18%40gmail.com/) | Ali Firas's seven-patch series; VNI bounds, dump/replay, memcg charges, and selftests. [Upstream acceptance bot](https://lists.openwall.net/linux-kernel/2026/10/21/37) | **Patch 1/7 merged** as above; patches **2-7 have no matching commits** in the acceptance notice. Do not count all seven as merged. |

## 2. Primary security advisories and first-party reports

| Project | Original record / credit | Notes |
| --- | --- | --- |
| Chrome DevTools MCP | [Maintainer GHSA-5hw5-4q87-m6x9](https://github.com/ChromeDevTools/chrome-devtools-mcp/security/advisories/GHSA-5hw5-4q87-m6x9) · [Chrome CNA CVE-2026-106484](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/106xxx/CVE-2026-106484.json) | GHSA credits `thesmartshadow` Reporter. Chrome CNA `assignerShortName: Chrome`; published 2026-10-28. Version 1.1.0-<1.5.0. Real MCP reproduction, roots bypass via extension rewrite after path validation. GHSA "No known CVE" field is older than published CVE. |
| OpenSSL | [OpenSSL advisory (29 Sep 2026)](https://openssl-library.org/news/secadv/20260929.txt) · [official vulnerabilities ledger](https://openssl-library.org/news/vulnerabilities/) | **CVE-2026-35191**, QUIC 3× anti-amplification accounting. **Ali Firas reported 13 Jun 2026**; Nikolas Gauder reported independently 22 Aug 2026; Neil Horman authored vendor fix. Low severity, modes without client-address validation, fixes 3.5.9 / 3.6.5 / 4.0.3. Distinct from rust-openssl memory-safety CVE. |
| libheif | [GHSA-xpw3-9rhw-482x](https://github.com/strukturag/libheif/security/advisories/GHSA-xpw3-9rhw-482x) · [USN-8683-1](https://ubuntu.com/security/notices/USN-8683-1) · [USN-8774-1](https://ubuntu.com/security/notices/USN-8774-1) | **CVE-2026-62291**, heap out-of-bounds write; two Ubuntu notices name Ali Firas. |
| cpp-httplib | [Maintainer GHSA-xvfx-w463-6fpp](https://github.com/yhirose/cpp-httplib/security/advisories/GHSA-xvfx-w463-6fpp) | **CVE-2026-28435**, compressed/decompressed payload budget bypass in streaming `ContentReader`. Maintainer credits `thesmartshadow` reporter; fixed 0.35.0. |
| fasthttp | [Go vulnerability GO-2026-4950](https://pkg.go.dev/vuln/GO-2026-4950) · [fix PR #2163](https://github.com/valyala/fasthttp/pull/2163) | **No CVE assigned in this audit.** Go DB credits Ali Firas (thesmartshadow); double-decoding auth bypass in ServeFile/ServeFS, fixed 1.70.0. PR #2163 author was `erikdubbelboer`, not Ali Firas. |
| Hickory DNS | [GHSA-5j98-2g5x-46v6](https://github.com/advisories/GHSA-5j98-2g5x-46v6) · [VulnCheck CNA record](https://www.cve.org/CVERecord?id=CVE-2026-93657) | **CVE-2026-93657**, failure to propagate bogus DNSSEC validation states; CNA explicitly credits Ali Firas. |
| uutils coreutils | [GHSA-cgg3-923w-v53m](https://github.com/uutils/coreutils/security/advisories/GHSA-cgg3-923w-v53m) · [VulnCheck CNA record](https://www.cve.org/CVERecord?id=CVE-2026-93658) | **CVE-2026-93658**, `install` ownership/mode sequencing with setuid risk; CNA credits Ali Firas. [Fix PR #13629](https://github.com/uutils/coreutils/pull/13629) merged, authored by another developer. |
| Nezha | [GHSA-qjpp-gffx-2wm9](https://github.com/advisories/GHSA-qjpp-gffx-2wm9) | **CVE-2026-100394**, dashboard process DoS; GitHub credits `thesmartshadow` reporter. |
| Cloudflare Pingora | [Maintainer GHSA-vx4q-2c55-cvmg](https://github.com/cloudflare/pingora/security/advisories/GHSA-vx4q-2c55-cvmg) · [RustSec](https://rustsec.org/advisories/RUSTSEC-2026-0390.html) | Credits `thesmartshadow`; CVE-2026-105299. Fix 0.9.0. Restricted deployment conditions; CDN customers not affected per Cloudflare. |
| zlib | [Ubuntu USN-8954-1](https://ubuntu.com/security/notices/USN-8954-1) · [research gist](https://gist.github.com/thesmartshadow/e0b9481792afb7c31e86fee1ff084490) | Ubuntu names `Ali Firas`; CVE-2026-85091. |
| vm2 | [GHSA-wjwh-qqvp-g4p4](https://github.com/advisories/GHSA-wjwh-qqvp-g4p4) | CVE-2026-92956; credits `thesmartshadow` **and** `zolbooo`. Proven with Node.js 26 under reported conditions. |
| xmldom | [Maintainer GHSA-wh4c-j3r5-mjhp](https://github.com/xmldom/xmldom/security/advisories/GHSA-wh4c-j3r5-mjhp) | CVE-2026-34601; reporter credit. |
| rust-openssl | [GHSA-phqj-4mhp-q6mq](https://github.com/advisories/GHSA-phqj-4mhp-q6mq) | CVE-2026-45784; reporter credit. Specific AES-KW-PAD behavior. |
| CoreDNS | [Maintainer advisory](https://github.com/coredns/coredns/security/advisories/GHSA-63cw-r7xf-jmwr) | CVE-2026-32936; credits reporter. Fix in 1.14.3. |
| CISA manage.get.gov | [Maintainer advisory](https://github.com/cisagov/manage.get.gov/security/advisories/GHSA-hfq4-89cf-8p8j) · [fix #5049](https://github.com/cisagov/manage.get.gov/pull/5049) | Authorization report; distinguish reported vulnerability from patch authorship. |
| Microsoft APM | [Maintainer advisory](https://github.com/microsoft/apm/security/advisories/GHSA-q5pp-gvjg-h7v4) | CVE-2026-45539; reporter credit. |
| Rack | [Maintainer advisory](https://github.com/rack/rack/security/advisories/GHSA-whrj-4476-wvmp) · [Ubuntu notice naming reporter](https://ubuntu.com/security/notices/USN-8066-1) | CVE-2026-25500. |
| RustFS | [GitHub Advisory Database](https://github.com/advisories/GHSA-mx42-j6wv-px98) | CVE-2026-39360, multipart copy authorization. |
| pyLoad | [Maintainer advisory](https://github.com/pyload/pyload/security/advisories/GHSA-7g4m-8hx2-4qh3) | CVE-2026-32808; **joint discovery with Ali Al-Akbar**. |
| systeminformation | [Maintainer advisory](https://github.com/sebhildebrandt/systeminformation/security/advisories/GHSA-hvx9-hwr7-wjj9) | CVE-2026-44724; NetworkManager profile name reaching shell. |
| Net-SNMP | [Issue #1134, reporter text and maintainer fix](https://github.com/net-snmp/net-snmp/issues/1134) | CVE-2026-89147; requires SMUX initialized and listener reachable; stock Debian service disables SMUX at runtime. |
| libp2p-rendezvous | [GHSA-gh9c-4324-26cm](https://github.com/advisories/GHSA-gh9c-4324-26cm) · [research gist](https://gist.github.com/thesmartshadow/25ef03f7ebbd12118a9d27695c885989) | CVE-2026-89146; TTL-triggered timer overflow. |

### Additional first-party or researcher-linked publication leads

These are supplementary references to published research, not an assertion that each vendor has merged a patch. In particular, unreviewed GitHub advisories and CNA records require checking current product status before quoting them as maintainer security announcements.

| Finding | Evidence link | Caveat |
| --- | --- | --- |
| su-exec · CVE-2026-82457 | [CNA-linked technical report](https://gist.github.com/thesmartshadow/ed96e2a88643c34a247c9b7cf9e311be) · [VulnCheck](https://www.vulncheck.com/advisories/su-exec-through-0.3-privilege-escalation-via-numeric-user-id) | Numeric identifier truncation; source record credits Ali Firas. |
| LiME · CVE-2026-85092 | [CNA-linked technical report](https://gist.github.com/thesmartshadow/5355949144749b431da41490b63598f5) · [VulnCheck](https://www.vulncheck.com/advisories/lime-through-1.12.0-arbitrary-file-overwrite-via-symlink-following) | Symlink-following acquisition destination; requires specific permissions/conditions. |
| uutils coreutils · CVE-2026-93658 | [Ubuntu CVE assessment](https://ubuntu.com/security/CVE-2026-93658) | Tracker, **not** evidence of an issued Ubuntu security notice. |
| Axios · CVE-2026-67320 | [GHSA-gcfj-64vw-6mp9](https://github.com/advisories/GHSA-gcfj-64vw-6mp9) | Requires prototype pollution plus interceptor cloning; not a universal request vulnerability. |
| Russh · CVE-2026-68930 | [GHSA-m65r-rprj-r5rg](https://github.com/advisories/GHSA-m65r-rprj-r5rg) | Authenticated caller; **not** an SSH login bypass. |
| Microsoft AVML · CVE-2026-61371 | [Researcher's technical report](https://gist.github.com/thesmartshadow/2d099071f847de8db3dc4bbaf4dfa6df) · [Microsoft fix #754](https://github.com/microsoft/avml/pull/754) | Discoverer credit is distinct from author of vendor fix #754. |
| jq · CVE-2026-43895 | [GHSA-7q7g-mrq3-phxr](https://github.com/jqlang/jq/security/advisories/GHSA-7q7g-mrq3-phxr) · [Ubuntu tracker](https://ubuntu.com/security/CVE-2026-43895) | Import path NUL handling; dependency-specific. |
| DigitalOcean do-markdownit · CVE-2025-59717 | [Researcher's write-up](https://github.com/thesmartshadow/writeup) · [Maintainer PR #152](https://github.com/digitalocean/do-markdownit/pull/152) | Proposed fix #152 was open at audit; avoid labelling accepted. |
| ownCloud Guests · CVE-2025-59716 | [Technical research report](https://gist.github.com/thesmartshadow/64ae0449e909174d0479a4f23657147f) · [PR #661](https://github.com/owncloud/guests/pull/661) | PR open at audit. |
| docopt.cpp · CVE-2025-67125 | [Technical research report](https://gist.github.com/thesmartshadow/672afe8828844c833f46f8ebe2f5f3bd) · [PR #168](https://github.com/docopt/docopt.cpp/pull/168) | PR open at audit. |

## 3. Downstream distribution updates, tracking, and corporate bulletins

| Original finding | Evidence | Record type and caution |
| --- | --- | --- |
| OpenSSL / CVE-2026-35191 | [OpenSSL advisory](https://openssl-library.org/news/secadv/20260929.txt) | **First-party discoverer credit**, independently verified; do not conflate severity Low with broader multi-CVE advisory severity. |
| OpenSSL / CVE-2026-35191 | [Ubuntu USN-8847-1](https://ubuntu.com/security/notices/USN-8847-1) | **Shipped Ubuntu notice**, CVE specifically affected **Ubuntu 26.04 LTS** within this notice. |
| OpenSSL / CVE-2026-35191 | [Debian DSA-6531-1](https://lists.debian.org/debian-security-announce/2026/msg00444.html) | **Shipped Debian security advisory** for affected trixie package. |
| OpenSSL / CVE-2026-35191 | [SUSE-SU-2026:24245-1](https://www.suse.com/support/update/announcement/2026/suse-su-202624245-1/) | **Shipped SUSE product security update** listing this CVE. |
| libheif / CVE-2026-62291 | [Ubuntu USN-8683-1](https://ubuntu.com/security/notices/USN-8683-1) | **Shipped Ubuntu notice**, names Ali Firas, CVE scope affects 24.04 LTS. |
| libheif / CVE-2026-62291 | [Ubuntu USN-8774-1](https://ubuntu.com/security/notices/USN-8774-1) | **Another shipped Ubuntu notice**, names Ali Firas, 26.04 LTS. Same finding; no double counting. |
| cpp-httplib / CVE-2026-28435 | [Debian tracker](https://security-tracker.debian.org/tracker/CVE-2026-28435) | **Distro tracker**, not a shipped DSA in this register. |
| zlib / CVE-2026-85091 | [Ubuntu USN-8954-1](https://ubuntu.com/security/notices/USN-8954-1) | **Shipped Ubuntu security notice**; directly names Ali Firas; 2026-10-22. |
| zlib / CVE-2026-85091 | [Debian security tracker](https://security-tracker.debian.org/tracker/CVE-2026-85091) · [Debian bug #1146895](https://bugs.debian.org/1146895) | **Distribution tracking/patching**, not a claim that every Debian suite is affected. Affected-range discussion remains important. |
| zlib / CVE-2026-85091 | [SUSE CVE assessment](https://www.suse.com/security/cve/CVE-2026-85091.html) | SUSE lists many products **not affected**. Do not describe the CVE page as a shipped zlib fix in those products. |
| Rack / CVE-2026-25500 | [Ubuntu USN-8066-1](https://ubuntu.com/security/notices/USN-8066-1) | **Shipped Ubuntu security notice**; names Ali Firas; 2026-02-26. |
| Rack / CVE-2026-25500 | [Debian DSA-6180-1](https://lists.debian.org/debian-security-announce/2026/msg00089.html) · [Debian tracker](https://security-tracker.debian.org/tracker/CVE-2026-25500) | **Shipped Debian security advisory**; 2026-03-26. |
| Rack / CVE-2026-25500 | [SUSE security tracker](https://www.suse.com/security/cve/CVE-2026-25500.html) | **Product impact and update status**; interpret states per product. |
| xmldom / CVE-2026-34601 | [IBM Cloud Pak for Integration bulletin](https://www.ibm.com/support/pages/security-bulletin-automation-assets-ibm-cloud-pak-integration-vulnerable-vulnerability-xmldom) | **IBM product-specific security bulletin**. |
| xmldom / CVE-2026-34601 | [IBM Maximo bulletin](https://www.ibm.com/support/pages/security-bulletin-ibm-maximo-application-suite-visual-inspection-component-uses-xmldom-which-vulnerable-cve-2026-34601) | **IBM product-specific security bulletin**. |
| xmldom / CVE-2026-34601 | [Red Hat assessment](https://access.redhat.com/security/cve/cve-2026-34601) · [Debian tracker](https://security-tracker.debian.org/tracker/CVE-2026-34601) · [Ubuntu CVE page](https://ubuntu.com/security/CVE-2026-34601) | **Vendor/distribution assessments**, not automatically shipped advisories. |
| rust-openssl / CVE-2026-45784 | [SUSE tracker and SUSE-SU references](https://www.suse.com/security/cve/CVE-2026-45784.html) · [Red Hat assessment](https://access.redhat.com/security/cve/cve-2026-45784) | **SUSE security updates for specified packages and Red Hat analysis**. Red Hat presence alone does not establish that its software is affected. |
| jq / CVE-2026-43895 | [Ubuntu CVE page](https://ubuntu.com/security/CVE-2026-43895) | **CVE tracker** (not a USN in this evidence). |

## 4. Directly authored and merged upstream contributions

Statuses checked against GitHub PR metadata on 2026-10-31.

| PR | Status | Merged at (UTC) |
| --- | --- | --- |
| [torvalds/linux `599d0e97610f`](https://github.com/torvalds/linux/commit/599d0e97610f09162d84c4ede4164628c066921e) | **Merged mainline** | 2026-10-21 |
| [ruby/rubygems #9493](https://github.com/ruby/rubygems/pull/9493) | Merged | 2026-05-26 |
| [cel-expr/cel-go #1302](https://github.com/cel-expr/cel-go/pull/1302) | Merged | 2026-05-19 |
| [google/zx #1349](https://github.com/google/zx/pull/1349) | Merged | 2025-10-14 |
| [akamai/cli #227](https://github.com/akamai/cli/pull/227) | Merged | 2026-10-09 |
| [ruby/json #948](https://github.com/ruby/json/pull/948) | Merged | 2026-03-06 |
| [google/humanio #4](https://github.com/google/humanio/pull/4) | Merged | 2025-10-22 |
| [seanmonstar/httparse #217](https://github.com/seanmonstar/httparse/pull/217) | Merged (documentation) | 2026-02-05 |

**Submitted but not merged / not to be labelled accepted patches:** [zlib #1317](https://github.com/madler/zlib/pull/1317) (closed unmerged); [microsoft/avml #763](https://github.com/microsoft/avml/pull/763) (closed unmerged); [digitalocean/do-markdownit #152](https://github.com/digitalocean/do-markdownit/pull/152) (open as checked); [docopt/docopt.cpp #168](https://github.com/docopt/docopt.cpp/pull/168) (open as checked).


## 5. Limits and unresolved attribution

- **CVE-2026-82455 (RubyGems) - rejected CVE record.** [Ubuntu's CVE page](https://ubuntu.com/security/CVE-2026-82455) describes the rejected status and maintainer disagreement with the security classification. The [merged RubyGems patch #9493](https://github.com/ruby/rubygems/pull/9493) remains a legitimate engineering contribution, but the rejected CVE should **not** be counted as an active accepted vulnerability.
- The GitHub profile README, `data/cves.txt`, GitHub advisory credit search, and personal research site cover different subsets of work. **Do not advertise an unverified global CVE count** until records are deduplicated and rejected/reserved IDs excluded.
- Linux kernel **patch 1/7 was merged into mainline**, confirmed by `torvalds/linux` commit `599d0e97610f`. The netdev application notice has no matching commits for patches 2-7; do not count those as merged.
- Chrome CNA's published `CVE-2026-106484` references `GHSA-5hw5-4q87-m6x9`, which credits `thesmartshadow`. The GHSA's older "No known CVE" display should not be treated as disproof of the later CNA record.
- A vendor security tracker is not synonymous with a vendor security bulletin or a fix. Use exact evidence type when writing about Red Hat, Ubuntu, Debian, Microsoft, IBM, and SUSE.
- Do not infer exploitation, universal product impact, or downstream reach from downloads or transitive dependency presence alone.

- **OpenSSL vs rust-openssl:** the upstream OpenSSL QUIC accounting vulnerability and the separate Rust OpenSSL bindings buffer-overflow finding must not be merged or described as one disclosure. The OpenSSL vendor names the discoverer and the separate fix author.
- **Multi-CVE distribution notices:** Ubuntu USN-8847-1 covers multiple CVEs; only CVE-2026-35191 is attributed to this researcher in this register, and the notice itself does not establish reporter credit.
- **fasthttp GO-2026-4950:** independently published security record with direct credit, but **not** counted as a CVE.
- **libheif:** Ubuntu issued two notices addressing one CVE across different Ubuntu releases; do not count as multiple vulnerabilities.

## 6. Advisory awaiting reporter-credit confirmation

- [lldpd GHSA-jmrh-hxvj-p42g](https://github.com/lldpd/lldpd/security/advisories/GHSA-jmrh-hxvj-p42g) - [Debian 1.0.23-1 upload changelog (26 Oct 2026)](https://tracker.debian.org/news/1815479/accepted-lldpd-1023-1-source-into-unstable/) confirms an upstream release shipped a fix for this out-of-bounds read. The maintainer advisory's reporter-credit field could not be independently retrieved in this audit. Keep credit conditional and do not invent a CVE.