# Real-SERP Competitor Intelligence Audit: Teer Keyword Clusters

**Auditor:** Expert SEO Competitor Intelligence Auditor  
**Date:** November 9, 2026  
**Methodology:** Live Google SERP extraction, Direct HTTP/DNS-over-HTTPS (DoH) inspection, Full HTML parsing (BeautifulSoup4), Heading/Word Count/Table/Schema/Ad-Network Reverse Engineering across 25 competitor URLs.

---

## Executive Summary & Market Landscape

| Cluster | Focus Keywords | Monthly Volume | KD | Top Competitor Strategy | Vulnerability Level | Our Exploitation Angle |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Khanapara Teer** | `khanapara teer result`, `khanapara teer list` | **3.35M** | 20 | Dedicated EMD (`khanapara.com`) + News portal (`goodreturns.in`) | **Medium** | Interactive live countdown, Instant Date Search in 2017–2026 archive, Morning/Night tabs |
| **2. Juwai Teer** | `juwai teer result`, `juwai teer` | **1.50M** | 41 | News portal (`goodreturns.in`) dominates; niche sites broken or <50 words | **VERY HIGH** | First fast dedicated Juwai hub with valid SSL, clear schedule timeline & dedicated common numbers |
| **3. Previous Results** | `shillong teer previous result`, `teer previous result` | **823K** | 18 | Raw 1,500+ row unpaginated tables (`shillongteerground.com`, `goodreturns.in`) | **HIGH** | Searchable/Filterable archive by date, house, ending; Hot/Cold number frequency analysis |
| **4. Common Numbers** | `shillong teer common number`, `teer common number` | **1.50M** | 31 | Ultra-thin utility pages (45–300 words), zero formulas, zero schemas | **VERY HIGH** | Deep analytical formula breakdown (FR+SR arithmetic, Club Chart cross-calc), interactive calculator |
| **5. Bhutan Teer** | `bhutan teer result` | **450K** | 12 | Generic homepages with 2 table rows; no dedicated landing pages | **EXTREME (Easiest Win)** | Dedicated `/bhutan-teer-result` page, Morning & Day timings, full monthly scorecard |

---

## Detailed Competitor Audit by Keyword Cluster

### Cluster 1: "Khanapara Teer Result" & "Khanapara Teer List"
* **Search Volume:** 3,350,000 / mo | **Keyword Difficulty:** 20 | **Target Intent:** Real-time winning numbers (F/R 4:15 PM, S/R 5:00 PM) & Historical number archives.

#### Top Ranking URLs Audited:
1. `https://khanapara.com/` (Home / Live Result Page)
2. `https://khanapara.com/khanapara-previous-result/` (Archive / Previous List)
3. `https://www.goodreturns.in/khanapara-teer-results.html` (Goodreturns Daily Result)
4. `https://www.goodreturns.in/khanapara-teer-results-chart.html` (Goodreturns Monthly/Yearly Chart)
5. `https://teer-results.com` (Multi-Teer Aggregator)

#### Verified On-Page & Technical Breakdown:
* **Page Titles:**
  - `khanapara.com`: `Khanapara Teer Result Today F/R & S/R | Live Assam Teer 2026` (Length: 60 chars — Perfect exact-match keyword placement).
  - `khanapara.com/khanapara-previous-result/`: `Khanapara Teer Previous Result List (2017–2026) | F/R & S/R Archive` (Length: 70 chars).
  - `goodreturns.in`: Dynamic date insertion: `Khanapara Teer Results Today On November 9, 2026 | Khanapara Teer Today First & Second Round Results - Goodreturns` (Length: 122 chars — Truncated on Google SERP).
  - `teer-results.com`: `Teer Results` (Extremely poor, lacks target keyword).
* **Headings Structure:**
  - `khanapara.com`: H1: `Khanapara Teer Result Today · F/R 4:15 PM, S/R 5:00 PM (2026)`. H2s cover user intent: *What is Khanapara Teer?*, *Khanapara Teer Result Time*, *How Calculated*, *Common Number Today*, *Prize Money*, *Previous Result List*, *FAQ*.
  - `khanapara.com/khanapara-previous-result/`: H1: `Khanapara Teer Previous Result List (2017–2026)`. H2s: *How to Read the List*, *Why Previous Result Matters*.
  - `goodreturns.in`: H1: `Khanapara Teer Results Today`. H2s: *Today's Results*, *Last 30 Days (Regular, Morning, Night)*, *Timings*, *FAQs*.
