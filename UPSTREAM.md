# Upstream

Ali Firas - `thesmartshadow`

Merged changes in the Linux kernel and externally maintained projects. The links lead to the actual commits or pull requests.

## Linux kernel

### VXLAN VNI-filter validation

**[`599d0e97610f` - vxlan: vnifilter: validate the VXLAN_VNIFILTER_ENTRY nest](https://github.com/torvalds/linux/commit/599d0e97610f09162d84c4ede4164628c066921e)**

`vxlan_vnifilter_process()` parsed a nested VNI-filter request while applying entries one at a time. Without a nested attribute policy at the outer level, an invalid later entry could cause an error after an earlier entry had already been installed and announced by `RTM_NEWTUNNEL`.

`NLA_POLICY_NESTED()` now connects `VXLAN_VNIFILTER_ENTRY` to `vni_filter_entry_policy`. Policy validation precedes entry dispatch, preventing policy-invalid attributes from causing that partial side effect.

`net-next` -> `torvalds/linux`  
[Commit](https://github.com/torvalds/linux/commit/599d0e97610f09162d84c4ede4164628c066921e) · [Series and review](https://lore.kernel.org/netdev/20261014123814.388557-1-alishmery18@gmail.com/)

Related VXLAN VNIFILTER work addresses 24-bit VNI bounds, capped request expansion, dump behavior, allocation and memcg accounting, FDB lifetime, and networking selftests. The kernel code path requires attention to GFP context, object lifetime and locking rather than only choosing an accounting flag.

## Accepted changes

### [RubyGems - #9493](https://github.com/ruby/rubygems/pull/9493)

Archive extraction could be redirected outside the destination by symlinks already present in the filesystem. Resolve and constrain the output path under `destination_dir` before writing, with regression coverage for the symlink case.

### [Google zx - #1349](https://github.com/google/zx/pull/1349)

`--prefer-local` cleanup followed an unsafe ownership assumption when dealing with external `node_modules` paths. Correct alias handling and symlink cleanup so the command does not remove targets outside its scope.

### [CEL-Go - #1302](https://github.com/cel-expr/cel-go/pull/1302)

Move the expression-size limit ahead of source-buffer construction. An oversized expression is rejected before the memory and parsing work that the limit was intended to bound.

### [Akamai CLI - #227](https://github.com/akamai/cli/pull/227)

Validate package command identifiers before they are used to construct output paths. Treat command metadata as untrusted path input.

### [Ruby JSON - #948](https://github.com/ruby/json/pull/948)

Reject negative generator depth at the native boundary instead of passing invalid state into the generator.

### [Google HumanIO - #4](https://github.com/google/humanio/pull/4)

Close accidental access to `/server.js` and replace a source-embedded service token with environment configuration.

### [httparse - #217](https://github.com/seanmonstar/httparse/pull/217)

Document the resource costs of retrying `Partial` on progressively growing buffers in streaming parser loops.

[Main profile](README.md) · [Research](RESEARCH.md)