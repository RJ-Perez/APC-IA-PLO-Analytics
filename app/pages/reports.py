import reflex as rx
from app.components.layout import layout
from app.states.report_state import ReportState
from app.states.dashboard_state import DashboardState


def report_type_card(
    title: str, icon: str, selected_type: rx.Var
) -> rx.Component:
    is_selected = selected_type == title
    return rx.el.button(
        rx.icon(
            icon,
            class_name=rx.cond(
                is_selected,
                "h-6 w-6 text-blue-600 mb-2",
                "h-6 w-6 text-slate-400 mb-2",
            ),
        ),
        rx.el.span(
            title,
            class_name=rx.cond(
                is_selected,
                "text-sm font-medium text-blue-700 text-center",
                "text-sm font-medium text-slate-600 text-center",
            ),
        ),
        on_click=ReportState.set_report_type(title),
        class_name=rx.cond(
            is_selected,
            "flex flex-col items-center justify-center p-4 border-2 border-blue-600 rounded-xl bg-blue-50 transition-colors w-full h-32",
            "flex flex-col items-center justify-center p-4 border-2 border-slate-200 rounded-xl bg-white hover:border-slate-300 hover:bg-slate-50 transition-colors w-full h-32",
        ),
    )


def report_configuration() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("file-text", class_name="h-5 w-5 text-blue-600 mr-2"),
            rx.el.h3(
                "Generate Report", class_name="text-lg font-bold text-slate-900"
            ),
            class_name="flex items-center mb-6",
        ),
        rx.el.div(
            report_type_card(
                "AUN-QA IA Summary Report",
                "clipboard-check",
                ReportState.selected_report_type,
            ),
            report_type_card(
                "PLO Attainment Report",
                "bar-chart-3",
                ReportState.selected_report_type,
            ),
            report_type_card(
                "Program Comparison Report",
                "git-compare-arrows",
                ReportState.selected_report_type,
            ),
            report_type_card(
                "Criteria Deep Dive Report",
                "search",
                ReportState.selected_report_type,
            ),
            class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.label(
                    "Year",
                    class_name="block text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1",
                ),
                rx.el.select(
                    rx.foreach(
                        DashboardState.year_options,
                        lambda y: rx.el.option(y, value=y),
                    ),
                    value=DashboardState.selected_year,
                    on_change=DashboardState.set_year,
                    class_name="w-full px-3 py-2 bg-white border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none appearance-none",
                ),
                class_name="relative w-full sm:w-48",
            ),
            rx.el.div(
                rx.el.label(
                    "Semester",
                    class_name="block text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1",
                ),
                rx.el.select(
                    rx.foreach(
                        DashboardState.semester_options,
                        lambda s: rx.el.option(s, value=s),
                    ),
                    value=DashboardState.selected_semester,
                    on_change=DashboardState.set_semester,
                    class_name="w-full px-3 py-2 bg-white border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none appearance-none",
                ),
                class_name="relative w-full sm:w-48",
            ),
            rx.el.div(
                rx.el.label(
                    "Program",
                    class_name="block text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1",
                ),
                rx.el.select(
                    rx.foreach(
                        DashboardState.program_options,
                        lambda p: rx.el.option(p, value=p),
                    ),
                    value=DashboardState.selected_program,
                    on_change=DashboardState.set_program,
                    class_name="w-full px-3 py-2 bg-white border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none appearance-none",
                ),
                class_name="relative w-full sm:w-64",
            ),
            rx.el.div(
                rx.el.button(
                    rx.cond(
                        ReportState.is_generating,
                        rx.icon(
                            "loader", class_name="h-4 w-4 mr-2 animate-spin"
                        ),
                        rx.icon("file-output", class_name="h-4 w-4 mr-2"),
                    ),
                    rx.cond(
                        ReportState.is_generating,
                        "Generating...",
                        "Generate Report",
                    ),
                    on_click=ReportState.generate_report,
                    disabled=ReportState.is_generating,
                    class_name="flex items-center px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium rounded-lg transition-colors mt-auto w-full sm:w-auto justify-center",
                ),
                class_name="flex-1 flex justify-end mt-4 sm:mt-0",
            ),
            class_name="flex flex-wrap gap-4 items-end",
        ),
        class_name="bg-white rounded-xl border border-slate-200 shadow-sm p-6 mb-8",
    )