* **Word Count & Content Depth:**
  - `khanapara.com`: 1,120 words (Solid informational content alongside the table).
  - `khanapara.com/khanapara-previous-result/`: 14,429 words (Heavy archive list spanning 2017 to 2026).
  - `goodreturns.in`: 2,374 to 4,842 words (Automated tabular data + boilerplate explanations).
  - `teer-results.com`: 953 words.
* **Table Structure:**
  - `khanapara.com`: 1 table with 31 rows (Current month history), headers `['Date', 'F/R (4:15)', 'S/R (5:00)']`.
  - `khanapara.com/previous`: 10 tables, table 1 has 261 rows (2026), table 2 has 304 rows (2025), etc.
  - `goodreturns.in`: 4 separate tables on daily page (`Date`, `Day`, `FR`, `SR`) separating Regular, Morning, and Night teer. 12 monthly tables on chart page.
* **UI Layout & Ad Clutter:**
  - `khanapara.com`: Fast, clean HTML, Google AdSense only. Mobile layout is readable but lacks interactive search/filtering for old years.
  - `goodreturns.in`: Excessive ad clutter. Google AdSense + MGID clickbait widgets + floating video ads. Page weight: 498KB–613KB HTML alone, 4.5MB total resources. Terrible mobile performance on Northeast 3G/4G.
* **Schema Markup:**
  - `khanapara.com`: Organization, WebSite, FAQPage, BreadcrumbList.
  - `goodreturns.in`: WebPage, Organization, BreadcrumbList, FAQPage.
  - `teer-results.com`: None (0 schemas).

#### Critical Competitor Gaps & Exploitation Strategy:
1. **No Interactive Date Filtering / Search:** On `khanapara.com/khanapara-previous-result/`, users must scroll through 10 gigantic tables with 2,500+ rows. We can implement an instant AJAX/JS search bar ("Select Year/Month" or "Type Date") to jump directly to any result.
2. **Missing Morning & Night Segmentation in Dedicated Sites:** `khanapara.com` focuses heavily on the 4:15 PM regular draw, neglecting Khanapara Morning (11:30 AM) and Night (8:30 PM). Goodreturns captures this traffic. By offering clear tabbed navigation (`Day (4:15 PM) | Morning (11:30 AM) | Night (8:30 PM)`), we capture all sub-cluster queries.
3. **No Live Status / Countdown Component:** None of the competitors have an animated countdown clock or real-time status pill (`Awaiting draw`, `Live updating...`, `Declared`).

---

### Cluster 2: "Juwai Teer Result" & "Juwai Teer"
* **Search Volume:** 1,500,000 / mo | **Keyword Difficulty:** 41 | **Target Intent:** Fast results for Juwai (Day: 2:00 PM & 2:35 PM, Morning: 10:30 AM, Night: 7:30 PM).

#### Top Ranking URLs Audited:
1. `https://www.goodreturns.in/juwai-teer-results.html`
2. `https://www.goodreturns.in/juwai-teer-results-chart.html`
3. `https://teer-results.com`
4. `https://teerresults.com`
5. `https://teertooday.com`
*(Note: Dedicated domain `teerjuwai.com` was inspected and found failing with SSL Handshake Failure and HTTP 409 errors).*

#### Verified On-Page & Technical Breakdown:
* **Page Titles:**
  - `goodreturns.in`: `Juwai Teer Results Today On November 9, 2026 | Juwai Teer Today First & Second Round Results - Goodreturns` (Captures exact keyword).
  - `teerresults.com`: `Teer Results: Official website of Shillong Teer and Khanapara Teer` (**Critical Mistake:** Completely omits "Juwai" from `<title>`!).
  - `teertooday.com`: `Teer | Shillong | Teer Results Online: teertooday.com` (Completely omits "Juwai" from `<title>`!).
  - `teer-results.com`: `Teer Results` (No keyword).
