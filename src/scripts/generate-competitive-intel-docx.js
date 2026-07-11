// Competitive intelligence document generator (All.Space + 10 competitors + holistic).
// Built with docx-js. House style: no em dashes. Data mirrors os/wiki/company + os/wiki/competitors.
// Usage: node src/scripts/generate-competitive-intel-docx.js [outputDir]
const fs = require("fs");
const path = require("path");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, LevelFormat, HeadingLevel,
  BorderStyle, Table, TableRow, TableCell, WidthType, ShadingType,
} = require(require.resolve("docx", { paths: ["/tmp/resume-build/node_modules", process.cwd()] }));

const ACCENT = "1F3B57";
const FONT = "Calibri";
const outDir = process.argv[2] || "/tmp/ci-docs";
fs.mkdirSync(outDir, { recursive: true });

const run = (t, o = {}) => new TextRun({ text: t, size: o.size || 21, bold: !!o.bold, italics: !!o.italic, color: o.color, font: FONT });
const rule = { bottom: { style: BorderStyle.SINGLE, size: 8, color: ACCENT, space: 2 } };
const h1 = (t) => new Paragraph({ children: [run(t, { size: 30, bold: true, color: ACCENT })], spacing: { before: 260, after: 120 }, border: rule });
const h2 = (t) => new Paragraph({ children: [run(t, { size: 24, bold: true, color: ACCENT })], spacing: { before: 200, after: 90 } });
const para = (t, o = {}) => new Paragraph({ children: Array.isArray(t) ? t : [run(t, o)], spacing: { after: o.after == null ? 100 : o.after, line: 276 } });
const bullet = (t) => new Paragraph({ children: Array.isArray(t) ? t : [run(t)], numbering: { reference: "b", level: 0 }, spacing: { after: 60, line: 264 } });
const title = (t, sub) => [
  new Paragraph({ children: [run(t, { size: 40, bold: true, color: ACCENT })], alignment: AlignmentType.CENTER, spacing: { after: 60 } }),
  new Paragraph({ children: [run(sub, { size: 20, italic: true })], alignment: AlignmentType.CENTER, spacing: { after: 40 }, border: rule }),
  new Paragraph({ children: [run("Prepared for York Space Systems / All.Space | Confidence markers: V verified, A owner-attested, I inferred | As of 2026-07-10", { size: 16, italic: true })], alignment: AlignmentType.CENTER, spacing: { after: 200 } }),
];

function cell(text, { bold = false, fill, w } = {}) {
  return new TableCell({
    width: w ? { size: w, type: WidthType.DXA } : undefined,
    shading: fill ? { fill, type: ShadingType.CLEAR } : undefined,
    margins: { top: 60, bottom: 60, left: 100, right: 100 },
    children: [new Paragraph({ children: [run(text, { bold, size: 18 })] })],
  });
}
function rankingTable(rows) {
  const border = { style: BorderStyle.SINGLE, size: 1, color: "BBBBBB" };
  const borders = { top: border, bottom: border, left: border, right: border, insideHorizontal: border, insideVertical: border };
  const widths = [700, 3000, 1800, 3860];
  const header = new TableRow({ tableHeader: true, children: [
    cell("#", { bold: true, fill: "D5E1EC", w: widths[0] }),
    cell("Competitor", { bold: true, fill: "D5E1EC", w: widths[1] }),
    cell("Tier", { bold: true, fill: "D5E1EC", w: widths[2] }),
    cell("Primary reason", { bold: true, fill: "D5E1EC", w: widths[3] }),
  ]});
  const body = rows.map((r) => new TableRow({ children: [
    cell(r[0], { w: widths[0] }), cell(r[1], { w: widths[1] }), cell(r[2], { w: widths[2] }), cell(r[3], { w: widths[3] }),
  ]}));
  return new Table({ width: { size: 9360, type: WidthType.DXA }, columnWidths: widths, rows: [header, ...body], borders });
}

function build(children, filename) {
  const doc = new Document({
    styles: { default: { document: { run: { font: FONT, size: 21, color: "202020" } } } },
    numbering: { config: [{ reference: "b", levels: [{ level: 0, format: LevelFormat.BULLET, text: "\u2022", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 360, hanging: 200 } } } }] }] },
    sections: [{ properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1080, bottom: 1080, left: 1080, right: 1080 } } }, children }],
  });
  return Packer.toBuffer(doc).then((buf) => { fs.writeFileSync(path.join(outDir, filename), buf); console.log("saved", filename); });
}

