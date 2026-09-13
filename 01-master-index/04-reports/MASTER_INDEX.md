---
id: DOC-CLX-037
folder_id: FS-IDX-005
tipo: documento-importado
status: confirmado
origem: export-claude-20260913
origem_filename: "MASTER_INDEX.md"
sha256: df03ca32b9ac1a9183be24309bbfbe3c9e27b2ad0bcb64826714c7d1c365891b
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

# MASTER INDEX · EXECUTAR SCANNER

```yaml
master_index:
  id: EXECUTAR_SCANNER_MASTER_INDEX
  version: 1.0
  language: pt-BR
  status: active
  root_document: DENSE_SCANNER_PRD_FRD_SPECS.md
  purpose: enable deterministic navigation and retrieval by AI agents
```

# 01 · CANONICAL FILES

| Priority | File | Role | Authority |
|---|---|---|---|
| 1 | DENSE_SCANNER_PRD_FRD_SPECS.md | Canonical PRD + FRD + Specs + AI handoff | Primary |
| 2 | MASTER_INDEX.md | Navigation, authority, IDs and retrieval map | Index |

# 02 · DOCUMENT AUTHORITY

```yaml
authority_order:
  1: explicit_source_defined_requirements
  2: canonical_dense_document
  3: derived_engineering_structures
  4: implementation_suggestions

conflict_rule:
  - explicit_source_defined_behavior_wins
  - open_questions_must_remain_open_until_decided
  - repository_existing_contracts_win_over_suggested_names
```

# 03 · SECTION MAP

| Section | Domain | Primary IDs |
|---|---|---|
| 00–03 | Product context and channels | EXECUTAR_SCANNER_SPEC |
| 04 | Product requirements | PRD-001..008 |
| 05 | Admin actions | entrada, copiloto, seletor, feito, saida |
| 06 | Entrada | FR-ENTRADA-001..006 |
| 07 | Copiloto | FR-COPILOTO-001..003 |
| 08 | Seletor | FR-SELETOR-001..005 |
| 09–10 | Feito and completion destination | FR-FEITO-001..007 |
| 11 | Saída | FR-SAIDA-001..005 |
| 12 | QR Jump | FR-QR-001..002 |
| 13 | Direct destinations | roadmap, notes_documents |
| 14–15 | State and action resolution | scanner state machine |
| 16–19 | Time, data and telemetry | execution_session, task_execution, scanner_event |
| 20–25 | UX, print, report and responsiveness | UX-001..006 |
| 26 | Non-functional requirements | NFR-001..007 |
| 27 | Error handling | explicit + TBD |
| 28–29 | Acceptance and QA | AC-001..010 |
| 30–34 | Dependencies and implementation | agent handoff |
| 35 | Feedback loop | planned vs actual |
| 36 | Open questions | OQ-001..011 |
| 37 | Provenance | source-defined vs derived |
| 38 | Definition of Done | delivery gate |
| 39–40 | Canonical statement and summary | agent context |

# 04 · REQUIREMENT INDEX

```yaml
requirements:
  PRD:
    - PRD-001
    - PRD-002
    - PRD-003
    - PRD-004
    - PRD-005
    - PRD-006
    - PRD-007
    - PRD-008

  FRD:
    entrada:
      - FR-ENTRADA-001
      - FR-ENTRADA-002
      - FR-ENTRADA-003
      - FR-ENTRADA-004
      - FR-ENTRADA-005
      - FR-ENTRADA-006
    copiloto:
      - FR-COPILOTO-001
      - FR-COPILOTO-002
      - FR-COPILOTO-003
    seletor:
      - FR-SELETOR-001
      - FR-SELETOR-002
      - FR-SELETOR-003
      - FR-SELETOR-004
      - FR-SELETOR-005
    feito:
      - FR-FEITO-001
      - FR-FEITO-002
      - FR-FEITO-003
      - FR-FEITO-004
      - FR-FEITO-005
      - FR-FEITO-006
      - FR-FEITO-007
    saida:
      - FR-SAIDA-001
      - FR-SAIDA-002
      - FR-SAIDA-003
      - FR-SAIDA-004
      - FR-SAIDA-005
    qr:
      - FR-QR-001
      - FR-QR-002

  UX:
    - UX-001
    - UX-002
    - UX-003
    - UX-004
    - UX-005
    - UX-006

  NFR:
    - NFR-001
    - NFR-002
    - NFR-003
    - NFR-004
    - NFR-005
    - NFR-006
    - NFR-007

  acceptance:
    - AC-001
    - AC-002
    - AC-003
    - AC-004
    - AC-005
    - AC-006
    - AC-007
    - AC-008
    - AC-009
    - AC-010
```

