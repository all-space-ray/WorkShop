<!--
origin: AI-distilled voice-sample extraction from Raymond Tayse's company email (Sent folder, ~2.5 years)
type: voice-samples (verbatim email prose, redacted; plus an extraction-agent analysis section)
produced_by: external AI harness (Claude.ai with mailbox access); first of two planned extractions (a second run via Fable 5 Max is pending for comparison)
received: 2026-07-11
ingested: 2026-07-11
note: Immutable source. Body below is verbatim as delivered, including the extraction agent's own "Observed voice patterns" section and any em dashes therein. Redaction placeholders ([NAME], [CLIENT], etc.) are the extractor's; sensitivity: business-sensitive, defense/B2B.
-->

# Voice samples: Raymond Tayse

Source: company email, Sent folder, ~2.5 years (approx 2024-03 to 2026-07)
Extracted: 2026-07-11
Total samples: 52  |  Coverage gaps: no external/press or purely personal/HR-negotiation register; almost everything is B2B/defense work email. Earliest verbatim sample is 2024-03 (mailbox extends earlier but was not sampled below the ~2.5-yr line). Light coverage of formal external prose to non-government partners; no apology-for-a-real-mistake beyond minor "I missed your name" notes.

Redaction key: [NAME] person, [CEO]/[MANAGER] specific role, [CLIENT] government customer or their staff, [VENDOR] supplier/partner, [COMPETITOR] competing product, [INVESTOR] investor/board, [COMPANY] other org, [PROGRAM] internal program/contract codename, [PRODUCT] product/feature codename, [AMOUNT] money, [NUMBER] quantity, [PART#] part number, [SHIP] hull/site, [PHONE]/[EMAIL]/[URL] contact. Only these specifics were swapped; wording, punctuation, capitalization, typos, and line breaks are otherwise verbatim. Signature blocks, "Sent from"/"Get Outlook" lines, EXTERNAL EMAIL banners, and quoted/forwarded text from others were removed as boilerplate and are not part of the samples.

## Samples

### Sample 1
- approx_date: 2024-03
- register: professional
- audience: internal peer / colleague (business development)
- intent: troubleshooting/technical explanation, analysis
- length: long
- authored_by_me: yes
- notes: Reply thinking through IP/contract rights; his signature numbered-analysis move. Company/contract specifics redacted.

> [NAME],
>
> I thought about what [NAME] said on the drive to the airport and have a few thoughts. There are a few ways in which the US Government can "dictate" who you are able to sell your product.
>
> 1. If the contract was written in such a way as to give them rights to your IP. This is usually not the case with contracts that modify a function or feature unless the resulting function or feature falls into one of the bellow categories; though this is not always the case. With that said, I have not read our [CLIENT] contracts and have no clue what was written (the contract with [VENDOR] goes back probably 2 years now and I have only been here about 4 months).
>
> 2. If the function or feature is any way classified. At which the classifying authority (usually the customer who wrote the specification) will require security sign-off on any products sold commercially. Generally, this reduces the scope of customers greatly and I do not believe this is the case here.
>
> 3. If the function or feature pushes the product over the threshold for the Export Administration Regulations (EAR) in which you need an export license to sell to foreign countries that must be approved. This is generally the case when you have encryption or TRANSEC on your product. I am unsure how this impacts foreign companies (Such as ours as we are not US). This is likely not the case in our situation as we have no encryption.
>
> 4. If the function or feature pushes the product over the threshold for the International Traffic of Arms Regulations (ITAR). This happens in communications equipment when your product has functions or features that directly correlate to inducing Low Probability of Interception (LPI) or Low Probability of Detection (LPD). Neither of which applies to our product. We need to stay away from this language as the [PART#] became ITAR after this language was propagated in reference to the DSSS waveform and had a drastic impact on international sales for [VENDOR].
>
> What I have done in the past, Initial Contracts, is to ensure there is a clear road map and path to feature X. That road map would have extended timelines for development and commercial deployment (assuming the feature does not fall into one of the above categories). We would then specify that due to opportunity costs and engineering resources, we would not be able to meet the timeline being requested. We would then provide a ROM for additional engineering resources, test equipment, lab gear, etc... to justify what it would cost to provide **Expedited Development** efforts which would sometimes fall under Non Recurring Engineering (NRE) or Professional Services Engineering (PSE) fees.
>
> The issue we have is we are already under contract and have been paid under that contract; again, I do not know the details of that contract. We are now asking for a modification to said contract and are on the wrong side of the leverage situation.
>
> I am available most of next week next week, and then I will be flying to Hawaii. Regardless of my technical expertise, I need to be there from the commercial side; [NAME] can leverage me for technical if he needs. Give me a call if you need anything.

### Sample 2
- approx_date: 2024-03
- register: professional
- audience: internal leadership (peers + CRO/CEO), group ("ALLCON")
- intent: status update (field test), troubleshooting narrative
- length: long
- authored_by_me: yes
- notes: End-of-day test report written from a hotel. Chronological day-by-day narration is a recurring long-form move.

> ALLCON,
>
> Ok, I am actually back at the hotel at a reasonable time tonight and can sit down and give some additional information regarding our testing.
>
> Monday: I arrived on site to find [VENDOR] setting up their equipment, upon further investigation and chatting with everyone I realized there were already problems with the [VENDOR] system. First, [VENDOR] decided they would not set up the wideband terminal ([COMPETITOR]) due to a missing cable. Secondly, they were troubleshooting the fiber interface between their system and ours.
>
> While this was happening [NAME] was continuing with his validation tests running through all of the test scenarios yet another time to ensure there would be no problems with our system. The only test scheduled for Monday was the 8kbps overnight test. At the 5:00 PM hotwash [VENDOR] failed to bring up the fact that the fiber interface was experiencing problems (and not trouble ticket was created). After the meeting, [NAME] ([VENDOR] engineer) asked for an additional 90 minutes to finish his troubleshooting; and if by 7:00 PM he did not have it resolved then we would move to the Coax cables. Troubleshooting, however, continued until approximately 11:00 PM and there was no resolution. I made the call to start moving the system over to the Coax so that we could proceed with the test that were required to prove our portion of the system. We officially started the test over Coax Beam 1 Modem 2 at approximately midnight. This test was Case 6 Sea State 4.
>
> Tuesday: The 8kbps test required the internal modem BER Tester as the JDSU units cannot go that low in data rate. The downside to the modem BER Tester is that if you lose lock on the modem then the Tester resets all the data. This means the data is only good until your first loss of lock. Fortunately for us, there was not a loss of lock until after 4 hours of the test. Outages were expected due to the heavy weather conditions at the hub side. However, within those 4 hours before loss of lock, we took 0 bit errors and everyone agreed this was a solid pass. We immediately moved to Sea State 6 and the Static tests.
>
> Before moving on, [VENDOR] did another 3 hours of fiber troubleshooting to no success. As we were running low on time and behind schedule, we moved forward with Test Case 3. Test Case 3 passed the static testing easily; then we ran into issues with SS4 and SS6. As SS6 was not in the critical path it was discarded. However, SS4 also failed and it was clearly a weather related issue in my opinion, but [VENDOR] insisted on creating a trouble ticket to be reviewed at the hotwash that evening. At this point all resources went to troubleshooting this ticket so we would have information available for the hotwash. Our conclusion, as expected, was weather and we briefed that at the hotwash.
>
> At this time we were quite behind schedule, but as the weather was starting to move on from [SHIP], we made the decision to push on through the evening to get as many of the tests completed as possible. We started with Test Case 7 SS6 then SS4 then Static. As you can see the results were getting better with each test due to the weather leaving [SHIP] and that was proven by screenshots while we progressed. Test Cases 4 and 5 went without issue and we set up Test Case 2 for the overnight testing and started at approximately 10:00 PM. All in all, from 5:00 - 10:00 went very smoothly and we left the site on a high note.
>
> Wednesday: The morning started great with absolutely fantastic overnight results with SS4. We moved on to SS6 which passed again with no issues. Upon moving to the static test for Case 2, we started getting massive amounts of frame errors on the JDSU. I am not going to go into details of my entire troubeshooting, but I was able to narrow it down to the JDSU over the course of a few hours. Upon consultation with the [CLIENT] it was clear there was intermittent problems with the JDSU at 32kbps. We just happen to get very lucky with the overnight and SS6. I talked with [CLIENT] and confirmed that we could move on with our additional tests as we had a 12 hour run on SS4 and that effectively proved this test.
>
> This brings us to Test Case 7; which happens to be the single most important test for this event. To be very frank, if we cannot pass Test Case 7 and 8 (8 is just 7 connecting to the [CLIENT] network backbone) then [CLIENT] would not be able to recommend us for use in the broader fleet as this is the actual use case. The static portion of this test went without a problem, but as soon as we moved to SS4, we took a couple frame losses which put us below threshold. I made the call to pause testing to start troubleshooting as I was confident this was not our system and the weather was clear skies on both sides of the link. This troubleshooting was long, extensive, and meticulous to prove without a doubt our system was working as intended. I can provide more information as needed if requested. What I was able to prove is it was either the JDSU or the hub side modem (neither could be ruled out without a few more troubleshooting steps). All troubleshooting steps were briefed at the hotwash and the [CLIENT] was in agreement with my conclusions but wanted me to talk to [CLIENT] before making any further decisions.
>
> While waiting for [CLIENT] to call me, [NAME] ([CLIENT] personnel) found an article describing an Ethernet version change in the JDSU that supposedly helped when using JDSU's that do not have the same firmware (ours did not because we had a 5800 unit while the hub had a 6000 unit). So we set the system back up to test with this other Ethernet version. While this test was running, I spoke with [CLIENT] about a variety of topics to include passing the tests that had a single frame loss (as an Ethernet frame has more than 300 bits, so it artificially increases the BER of a short test), the Ethernet version change, the Fiber issues that [VENDOR] was having, and a few other topics.
>
> The important takeaways was 1) he was in agreement with the tests that had a single frame loss should not be viewed as a failure as long as we could show it was weather related. 2) he was not aware of the Ethernet version information and was keen to learn the results. 3) He was quite upset about the fiber issue as he was told the fiber issue was within our system and not the [VENDOR] system. He said he would talk to the [CLIENT] about the issue and get back with me later today.
>
> Going back inside the 30 min pre-test on SS4 using the new Ethernet version finished without a single error. We immediately started the official test with SS4 for 30 minutes and it finished without a single error. At this point the test was considered successful and we concluded testing for the evening. At which point I took the [NUMBER] [CLIENT] Personnel, 1 [VENDOR] Personnel, and [NUMBER] All Space Personnel out to dinner. At dinner I received a phone call from [CLIENT] who was pleased with the test results, but informed me that he discussed with the [CLIENT] and it was determined that if the fiber does not work in Hawaii, we will not be going onto the boat. From my understanding, he (or someone on his team) would be passing that information to [VENDOR] tomorrow. There will be no backup to the fiber cables, this is a critical item for reasons beyond the scope of this email.
>
> I know this was a lengthy email, and it is getting quite late in the day. I just wanted to give a little more color to what has transpired over the last few days.
>
> [NAME], feel free to call me on my cell phone tomorrow if you have any additional questions.

