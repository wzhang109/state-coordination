# Prompt / Output Log Template

Use this template to document AI-assisted coding runs. Do not rely on undocumented prompts for final measurement.

| Field | Description |
|---|---|
| run_id | Unique identifier for the coding run |
| date | Date of run |
| model | Model name/version |
| prompt_version | Version of prompt used |
| rubric_version | Version of coding rubric used |
| source_batch | Source documents included |
| input_fields | Fields supplied to the model |
| output_schema | Expected structured output fields |
| reviewer | Human reviewer |
| benchmark_sample | Benchmark file or sample identifier |
| known_issues | Known model/prompt limitations |
| decision | Accepted, revised, or rejected |

## Minimal structured output schema

```json
{
  "source_id": "string",
  "sector": "string",
  "year": 1980,
  "dimension": "persistence | specificity | network_breadth | allocation",
  "score": 0,
  "evidence": "short passage excerpt or source reference",
  "reasoning_summary": "brief explanation tied to rubric",
  "confidence": "low | medium | high",
  "review_status": "needs_review | accepted | revised"
}
```