* **Headings Structure:**
  - `goodreturns.in`: H1: `Juwai Teer Results Today`. H2s: `Today's Juwai Teer Results`, `Juwai Teer Result – Last 30 Days`, `Juwai Morning Teer Result – Last 30 Days`, `Juwai Night Teer Result – Last 30 Days`, `Juwai Teer Result Timings`, `Juwai Teer Result FAQs`.
  - `teerresults.com`: H1: `Teer Results`. H2: `Juwai Teer Results` (Only a single H2, zero descriptive text).
  - `teertooday.com`: 0 H1 tags! Only H2 is the raw date `07-11-2026`.
* **Word Count & Content Depth:**
  - `goodreturns.in`: 2,373 words (Daily) & 4,731 words (Chart).
  - `teerresults.com`: **Only 10 words** of visible text!
  - `teertooday.com`: **Only 43 words** of visible text!
  - `teer-results.com`: 953 words (generic multi-teer text).
* **Table Structure:**
  - `goodreturns.in`: 4 tables (Daily FR/SR, Last 30 days Regular, Morning, Night). 12 monthly tables on Chart page.
  - `teer-results.com`: 1 minimal table row: `F/R (2:00PM)` and `S/R (2:35PM)`. Sample: `16 | 43`.
  - `teerresults.com`: 0 static HTML tables (rendered via client-side scripts, invisible to search engines that do not render heavy JS).
* **UI Layout & Ad Clutter:**
  - Niche sites look like broken 1990s HTML tables with no mobile responsiveness.
  - `goodreturns.in` is overloaded with MGID native ads and video units.
* **Schema Markup:**
  - `goodreturns.in`: WebPage, Organization, BreadcrumbList, FAQPage.
  - All niche sites (`teerresults.com`, `teertooday.com`, `teer-results.com`): 0 relevant schemas.

#### Critical Competitor Gaps & Exploitation Strategy:
1. **Severe Niche Competitor Weakness:** The dedicated niche sites for Juwai are virtually abandoned, lack text, lack schema, and have title-tag blunders. Goodreturns only ranks because of domain authority.
2. **Missing Dedicated Hub:** No site provides a specialized, mobile-first experience for Juwai players.
3. **Timing Confusion:** Juwai draws earlier than Shillong and Khanapara (Round 1: 2:00 PM, Round 2: 2:35 PM). Competitors do not highlight this clearly, causing user frustration.
4. **Action Plan:** Launch a dedicated `/juwai-teer-result` page featuring:
   - Live result cards with 2:00 PM & 2:35 PM countdowns.
   - 3-tier sub-tabs: Juwai Day, Juwai Morning (10:30 AM), and Juwai Night (7:30 PM).
   - FAQ schema and SportsEvent/Table schema.

---

### Cluster 3: "Shillong Teer Previous Result" & "Teer Previous Result"
* **Search Volume:** 823,000 / mo | **Keyword Difficulty:** 18 | **Target Intent:** Historical archives, verifying past winning numbers, trend analysis.

#### Top Ranking URLs Audited:
1. `https://shillongteerdaily.in`
2. `https://www.goodreturns.in/shillong-teer-results-chart.html`
3. `https://teer-results.com/prev-result.php`
4. `https://shillongteerground.com/previous-results/`
5. `https://teerresults.com/previous-results-2026.php`

#### Verified On-Page & Technical Breakdown:
* **Page Titles:**
  - `shillongteerground.com/previous-results/`: `Teer Previous Results | Shillong Teer Ground` (Clean keyword match).
  - `goodreturns.in`: `Shillong Teer Chart | Shillong Teer Results Chart 2026 | Shillong Teer Previous Results Chart With Number - Goodreturns` (Targeted).
  - `teerresults.com/previous-results-2026.php`: `Teer Results: Previous Teer Results 2026`.
  - `teer-results.com/prev-result.php`: `Prev Result | Teer Results` (Weak).
  - `shillongteerdaily.in`: `Shillongteerdaily.in | Shillong Teer Result Today` (Homepage targets live rather than archive).