### Sample 3
- approx_date: 2024-03
- register: professional
- audience: external partner (departing counterpart)
- intent: thank-you/relationship note (goodbye)
- length: line
- authored_by_me: yes
- notes: Warm one-line send-off to someone leaving.

> [NAME],
>
> I wish you well wherever you are going; wherever it is, they will be lucky to have you.

### Sample 4
- approx_date: 2024-03
- register: professional
- audience: vendor/partner
- intent: logistics/troubleshooting question
- length: short
- authored_by_me: yes

> [NAME],
>
> I am under the impression that the shipper will be here with a sprinter van to pick up all of the gear. This is not a problem, but nothing can really be palletized as we would have no means of lifting them into the van; let alone the footprint issues. With that said, do we need to include pallets for the [CLIENT] for them to ship the equipment to Hawaii or will they take care of that on there end?
>
> Thanks,

### Sample 5
- approx_date: 2024-09
- register: professional
- audience: direct report / commercial teammate
- intent: request / directive framed as "we need to understand"
- length: short
- authored_by_me: yes

> [NAME],
>
> We need to better understand how or if we can offer additional discounts to customers who may see our price and have sticker shock. Furthermore, we need to understand the process of an order that is not simplified acquisition (over [AMOUNT]?) and how that process works.

### Sample 6
- approx_date: 2025-03
- register: professional
- audience: investors/leadership + CRO (mixed internal/board)
- intent: persuasion / strategic status; answering a set of questions
- length: long
- authored_by_me: yes
- notes: Structured strategic reply; leans on program knowledge; invites correction at the end (a signature closing move).