def ia_summary_content() -> rx.Component:
    return rx.el.div(
        rx.el.table(
            rx.el.thead(
                rx.el.tr(
                    rx.el.th(
                        "ID",
                        class_name="px-4 py-2 text-left text-xs font-semibold text-slate-500 uppercase border-b border-slate-200",
                    ),
                    rx.el.th(
                        "Criteria Name",
                        class_name="px-4 py-2 text-left text-xs font-semibold text-slate-500 uppercase border-b border-slate-200",
                    ),
                    rx.el.th(
                        "Score",
                        class_name="px-4 py-2 text-left text-xs font-semibold text-slate-500 uppercase border-b border-slate-200",
                    ),
                    rx.el.th(
                        "Compliance %",
                        class_name="px-4 py-2 text-left text-xs font-semibold text-slate-500 uppercase border-b border-slate-200",
                    ),
                    rx.el.th(
                        "Status",
                        class_name="px-4 py-2 text-left text-xs font-semibold text-slate-500 uppercase border-b border-slate-200",
                    ),
                )
            ),
            rx.el.tbody(
                rx.foreach(
                    DashboardState.ia_criteria_base,
                    lambda c: rx.el.tr(
                        rx.el.td(
                            c["id"],
                            class_name="px-4 py-2 text-sm border-b border-slate-100",
                        ),
                        rx.el.td(
                            c["name"],
                            class_name="px-4 py-2 text-sm font-medium border-b border-slate-100",
                        ),
                        rx.el.td(
                            c["score"],
                            class_name="px-4 py-2 text-sm border-b border-slate-100",
                        ),
                        rx.el.td(
                            f"{c['compliance_pct']}%",
                            class_name="px-4 py-2 text-sm border-b border-slate-100",
                        ),
                        rx.el.td(
                            c["status"],
                            class_name="px-4 py-2 text-sm border-b border-slate-100",
                        ),
                    ),
                )
            ),
            rx.el.tfoot(
                rx.el.tr(
                    rx.el.td(
                        "Summary",
                        colspan=2,
                        class_name="px-4 py-2 font-bold text-sm bg-slate-50",
                    ),
                    rx.el.td(
                        f"{DashboardState.avg_ia_score}",
                        class_name="px-4 py-2 font-bold text-sm bg-slate-50",
                    ),
                    rx.el.td(
                        f"{DashboardState.overall_compliance}%",
                        class_name="px-4 py-2 font-bold text-sm bg-slate-50",
                    ),
                    rx.el.td("", class_name="px-4 py-2 bg-slate-50"),
                )
            ),
            class_name="w-full mb-8 border-collapse",
        ),
        rx.el.div(
            rx.el.h4(
                "Key Findings", class_name="font-bold text-slate-800 mb-2"
            ),
            rx.el.ul(
                rx.el.li(
                    "Facilities (6.4/7.0) and Teaching & Learning (6.1/7.0) show strong compliance.",
                    class_name="mb-1 text-sm text-slate-700",
                ),
                rx.el.li(
                    "Internationalization requires immediate attention, currently scoring 3.8/7.0.",
                    class_name="mb-1 text-sm text-slate-700",
                ),
                class_name="list-disc pl-5 mb-6",
            ),
            rx.el.h4(
                "Recommendations", class_name="font-bold text-slate-800 mb-2"
            ),
            rx.el.ul(
                rx.el.li(
                    "Develop partnerships for international exchange programs.",
                    class_name="mb-1 text-sm text-slate-700",
                ),
                rx.el.li(
                    "Review academic staff recruitment and retention policies.",
                    class_name="mb-1 text-sm text-slate-700",
                ),
                class_name="list-disc pl-5",
            ),
        ),
    )


