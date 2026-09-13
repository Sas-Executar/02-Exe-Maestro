---
id: DOC-CLX-038
folder_id: FS-EXE-001
tipo: documento-importado
status: confirmado
origem: export-claude-20260913
origem_filename: "DENSE_SCANNER_PRD_FRD_SPECS.md"
sha256: 8dbc6896d2f2bfba3816878b5cb88a08676c00e02b26dfa4a671520c7c70037d
projeto: ECOSSISTEMA_15-08_FILESYSTEM
---

# EXECUTAR · SCANNER
## DENSE PRD + FRD + SPECS + AI HANDOFF

```yaml
document:
  id: EXECUTAR_SCANNER_SPEC
  version: 1.0
  language: pt-BR
  status: draft_structured_from_authoritative_brief
  source_of_truth:
    - Scanner PRD.txt
  intended_readers:
    - AI coding agents
    - product agents
    - design agents
    - engineering agents
    - QA agents
  authority_rules:
    - Explicit product behavior in this document must not be reinterpreted.
    - Do not introduce confirmation steps where zero-friction behavior is specified.
    - Do not change scanner actions without an explicit product decision.
    - Treat OPEN_QUESTION and TBD fields as unresolved.
    - Existing repository conventions take precedence over suggested implementation names.
```

# 00 · EXECUTIVE PRODUCT DEFINITION

Scanner is a physical-to-digital execution interface inside the EXECUTAR application.

Its purpose is to allow the user to point the application scanner at printed symbols or QR elements and immediately execute the corresponding application action.

```text
SCAN
  ↓
RECOGNIZE
  ↓
RESOLVE CONTEXT
  ↓
EXECUTE ACTION
  ↓
DISPLAY RESULT / UNDO WHEN APPLICABLE
```

The scanner is primarily an execution trigger, not merely navigation.

# 01 · CORE PRODUCT PRINCIPLE

```yaml
core_principle:
  statement: "Escaneou, alguma coisa acontece."
  objective: minimize friction between physical planning artifacts and digital execution
  default_behavior: execute_immediately
  intermediate_steps: prohibited_when_context_is_sufficient
  confirmation:
    default: false
    allowed_when:
      - execution_context_missing
      - active_task_cannot_be_resolved
      - explicit_exception_defined
  recovery_pattern:
    preferred: undo
    avoid: pre_action_confirmation
```

# 02 · PRODUCT CONTEXT

The scanner operates together with printable EXECUTAR Status Reports.

```yaml
print_formats:
  - Prisma
  - Triped Envelope
```

```yaml
layout_capabilities:
  - responsive_reallocation
  - overflow_management
  - adaptive_scaling
  - resizing
  - dynamic_placeholders
  - variable_project_duration
  - multi_project_content
```

The same model must support one project or multiple projects and short or long planning horizons without changing the semantic information architecture.

# 03 · OUTPUT CHANNELS

```yaml
output_channels:
  - application_ui
  - printed_report
  - html
  - email
  - terminal_or_plain_text
```

Each renderer may adapt presentation but must preserve semantic meaning, IDs and action identity.

# 04 · PRD — PRODUCT REQUIREMENTS

## PRD-001 · Immediate action
When a valid scanner element is recognized, the application must execute its configured action immediately whenever sufficient context exists.

## PRD-002 · No unnecessary confirmation
The scanner must not present an intermediate confirmation step for normal pre-authorized actions.

## PRD-003 · Context-aware execution
The scanner must use canonical application state to determine what action should occur.

## PRD-004 · Physical print compatibility
Symbols and QR elements must remain reliably readable after printing.

## PRD-005 · Execution telemetry
Scanner interactions must generate execution data usable for historical analysis, planned-versus-actual comparison, insights, predictions and long-term model training.

## PRD-006 · Fast scanning
The scanner interface must prioritize capture speed over a large camera preview.

## PRD-007 · Direct destination navigation
Printed destination elements such as Roadmap or Documents must open their corresponding destination directly.

## PRD-008 · Automatic workflows
A scan can execute navigation, agent triggers, timers, task-state transitions and communication flows.

# 05 · ADMIN ACTIONS

```yaml
admin_actions:
  - entrada
  - copiloto
  - seletor
  - feito
  - saida
```

# 06 · FRD — ENTRADA

## FR-ENTRADA-001
Scanning Entrada performs user check-in.

