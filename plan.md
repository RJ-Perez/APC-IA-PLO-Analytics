
# APC IA-PLO Dashboard — Implementation Plan

## Design Direction
- **Accent Color:** Blue-600 (#2563EB) with teal-500 secondary for PLO sections
- **Surface Style:** White cards with subtle borders on slate-50 background
- **Sidebar:** Light sidebar (white bg, border-right), with APC branding
- **Typography:** Inter font, strong hierarchy with semibold headings
- **Aesthetic:** Clean, institutional, data-dense but readable — inspired by Linear/Stripe dashboards
- **Charts:** Recharts with consistent blue/teal/amber/emerald palette

---

## Phase 1: Core Layout, Navigation, State Management & Data Models ✅
- [x] Define all state classes: AuthState (RBAC with roles: Admin, Program Chair, Faculty, Stakeholder), DashboardState (IA metrics, PLO data, filters), ReportState
- [x] Build app shell: light sidebar with APC branding, top header with user info/role badge, main content area
- [x] Create navigation structure: Dashboard (home), IA Assessment, PLO Analytics, Data Management, Reports, Settings
- [x] Implement login page with role selection and session management
- [x] Populate realistic sample data for IA indicators (11 AUN-QA criteria) and PLO attainment across 5+ programs

---

## Phase 2: IA Dashboard & PLO Analytics Visualization ✅
- [x] Build IA Compliance Dashboard: overall compliance gauge, criteria-level bar chart, year-over-year trend line chart, status cards with color-coded indicators
- [x] Build PLO Analytics page: program selector filter, PLO attainment grouped bar chart by program, heatmap-style table showing PLO×Course matrix, trend analysis line chart
- [x] Add drill-down capability: clicking IA criteria or PLO shows detailed breakdown modal/panel
- [x] Implement year/semester filter controls that update all visualizations
- [x] Add KPI summary cards at top of each dashboard (total programs, avg attainment, compliance %, alerts)

---

## Phase 3: Data Management, Reporting Engine & Final Polish ✅
- [x] Build Data Input page: tabbed interface for IA Indicators input and PLO Assessment input with forms, validation, edit/delete capabilities
- [x] Create data tables with search, sort, and pagination for managing assessment records
- [x] Build Reports page: report template selector (AUN-QA IA Summary, PLO Attainment Report, Program Comparison), date range picker, generate/preview functionality
- [x] Implement CSV export for report data and print-friendly report view
- [x] Add Settings page: user profile, role management table (admin only), system preferences
- [x] Final responsive design polish and empty/loading states