* **Headings Structure:**
  - `shillongteerground.com/previous-results/`: **0 H1 tags!** Only a single H2: `Previous Results`. No H3s.
  - `goodreturns.in`: H1: `Shillong Teer Results Chart`. 10 H2s: Month-by-month headings for 2026.
  - `teerresults.com/previous-results-2026.php`: H1: `Teer Results`, `PREVIOUS TEER RESULTS`. H2: `Check Previous Juwai Teer Results` (Internal content mismatch!).
  - `teer-results.com/prev-result.php`: H1: `OFFICIAL SHILLONG TEER SPORT'S SCORE`. H2: `Download Our App Today:`.
* **Word Count & Content Depth:**
  - `shillongteerground.com/previous-results/`: 7,848 words (A pure raw data dump of past dates).
  - `goodreturns.in`: 9,375 words across 12 tables.
  - `teerresults.com/previous-results-2026.php`: 1,362 words.
  - `teer-results.com/prev-result.php`: **Only 79 words** (Empty shell).
* **Table Structure:**
  - `shillongteerground.com`: **1 monstrous table with 1,568 rows!** (`Date | F/R | S/R`, sample: `20-03-2020 | 55 | 86`). Unpaginated, infinite scroll.
  - `goodreturns.in`: 12 tables, up to 121 rows per table.
  - `teerresults.com`: 1 table with 264 rows.
* **UI Layout & Ad Clutter:**
  - `shillongteerground.com`: Extremely aggressive monetization. Injected with **Adsterra** popunders and Google AdSense banners. Clicking anywhere triggers unwanted full-screen tabs.
  - `shillongteerdaily.in`: Google AdSense + Monetag push/vignette ads.
  - `goodreturns.in`: Page weight is an astonishing **802KB HTML**! Takes 4+ seconds to load.
* **Schema Markup:**
  - `goodreturns.in`: WebPage, Organization, BreadcrumbList, FAQPage.
  - `shillongteerground.com`, `teerresults.com`, `teer-results.com`: **0 schemas!**

#### Critical Competitor Gaps & Exploitation Strategy:
1. **Unusable Mobile UX (1,568-Row Dump):** On mobile, scrolling through 1,500+ rows is painful. Users cannot easily jump to a specific month or year.
2. **Total Lack of Search / Query Filter:** Not one competitor allows filtering by number (e.g. "Show every date where FR was 55").
3. **No Frequency Analytics:** Serious teer players track repeat rates, house frequency, and ending frequencies. Offering a simple statistical summary ("Most frequent numbers this month") will drive massive user retention and repeat visits.
4. **Action Plan:** Build a blazing-fast, paginated Previous Results engine with:
   - Date picker + Quick Year selector (2024, 2025, 2026).
   - "Filter by House / Ending / Number" search input.
   - Clean UI without popunders or interstitial traps.

---

### Cluster 4: "Shillong Teer Common Number" & "Teer Common Number"
* **Search Volume:** 1,500,000 / mo | **Keyword Difficulty:** 31 | **Target Intent:** Daily mathematical predictions, Target numbers, House, Ending, Direct numbers.

#### Top Ranking URLs Audited:
1. `https://teerofshillong.com`
2. `https://shillongteerground.com/common-numbers/`
3. `https://teerresults.com/common-numbers.php`
4. `https://teer-results.com/vip-common-number.php`
5. `https://teerresults.com/teer-formula.php`

#### Verified On-Page & Technical Breakdown:
* **Page Titles:**
  - `shillongteerground.com/common-numbers/`: `Shillong Teer Common Numbers | Shillong Teer Ground` (Targeted).
  - `teerresults.com/common-numbers.php`: `Teer Results: Shillong Teer Common Numbers, Khanapara Teer Common Numbers`.
  - `teerofshillong.com`: `Teer | Teer Result | Shillong Teer | Khanapara | Juwai Teer results today` (Keyword stuffing title, omits "Common Number").
  - `teer-results.com/vip-common-number.php`: `VIP & Common Number | Teer Results`.
  - `teerresults.com/teer-formula.php`: `SHILLONG TEER FORMULA | KHANAPARA TEER FORMULA`.
* **Meta Descriptions:**
  - `shillongteerground.com`: `Get Teer Common Numbers` (Extremely thin — only 4 words!).
  - `teerresults.com/teer-formula.php`: Contains embarrassing typos: `Learn how to claulte Shillong Teer numbers...` ("claulte").
  - `teer-results.com`: `None`.