const section = (heading, items) => [h2(heading), ...items.map((i) => bullet(i))];

// ---------------- All.Space dossier ----------------
const allspace = [
  ...title("All.Space", "Company and Product Intelligence Dossier (a York Space Systems company)"),
  h1("1. Snapshot"),
  para("All.Space (formerly Isotropic Systems) builds the Hydra range of multi-link, multi-orbit, electronically steered satellite terminals using a proprietary lens-array beamforming architecture. As of 2026-07-08 it is a wholly owned subsidiary of York Space Systems. Its defining claim is the only terminal that maintains simultaneous, full-duplex connections to two or more independent satellites across different orbits and bands from a single aperture, with inherent anti-jam resilience for contested environments. (V)"),
  h1("2. History"),
  ...["Founded 2013 as Isotropic Systems Ltd in Reading, England, by John Finney (ex-SES MEO executive) and Jeremiah Turpin (Chief Scientist). (V)",
    "2013 to 2022: delivered development programs with the European Space Agency, UK Space Agency, UK MOD, and US DoD; funded by SES (lead), Boeing HorizonX, UK Future Fund, and others. (V)",
    "2022-08-01: rebranded to All.Space (same legal entity); unveiled fifth-generation smart terminal. (V)",
    "2023: first terminal delivered to SES for testing; John Finney stepped down as CEO, succeeded by Paul McCarter (former COO); closed 44M USD Series C led by defense-focused Boka Group (total funding ~160M USD). (V)",
    "2025: Hydra 2 and Hydra MAX productized; certified on SES Ka-band GEO and O3b mPOWER Ka-band MEO. (V)",
    "2026 (~June): redomiciled UK to US; new technical and manufacturing hub in Florence-Muscle Shoals, Alabama. (V)",
    "2026-07-08: York Space Systems acquisition closed. (V)"].map((i) => bullet(i)),
  h1("3. The York Space Systems acquisition (closed 2026-07-08)"),
  ...["Terms: ~300M USD total (down from 355M USD announced late April 2026): ~155M USD cash + 5.9M York common shares. All.Space operates as a wholly owned York subsidiary and continues as a merchant supplier. (V)",
    "Acquirer: York Space Systems (CEO Dirk Wallinger) builds tactical spacecraft plus a Mission Operations Command and Control layer; also acquired Orbion Space Technology (propulsion) in March 2026. (V)",
    "Rationale: combine All.Space jam-resistant multi-link terminals with York spacecraft + C2 into a complete tactical ecosystem for assured comms and positioning in GPS-denied and jammed environments. (V)",
    "Implications: US domicile plus Alabama manufacturing removes foreign-ownership barriers to US defense programs; York prime status opens platform pull-through; balance-sheet stability after a capital-intensive decade. (I)"].map((i) => bullet(i)),
  h1("4. Product: the Hydra Terminal Range"),
  para("Core architecture (V): a proprietary multi-lens array performing RF/digital beamforming with patented dielectric lens technology (marketed as optical beamforming). Dielectric lenses focus energy onto independent, electronically switchable feeds to form multiple high-gain beams with no moving parts. The lens architecture provides inherent spatial filtering that rejects off-axis interference and jamming. Digital beamforming enables vector-based mono-pulse tracking above 400 Hz under intense motion."),
  ...section("Product line", [
    "Hydra 2 (fielded): dual-link, Mil Ka + Comm Ka, two satellites across GEO and/or MEO simultaneously; 86 cm dia x 18 cm, 77 kg; pointing under 0.1 deg in motion; 125 MHz Rx IBW per link; 3 swappable bays; certified SES Ka GEO + O3b mPOWER. (V)",
    "Hydra MAX (announced 2025; Gen 2 in 2026): world-first 500 MHz instantaneous bandwidth per beam (1 GHz aggregate) across comm+mil Ka; full-duplex on both beams simultaneously across full scan; integrated modems, tactical comms, edge compute. (V)",
    "Hydra 4 (roadmap): Hydra 2 base + Starlink (Ku) + Iridium (L). (V)",
    "Hydra KuKa (roadmap): simultaneous Ka + Ku across all orbits. (V)",
    "Hydra MAX 2 (2027): dual Ka across LEO+HEO+MEO+GEO. (V)",
  ]),
  para("Connectivity targets (V): WGS, SES O3b mPOWER, Viasat 3 & GX, Amazon Kuiper/Leo, Telesat Lightspeed; network- and platform-agnostic; MIL-STD engineered for multinational interoperability."),
  h1("5. Competitive advantages"),
  ...["True simultaneous multi-link full-duplex (transmit and receive on 2+ independent beams at once), not just orbit switching. Company claims this as unique. (V/I)",
    "Inherent anti-jam resilience from lens-array spatial filtering: the central reason York valued the company. (V)",
    "No-penalty second beam on the same aperture. (A)",
    "Breadth of orbit/band coverage (GEO/MEO/HEO/LEO; Mil+Comm Ka; adding Ku/L) from one device. (V)",
    "US defense prime backing (York): spacecraft + C2 + propulsion ecosystem, US domicile, domestic manufacturing. (V/I)"].map((i) => bullet(i)),
  h1("6. Vulnerabilities and risks"),
  ...["SWaP-C premium: 77 kg / 86 cm is heavier and likely costlier than flat-panel ESAs; strongest in the high-end tactical niche. (I)",
    "Merchant-model exposure: Starlink withdrew third-party antenna support (mid-2025), forcing a pivot to Amazon Leo/Kuiper Ka and WGS. (A/I)",
    "Production scale: later to volume than several competitors. (I)",
    "Direct account pressure from Kymeta on the same US Navy programs (NGC2, ONR via Bascom Hunter). (V)"].map((i) => bullet(i)),
  para("Sources: All.Space website and datasheets (2025); SpaceNews (2022-2023); Via Satellite, Space & Defense, GovConWire, SatNow (2026-07). Full log in the competitive landscape research record.", { size: 16, italic: true, after: 0 }),
];