> ALLCON,
>
> Had a discussion with [INVESTOR], [INVESTOR], and [NAME] today regarding the email below; with the primary problem statement of "How to get the orders from 30's to 60's on the [PROGRAM] PoR."
>
> Ultimately, the fastest way to achieve this is to get additional funding for the [PROGRAM] program through the [VENDOR] SBIR. Currently the [CLIENT] has no means of utilizing our terminal outside of the [PROGRAM] package. Though we were able to get them [AMOUNT] in plus up money last year, they were only able to purchase our antenna's as "Destructible Test Units" which they are hoping to be able to use as spare antenna's long term. As the [PROGRAM] package is north of [AMOUNT] each and contains only a single [COMPANY] antenna, this would be a very large plus-up of funds with a majority going to [VENDOR]'s margins.
>
> We are also facing deployment challenges as the CONOPS for their deployment schedule (was originally scheduled to start in February) has slipped to the right and they may not be able to start deployment of systems until June/July given the lack of funding distribution throughout the DoD until the consultation period between the services is complete in another 30 days or so.
>
> With that said, the [CLIENT] is quite aware of the markups [VENDOR] is putting onto these systems, and they would like to be able to integrate the [COMPANY] antenna into other programs under the [PROGRAM] umbrella. In order to accomplish this, they need to justify purchasing our antenna's directly from us and provide the integrators the antenna's as Government Furnished Equipment (GFE).
>
> The first challenge here is having a contract vehicle in which they could purchase from us directly. We have spent the last 8 months or so working on getting our terminal listed on the Government Services Agency (GSA) schedule. We believe we are about 30 days out from the completion of this effort. This will give the [CLIENT], and any other service, a direct contract vehicle to purchase from [COMPANY] directly. To assist us the [CLIENT] program office has directly contacted GSA to push for expedited servicing; we have direct conformation from GSA that this indeed has moved us to the top of the pile.
>
> The second challenge they are facing is justifying the purchase of equipment outside of [VENDOR]'s Small Business Innovation Research (SBIR) contract without [VENDOR] contesting. To accomplish this there needs to be a "sole source justification" presented up the chain. Once on the GSA, the justifications the [CLIENT] is looking to use is 1. Price; as the markups by [VENDOR] are over 100% 2. Direct to source engineering partnership; this is to develop future technologies required such as antenna diversity and DIFI and 3. Support services; indicating we are the subject matter experts and uniquely qualified to troubleshoot and fix the terminals in case of failure. We have the backing of several people in the program looking to push this narrative once we are on the GSA schedule.
>
> Question 2 regarding having the [CLIENT] issue a Military Interdepartmental Purchase Request (MIPR) money from their [COMPETITOR] Procurement to the [CLIENT] is not something we feel is likely to happen or even possible to happen. This would require breaking a contract ([AMOUNT] IDIQ with [COMPETITOR]), getting both services to agree to this transfer of money, and all while risking the future budget of the [CLIENT] for their own programs. If I am wrong in those statements, it just demonstrates my lack of understanding and lack of knowledge on how to proceed.
>
> Question 3 regards getting a DISA contract. I was not clear on the intention of getting a DISA contract. If it is for the purpose of having a Government Wide Acquistion Contract (GWAC) vehicle in which the [CLIENT] can purchase our equipment, I believe we will have a far better GWAC in the GSA Schedule which we believe is imminent.
>
> There are several articles on this subject ([URL]) here is the first one I came across posted 5 days ago regarding President Trumps recent Executive Order. The key information is as follows:
>
> "Under this Executive Order, GSA, in collaboration with the Office of Management and Budget (OMB), will lead efforts to consolidate procurement activities for commercial goods and services government-wide. This includes transferring the management of all Government-Wide Acquisition Contracts (GWACs) directly to GSA. Currently, GSA already manages several substantial, multi-year IT contract vehicles."
>
> In my estimation, GSA is the best contract vehicle for us to be on currently. With that said, there is no reason to limit our ability to be on multiple contract vehicles. I will reach out to people in DISA to see if there are any suitable contract vehicles for [COMPANY] and what it would take for us to initiate the process of getting on said contract vehicle.
>
> [NAME], [NAME], [NAME], or [NAME], please feel free to correct me on anything I have said above or even to add additional context to our discussions.

### Sample 7
- approx_date: 2025-03
- register: professional
- audience: customer (government engineer)
- intent: request (set up market-research discussion)
- length: short
- authored_by_me: yes
- notes: "requirements" in scare quotes with a parenthetical explaining why; cites the $1/$10/$100 rule.