* **Headings Structure:**
  - `shillongteerground.com`: H1: `Shillong Teer Common Numbers`. H2: `Date:—`. Zero analytical content.
  - `teerresults.com/common-numbers.php`: H1: `Teer Results`. H2s: `Welcome`, `07-11-2026`, `TEER COMMON NUMBERS`, `Juwai Numbers`, `Shillong Numbers`, `Khanapara Numbers`.
  - `teer-results.com/vip-common-number.php`: H1: `OFFICIAL SHILLONG TEER SPORT'S SCORE`. H2s: `Download App`, `Shillong Common Number`, `Bhutan Common Number`.
* **Word Count & Content Depth:**
  - `shillongteerground.com/common-numbers/`: **Only 46 words!** (Extreme thin content vulnerability).
  - `teer-results.com/vip-common-number.php`: **Only 45 words!**
  - `teerresults.com/common-numbers.php`: 339 words.
  - `teerresults.com/teer-formula.php`: 296 words.
  - `teerofshillong.com`: 932 words.
* **Table Structure:**
  - All use standard 3 columns: `Direct | House | Ending`.
  - Example on `teerresults.com`:
    - Direct: `24, 78, 91`
    - House: `2, 7`
    - Ending: `4, 8`
  - On `teer-results.com/vip-common-number.php`, the tables are empty shells (1 row with headers only).
* **UI Layout & Ad Clutter:**
  - Popunder ads from Adsterra on `shillongteerground.com`.
  - Fake "VIP Number" click triggers.
* **Schema Markup:**
  - 0 schemas across `shillongteerground.com`, `teer-results.com`, `teerofshillong.com`. Only `teerresults.com` has a generic `WebSite` schema.

#### Critical Competitor Gaps & Exploitation Strategy:
1. **Severe "Thin Content" Penalty Risk:** The top competitors provide under 50 words of real text. This makes them highly susceptible to Google's Helpful Content System updates.
2. **Zero Transparency & Calculation Methodology:** None explain *how* common numbers are calculated. Players know numbers come from mathematical formulas (e.g. Previous Day F/R + S/R sum formula, Club Chart cross-referencing, Dream Number symbolism).
3. **No Responsible Gaming Warning:** None display ethical disclaimers (e.g., "Common numbers are mathematical speculations based on historical frequency, not guaranteed outcomes").
4. **Action Plan:** Create a high-EEAT `/shillong-teer-common-number` guide featuring:
   - Daily calculated House, Ending, and Direct numbers.
   - Explanation of the 3 main calculation formulas (Previous day addition, Date formula, House-Ending pairing).
   - Dream Number quick lookup dictionary.
   - Comprehensive FAQ Schema & HowTo Schema.

---

### Cluster 5: "Bhutan Teer Result"
* **Search Volume:** 450,000 / mo | **Keyword Difficulty:** 12 | **Target Intent:** Live results for Bhutan Morning (10:30 AM / 11:30 AM) and Bhutan Day (4:15 PM / 5:15 PM).

#### Top Ranking URLs Audited:
1. `http://teerresult.co`
2. `https://teer-results.com`
3. `https://teertooday.com`
4. `https://shillongteerdaily.in`
5. `https://teerresults.com`

#### Verified On-Page & Technical Breakdown:
* **The State of the Bhutan SERP (Massive Opportunity):**
  - **KD is only 12** with **450K monthly searches**.
  - **Not a single top ranking domain has a dedicated `/bhutan-teer-result` page!**
  - They are all ranking via generic homepages that lump Bhutan in as an afterthought at the bottom of the page.
* **Competitor Status & Failures:**
  - `teerresult.co`: Trapped behind a Cloudflare challenge screen (`One moment, please...`, 11 words, 0 tables).
  - `teer-results.com`: Only 2 table rows on its homepage (`Bhutan Morning Results` and `Bhutan Teer Results`, 953 words generic multi-teer text).
  - `teertooday.com`: 43 words total, 0 H1s.
  - `shillongteerdaily.in`: 0 dedicated Bhutan tables.
  - `teerresults.com`: 10 words total.