## FR-ENTRADA-002
After check-in, the system opens the current deliverable context.

## FR-ENTRADA-003
The system resolves the task the user should start.

## FR-ENTRADA-004
The task begins automatically.

## FR-ENTRADA-005
A progressive execution timer begins automatically.

```yaml
timer:
  mode: count_up
  starts_on: successful_checkin
  purpose:
    - record_real_execution_time
    - compare_planned_vs_actual
```

## FR-ENTRADA-006
The user must not manually navigate to the task and press a second Start command.

```text
SCAN ENTRADA
   ↓
CHECK-IN
   ↓
RESOLVE CURRENT DELIVERABLE
   ↓
RESOLVE CURRENT TASK
   ↓
OPEN TASK
   ↓
START TASK
   ↓
START PROGRESSIVE TIMER
```

# 07 · FRD — COPILOTO

## FR-COPILOTO-001
Scanning Copiloto opens the AI Copilot chat.

## FR-COPILOTO-002
The scan simultaneously triggers the existing command:

```text
bom dia copiloto
```

## FR-COPILOTO-003
The trigger executes before or while the chat is opening so the daily briefing is already processing upon entry.

# 08 · FRD — SELETOR

## FR-SELETOR-001
Scanning Seletor opens a shortcut selector.

## FR-SELETOR-002
The selector supports up to five shortcuts.

```yaml
max_shortcuts: 5
```

## FR-SELETOR-003
Default examples:

```yaml
default_shortcuts:
  - documentos
  - roadmap
  - sprint
  - hoje
  - tarefas_feitas
```

## FR-SELETOR-004
The user can customize selector shortcuts.

## FR-SELETOR-005
Selecting a shortcut opens its application destination directly.

# 09 · FRD — FEITO

## FR-FEITO-001
If the user has an active check-in, the system must know the currently active task.

## FR-FEITO-002
Scanning Feito while an active task exists completes that task automatically.

## FR-FEITO-003
No pre-completion confirmation is displayed in this normal path.

## FR-FEITO-004
After completion, the interface shows Undo.

## FR-FEITO-005
Scanning Feito without an active check-in requires confirmation.

## FR-FEITO-006
If check-in and timer are active but Feito is not scanned, the system applies a 30-minute margin and sends a notification.

```yaml
completion_grace_period_minutes: 30
```

## FR-FEITO-007
Accepting the notification action can mark the task completed.

# 10 · POST-COMPLETION LOCATION

```yaml
post_completion_destination:
  source_term: backlog
  status: SOURCE_DEFINED_BUT_AMBIGUOUS
  agent_rule:
    - preserve_behavior_until_clarified
    - do_not_silently_rename_destination
```

# 11 · FRD — SAÍDA

## FR-SAIDA-001
Scanning Saída performs daily checkout.

## FR-SAIDA-002
Checkout initiates the end-of-day closing workflow.

## FR-SAIDA-003
The system generates the final report for the current day.

## FR-SAIDA-004
The system generates a summary of the following day.

## FR-SAIDA-005
The system sends these outputs to the user's configured communication channel.

# 12 · QR JUMP

## FR-QR-001
Scanning QR Jump opens the most recent currently open task directly.

```yaml
qr_jump:
  destination: most_recent_open_task
  intermediate_screen: false
```

## FR-QR-002
QR Jump must remain physically small while maintaining reliable print scanning.

# 13 · DIRECT DESTINATIONS

```yaml
direct_destinations:
  roadmap:
    destination: roadmap
  notes_documents:
    destination: documents
```

# 14 · STATE MODEL

```yaml
states:
  idle:
    description: no active execution session
  checked_in:
    description: daily execution session is active
  task_active:
    description: active task exists and progressive timer is running
  task_completed:
    description: current task has been marked done
  checked_out:
    description: daily execution session has been closed
```

# 15 · ACTION RESOLUTION MATRIX

| Scan | Required Context | Immediate Action | Confirmation | Recovery |
|---|---|---|---|---|
| Entrada | User + plan | Check-in + resolve task + start timer | No | TBD |
| Copiloto | User | Open Copilot + trigger daily briefing | No | TBD |
| Seletor | User | Open shortcut selector | No | Normal navigation |
| Feito | Active check-in + task | Complete active task | No | Undo |
| Feito | No active check-in | Resolve potentially ambiguous completion | Yes | Cancel |
| Saída | Active user/day | Checkout + daily closing workflow | No | TBD |
| QR Jump | Open-task context | Open latest open task | No | Normal navigation |
| Roadmap | Roadmap available | Open roadmap | No | Normal navigation |
| Notes/Documents | Documents available | Open documents | No | Normal navigation |