# 05 · CRITICAL PRODUCT CONTRACTS

```yaml
critical_contracts:
  scan_means_action:
    rule: valid_scan_executes_immediately_when_context_exists
  entrada:
    rule: checkin_plus_task_resolution_plus_progressive_timer
  copiloto:
    rule: open_chat_plus_trigger_bom_dia_copiloto
  seletor:
    rule: up_to_five_default_or_custom_shortcuts
  feito:
    normal: complete_without_confirmation_plus_undo
    exception: confirmation_when_no_checkin
  saida:
    rule: checkout_plus_day_close_plus_reports_plus_delivery
  qr_jump:
    rule: open_most_recent_open_task
  timing:
    rule: progressive_not_countdown
  state:
    rule: scanner_uses_canonical_application_execution_state
  print:
    rule: adaptive_layout_must_preserve_scannability
```

# 06 · DEPENDENCIES

```yaml
dependencies:
  - existing_application_scanner
  - authentication_context
  - user_plan
  - deliverable_model
  - task_model
  - active_execution_state
  - progressive_time_tracking
  - copilot_agent
  - trigger_bom_dia_copiloto
  - roadmap
  - documents
  - notification_system
  - daily_report_generator
  - communication_channel
```

# 07 · OPEN DECISION INDEX

```yaml
open_questions:
  OQ-001: terceiracte_meaning
  OQ-002: backlog_post_completion_semantics
  OQ-003: most_recent_open_task_ranking
  OQ-004: behavior_after_feito_when_next_task_exists
  OQ-005: thirty_minute_margin_reference_point
  OQ-006: undo_availability_window
  OQ-007: duplicate_scan_behavior
  OQ-008: offline_scanner_behavior
  OQ-009: minimum_printed_target_dimensions
  OQ-010: supported_checkout_communication_channels
  OQ-011: triped_envelope_exact_geometry
```

# 08 · AGENT RETRIEVAL INSTRUCTIONS

```yaml
agent_retrieval:
  product_intent:
    read_sections:
      - 00
      - 01
      - 02
      - 03
      - 04
      - 05
  scanner_behavior:
    read_sections:
      - 06
      - 07
      - 08
      - 09
      - 10
      - 11
      - 12
      - 13
      - 14
      - 15
  time_or_data:
    read_sections:
      - 16
      - 17
      - 18
      - 19
      - 35
  design_or_print:
    read_sections:
      - 20
      - 21
      - 22
      - 23
      - 24
      - 25
  implementation:
    read_sections:
      - 26
      - 27
      - 30
      - 31
      - 32
      - 33
      - 34
  validation:
    read_sections:
      - 28
      - 29
      - 38
  ambiguity:
    read_sections:
      - 36
      - 37
  never:
    - silently_close_open_questions
    - add_confirmation_to_zero_friction_paths
    - create_parallel_execution_state
    - replace_progressive_timer_with_countdown
```

# 09 · REQUIRED REPOSITORY DISCOVERY

```yaml
required_repository_discovery:
  - scanner_implementation
  - current_task_resolution
  - checkin_checkout_state
  - timer_logic
  - bom_dia_copiloto_trigger
  - notification_service
  - daily_report_generator
  - next_day_summary_generator
  - user_communication_channel
```

# 10 · DELIVERY GATE

```yaml
delivery_gate:
  complete_when:
    - all_admin_scanner_actions_match_contract
    - canonical_state_is_reused
    - progressive_timer_is_persisted
    - zero_friction_paths_remain_zero_friction
    - undo_is_available_for_normal_feito
    - exception_paths_match_spec
    - daily_close_pipeline_executes
    - qr_and_direct_destinations_work
    - printed_targets_are_reliably_scannable
    - telemetry_supports_planned_vs_actual_analysis
    - unresolved_questions_are_not_hardcoded
```