// ---------------- Competitor data ----------------
const competitors = [
  { slug: "kymeta", name: "Kymeta Corporation", tier: "CRITICAL (rank 1 of 10)",
    snap: "Redmond, WA; founded 2012. The world-leading flat-panel satellite terminal manufacturer, built on metamaterial-based electronically steered antennas, 150+ patents. The single most direct threat to All.Space: overlapping multi-band/multi-orbit ESA product, deeper current DoD program momentum, and a lower-SWaP flat-panel form factor. (V)",
    tech: ["Metamaterial ESA: software-defined flat panels, no moving parts, hybrid satellite+cellular, edge processing. (V)",
      "KuKa 8 Series: first multi-band (Ku + Ka), multi-orbit (GEO/MEO/LEO/HEO), single-aperture flat-panel ESA; four concurrent beams (2 Tx + 2 Rx) from one metamaterial surface (demoed June 2025, TRL6); 35.4 x 35.4 x 3.9 in; dual-modem. Prototypes mid-2026, commercial 2027. (V)"],
    contracts: ["US Army NGC2 pilot: selected as multi-orbit SATCOM provider, Q3 2025. (V)",
      "ONR contract via Bascom Hunter (2026-04-14): first single-antenna multi-band multi-orbit terminal for US Navy testing from Q2 2026. Same prime and Navy relationship as All.Space STtNG: direct account collision. (V)",
      "New CEO Manny Mora (Nov 2025), 40-year General Dynamics Mission Systems veteran, hired to align to DoD/JADC2. (V)"],
    threat: ["Direct product overlap, winning the exact accounts All.Space pursues, more DoD traction now, lower-SWaP flat panel. (I)",
      "All.Space counter: Hydra offers true simultaneous full-duplex dual-link today and stronger lens anti-jam; KuKa is prototype (mid-2026) to commercial (2027). Watch schedule and whether four-beam matches full-duplex-both-beams in the field. (I)"],
    mon: ["Newsroom: kymetacorp.com/about/news-insights", "Track NGC2, ONR/Bascom Hunter deliveries, KuKa milestones, DoD awards (SAM.gov/USAspending)."] },
  { slug: "thinkom", name: "ThinKom Solutions", tier: "HIGH (rank 2 of 10)",
    snap: "Hawthorne, CA. Established mobility SATCOM leader, best known for patented VICTS technology, a steerable mechanically-actuated phased array with an ultra-low profile that tracks any orbit. Deep aviation IFC base, now pushing into contested-environment defense ground stations and digital arrays. (V)",
    tech: ["VICTS: conformal, low-profile, mechanically-actuated phased array; any orbit. Not a pure solid-state ESA (mechanical elements). (V)",
      "ThinAir Ka2517: multi-orbit Ka on SES Open Orbits (MEO + GEO). (V)",
      "Containerized Digital Array: software-defined multi-beam/multi-orbit/multi-band/multi-network (LEO/MEO/GEO/HEO); C, Ku, K, Ka (comm+mil), Q now; low visual/heat/wind signature for a survivable proliferated ground segment. (V)"],
    contracts: ["3.9M USD DoD portable ground stations (follow-on, Feb 2026): airline-checkable phased-array gateways for dismounted forces. (V)",
      "1.9M USD SpaceWERX D2P2 SBIR (Jan 2026): containerized transportable ground entry point for the Air Force. (V)",
      "Ongoing SES multi-orbit service partnership via ThinAir Ka. (V)"],
    threat: ["Proven, deployed at scale, genuinely multi-orbit, strong DoD + aviation, moving into the contested-environment terminal niche. (I)",
      "All.Space counter: VICTS is mechanical-hybrid and single-beam-oriented; All.Space wins on solid-state simultaneous dual-link and lens anti-jam for the most contested tactical use. (I)"],
    mon: ["Newsroom: thinkom.com/news", "Track DoD portable/containerized awards, SES expansions, any move to solid-state ESA."] },
  { slug: "cesiumastro", name: "CesiumAstro", tier: "HIGH (rank 3 of 10)",
    snap: "Austin, TX. Developer of software-defined active phased arrays for space and defense (Skylark, Vireo, Nightingale). Very well capitalized (~470M USD combined equity and debt) and scaling production. Strongest in payloads and arrays, now expanding into mobile terminals. (V)",
    tech: ["Scalable active phased array architecture: true solid-state AESA, software-defined, modular small to large aperture; mobile-ready from ground vehicles to airborne. (V)",
      "Skylark product line expanded 2026 with a large-aperture array variant. (V)"],
    contracts: ["MDA GMD Weapon System IFICS (April 21, 2026): new large-aperture active phased array (Skylark expansion) for missile-defense modernization. (V)",
      "Founder/CEO Shey Sabripour; standardized platforms across satellites, payloads, terminals, and computing. (V)"],
    threat: ["Genuine active phased array, exceptional funding, defense momentum, stated push into mobile terminals. (I)",
      "All.Space counter: CesiumAstro heritage is payloads/arrays rather than fielded multi-orbit mobility terminals; All.Space ships a certified tactical terminal today. Watch for a CesiumAstro multi-orbit ground terminal. (I)"],
    mon: ["Newsroom: cesiumastro.com/press-release", "Track terminal (vs payload) announcements, MDA/SDA awards, funding."] },
  { slug: "hanwha-phasor", name: "Hanwha Phasor", tier: "MEDIUM-HIGH (rank 4 of 10)",
    snap: "London, UK; a division of Korean group Hanwha. Builds the A7700 AESA, a modular multi-beam, constellation-agnostic flat panel. Ku-band first (entry ~2025), Ka planned. Aero-first but scalable to land and naval; Hanwha capital and defense pedigree. (V)",
    tech: ["A7700 AESA: modular square-tile array scalable to platform size (howitzer to ship to airliner); two receive beams (company calls this fairly unique); constellation-agnostic (GEO + LEO); cryogenic cooling designed out; ~120 mm height. (V)",
      "Ka-band planned after Ku via technology reuse, to arrive alongside Ka LEO networks. (V)"],
    contracts: ["Eutelsat OneWeb terminal qualification (LEO). (V)",
      "Lufthansa Technik radomes + EASA/FAA STC (EASA Q3 2025, FAA Q4 2025); Kontron power components; Plexus manufacturing. (V)"],
    threat: ["Hanwha capital + defense pedigree, modular scalability, dual-Rx-beam differentiation, aero certification progress. (I)",
      "All.Space counter: Hanwha is Ku-first and aero-led; All.Space leads on Mil-Ka and simultaneous multi-orbit tactical today. Threat rises as Hanwha Ka and land/naval variants mature. (I)"],
    mon: ["Newsroom: hanwhaphasor.com; Runway Girl Network, EDR Magazine", "Track Ka timing, land/naval variants, STC completions, defense awards."] },
  { slug: "ball-bae-systems", name: "Ball Aerospace / BAE Systems (Space & Mission Systems)", tier: "MEDIUM-HIGH (rank 5 of 10)",
    snap: "Boulder, CO. Ball Aerospace was acquired by BAE Systems (2024) and operates as BAE Systems Space & Mission Systems. Supplies ESA tile technology and multi-orbit ESAs at defense-prime scale; more a tile supplier and integrator than a merchant tactical-terminal vendor. (V)",
    tech: ["ESA tiles: building-block phased-array tiles used in partner terminals (e.g., Stellar Blu multi-orbit multi-beam aero ESA on BAE/Ball tiles). (V)",
      "Ku-band multi-orbit ESA for mobile platforms with dynamic LEO/MEO/GEO switching. (V)",
      "Defense-prime systems integration, mission systems, and space payload heritage. (V)"],
    contracts: ["Prime-scale DoD/Space Force relationships across mission systems (broad; specific antenna awards tracked via SAM.gov/USAspending). (V/I)"],
    threat: ["Prime-scale relationships, deep RF/ESA engineering, tile ecosystem that can arm multiple terminal makers. (I)",
      "All.Space counter: BAE/Ball competes at tile/component and integrator layer; All.Space owns a differentiated end terminal. Watch for BAE-branded terminals or exclusive tile deals strengthening a rival. (I)"],
    mon: ["Newsroom: baesystems.com/space", "Track tile partnerships (who they arm), any BAE-branded terminal, Space Force awards."] },
  { slug: "get-sat", name: "Get SAT", tier: "MEDIUM (rank 6 of 10)",
    snap: "Israel (with US operations). Specialist in compact, all-in-one military Ka-band ESAs for airborne ISR, tactical airlift, and C2. The Aero Blade M line is notably smaller and lighter than Hydra, competing where low SWaP decides. (V)",
    tech: ["Aero Blade M SOLO Ka: next-gen ESA, no moving parts, integrated modem/ACU/converter/tracking/RF; GEO+MEO+LEO switching; Tx 27.6-31 GHz, Rx 17.7-21.2 GHz; max EIRP 53 dBW; G/T 12.5 dB/K; ~23 kg; DO-160. (V)",
      "Aero Blade M PICO Ka: ultra-compact 1.6 kg dual-beam Rx ESA; modem-agnostic; GEO/MEO/LEO. (V)"],
    contracts: ["Defense/government airborne integrations (tracked via SAM.gov/USAspending and company news). (V/I)"],
    threat: ["Leading compact low-SWaP mil-Ka ESA for air and tactical edge; integrated single-box design. (I)",
      "All.Space counter: Get SAT is mostly single-link airborne, not simultaneous multi-orbit dual-full-duplex; All.Space wins where multi-link resilience and aggregate throughput matter. Overlap in airborne tactical. (I)"],
    mon: ["Newsroom: getsat.com/news", "Track new bands/multi-link products, US DoD wins, platform integrations."] },
  { slug: "intellian", name: "Intellian Technologies", tier: "MEDIUM (rank 7 of 10)",
    snap: "Seoul, South Korea. Global leader in SATCOM antennas and ground gateways with enormous manufacturing scale, dominant in maritime VSAT, now expanding into flat-panel ESA and government/defense. New 20,575 sqm campus adds phased-array flat-panel and LEO terminal lines. (V)",
    tech: ["Flat Panel Series (AESA): proprietary element + custom vector-amplifier chipset; new agile Manpack; Ka multi-orbit flat panels previewed. (V)",
      "ARC-M4 Block 1: simultaneous X + Mil Ka + comm Ka (WGS). v130NX PM Dual-Ka (AN/USC-73): electronic Mil/Comm Ka switching for maritime WGS. (V)",
      "ARC-M4-L24: 2.4 m tactical WGS flyaway, claimed industry-first simultaneous X + Mil Ka flyaway. OW11FA: Ku LEO aero with Panasonic Avionics (OneWeb). Telesat Lightspeed LEO terminal. (V)"],
    contracts: ["Panasonic Avionics OW11FA aero partnership; Telesat Lightspeed terminal selection. (V)"],
    threat: ["Vast manufacturing scale, maritime/WGS incumbency, aggressive flat-panel ESA expansion, design-reuse strategy. (I)",
      "All.Space counter: Intellian multi-orbit Ka ESA still emerging, heritage mechanically-steered maritime; All.Space leads on simultaneous multi-orbit tactical resilience. Intellian threat is breadth, scale, price. (I)"],
    mon: ["Newsroom: intelliantech.com/en/news", "Track Ka multi-orbit ESA launch, tactical flyaway specs (late 2026), naval/DoD awards, Telesat/OneWeb ramps."] },
  { slug: "viasat", name: "Viasat", tier: "MEDIUM, coopetition (rank 8 of 10)",
    snap: "Carlsbad, CA. A vertically integrated operator and hardware maker: owns Ka networks (Global Xpress via Inmarsat, ViaSat-3) and builds terminals/modems. To All.Space it is both a network partner (Hydra targets GX/Viasat-3 certification) and a competitor that controls Ka capacity and can favor its own hardware. (V)",
    tech: ["Networks: Global Xpress and ViaSat-3 Ka-band; large government and mobility service business. (V)",
      "Terminals and modems: builds/certifies terminals; CBM-400 software-defined modem is WGS-certified. (V)"],
    contracts: ["Broad government service contracts; capacity + terminal bundling (public company; earnings disclosures). (V/I)"],
    threat: ["Controls networks All.Space rides and can bundle/prefer own terminals; competes at system/service level; leverage is capacity + bundling. (I)",
      "All.Space counter: network-agnostic multi-orbit is the antithesis of single-network lock-in; GX/Viasat-3 certification turns Viasat into a channel. Watch for proprietary bundles excluding third-party antennas. (I)"],
    mon: ["Newsroom: news.viasat.com; investor relations", "Track terminal bundling, GX/ViaSat-3 capacity and certifications, DoD service awards."] },
  { slug: "l3harris", name: "L3Harris Technologies", tier: "MEDIUM, frenemy (rank 9 of 10)",
    snap: "Melbourne, FL. A defense prime that owns the protected-tactical modem layer (Navy WAM; Air Force/Army A3M with the Protected Tactical Waveform) and builds terminals and multi-orbit systems (DEUCSI). Both an All.Space integration partner and a system-level competitor. (V/A)",
    tech: ["Modems: WAM (Navy) and A3M (Air Force/Army, PTW); owns critical protected-waveform modem IP. (V)",
      "Terminals/systems: multi-orbit terminal development under AFRL DEUCSI; ground multiband terminals; early Amazon Leo partner. (V)"],
    contracts: ["A3M ($500M-ceiling program) and WAM Navy modem programs; DEUCSI multi-orbit terminal awards. (V)"],
    threat: ["As the modem supplier inside tactical terminals, L3Harris can shape integration and bundle its own terminal solutions while also being a partner and customer. Genuinely two-sided. (I)",
      "All.Space counter: All.Space integrates L3Harris modems (WAM) and benefits from partnership; risk is L3Harris favoring an in-house or partner antenna. Manage as key partner, monitor for competitive terminal moves. (I)"],
    mon: ["Newsroom: l3harris.com/newsroom; investor relations", "Track L3Harris terminal/antenna moves, A3M/WAM expansions, DEUCSI, Amazon Leo integration."] },
  { slug: "spacex-starshield", name: "SpaceX Starshield / Amazon Leo (vertically integrated constellations)", tier: "STRATEGIC / vertical (rank 10 of 10)",
    snap: "Not ESA-terminal peers but constellation operators bundling their own phased-array terminals, threatening the entire third-party (merchant) terminal model All.Space depends on. Starshield is militarized, encrypted Starlink. Amazon Leo (rebranded from Project Kuiper Nov 2025) had 390+ satellites by July 2026, commercial ~Q3 2026. (V)",
    tech: ["Vertically integrated networks + own user terminals; Starlink/Starshield primarily Ku; Amazon Leo Ka-capable. (V)",
      "Closed ecosystems: terminals serve their own constellations, not cross-vendor multi-orbit resilience. (I)"],
    contracts: ["Starshield DoD engagements; Amazon Leo enterprise/government rollout with partners incl. L3Harris. (V)"],
    threat: ["Vertical integration + bundling commoditizes connectivity and squeezes independent terminal makers; Starlink already withdrew third-party antenna support (mid-2025). Band-adjacent but existential to the merchant model. (V/I)",
      "All.Space counter: its whole proposition is the opposite of single-network lock-in; operator restrictions make multi-orbit, multi-vendor, anti-jam terminals more valuable to defense. (I)"],
    mon: ["spacex.com/starshield; aboutamazon.com/news/amazon-leo", "Track third-party access policies, Starshield awards, Amazon Leo commercial/gov offerings, Ka bundling."] },
];