# 16 · TIME TRACKING

```yaml
time_tracking:
  source_of_start: entrada_scan
  direction: progressive
  records_actual_time: true
  planned_time_exists: true
  comparison_required: planned_vs_actual
```

# 17 · DATA REQUIREMENTS

```yaml
execution_session:
  user_id: required
  date: required
  checkin_at: required
  checkout_at: nullable
  active_deliverable_id: nullable
  active_task_id: nullable

task_execution:
  task_id: required
  planned_duration: nullable
  started_at: required
  completed_at: nullable
  actual_duration: derived
  completion_source:
    enum:
      - scanner_feito
      - notification
      - application_ui
      - other
  undo_status: nullable

scanner_event:
  event_id: required
  user_id: required
  scanned_at: required
  recognized_action: required
  execution_context: required
  result: required
```

# 18 · ANALYTICS / MODEL LEARNING

```yaml
learning_objectives:
  - analyze_planning_vs_execution
  - understand_actual_effort
  - generate_insights
  - improve_predictions
  - support_long_term_model_training
```

# 19 · EVENT MODEL

```yaml
events:
  - scanner.scan_detected
  - scanner.action_resolved
  - scanner.action_executed
  - scanner.action_failed
  - execution.checkin_started
  - execution.task_started
  - execution.task_completed
  - execution.task_completion_undone
  - execution.checkout_started
  - execution.checkout_completed
  - copilot.daily_briefing_triggered
  - report.daily_generated
  - report.next_day_summary_generated
```

# 20 · UX SPEC

## UX-001
Default interaction: SCAN → ACTION.

## UX-002
For reversible actions with sufficient context, execute first and allow Undo.

## UX-003
Use confirmation only when context is ambiguous or missing.

## UX-004
Scanner camera UI should be compact and optimized for rapid recognition.

## UX-005
After scanning, the result must be immediately perceivable.

## UX-006
Scanner destinations should resolve as direct deep links.

# 21 · PRINT / RECOGNITION SPECS

```yaml
print_scanner_requirements:
  high_contrast: required
  sufficient_ink_density: required
  reliable_symbol_edges: required
  print_scaling_tolerance: required
  qr_legibility: required
  camera_detection_speed: high_priority
```

# 22 · RECOGNITION STRATEGY

```yaml
recognition_strategy:
  term_from_source: terceiracte
  status: OPEN_QUESTION
  agent_instruction:
    - do_not_infer_library_or_technology
    - verify_existing_scanner_implementation
```

# 23 · REPORT GENERATION

```text
USER PLAN
   ↓
PLAN MODEL
   ↓
STATUS REPORT DATA MODEL
   ↓
LAYOUT ALLOCATION
   ├── Prisma
   └── Triped Envelope
   ↓
OUTPUT RENDERER
   ├── Print
   ├── HTML
   ├── Email
   └── Terminal
```

# 24 · PLACEHOLDER MODEL

```yaml
placeholders:
  identity:
    - user
    - date
    - project
    - deliverable
  planning:
    - planned_tasks
    - planned_duration
    - roadmap
    - sprint
    - current_day
  execution:
    - active_task
    - completed_tasks
    - actual_duration
    - checkin_state
  scanner:
    - entrada_action
    - copiloto_action
    - selector_actions
    - feito_action
    - saida_action
    - qr_jump_target
```

# 25 · RESPONSIVE CONTENT RULE

```text
SAME SEMANTIC CONTENT
        ↓
FORMAT CONSTRAINTS
        ↓
REALLOCATE
        ↓
RESIZE
        ↓
CONTROL OVERFLOW
        ↓
PRESERVE SCANNABILITY
```

# 26 · NFR

## NFR-001 · Performance
Recognition and action dispatch must feel immediate.

## NFR-002 · Reliability
A recognized target must map deterministically to its intended action.

## NFR-003 · Print robustness
Targets must remain readable across supported print outputs.

## NFR-004 · State consistency
Scanner actions must operate against the same canonical active-task state used by the application.

## NFR-005 · Idempotency
Duplicate-scan behavior is TBD.

## NFR-006 · Auditability
Enough execution event data must be retained for planned-versus-actual analysis.

