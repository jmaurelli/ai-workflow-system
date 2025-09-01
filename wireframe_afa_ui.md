# Log Viewer UI (Lo-Fi Wireframe with Pass/Fail Indicators)

-----------------------------------------------------------------
| ✅ Connectivity | [Search Box] [Filter ▼] [Export ⬇]          |
| ❌ VSSH         |----------------------------------------------|
| ✅ Data Collect |                                              |
| ❌ Data Parsing |                  LOG VIEWER                  |
| ✅ Report Anal. |                                              |
|                 |  [2025-08-18 12:00:00] ModuleX - INFO ...    |
|                 |  [2025-08-18 12:00:01] ModuleY - ERROR ...   |
|                 |  [2025-08-18 12:00:02] ModuleY - STACK ...   |
|                 |                                              |
|                 |  (continuous scrollable raw logs)            |
|                 |                                              |
|                 |----------------------------------------------|
|                 | Context Window:  ⬅ 10 lines ➡  [Configure]  |
-----------------------------------------------------------------

Legend:
- ✅ / ❌ indicate **stage pass/fail status**
- Left-hand column: **Stage Chips** (clickable to jump to logs)
- Top row: **Search / Filter / Export controls**
- Center: **Main raw log viewer (scrollable, syntax highlighted)**
- Bottom: **Context window size controls**
