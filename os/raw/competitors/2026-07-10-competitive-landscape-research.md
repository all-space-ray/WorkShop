# Competitive landscape research log (2026-07-10)

> **Origin:** Web research conducted 2026-07-10 for the All.Space competitive intelligence effort.
> **Type:** research log / source capture
> **Status:** Immutable raw source. Every claim below carries its source; wiki pages distill and cite this.
> **Confidence marking:** V = verified against a cited public source; A = owner-attested; I = inferred/analytical.

## All.Space (subject company)

- Founded 2013 as Isotropic Systems Ltd (Reading, England); rebranded All.Space on 2022-08-01 (same legal entity). Founders John Finney and Jeremiah (Jeremy) Turpin. (V: all.space/about-us; SpaceNews 2022-08-01)
- ~$160M+ total funding since 2013; investors include SES (led rounds), Boeing (HorizonX), Boka Group (led Series C, defense-focused), AE Industrial Partners, Seraphim Space, Promus Ventures, Orbital Ventures, UK Future Fund, UK Space Agency grants. Series C: $44M, Oct 2023. (V: SpaceNews 2023-10-03, 2022-08-01; all.space 2021-02-08)
- Leadership: John Finney (founder, ex-SES MEO exec) stepped down as CEO ~Sept 2023; succeeded by Paul McCarter (ex-COO). Jeremy Turpin Chief Scientist & co-founder. (V: SpaceNews 2023-10-03; theorg.com)
- Delivered first terminal to SES for test ~early 2023; terminal certified on SES Ka-band GEO and O3b mPOWER Ka-band MEO. (V: Hydra 2 datasheet 2025-07)
- **York Space Systems acquisition CLOSED 2026-07-08.** Total ~$300M (down from $355M announced late April 2026): ~$155M cash + 5.9M York common shares. All.Space now a wholly owned York subsidiary, continues as merchant supplier. (V: Via Satellite 2026-07-08; Space & Defense; GovConWire 2026-07-09; SatNow)
- All.Space redomiciled UK -> US during the process (~June 2026); new technical/manufacturing hub in Florence-Muscle Shoals, Alabama. (V: Via Satellite 2026-07-08)
- York CEO Dirk Wallinger; York also acquired Orbion Space Technology (electric propulsion) March 2026. York builds spacecraft/tactical platforms + Mission Operations C2. Rationale: complete tactical ecosystem (resilient comms + positioning in contested/GPS-denied/jammed environments). (V: GovConWire; SatNow; Via Satellite)

### All.Space product (Hydra Terminal Range) (V: all.space datasheets/insights 2025)