* **Headings Structure:**
  - 0 competitors have an H1 dedicated to "Bhutan Teer Result Today".
  - H2s are either nonexistent or generic date stamps.
* **Table Structure:**
  - Minimal 2-column tables: `F/R | S/R` with times.
* **Schema Markup:**
  - 0 schemas for Bhutan Teer across all sites.

#### Critical Competitor Gaps & Exploitation Strategy:
1. **Complete Lack of Dedicated URL Authority:** Because competitors try to rank for Shillong, Khanapara, Juwai, and Bhutan all on one single homepage, a dedicated, fast, mobile-optimized URL `https://.../bhutan-teer-result` with exact meta tags, H1, FAQ, and structured tables will achieve top 3 rankings rapidly.
2. **Domain Outages & Instability:** Several niche Bhutan domains (`teerbutan.com`, `teerbhutanmorning.com`) suffer from DNS timeouts and server errors. A reliable, 99.9% uptime site will win user trust and search rankings immediately.
3. **Action Plan:** Launch a dedicated `/bhutan-teer-result` page with:
   - Dedicated Morning (10:30 AM & 11:30 AM) and Day (4:15 PM & 5:15 PM) live result tables.
   - Bhutan previous result monthly archive.
   - Clear FAQ schema explaining draw timings, rules, and calculation.

---

## Technical & On-Page SEO Comparison Matrix

| Factor | Khanapara.com | Goodreturns.in | ShillongTeerGround | TeerResults.com | Teer-Results.com | **Our Blueprint Site** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Page Speed / Weight** | ~43 KB (Fast) | 500–800 KB (Very Slow) | ~100 KB (Medium) | ~26 KB (Fast) | ~27 KB (Fast) | **< 35 KB (Ultra Fast)** |
| **Ad Clutter** | Moderate (AdSense) | Extreme (MGID + Video) | Intrusive (Adsterra popups)| Moderate (AdSense) | Moderate (AdSense) | **Clean (Native Ads / High CPM)** |
| **Mobile Responsiveness** | Fair | Poor (Heavy shifts) | Terrible (1,500-row scroll) | Outdated HTML tables | Cluttered | **100% Mobile-First / Flex & Grid** |
| **Schema Markup** | Org, WebSite, FAQ | WebPage, Org, FAQ | None | WebSite only | None | **LiveBlogPosting, FAQ, SportsEvent** |
| **Interactive Search** | None | None | None | None | None | **Instant Date & Number Search** |
| **Live Timers / Badges**| None | None | None | None | None | **Real-Time Countdown & Status** |
| **Thin Content Risk** | Low (1,120 words) | Low (2,000+ words) | High (<50 words on subpages)| High (<300 words) | High (<50 words on VIP) | **Optimal (800–1,500 rich words)** |

---

## Key Tactical Recommendations for Outranking Competitors

1. **Deploy Dedicated URL Architecture:**
   - `/khanapara-teer-result` (Dedicated Live & Today Result)
   - `/khanapara-teer-previous-result-list` (Interactive 2017–2026 Archive with Search)
   - `/juwai-teer-result` (Immediate capture of #1 spot from broken competitors)
   - `/shillong-teer-previous-result` (Paginated, searchable archive with hot/cold metrics)
   - `/shillong-teer-common-number` (High-EEAT guide with formula breakdown)
   - `/bhutan-teer-result` (Immediate win in KD 12 vacuum)
2. **Implement Interactive Utility Features Competitors Lack:**
   - **Live Draw Countdown Timer:** Visual countdown to exact round timings.
   - **Instant Date Picker & Number Filter:** Dropdown/search for previous result tables.
   - **Formula Calculator:** User enters yesterday's FR/SR and receives predicted House & Ending.
3. **Speed & UX Supremacy:**
   - Clean, lightweight HTML (<35KB), avoiding the 600KB+ bloat and intrusive popunders of `goodreturns.in` and `shillongteerground.com`.
   - 0 layout shifts (CLS < 0.05), First Contentful Paint < 0.8s on 4G networks.
4. **Rich Schema Markup:**
   - Add `FAQPage` schema on every cluster page.
   - Add `SportsEvent` or `Table`/`Dataset` schema for result logs.
   - Add `BreadcrumbList` for structural crawl clarity.