## NFR-007 · Cross-channel consistency
Print, HTML, e-mail and terminal representations must preserve semantic action identity.

# 27 · ERROR HANDLING

```yaml
explicit:
  feito_without_checkin:
    behavior: ask_for_confirmation
  active_task_without_feito_after_margin:
    delay_minutes: 30
    behavior: send_notification
    notification_action: complete_task

unresolved:
  unknown_scan: TBD
  duplicate_scan: TBD
  scan_network_failure: TBD
  scan_when_offline: TBD
  scan_saida_without_checkin: TBD
  entrada_when_already_checked_in: TBD
  feito_after_task_already_completed: TBD
  undo_timeout: TBD
```

# 28 · ACCEPTANCE CRITERIA

## AC-001
Entrada creates check-in, resolves/opens current task, starts execution and starts progressive timer.

## AC-002
Copiloto opens chat and triggers `bom dia copiloto`.

## AC-003
Seletor opens up to five default/customizable shortcuts.

## AC-004
Feito with active check-in completes task without confirmation and exposes Undo.

## AC-005
Feito without check-in requires confirmation.

## AC-006
Missing completion triggers the defined 30-minute notification path.

## AC-007
Saída closes the day, generates daily report and next-day summary, and sends them.

## AC-008
QR Jump opens the most recent open task.

## AC-009
Roadmap target opens Roadmap directly.

## AC-010
Notes/Documents target opens Documents directly.

# 29 · QA TEST MATRIX

```yaml
critical_tests:
  entrada_happy_path:
    expected:
      - checkin_active
      - active_task_resolved
      - task_opened
      - timer_running
  copiloto_happy_path:
    expected:
      - chat_opened
      - daily_trigger_fired
  feito_happy_path:
    expected:
      - task_completed
      - timer_finalized
      - undo_available
      - no_confirmation
  feito_without_checkin:
    expected:
      - confirmation_required
  completion_timeout:
    expected:
      - notification_after_configured_margin
      - notification_can_complete_task
  saida_happy_path:
    expected:
      - checkout
      - closing_workflow
      - daily_report
      - next_day_summary
      - communication_delivery
  qr_jump:
    expected:
      - latest_open_task_opened_directly
```

# 30 · IMPLEMENTATION DEPENDENCIES

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

# 31 · AGENT IMPLEMENTATION RULES

```yaml
agent_rules:
  source_authority:
    - explicit_requirements_override_inferred_ux_conventions
  before_coding:
    - locate_current_scanner_implementation
    - locate_task_execution_state
    - locate_checkin_checkout_implementation
    - locate_timer_implementation
    - locate_bom_dia_copiloto_trigger
    - locate_notification_infrastructure
    - locate_report_generator
    - locate_communication_delivery_channel
  prohibited_without_approval:
    - add_confirmation_to_normal_entrada
    - add_confirmation_to_normal_feito_with_active_checkin
    - convert_progressive_timer_to_countdown
    - remove_undo_behavior
    - replace_direct_navigation_with_intermediate_screens
    - remove_scanner_actions_due_to_print_layout_constraints
    - invent_behavior_for_unresolved_edge_cases
  implementation_strategy:
    - reuse_existing_domain_state
    - scanner_commands_should_be_thin_triggers
    - avoid_parallel_scanner_only_task_state
    - preserve_deterministic_mappings
    - log_execution_telemetry
```

# 32 · COMMAND CONTRACT MODEL

```text
scan(target)
    ↓
recognize(target)
    ↓
resolveAction(target)
    ↓
resolveExecutionContext()
    ↓
validateContext()
    ↓
execute(command)
    ↓
persistEvent()
    ↓
returnFeedback()
```

# 33 · SECURITY / AUTHORIZATION

```yaml
authorization:
  automatic_actions: source_required
  authentication_model: existing_application_authority
  new_security_model: not_defined
```

# 34 · AI / COPILOT INTEGRATION

```text
SCAN
 ├─→ TRIGGER "bom dia copiloto"
 └─→ OPEN CHAT
```

# 35 · DATA FEEDBACK LOOP

```text
PLAN
  ↓
SCANNER EXECUTION
  ↓
ACTUAL EXECUTION DATA
  ↓
PLANNED VS ACTUAL ANALYSIS
  ↓
INSIGHTS + PREDICTIONS
  ↓
FUTURE MODEL / PLAN IMPROVEMENT
```

