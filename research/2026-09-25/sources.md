# Source and verification record

Accessed 25 September 2026. Sources were found by following the existing 1994 automotive testing-institution provision. This was a targeted search, not an exhaustive review. No source independently validates the research design.

| ID | Document and locator | Provenance and limitation |
|---|---|---|
| S01 | [汽车工业产业政策](https://news.sina.com.cn/o/2004-06-02/11322697046s.shtml), Article 18 | Sina reprint dated 2004-06-02, attributed to People's Daily Online, reproducing the 1994 policy. Existing project source; not an inspected original gazette. Supports policy intent only. |
| S02 | [汽车质量监督检验和新产品鉴定试验机构暂行管理办法](https://policy.mofcom.gov.cn/claw/clawContent.shtml?id=3985), dated 1994-08-24; Articles 3, 6–7, 10, 14–15 | Ministry of Commerce database reproduction, explicitly sourced from 北大法宝. Issuing body: 机械工业部. Original formal text not inspected. Used as a historical rule, not a statement of current legal validity. |
| S03 | [关于12家新生产机动车排放污染检测机构增加检测业务的通知](https://www.mee.gov.cn/gkml/zj/bgt/200910/t20091022_173901.htm), 环办〔2005〕13号; metadata and attachment rows 1–12 | Primary administrative notice, issued by 国家环保总局办公厅; hosted by the Ministry of Ecology and Environment. Document date 2005-01-26, index 000014672/2005-00036. Main empirical source. Table describes scope-specific qualification and venues, not realized transactions. |
| S04 | [实验室认可、资质认定历程](https://www.tatc.com.cn/mobile/quality), historical bullets for 1987, 1988, 1990, 1994–95 and 2002 | Testing center's own retrospective account; page publication date unspecified. Describes transfers, preparation and accreditation. Cited underlying approval documents were not retrieved. Current qualifications must not be projected backward. |
| S05 | [争做交通强国科技先锋，助力首都交通智慧发展](https://www.beijing.gov.cn/gate/big5/www.beijing.gov.cn/renwen/jrbj/kjcx/201810/t20181030_1874038.html), 2018-10-30, section on earlier planning and construction | Beijing government portal reprinting 北京日报, by 康健. Retrospective newspaper account, not a contemporary project approval or an independent engineering audit. Used for chronology only. |

## S03 extraction and provenance

- Local HTML retrieved directly from the official URL on 2026-09-25; **84,444 bytes**.
- SHA256: `4d554545285bce77b1ebee18f7b3e20735b8554922e5988b2bdc453d65b45e01`.
- Encoding: UTF-8. Source title, date and document identifier checked against page metadata and body.
- Included columns: printed serial number, institution name, test project, test venue. Removed HTML formatting whitespace. Preserved punctuation and historical names.
- Excluded contact names, telephone/fax numbers, addresses and email addresses. Full HTML retained locally for verification, not included in the public package.
- The table uses rowspan for contact subrows. The parser keeps the numbered institution rows only; it does not fill contact subrows into extra observations.
- Split venue cells on `、`, producing the long-form links. No inferred ownership, modern name matching, capacity weighting or missing-as-zero substitution.
- Compared all twelve extracted institution/venue rows to the official table during preparation. This was an AI-assisted source check, **not** independent double coding.
- Verified exact reproduction from the saved HTML and separately from the committed transcription. The script rejects unexpected source identifiers, missing/duplicate row IDs, mixed scope, and unmapped venue names.

The HTML fingerprint may change with the website shell while the table stays the same. Re-extraction checks the included fields; a new fingerprint alone does not prove that research data changed. If the page is unavailable, offline reproduction checks calculations but cannot independently authenticate the transcription.

## Historical names and linkage limits

`V01` is exactly `交通部公路交通实验场` in S03. S05 describes the Ministry's 公路交通综合试验场 at Tongzhou. Treating these as the same historical ground is a **working contextual match**, based on Ministry affiliation and the reported site history, rather than a verified persistent facility identifier. The counts in this release use only exact venue strings within S03 and do not depend on that cross-source match. Verify original project identifiers before joining a facility-year panel.

Tianjin's lineage in S04 is linked provisionally to S03 row 4 through the named national passenger-car inspection center. Corporate/legal identity over time has not been fully reconstructed. A center, its parent organization and an external proving ground must remain separate entities.

## Why these sources do not form a causal chain

S01 sets industrial-policy intent. S02 regulates testing institutions and cites the Product Quality Law. S03 explicitly cites 环办〔2000〕116号, an environmental-regulator qualification circular. Their common testing theme does not establish that S01 funded a specific project or caused S03. The original project approvals, intervening decisions, client records and counterfactual remain missing.