function competitorDoc(c) {
  return [
    ...title(c.name, "Competitor Intelligence Dossier"),
    para([run("Threat rank / tier: ", { bold: true }), run(c.tier)]),
    para([run("Competes against: ", { bold: true }), run("All.Space (a York Space Systems company)")]),
    h1("Snapshot"), para(c.snap),
    ...section("Technology and products", c.tech),
    ...section("Recent activity and contracts", c.contracts),
    ...section("Threat assessment", c.threat),
    ...section("Monitoring sources", c.mon),
    para("Confidence markers: V verified against cited public sources, A owner-attested, I inferred. Sources captured in the competitive landscape research log. As of 2026-07-10.", { size: 16, italic: true, after: 0 }),
  ];
}

// ---------------- Holistic report ----------------
const holistic = [
  ...title("All.Space Competitive Landscape", "Holistic Threat Ranking, Company Profiles, and Weekly Monitoring Plan"),
  h1("Executive summary"),
  para("This report ranks the ten most significant competitors to All.Space (a York Space Systems company), weighting Ka-band and electronically steered antenna (ESA) manufacturers as the highest threats per direction. It profiles each competitor, identifies the strategic findings that matter most, and defines a weekly monitoring and automation plan with concrete data sources. Three findings drive everything: Kymeta is the clear and present danger (it is winning the exact Navy/Army accounts All.Space targets); the threat is bimodal (direct ESA rivals plus structural threats from network and modem owners who can bundle or restrict access); and All.Space's defensible moat is anti-jam resilience via lens-array simultaneous full-duplex beamforming, which is precisely what York acquired. (V/I)"),
  h1("Scoring model"),
  ...["Product overlap (ESA / multi-orbit / Ka) - weight 30%", "DoD/program momentum - weight 25%", "Technology maturity / fielded status - weight 20%", "Scale and capital - weight 15%", "Account collision with All.Space - weight 10%"].map((i) => bullet(i)),
  h1("Threat ranking"),
  rankingTable([
    ["1", "Kymeta", "CRITICAL (4.7)", "Direct multi-band/multi-orbit ESA winning the same Navy/Army programs"],
    ["2", "ThinKom", "HIGH (4.0)", "Proven, fielded multi-orbit Ka + contested-environment digital arrays"],
    ["3", "CesiumAstro", "HIGH (3.8)", "True active phased array, ~470M USD funded, MDA win, mobile terminals push"],
    ["4", "Hanwha Phasor", "MED-HIGH (3.4)", "A7700 AESA, Hanwha capital, aero-certified, Ka on roadmap"],
    ["5", "Ball / BAE Systems", "MED-HIGH (3.3)", "Prime-scale ESA tiles arming rivals + own multi-orbit ESA"],
    ["6", "Get SAT", "MEDIUM (3.0)", "Leading compact low-SWaP mil-Ka ESA for airborne/tactical"],
    ["7", "Intellian", "MEDIUM (2.9)", "Massive scale + WGS incumbency expanding into flat-panel ESA"],
    ["8", "Viasat", "MEDIUM (2.6)", "Owns Ka networks All.Space rides; bundles terminals (coopetition)"],
    ["9", "L3Harris", "MEDIUM (2.5)", "Owns the modem layer; partner and potential competitor (frenemy)"],
    ["10", "SpaceX Starshield / Amazon Leo", "STRATEGIC (2.4)", "Vertically integrated constellations bundling own terminals"],
  ]),
  new Paragraph({ children: [], spacing: { after: 120 } }),
  h1("Competitor profiles"),
  ...competitors.flatMap((c) => [
    h2(c.name + " - " + c.tier),
    para(c.snap),
    para([run("Key technology: ", { bold: true }), run(c.tech[0])]),
    para([run("Recent/contracts: ", { bold: true }), run(c.contracts[0])]),
    para([run("Why it matters: ", { bold: true }), run(c.threat[0])]),
  ]),
  h1("The three findings that matter most"),
  ...["Kymeta is the clear and present danger: it is winning the exact US Navy and Army accounts All.Space targets, through the same prime (Bascom Hunter), with a new DoD-veteran CEO. Treat it as the primary opponent in every account plan. (V)",
    "The threat is bimodal: ranks 1-6 are direct ESA/terminal rivals racing on multi-orbit Ka; ranks 8-10 are structural threats (network and modem owners who can bundle or restrict access). All.Space must win the terminal race AND defend the merchant model against vertical integration. (I)",
    "Anti-jam resilience is All.Space's defensible moat: every credible competitor can do multi-orbit switching; the lens-array simultaneous full-duplex + spatial-filtering anti-jam story is what York bought and what differentiates in contested environments. Concentrate proof points there. (I)"].map((i) => bullet(i)),
  h1("Weekly monitoring and automation plan"),
  para("Keep this intelligence current with a weekly automated refresh that an agent runs and files into the wiki."),
  ...section("What to monitor per competitor", ["Press releases / newsroom", "Federal contract awards", "Industry trade press", "Capital events (funding, M&A)", "Program signals in target accounts (Navy, Army, Space Force, MDA, allied)"]),
  ...section("Authoritative contract sources (free, structured)", [
    "SAM.gov: contract opportunities and awards; save searches per competitor name; APIs available (registration).",
    "USAspending.gov: award data filterable by recipient and agency; NAICS 334220 and 517410; public API for automation.",
    "defense.gov/News/Contracts: daily DoD contract announcements over 7.5M USD.",
    "Optional paid: Highergov, GovTribe, GovWin for pipeline/forecast depth."]),
  ...section("Industry feeds (RSS available)", [
    "SpaceNews (spacenews.com) - primary satellite/defense contract news.",
    "SatNews (satnews.com) - high-volume industry announcements.",
    "Via Satellite (satellitetoday.com) - analysis and executive interviews.",
    "Runway Girl Network - aero ESA/IFC depth; Breaking Defense, EDR Magazine, GovConWire, SpaceandDefense.io, KeepTrack.",
    "Google/news alerts for each company plus terms: electronically steered antenna, flat panel antenna, multi-orbit terminal, Ka-band terminal, SATCOM contract."]),
  ...section("The weekly loop (agent-run)", [
    "Pull: fetch each competitor newsroom (RSS or fetch-and-diff), pull SpaceNews/SatNews feeds filtered to the competitor list, query the USAspending API for new awards to each competitor in the trailing 8 days.",
    "Filter: keep last-week items relevant to ESA/terminals/Ka/contracts/leadership/capital.",
    "File: append dated, sourced bullets to each competitor page under Updates (newest first); store raw items per competitor.",
    "Re-score: on a product ship, a target-account win, or a major raise, update the ranking.",
    "Report + commit: produce a one-page week-in-review (biggest moves, ranking changes, recommended actions) and commit."]),
  ...section("Cadence", ["Weekly: automated pull + file + report.", "Monthly: human review of the ranking and top findings.", "Event-driven: immediate ingest on a target-account loss, a competitor acquisition, or a network access-policy change."]),
  h1("Market context"),
  ...["Flat panel antenna market ~0.8B USD (2025) growing to ~8.81B USD by 2033 (~30% CAGR). (V)",
    "Space Force SCAR (1.7B USD ground antenna program) terminated June 2026 and recompeting toward commercial systems: an opportunity signal. (V)",
    "FY2027 1T USD defense bill; 152B USD reconciliation funds must be obligated by Oct 1 2026: a contract-acceleration window. (V)"].map((i) => bullet(i)),
  para("Confidence markers: V verified against cited public sources, A owner-attested, I inferred. Full sourcing in the competitive landscape research log. As of 2026-07-10.", { size: 16, italic: true, after: 0 }),
];

// ---------------- Build all ----------------
Promise.resolve()
  .then(() => build(allspace, "All.Space - Company Dossier.docx"))
  .then(() => competitors.reduce((p, c, i) => p.then(() => build(competitorDoc(c), `Competitor ${String(i + 1).padStart(2, "0")} - ${c.name.split(" (")[0].replace(/[\/]/g, "-")}.docx`)), Promise.resolve()))
  .then(() => build(holistic, "All.Space Competitive Landscape - Holistic Report.docx"))
  .then(() => console.log("ALL DONE"));