# 36 · OPEN QUESTIONS

```yaml
open_questions:
  OQ-001:
    question: What exactly does "terceiracte" refer to?
  OQ-002:
    question: What is the canonical post-completion destination currently called "backlog"?
  OQ-003:
    question: How is "most recent open task" ranked for QR Jump?
  OQ-004:
    question: What happens after Feito if another planned task exists?
  OQ-005:
    question: What is the exact reference point for the 30-minute margin?
  OQ-006:
    question: What is the Undo availability window?
  OQ-007:
    question: What should happen on duplicate scans?
  OQ-008:
    question: What is scanner behavior offline?
  OQ-009:
    question: What minimum printed QR/symbol dimensions are acceptable?
  OQ-010:
    question: What exact communication channels are supported after Saída?
  OQ-011:
    question: What is the canonical definition and geometry of Triped Envelope?
```

# 37 · SOURCE-DEFINED VS DERIVED

```yaml
source_defined:
  - scanner_already_exists
  - entrada_equals_checkin
  - entrada_starts_execution
  - timer_is_progressive
  - copiloto_triggers_bom_dia_copiloto
  - seletor_supports_up_to_five_buttons
  - selector_is_customizable
  - feito_automatically_completes_active_task
  - feito_normally_has_no_confirmation
  - feito_exposes_undo
  - feito_without_checkin_requires_confirmation
  - thirty_minute_margin_notification_exists
  - notification_can_trigger_completion
  - saida_equals_checkout
  - saida_sends_daily_report
  - saida_sends_next_day_summary
  - qr_jump_opens_latest_open_task
  - roadmap_and_documents_open_directly
  - print_recognition_requires_reliable_visual_elements
  - execution_information_feeds_future_analysis_and_model_training
  - report_supports_prisma_and_triped_envelope
  - report_adapts_to_duration_and_multi_project_variation

derived_for_engineering_structure:
  - requirement_ids
  - event_names
  - conceptual_command_names
  - conceptual_data_entities
  - state_diagram_notation
  - test_case_identifiers
  - agent_implementation_checklist
```

# 38 · DEFINITION OF DONE

```yaml
definition_of_done:
  - all_five_admin_scanner_actions_match_defined_flows
  - entrada_creates_usable_execution_context
  - progressive_timing_data_is_persisted
  - copiloto_executes_trigger_automatically
  - seletor_supports_default_and_custom_destinations
  - feito_is_zero_friction_when_context_exists
  - feito_supports_undo
  - missing_checkin_exception_behaves_as_specified
  - thirty_minute_notification_behavior_is_implemented
  - saida_closes_daily_execution_cycle
  - report_and_next_day_summary_are_dispatched
  - qr_jump_resolves_latest_open_task
  - direct_scanner_destinations_work
  - printed_targets_pass_scanner_reliability_tests
  - scanner_events_feed_execution_analytics
  - prisma_rendering_preserves_scanner_semantics
  - triped_envelope_rendering_preserves_scanner_semantics
  - unresolved_product_decisions_are_not_silently_hardcoded
```

# 39 · CANONICAL PRODUCT STATEMENT

The EXECUTAR Scanner converts printed planning elements into immediate application commands: Entrada starts execution, Copiloto activates intelligence, Seletor opens shortcuts, Feito completes active work with Undo instead of friction, Saída closes the day, and QR/direct targets take the user immediately to the relevant execution context.

# 40 · AGENT HANDOFF SUMMARY

```yaml
handoff:
  objective: connect_the_physical_EXECUTAR_report_to_digital_execution
  primary_user_loop:
    - scan_entrada
    - execute_task
    - optionally_use_copiloto_or_navigation_targets
    - scan_feito
    - continue_execution
    - scan_saida
  main_design_rule:
    - scan_means_action
  main_state_rule:
    - scanner_actions_use_canonical_application_execution_state
  main_ux_rule:
    - prefer_automatic_execution_plus_undo_over_confirmation
  main_data_rule:
    - preserve_execution_telemetry_for_planned_vs_actual_intelligence
  main_print_rule:
    - responsiveness_must_not_compromise_scanner_readability
  highest_priority_unknowns:
    - terceiracte_meaning
    - backlog_meaning
    - thirty_minute_timer_reference_point
    - duplicate_scan_behavior
    - offline_behavior
    - triped_envelope_exact_geometry
```