- Architecture: proprietary multi-lens array performing RF digital beamforming with patented dielectric lens technology ("optical beamforming"); each lens pairs with independent electronically switchable feeds; no moving parts; solid-state. Inherent spatial filtering rejects off-axis interference/jamming. Analogy used by company: Lycurgus cup optical filtering. (V: all.space technical briefs)
- Hydra 2 (dual-link Ka): 2 full-duplex links, Mil Ka + Comm Ka, GEO and/or MEO simultaneous; future LEO Ka. 86cm dia x 18cm H, 77kg. Az 360, El 20-90. Pointing <0.1 deg with motion. Rx max IBW 125 MHz/link. 3 swappable multi-purpose bays (modems, RF-over-fiber, WiFi). Certified SES Ka GEO + O3b mPOWER; Viasat GX/HTS certification planned. MIL-STD ruggedized. (V: Hydra 2 datasheet 2025-07)
- Hydra MAX: world-first 500 MHz instantaneous bandwidth per beam = 1 GHz aggregate across comm+mil Ka; 86cm on-the-move; full duplex on BOTH beams simultaneously across full scan (differentiator: competitors only switch, don't do simultaneous dual full-duplex); digital beamforming mono-pulse tracking >400 Hz; integrated modems/tactical comms/edge compute; connects WGS, O3b mPOWER, Viasat 3 & GX, Amazon Kuiper, Telesat Lightspeed. (V: all.space Hydra MAX announcement)
- Roadmap: Hydra 4 (adds Starlink Ku + Iridium L to Hydra 2 base). Hydra KuKa (Ka+Ku simultaneous, all orbits). Hydra MAX Gen 2 available 2026; Hydra MAX 2 dual Ka (LEO+HEO+MEO+GEO) 2027. (V: Executive Briefing 2025-09)
- Positioning: "One device, all networks, no compromise"; only fully-capable multi-link terminal connecting simultaneously to all satellite + cellular networks. Government & defense focus; COTM land/sea; multinational interoperability. (V: all.space/about-us)

### Competitive advantages (I, grounded in V specs)

1. True simultaneous multi-link full-duplex (send+receive on 2+ independent beams at once), not just switching. Unique per company claims.
2. Lens-array beamforming gives inherent anti-jam spatial filtering (resilience in contested/EW environments) - the core York acquisition rationale.
3. No-penalty second beam on same aperture (owner-attested differentiator; consistent with dual-lens architecture).
4. Network + platform agnostic; broad orbit/band coverage (GEO/MEO/HEO/LEO, Mil+Comm Ka, adding Ku/L).
5. Now backed by a US defense prime (York) with spacecraft + C2 + propulsion; US-domiciled with Alabama manufacturing; solves foreign-ownership barriers to US defense sales.

### Vulnerabilities (I)

1. Higher SWaP/weight (77 kg, 86cm) and cost vs some flat panels; premium tactical niche.
2. Starlink dropped third-party antenna support (mid-2025) - hit the merchant-terminal model; drove pivot to Amazon Leo/Kuiper Ka + WGS. (A, from prior owner interviews; consistent with industry)
3. Later to volume production than some competitors; scaling risk.
4. Kymeta winning the same Navy programs (NGC2, ONR/Bascom Hunter) All.Space targets.

## Competitors (ESA / Ka-band weighted, ranked by threat)

### 1. Kymeta (Redmond, WA) - CRITICAL
- World-leading flat-panel ESA maker; founded 2012; metamaterial-based ("Intelligent Communications Platforms"); >150 patents. (V: Kymeta releases 2026-03)
- KuKa 8 Series: first multi-band (Ku 10.7-14.5 + Ka 17.7-31.0 GHz), multi-orbit (GEO/MEO/LEO/HEO), single-aperture flat-panel ESA; 4 concurrent beams (2 Tx + 2 Rx) from one metamaterial surface (demoed June 2025, TRL6); dims 35.4x35.4x3.9 in; prototypes mid-2026, commercial 2027; dual-modem. (V: Kymeta/GlobeNewswire/SatNews 2026-03-23)
- Wins: US Army NGC2 pilot multi-orbit SATCOM provider (Q3 2025); ONR contract via Bascom Hunter to deliver first single-antenna multi-band multi-orbit terminal, testing from Q2 2026 (SAME prime and Navy relationship as All.Space STtNG). (V: Kymeta 2026-04-14)
- New CEO Manny Mora (Nov 2025), 40-yr General Dynamics Mission Systems veteran, brought in to align to JADC2/DoD. (V: SatNews 2026-03-23)
- Threat: direct product overlap, winning the exact accounts, deeper DoD momentum, lower SWaP flat-panel form factor.

### 2. ThinKom Solutions (Hawthorne, CA) - HIGH
- VICTS (Variable Inclination Continuous Transverse Stub) - a steerable mechanically-actuated phased array; ultra-low-profile; any orbit. Established aviation IFC leader. (V: SpaceNews; ThinKom)
- ThinAir Ka2517 multi-orbit Ka on SES Open Orbits (MEO+GEO). Containerized Digital Array: software-defined multi-beam/multi-orbit/multi-band/multi-network (LEO/MEO/GEO/HEO), C/Ku/K/Ka(comm+mil)/Q now, more in dev; for contested environments. (V: ThinKom 2026)
- 2026 wins: $3.9M DoD portable ground stations (follow-on, Feb 2026); $1.9M SpaceWERX D2P2 containerized GEP for DAF (Jan 2026); portable gateway for dismounted forces. (V: ThinKom/SpaceNews 2026)
- Threat: proven, deployed at scale, multi-orbit, strong DoD + aero; but VICTS is mechanical-hybrid (not pure solid-state ESA) and single-beam-oriented.

### 3. CesiumAstro (Austin, TX) - HIGH
- Software-defined active phased arrays (Skylark, Vireo, Nightingale product lines); ~$470M combined equity+debt raised; scaling production. (V: CesiumAstro 2026)
- MDA GMD Weapon System IFICS large-aperture array (April 2026, Skylark expansion). Software-defined mobile-ready terminals; ground vehicles to airborne. (V: CesiumAstro 2026-04-21)
- Threat: true active phased array, very well funded, defense-scaling, adjacent into terminals; more payload/array heritage than mobility terminals to date.

### 4. Hanwha Phasor (London, UK; Hanwha Group Korea) - MEDIUM-HIGH
- A7700 AESA; multi-beam (two Rx beams - "fairly unique"), constellation-agnostic; Ku-band first (market entry ~2025), Ka planned via tech reuse; modular tiles scalable howitzer->ship->airliner. (V: EDR/RunwayGirl/battle-updates 2023-2024)
- Partnerships: Eutelsat OneWeb (LEO qualification), Kontron (power components), Lufthansa Technik (radomes + EASA/FAA STC; EASA Q3 2025, FAA Q4 2025), Plexus (manufacturing). (V: 2024)
- Threat: Hanwha defense backing + capital; aero-first but scalable to land/naval; Ka still ahead.

### 5. Ball Aerospace / BAE Systems (Boulder, CO) - MEDIUM-HIGH
- Ball Aerospace acquired by BAE Systems (2024) -> BAE Systems Space & Mission Systems. ESA tiles (used by Stellar Blu for multi-orbit multi-beam aero ESA). Ku-band multi-orbit ESA for mobile platforms, dynamic LEO/MEO/GEO switching. Defense prime scale. (V: RunwayGirl; flat-panel market reports)
- Threat: prime-scale defense integration + ESA tile technology; more component/tile + integrator than merchant tactical terminal.

### 6. Get SAT (Israel; US ops) - MEDIUM
- Compact all-in-one mil-Ka ESA terminals (Aero Blade M PICO/SOLO Ka); GEO+MEO+LEO, dual-beam Rx, no moving parts, modem-agnostic + integrated modems; airborne ISR/tactical/C2. SOLO Ka: 53 dBW EIRP, 12.5 dB/K G/T, 23 kg. (V: getsat.com product pages)
- Threat: leading compact/low-SWaP mil-Ka ESA for air/tactical; smaller/lighter than All.Space; narrower (mostly single-link airborne) scope.

### 7. Intellian (Seoul, Korea) - MEDIUM
- AESA/ESA Flat Panel Series (proprietary element + vector-amplifier chipset); maritime/land/gov. ARC-M4 Block 1: simultaneous X + Mil Ka + comm Ka. v130NX PM Dual-Ka (AN/USC-73) WGS. OW11FA Ku LEO aero (w/ Panasonic Avionics). Telesat Lightspeed LEO terminal. ARC-M4-L24 2.4m tactical WGS flyaway (X + Mil Ka, industry-first claim). New 20,575 sqm campus, phased-array flat-panel lines. (V: Intellian/SatNews/Via Satellite 2026-03/04)
- Threat: huge manufacturing scale, maritime/WGS incumbency, expanding into flat-panel ESA + gov; reuse strategy; Ka multi-orbit ESA still emerging.

### 8. Viasat (Carlsbad, CA) - MEDIUM (coopetition)
- Operator + terminal maker (Global Xpress via Inmarsat, ViaSat-3). Owns networks All.Space rides; also builds/certifies terminals; CBM-400 software-defined modem (WGS). More partner+network than direct ESA terminal competitor, but competes at system level and controls Ka capacity. (V: prior fact-check registry; flat-panel market reports)
- Threat: controls Ka networks + bundles terminals; can favor own hardware.

### 9. L3Harris (Melbourne, FL) - MEDIUM (frenemy)
- Defense prime; modems (WAM for Navy, A3M with PTW) + terminals + DEUCSI multi-orbit terminal work; All.Space integration partner (WAM into All.Space antenna per prior interviews) yet competes at terminal/system level. Amazon Leo early partner. (V: prior fact-check registry; SpaceNews DEUCSI)
- Threat: prime scale, owns the modem layer, could integrate/backward-compete; also a customer/partner.

### 10. SpaceX Starshield / Amazon Leo (Kuiper) - STRATEGIC / VERTICAL
- Vertically integrated constellations bundling their own phased-array user terminals; Starshield = militarized Starlink (encrypted, gov). Amazon Leo (rebranded from Project Kuiper Nov 2025), 390+ sats by July 2026, commercial ~Q3 2026, L3Harris partner. Mostly Ku (Starlink) but band-adjacent and existential to the merchant/third-party-antenna model - Starlink already withdrew third-party antenna support mid-2025. (V: Amazon/Verge/Euronews 2025-2026; prior registry)
- Threat: scale + vertical integration + bundling; commoditizes connectivity; but closed ecosystems and not multi-orbit-agnostic tactical terminals.

## Market context
- Flat panel antenna market ~US$0.8B(2025) growing to ~US$8.81B by 2033, ~30% CAGR. Players named: Kymeta, ThinKom, Hanwha Phasor, TTI Norte, L3Harris, Ball Aerospace, RadioWaves, NXT Communications, Isotropic/All.Space, China Starwin. (V: DataM/openpr 2026)
- Space Force SCAR ($1.7B ground antenna program, AeroVironment/BlueHalo BADGER) terminated June 2026, recompeting toward commercial systems - opportunity signal. (V: SpaceNews; KeepTrack 2026-06-25)
- FY2027 $1T defense bill; $152B reconciliation funds must be obligated by Oct 1 2026 - contract acceleration window. (V: KeepTrack 2026-06-25)

## Monitoring sources (for weekly automation)
- Federal contracts: SAM.gov (opportunities + awards), USAspending.gov (award data, filterable by recipient). (V)
- Industry news: SpaceNews, SatNews, Via Satellite, Runway Girl Network (aero), EDR Magazine, Breaking Defense, GovConWire, SpaceandDefense.io. (V, observed as sources here)
- Company newsrooms (press-release pages) per competitor (URLs captured on each wiki page).
- DoD daily contracts announcements (defense.gov/News/Contracts).