def plo_summary_content() -> rx.Component:
    return rx.el.div(
        rx.el.table(
            rx.el.thead(
                rx.el.tr(
                    rx.el.th(
                        "PLO ID",
                        class_name="px-4 py-2 text-left text-xs font-semibold text-slate-500 uppercase border-b border-slate-200",
                    ),
                    rx.el.th(
                        "Description",
                        class_name="px-4 py-2 text-left text-xs font-semibold text-slate-500 uppercase border-b border-slate-200",
                    ),
                    rx.el.th(
                        "Attainment %",
                        class_name="px-4 py-2 text-left text-xs font-semibold text-slate-500 uppercase border-b border-slate-200",
                    ),
                    rx.el.th(
                        "Target",
                        class_name="px-4 py-2 text-left text-xs font-semibold text-slate-500 uppercase border-b border-slate-200",
                    ),
                    rx.el.th(
                        "Status",
                        class_name="px-4 py-2 text-left text-xs font-semibold text-slate-500 uppercase border-b border-slate-200",
                    ),
                )
            ),
            rx.el.tbody(
                rx.foreach(
                    DashboardState.filtered_plo_data,
                    lambda p: rx.el.tr(
                        rx.el.td(
                            p["plo_id"],
                            class_name="px-4 py-2 text-sm border-b border-slate-100",
                        ),
                        rx.el.td(
                            p["description"],
                            class_name="px-4 py-2 text-sm border-b border-slate-100",
                        ),
                        rx.el.td(
                            f"{p['attainment_pct']}%",
                            class_name="px-4 py-2 text-sm border-b border-slate-100",
                        ),
                        rx.el.td(
                            "80.0%",
                            class_name="px-4 py-2 text-sm border-b border-slate-100",
                        ),
                        rx.el.td(
                            rx.cond(
                                p["attainment_pct"].to(float) >= 80.0,
                                rx.el.span(
                                    "Met",
                                    class_name="text-emerald-600 font-medium",
                                ),
                                rx.el.span(
                                    "Not Met",
                                    class_name="text-red-600 font-medium",
                                ),
                            ),
                            class_name="px-4 py-2 text-sm border-b border-slate-100",
                        ),
                    ),
                )
            ),
            class_name="w-full mb-8 border-collapse",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    "Average Attainment", class_name="text-sm text-slate-500"
                ),
                rx.el.p(
                    f"{DashboardState.avg_plo_attainment}%",
                    class_name="text-xl font-bold text-slate-900",
                ),
                class_name="p-4 bg-slate-50 rounded-lg border border-slate-200",
            ),
            rx.el.div(
                rx.el.p(
                    "PLOs Meeting Target", class_name="text-sm text-slate-500"
                ),
                rx.el.p(
                    f"{DashboardState.plos_above_target} / {DashboardState.total_plos_assessed}",
                    class_name="text-xl font-bold text-slate-900",
                ),
                class_name="p-4 bg-slate-50 rounded-lg border border-slate-200",
            ),
            class_name="grid grid-cols-2 gap-4",
        ),
    )


def report_preview() -> rx.Component:
    return rx.cond(
        ReportState.report_generated,
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.image(
                            src="placeholder.svg",
                            class_name="h-10 w-10 rounded-full object-cover",
                        ),
                        class_name="p-2 bg-blue-50 rounded-lg mr-4",
                    ),
                    rx.el.div(
                        rx.el.h2(
                            "Asia Pacific College",
                            class_name="text-xl font-bold text-slate-900",
                        ),
                        rx.el.p(
                            ReportState.selected_report_type,
                            class_name="text-sm font-medium text-slate-500",
                        ),
                    ),
                    class_name="flex items-center",
                ),
                rx.el.div(
                    rx.el.p(
                        f"Period: {DashboardState.selected_semester} {DashboardState.selected_year}",
                        class_name="text-sm text-slate-600 text-right",
                    ),
                    rx.el.p(
                        f"Scope: {DashboardState.selected_program}",
                        class_name="text-sm text-slate-600 text-right",
                    ),
                ),
                class_name="flex justify-between items-start mb-6",
            ),
            rx.el.hr(class_name="border-slate-200 mb-6"),
            rx.match(
                ReportState.selected_report_type,
                ("AUN-QA IA Summary Report", ia_summary_content()),
                ("PLO Attainment Report", plo_summary_content()),
                rx.el.div(
                    rx.el.p(
                        "Detailed report preview will be available here.",
                        class_name="text-slate-500 italic",
                    )
                ),
            ),
            rx.el.div(
                rx.el.button(
                    rx.icon("download", class_name="h-4 w-4 mr-2"),
                    "Export CSV",
                    on_click=ReportState.export_csv,
                    class_name="flex items-center px-4 py-2 border border-emerald-600 text-emerald-600 hover:bg-emerald-50 text-sm font-medium rounded-lg transition-colors",
                ),
                rx.el.button(
                    rx.icon("printer", class_name="h-4 w-4 mr-2"),
                    "Print Report",
                    on_click=rx.call_script("window.print()"),
                    class_name="flex items-center px-4 py-2 border border-slate-300 text-slate-700 hover:bg-slate-50 text-sm font-medium rounded-lg transition-colors",
                ),
                class_name="flex justify-end gap-3 mt-8 pt-6 border-t border-slate-100",
            ),
            class_name="bg-white rounded-xl border border-slate-200 shadow-sm p-8 print:shadow-none print:border-none",
        ),
        rx.fragment(),
    )


def reports_page() -> rx.Component:
    content = rx.el.div(
        report_configuration(), report_preview(), class_name="animate-fade-in"
    )
    return layout(content, "Reports", "Home / Reports", "/reports")