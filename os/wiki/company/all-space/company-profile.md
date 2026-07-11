---
type: entity
created: 2026-07-10
updated: 2026-07-10
tags: [company, all-space, york, product, hydra, esa, satcom, acquisition]
sources: [../../../raw/competitors/2026-07-10-competitive-landscape-research.md]
---

# All.Space: comprehensive company profile

> **As of:** 2026-07-10. Confidence markers: (V) verified against a cited public source, (A) owner-attested, (I) inferred/analytical. Full sourcing in the [research log](../../../raw/competitors/2026-07-10-competitive-landscape-research.md).

## Snapshot

All.Space (formerly Isotropic Systems) builds the Hydra range of multi-link, multi-orbit, electronically steered satellite terminals using a proprietary lens-array beamforming architecture. As of 2026-07-08 it is a wholly owned subsidiary of York Space Systems. Its defining claim is the only terminal that maintains simultaneous, full-duplex connections to two or more independent satellites across different orbits and bands from a single aperture, with inherent anti-jam resilience for contested environments. (V)

## History

- **2013:** Founded as Isotropic Systems Ltd in Reading, England, by John Finney (ex-SES MEO executive) and Jeremiah "Jeremy" Turpin (Chief Scientist), to solve multi-orbit ground-segment connectivity. (V)
- **2013-2022:** Delivered development programs with the European Space Agency, UK Space Agency, UK MOD, and US DoD. Raised progressively from SES (lead), Boeing HorizonX, UK Future Fund, UK Space Agency, Orbital Ventures, Space Angels, Firmament Ventures. (V)
- **2022-08-01:** Rebranded to All.Space (same legal entity) and unveiled its fifth-generation smart terminal. (V)
- **2023:** Delivered first terminal to SES for testing (early 2023); founder John Finney stepped down as CEO (~Sept 2023), succeeded by Paul McCarter (former COO); closed $44M Series C led by defense-focused Boka Group (total funding ~$160M+). (V)
- **2025:** Hydra 2 and Hydra MAX productized; certified on SES Ka-band GEO and O3b mPOWER Ka-band MEO. (V)
- **2026 (~June):** Redomiciled from the UK to the US; established a technical and manufacturing hub in Florence-Muscle Shoals, Alabama. (V)
- **2026-07-08:** York Space Systems acquisition closed. (V)

## The York Space Systems acquisition (closed 2026-07-08)

- **Terms:** ~$300M total (reduced from $355M announced late April 2026): ~$155M cash + 5.9M York common shares. All.Space operates as a wholly owned York subsidiary and continues as a merchant supplier to the wider industry. (V)
- **Acquirer:** York Space Systems (CEO Dirk Wallinger) builds spacecraft delivering tactical capabilities in theater, plus a Mission Operations Command and Control (C2) layer. York also acquired Orbion Space Technology (electric propulsion) in March 2026, part of a propulsion + communications + mission-operations roll-up strategy. (V)
- **Strategic rationale (stated):** combine All.Space's jam-resistant multi-link terminals with York's spacecraft infrastructure and C2 to form a "complete tactical ecosystem" delivering assured communications and positioning across space, land, air, and maritime in GPS-denied and jammed environments. Wallinger cited that in current conflicts high-bandwidth commercial SATCOM has been jammed so effectively that forces reverted to fiber; as unmanned systems scale, resilient comms + assured positioning become primary requirements. (V)
- **Implications (I):** US domicile + Alabama manufacturing removes the foreign-ownership barrier to US defense programs; York prime status opens pull-through onto York platforms and programs; All.Space gains balance-sheet stability after a capital-intensive decade; continues merchant sales so existing customer commitments remain intact (per McCarter). (V/I)

## Product: the Hydra Terminal Range

**Core architecture (V):** a proprietary multi-lens array performing RF/digital beamforming with patented dielectric lens technology (marketed as optical beamforming). Engineered dielectric lenses focus energy onto independent, electronically switchable feeds to form multiple high-gain beams with no moving parts (solid-state). The lens architecture provides inherent spatial filtering that rejects off-axis interference and jamming. Digital beamforming enables vector-based mono-pulse tracking above 400 Hz for high-integrity links under intense motion.

| Product | Key capability | Status |
|---------|----------------|--------|
| **Hydra 2** | Dual-link, Mil Ka + Comm Ka, two satellites across GEO and/or MEO simultaneously; 86 cm dia x 18 cm, 77 kg; Az 360 / El 20-90; pointing <0.1 deg in motion; 125 MHz Rx IBW/link; 3 swappable bays; certified SES Ka GEO + O3b mPOWER | Fielded (V) |
| **Hydra MAX** | World-first 500 MHz instantaneous bandwidth per beam (1 GHz aggregate) across comm+mil Ka; full-duplex on both beams simultaneously across full scan; integrated modems/tactical comms/edge compute; 86 cm on-the-move | Announced 2025; Gen 2 in 2026 (V) |
| **Hydra 4** | Hydra 2 base + Starlink (Ku) + Iridium (L) | Roadmap (V) |
| **Hydra KuKa** | Simultaneous Ka + Ku across all orbits | Roadmap (V) |
| **Hydra MAX 2** | Dual Ka (LEO+HEO+MEO+GEO) | 2027 (V) |

**Connectivity targets (V):** WGS, SES O3b mPOWER, Viasat 3 & GX, Amazon Kuiper/Leo, Telesat Lightspeed; network- and platform-agnostic (armored, naval, dismounted). MIL-STD engineered for cross-theater, multinational interoperability.

## Competitive advantages

1. **True simultaneous multi-link full-duplex** (transmit and receive on 2+ independent beams at once across the full scan range), not just orbit switching. Company claims this as unique. (V/I)
2. **Inherent anti-jam resilience** from lens-array spatial filtering: the central reason York valued the company for contested-environment operations. (V)
3. **No-penalty second beam on the same aperture** (A; consistent with the dual-lens architecture): dual full links without doubling apertures.
4. **Breadth of orbit/band coverage** (GEO/MEO/HEO/LEO; Mil+Comm Ka; adding Ku/L) from one device. (V)
5. **US defense prime backing** (York): spacecraft + C2 + propulsion ecosystem, US domicile, domestic manufacturing. (V/I)

## Vulnerabilities and risks

1. **SWaP-C premium:** at 77 kg / 86 cm, Hydra is heavier and likely costlier than flat-panel ESAs; strongest in the high-end tactical niche rather than volume mobility. (I)
2. **Merchant-model exposure:** Starlink withdrew third-party antenna support (mid-2025), forcing a pivot toward Amazon Leo/Kuiper Ka and WGS; vertically integrated constellations threaten the third-party terminal model. (A/I)
3. **Production scale:** later to volume than several competitors; execution risk as York scales demand. (I)
4. **Direct account pressure from Kymeta:** Kymeta is winning the same US Navy programs (NGC2, ONR via Bascom Hunter) All.Space targets. (V)

## Related

- [Threat ranking](../../competitors/threat-ranking.md) - the ten competitors ranked
- [Competitors section](../../competitors/README.md)
- [York Space Systems](../york/README.md)
- [Monitoring and automation](../../competitors/monitoring-and-automation.md)