> [NAME],
>
> We are engaging with a consulting firm to develop our [PRODUCT] solution, and they are looking for as many end user "requirements" as possible. I am putting requirements in quotes because there is no expectation that anything you or the [CLIENT] tells us can or should be used as a definitive requirement. However, understanding the needs of the [CLIENT] and other US Services is imperative at this stage of design ($1/$10/$100) rule.
>
> Would it be possible to set up an informal technical discussion to get market research on your potential needs for this functionality as your needs are highly valued in this process.

### Sample 8
- approx_date: 2025-03
- register: professional
- audience: customer (government contracting staff)
- intent: technical explanation (part number confirmation)
- length: short
- authored_by_me: yes
- notes: Decodes a part number component-by-component. Part numbers redacted.

> [NAME],
>
> The correct part number is [PART#]
>
> That is 2 Beam, 125MHz Instantaneous bandwidth per beam, 86 cm size, Fiber Module Set & Gain Flattening, White, Version 1.
>
> This is the version that you purchased through the [PROGRAM] contract for the [NUMBER] Units and is the correct current part number for the [CLIENT] terminal.

### Sample 9
- approx_date: 2025-03
- register: professional
- audience: investor
- intent: status update
- length: short
- authored_by_me: yes
- notes: Reports a phone call; quotes the customer; closes with gratitude.

> [NAME],
>
> I just got off the phone with [CLIENT] (APM [PROGRAM]) as he is sourcing a vehicle for the [AMOUNT] purchase. I asked if they had secured the funds, and he said "apparently they were contacted by [NAME]'s office" and have a meeting scheduled with his office next Thursday. In the mean time they are trying to get their ducks in a row to show how they will proceed.
>
> They would like to go through the GSA contracting vehicle (but they are not sure if it will be available in time), so they are talking with the [CLIENT] to use the [PROGRAM] contract vehicle (that they used to spend the [AMOUNT] last year).
>
> Thank you very much for everything.

### Sample 10
- approx_date: 2025-03
- register: professional
- audience: investor (board/AE partner)
- intent: troubleshooting a political/process problem; candid uncertainty
- length: short
- authored_by_me: yes
- notes: Shows how he frames a stalemate; "no one seems to want to stick their neck out."

> [NAME],
>
> After a couple back and forth conversations with the [CLIENT] personnel today, I was informed they have no authority to contact a congressional office, but they are obligated by law to respond to congressional inquiries.
>
> It was suggested that we ask [NAME]'s office to contact them about [PROGRAM]'s plans for the [AMOUNT] as an official inquiry as they would be forced to take action on the inquiry and move the ball.
>
> The problem I am having is we have people on our side who specializes in this saying this is the new way it needs to work (and I believe you all). Unfortunately, the [CLIENT] is insisting this is not how it works and literally no one seems to want to stick their neck out to test it given the current climate.

### Sample 11
- approx_date: 2026-02
- register: professional
- audience: internal leadership (CCO) + commercial peers
- intent: giving feedback / scoping a complex question; delegating
- length: short
- authored_by_me: yes
- notes: Breaks a big question into who-should-own-what, one function per paragraph.

> [NAME],
>
> There is a lot to unpack in one question here. I think we may need to involve other people in the discussion/answer.
>
> Legal should be part as OCI, and FAR slowdown compliance has legal consequences for non-compliance with FAR 9.5 and I would rather ensure we are saying 1. The minimum we have to and 2. Nothing that implies we are not following the law.
>
> Contracts should be involved as that is how flow down FAR's to our subs. [NAME] took the lead on the [VENDOR] contract and we should add him.
>
> Program management as this is how we enforce and validate compliance. I think [NAME] would be an excellent resource here as she has a strong DoD PM background.
>
> [NAME] (already on this), has worked our GSA Contract with [VENDOR] and we are fully compliant. However, we have no subs on any GSA purchase so we have not performed any activities other than provide an SBO to describe our intent to find small business subcontractors when applicable and available.
>
> Not sure how to answer this question via a short answer other than we comply with all federal laws and regulations.

### Sample 12
- approx_date: 2025-10
- register: professional
- audience: customer (Army engineer) + internal engineer
- intent: troubleshooting/technical explanation; walking back an earlier claim
- length: short
- authored_by_me: yes
- notes: Owns his own imprecision ("I just kind of latched on to that"; "I have no empirical proof").

> [NAME],
>
> I want to clarify my previous comment about the turn rate. There was a specified U-Turn rate for the MTP that was agreed to by all (at least that is what I am told and am trying to locate said information; [NAME] may be able to clarify). I do not know off the top of my head at the moment what it is, nor do I know the Z-Axis turn rate for the [PROGRAM] profile. A comment was made at the TRR questioning the turn rate of the [PROGRAM] profile and I just kind of latched on to that (I have no empirical proof that it is exceeding the MTP capabilities).
>
> We should check to ensure the turn rate of the profile does not exceed the slew rate of the MTP however.

### Sample 13
- approx_date: 2025-09
- register: professional
- audience: customer (Army engineer) + internal engineer
- intent: troubleshooting/technical explanation; inviting collaboration
- length: short
- authored_by_me: yes
- notes: Verbatim from the quoted prior message in the same thread as Sample 12.

> [NAME],
>
> I agree that it needs more imperial measurements to pass/fail. I am not sure how we time sync the motion test platform with the All Space tilt platform for validation.
>
> Assuming we can sync the logs and get a visual indication of tilt angle given a point in time against the motion test profile, what are the proposed +/- variances? The MTP was designed to move in the Z axis at a certain u-turn rate (I do not have the exact number off hand), but we need to ensure the z axis is not exceeding that on the [PROGRAM] profile. Then we need to assume some level of inaccuracies as the MTP is reactive in nature (we do not know the profile in advance) this it can never be 1:1.
>
> We are open to suggestions in creating a test that can validate the system to everyone's expectations.

### Sample 14
- approx_date: 2025-09
- register: casual
- audience: internal leadership (CRO)
- intent: venting frustration / rhetorical critique
- length: line
- authored_by_me: yes
- notes: Blunt internal reaction; ends on a pointed rhetorical question.

> In order to meet Oct 29, they are going to have to just pencil whip this test or give us a waiver... Why all the pretense at this point?

### Sample 15
- approx_date: 2026-07
- register: professional
- audience: customer (Navy COR)
- intent: technical explanation
- length: short
- authored_by_me: yes
- notes: Opens "Brother [NAME]" (his familiar salutation to trusted government counterparts); the "Technically speaking, no it does..." line is verbatim (an apparent slip he leaves as-is).

> Brother [NAME],
>
> Technically speaking, no it does need a specific orientation, because you calibrate during install. However, for human readability on the GUI and to not confuse sailors, it is recommended you have the front of the antenna as close to the front of the bow (orientation wise) as possible.

### Sample 16
- approx_date: 2026-07
- register: professional
- audience: internal cross-functional group (sales/product)
- intent: giving feedback / gentle pushback on a market idea
- length: short
- authored_by_me: yes
- notes: "I like how you are thinking but..." — a characteristic affirm-then-redirect opener; draws on personal history for authority.

> [NAME],
>
> I like how you are thinking but in my past experience with the [CLIENT], [CLIENT], [CLIENT], and [CLIENT], they are all extremely cost sensitive. The value add we have over a combo [COMPETITOR] / [COMPETITOR] setup (for around [AMOUNT] CAPEX) is in the contested environment, of which they do not participate in. I do have a history of pursuits in this market from the Modem Manufacture standpoint and the biggest takeaway is they want as much throughput as physically possible for as cheap as possible.

### Sample 17
- approx_date: 2026-07
- register: casual
- audience: cross-functional group (same thread as Sample 16)
- intent: adding a follow-on point
- length: line
- authored_by_me: yes
- notes: "One more note," add-on; draws a comparison to make the point land.

> One more note,
>
> Remember these guys are servicing hundreds of people connected to them in an emergency situation. Unlike the military who have at most a couple dozen users on the terminal in a unit.

### Sample 18
- approx_date: 2026-04
- register: professional
- audience: internal peers (sales/product)
- intent: status update + handoff/request
- length: short
- authored_by_me: yes
- notes: Reports a call, names the constraint plainly ("resources are very limited"), delegates the next step.

> [NAME],
>
> I just got off the phone with [NAME] from [VENDOR]. His customer, [COMPANY], has multiple networks to include [CLIENT] and [CLIENT] in which he has been pitching out multi-Beam terminal with [PRODUCT] as the data manager. [COMPANY] would like to see a demo sooner than later, but as we are aware, resources are very limited at the moment.
>
> Please reach out to [NAME] to see how best to accomplish this.

### Sample 19
- approx_date: 2026-04
- register: professional
- audience: internal team ("ALLCON")
- intent: announcement / scheduling heads-up
- length: short
- authored_by_me: yes
- notes: Contains a verbatim typo ("kn9w"), which he leaves in.

> ALLCON,
>
> I just took a call from [NAME] and he has the crane operator coming tomorrow to do a site survey. What he is not sure is if they can do the actual craning by Monday. He would like to know if there is a possibility [NAME] could be there the following week?
>
> He said he would kn9w more by Noon PST tomorrow, but he wanted to give a heads up sooner than later.

### Sample 20
- approx_date: 2025-01
- register: professional
- audience: customer (government contractor)
- intent: relationship note + scheduling follow-up
- length: short
- authored_by_me: yes
- notes: "Hey [Name]," opener; New Year warmth mentioning family before the ask.

> Hey [NAME],
>
> Happy New Year, I hope you had a good break / rest over the last couple weeks; my family and I just relaxed at home and it was fantastic.
>
> I am reaching out to follow up on your last message regarding a meeting on January 30th. Have we confirmed this date and time?

### Sample 21
- approx_date: 2025-01
- register: professional
- audience: customer (government engineers)
- intent: sharing a document / soft pitch
- length: short
- authored_by_me: yes

> [NAME] / [NAME],
>
> As the technical team is currently working on requirements and justifications for moving forward with Phase 3, and potentially Inc 3, I wanted to pass along a very high level multi-antenna whitepaper that our team has put together. Feel free to pass this along to anyone you see fit in the [CLIENT].

### Sample 22
- approx_date: 2025-07
- register: professional
- audience: internal (IT support), cc manager
- intent: logistics request
- length: short
- authored_by_me: yes
- notes: Attributes the ask to someone else ("I was told by [Name] that I need to..."), "Apparently" hedge.

> I was told by [NAME] that I need to let you know that I will be in the UK Office between July 22 and July 25. Apparently something needs to be done to ensure my Teams (on my phone) and my Laptop still work as I will be out of the USA.
>
> Let me know if there is anything else I need to do.

### Sample 23
- approx_date: 2026-07
- register: professional
- audience: vendors/partners
- intent: request (equipment loan)
- length: short
- authored_by_me: yes
- notes: "running up against the wall"; escalates urgency while lowering the bar ("really anything," "literally anything for this purpose will do").

> [NAME] / [NAME],
>
> We are apparently running up against the wall when it comes to testing and validation of the [CLIENT] terminals soon to be out of Alabama as that is where the factory is. We have the one digitizer in the UK for integration testing and validation, but we could really use something (really anything) in Alabama. This just needs to be a L-Band to Ethernet digitizer. It does not have to be a sentry, even an outdoor unit or literally anything for this purpose will do. Do you guys have anything you can loan us temporarily?

### Sample 24
- approx_date: 2026-07
- register: casual
- audience: internal leadership (CRO)
- intent: giving feedback / candid pushback
- length: short
- authored_by_me: yes
- notes: "But two things..." enumerating in prose; "unless we straight out lie, it will be a problem" — plainspoken about integrity.

> That is correct.
>
> [NAME] and [NAME] asked me point blank if we were "legally obligated" of course we do not have contracts that specifically call out [PRODUCT] power supplies.
>
> But two things... The [CLIENT] can still hit the PS limit, so those need to be eventually replaced; I made this abundantly clear. Secondly, as you just stated, it is very obvious looking at the terminal that the [PRODUCT] Bay is completely different then the [PRODUCT] Bay. It is quite obvious it is not what "should" be in that bay. Customers are going to ask, and unless we straight out lie, it will be a problem.

### Sample 25
- approx_date: 2026-06
- register: professional
- audience: internal peers (ops/engineering)
- intent: giving feedback line-by-line on meeting minutes; candor
- length: short
- authored_by_me: yes
- notes: Verbatim from his inline "blue" responses to an action list. "I honestly do not like this question." and "unless we straight out lie" recur as candor markers.

> I honestly do not like this question. We do not have a "contract" with most of these customers, and where we do it does not go into enough detail to describe a [PRODUCT] vs. [PRODUCT] Power supply. Customer expectations, and long term sales are what we need to be discussing. From a legal / contractual standpoint, I think we are good.

### Sample 26
- approx_date: 2026-05
- register: professional
- audience: internal leadership (CRO) + peers
- intent: analysis / explaining a price delta; correcting a premise
- length: short
- authored_by_me: yes
- notes: Opens mid-life ("In the car at the moment... doctors appointment for my wife") then delivers a clean numeric breakdown; ends with a blunt strategic verdict.

> In the car at the moment, and will be for a while as I am headed to a doctors appointment for my wife in DC. I have added [NAME] for clarity here. I do not know what you are talking about with a [AMOUNT] difference, but that is very explainable depending on options chosen (we would need to see the two quotes to explain the difference).
>
> However from a raw numbers point of view. I believe the 2 -> 4 Baseplate is like ~[AMOUNT]. The [PRODUCT] Modem module is ~[AMOUNT]. The [COMPETITOR] antenna is ~[AMOUNT], and one year of [COMPETITOR] service (now required on purchase of antenna) is more than [AMOUNT] (I believe, and [NAME] can give you more accurate numbers). This does not count any other options that may have been removed; again I do not see any quotes on this email to compare to give you more information.
>
> Point being, the reality is from a pure financial standpoint, we do not nor have we ever offered any real value for the upsell of the [PRODUCT].

### Sample 27
- approx_date: 2026-07
- register: casual
- audience: internal peers/leadership (thread)
- intent: giving feedback / raising a risk
- length: line
- authored_by_me: yes

> If we are getting corrosion before even being at sea... This could be a real problem and present in [PRODUCT].
>
> What is our plan for mitigating this? Build a couple hundred fan modules to use as replacements as these things die?

### Sample 28
- approx_date: 2026-07
- register: casual
- audience: internal peers
- intent: recommendation ("in my opinion")
- length: line
- authored_by_me: yes

> We need to get fan modules ready for the [CLIENT] from [NAME]. If these are going to fail, we should be proactive in my opinion.

### Sample 29
- approx_date: 2026-05
- register: professional
- audience: internal engineers/product
- intent: accepting risk with a caveat
- length: line
- authored_by_me: yes
- notes: "is all I am getting at here" — a characteristic clarifying tag.

> I am fine with waiting if it is really a surface scratch. If water does ingress and requires a full terminal replacement (like the [CLIENT]), we are accepting that risk being on us is all I am getting at here.

### Sample 30
- approx_date: 2026-05
- register: casual
- audience: internal engineers
- intent: expressing concern (quick reply)
- length: line
- authored_by_me: yes
- notes: "to be honest" tag; ellipsis.

> Accurate if that scratch is cosmetic... zooming in on picture gives me concern to be honest.

### Sample 31
- approx_date: 2025-03
- register: casual
- audience: customer (Navy counterpart)
- intent: technical detail, familiar tone
- length: line
- authored_by_me: yes
- notes: "Hey Brother," salutation to a trusted government contact.

> Hey Brother,
>
> The part number with 03A does not have the Gain Flattening feature and we had to have [NAME] change it last minute last time to 07A.

### Sample 32
- approx_date: 2025-03
- register: casual
- audience: customer (Navy counterpart)
- intent: light correction / misfire acknowledgment
- length: line
- authored_by_me: yes

> Hahaha,
>
> Yea was meant for [NAME].

### Sample 33
- approx_date: 2025-03
- register: professional
- audience: internal/partner teammate
- intent: thank-you / praise
- length: line
- authored_by_me: yes

> [NAME],
>
> This is excellent and exactly what I was hoping for. Thank you, and your team for the rapid response.

### Sample 34
- approx_date: 2025-03
- register: professional
- audience: internal peers
- intent: evaluation / expressing a preference
- length: line
- authored_by_me: yes
- notes: "This would indeed be unfortunate" — his formal register even in a quick internal note.

> Do we know if [VENDOR] or [VENDOR] can handle 750? This would indeed be unfortunate as I was really leaning towards [VENDOR] based on their technology, professionalism, and what appears to be a strong desire to be a partner.

### Sample 35
- approx_date: 2025-03
- register: professional
- audience: internal (CEO)
- intent: apology / logistics
- length: short
- authored_by_me: yes
- notes: Owns a small oversight without over-apologizing.

> [NAME],
>
> Apologies I did not add you to this email. I was not added to the original thus did not have a reply all function and when I manually added everyone I missed your name.

### Sample 36
- approx_date: 2024-09
- register: professional
- audience: internal leadership (CRO)
- intent: managing expectations
- length: line
- authored_by_me: yes

> We will see what we can do, these are not just published.

### Sample 37
- approx_date: 2025-01
- register: casual
- audience: internal peer (engineer)
- intent: status update, casual
- length: short
- authored_by_me: yes
- notes: "been a crazy week"; life detail ("in the car waiting to drop off my son"); concrete self-commitment with a time window.

> Thanks for the reminder, been a crazy week. I read this in the car waiting to drop off my son. It looks great. I will think about the "Resulting Benefits" section on the drive home and will put pen to paper in about 45 - 60 min.

### Sample 38
- approx_date: 2025-01
- register: casual
- audience: internal peers (engineer, CRO)
- intent: praise + request for sign-off
- length: line
- authored_by_me: yes
- notes: "Excellent work [Name]!" — his standard praise opener; exclamation used sparingly for genuine praise.

> Excellent work [NAME]!
>
> [NAME] / [NAME], I think the document is in it's final form. Please read over it one time and give your approval for me to send to [NAME], [NAME], and [NAME].

### Sample 39
- approx_date: 2025-07
- register: terse
- audience: internal engineering distribution (large)
- intent: technical answer
- length: line
- authored_by_me: yes

> -40 is our current spec; and likely will continue to be.

### Sample 40
- approx_date: 2025-07
- register: professional
- audience: internal leadership (SVP/exec)
- intent: reassurance / process explanation
- length: short
- authored_by_me: yes
- notes: "Absolutely." affirming opener; explains a gate process calmly.

> [NAME],
>
> Absolutely. This is just Gate 0, in which the outcome is suppose to be giving the green light for the resources (Engineering, Delivery) to define exactly what is needed. There are additional gates to approve any work required.

### Sample 41
- approx_date: 2025-07
- register: professional
- audience: vendor (engineer)
- intent: thank-you + status
- length: line
- authored_by_me: yes
- notes: "I needed some good news." — small human aside.

> [NAME],
>
> Thank you, I needed some good news.
>
> Still working on getting the bailment signed for you.

### Sample 42
- approx_date: 2025-07
- register: professional
- audience: internal peers
- intent: request; flags internal-only info
- length: line
- authored_by_me: yes
- notes: Leads with an explicit "*ALL SPACE INTERNAL*" handling marker.

> *ALL SPACE INTERNAL*
>
> [NAME], I know we talked about this the other day in the broader ICD discussion. Do we have STEP files available to send to [VENDOR], or at least an approximate date [NAME] can pass to them?

### Sample 43
- approx_date: 2026-02
- register: terse
- audience: internal peers/leadership
- intent: status/opinion
- length: line
- authored_by_me: yes

> I do not think [NUMBER] terminals is going to be the number anymore.

### Sample 44
- approx_date: 2026-02
- register: professional
- audience: internal peers/leadership
- intent: reminder / reinforcing a priority
- length: line
- authored_by_me: yes

> [NAME],
>
> [NAME] already asked my questions regarding contract funding. I just need to reiterate to everyone we have another deployment plan with the [CLIENT] that we need to honor as well with the [PRODUCT] terminals.

### Sample 45
- approx_date: 2026-02
- register: casual
- audience: vendor/partner
- intent: quick contact request
- length: line
- authored_by_me: yes
- notes: Subject line itself was "Hey Hit me up"; very informal with a trusted contact.

> [NAME],
>
> Hit me up on my cell when you get a chance.

### Sample 46
- approx_date: 2026-02
- register: professional
- audience: vendor (partner engineers)
- intent: scheduling/logistics
- length: line
- authored_by_me: yes

> [NAME],
>
> Yes, [NAME] and I have slots between 9 and 11 on Tuesday.

### Sample 47
- approx_date: 2026-02
- register: professional
- audience: internal peers
- intent: sharing reference info + flagging a concern
- length: short
- authored_by_me: yes
- notes: "Just for reference..." opener; parenthetical noting he already pushed back on the vendor.

> All,
>
> Just for reference...
>
> Previously [NAME] got the LSDR Modems for [AMOUNT] each. This quote has them at ~[AMOUNT] each (I have already questioned [NAME] about this).

### Sample 48
- approx_date: 2025-03
- register: professional
- audience: vendor (external engineer)
- intent: request + probing question
- length: line
- authored_by_me: yes
- notes: "I would assume... What would be the implications of..." — assume-then-ask structure.

> [NAME],
>
> I would assume 0-40C is an acceptable temperature range. What would be the implications of having to do 0-50C?

### Sample 49
- approx_date: 2026-07
- register: terse
- audience: internal peer
- intent: quick answer + loop-in
- length: line
- authored_by_me: yes
- notes: Verbatim typo "Add8ng"; adds a colleague "for validation."

> [NAME],
>
> I am pretty sure it is. Add8ng [NAME] for validation.

### Sample 50
- approx_date: 2026-04
- register: professional
- audience: internal leadership (CRO/service)
- intent: acknowledgment + describing action taken
- length: short
- authored_by_me: yes
- notes: "Will do." then a compact log of what he did; commits to a process change.

> [NAME],
>
> Will do. I called [NAME] immediately (it was already 8PM EST). I then write an email describing what happened. I will add SK moving forward.

### Sample 51
- approx_date: 2024-12
- register: casual
- audience: customer (Navy counterpart)
- intent: banter / rapport
- length: line
- authored_by_me: yes
- notes: Rare bit of levity with a customer.

> Haha, looks that way for the wife.

### Sample 52
- approx_date: 2026-07
- register: professional
- audience: colleague (document author) via document comment
- intent: giving feedback / editorial critique
- length: line
- authored_by_me: uncertain
- notes: Captured as a Word "added a comment" notification, so exact rendering may include system framing; wording is his. Included as an example of his critique voice. First line is a substantive comment on leadership; second is a copy-edit note.

> Arguably it can never be rebuilt through command. It must be earned through actions.

> These exact words are duplicated in a paragraph below. I would reword one of them as it was obvious I read it twice.

## Observed voice patterns

Every observation below is drawn from the samples above; sample numbers are cited in parentheses.

**Sentence rhythm and length.** Ray mixes register by message length, not by audience. His short replies are one or two sentences and land hard (14, 27, 30, 36, 43). His long messages (1, 2, 6) are built from medium-length declarative sentences stacked into a chronological or logical sequence, rarely ornamental. In the long pieces he narrates in strict order — "Monday:… Tuesday:… Wednesday:" (2) or numbered "1.… 2.… 3.… 4." (1, 6) — and keeps each paragraph to a single idea. Even inside a rushed note he'll deliver a clean itemized breakdown (26). The overall feel is an operator thinking on paper: he explains the situation, states what he did or recommends, and stops.

**Formality and how it shifts by audience.** His baseline is professional-neutral and consistent whether writing to a customer, a peer, or the CEO. What shifts is the salutation and the amount of banter, not the diction. With trusted government counterparts he opens "Brother [NAME]" or "Hey Brother" (15, 31) and will drop a "Hahaha" (32) or "Haha, looks that way for the wife" (51); with vendors he can be as loose as "Hit me up on my cell" (45). But his sentence construction stays formal even in casual contexts — "This would indeed be unfortunate" (34), "unless we straight out lie, it will be a problem" (24) — so the tonal range is narrow and controlled. He almost never code-switches into slang mid-sentence.

**Vocabulary and recurring phrases.** Signature connectives: "With that said," (1, 4, 6, 16), "Point being," (26), "Furthermore," (5), "Ultimately," (6), "However" and "However from a raw numbers point of view" (6, 26). He hedges with "Apparently"/"apparently" (14 subject, 22, 23), "I believe," "I am pretty sure" (49), "I do not have the exact number off hand" (12, 13), and "in my opinion" (28). He intensifies sparingly with "abundantly clear" (24), "literally anything" / "really anything" (23), and "absolutely" (40). Candor markers recur: "To be frank"/"very frank" (2), "I honestly do not like this question" (25), "to be honest" (30), "is all I am getting at here" (29). He softens disagreement with an affirm-then-redirect: "I like how you are thinking but…" (16), "Absolutely. This is just…" (40).

**Punctuation and formatting habits.** Heavy user of the trailing ellipsis "..." to mark a pause or an implied "and you see where this goes" (14, 23, 24, 27, 30, 47, 49). Frequent parentheticals to add caveats or sourcing — "(I believe, and [Name] can give you more accurate numbers)" (26), "(I have already questioned [Name] about this)" (47), "(orientation wise)" (15). Uses quotation marks around contested or borrowed terms: "requirements" (7), "legally obligated" (24), "used" / "NOS" (PSU thread), "dictate" (1). Numbered lists appear inline in prose ("1. … 2. …") rather than as bullet blocks (1, 6, 11, 24). Greeting is almost always "Name," or "Name / Name," on its own line, followed by a blank line. Occasional em-dash-free style — he prefers periods and semicolons; he uses semicolons fairly often to join related clauses ("…as spare antenna's long term; " / "let alone the footprint issues;"). ALLCON and "*ALL SPACE INTERNAL*" are his group-address and handling conventions (2, 6, 19, 42). No emoji in his own prose. Capitalizes program/product nouns.

**Greetings and sign-offs by register.** Formal/professional and casual alike open with the first name and a comma ("[Name]," — most samples), or two names slashed ("Joel / Keith," "Scott / Kurt," 8, 21, 23). Familiar customers get "Brother [Name]," or "Hey [Name]," (15, 20, 31). Group sends open "ALLCON," or "All," (2, 6, 19, 47). Sign-offs are minimal: he most often just ends on the last sentence with no closing word, sometimes "Thanks," (4) or "Thank you," and occasionally a warm full sentence ("Thank you very much for everything." 9; "I wish you well… they will be lucky to have you." 3). He does not use "Best" or "Regards" himself (those appear only in others' quoted text).

**Signature moves.** (1) Reports firsthand action as evidence — "I just got off the phone with…", "I just took a call from…" (9, 18, 19). (2) Invites correction at the end of anything analytical — "please feel free to correct me…", "[Name] can give you more accurate numbers" (6, 26). (3) Cites his own prior experience for authority — "in my past experience with…", "I do have a history of pursuits in this market" (16). (4) Owns imprecision openly rather than bluffing — "I just kind of latched on to that (I have no empirical proof…)" (12), "if I am wrong… it just demonstrates my lack of understanding" (6). (5) Threads personal life into work notes matter-of-factly — dropping off his son, doctor's appointment for his wife, family relaxing over the break (37, 26, 20). (6) Frames complex questions by mapping which function/person should own each piece (11). (7) A recurring integrity beat: names the honest/legal thing plainly ("unless we straight out lie," 24; "Nothing that implies we are not following the law," 11).

**Anti-patterns (things he rarely or never does).** He does not use emoji, exclamation points except for genuine praise ("Excellent work [Name]!", 38), or hype adjectives ("amazing," "incredible"). He does not write with bulleted marketing formatting in his own prose. He does not use "Best/Regards/Cheers" sign-offs. He rarely gushes or over-apologizes — apologies are one clause and factual (35, "Apologies I did not add you… I missed your name"). He avoids corporate throat-clearing like "I hope this email finds you well" (that phrasing shows up only from counterparts, not him). He doesn't soften bad news into vagueness; he states the risk directly (24, 27, 29). He leaves his own typos in ("kn9w," "Add8ng," "9n," "then" for "than," "there end," "it's" for "its") — his sent mail is fast and unpolished, not fussed over.

**Registers with thin coverage.** Nearly all available mail is defense/B2B work correspondence. There is little to no: purely external formal prose to non-government commercial partners; long persuasive/marketing copy authored by him (he shares decks/whitepapers others wrote rather than writing the pitch prose himself, 21); public-facing announcements; personal/HR self-advocacy beyond short logistics; or a substantive apology for a real error. A voice model should be cautious extrapolating him into polished long-form marketing or effusive relationship writing — his warmth shows up in short, plain asides, not extended sentiment.
