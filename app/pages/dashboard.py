import reflex as rx
from app.components.layout import layout
from app.states.auth_state import AuthState
from app.states.dashboard_state import DashboardState


def stat_card(
    title: str, value: str, subtitle: str, icon: str, color_class: str | rx.Var
) -> rx.Component:
    color_class_var = rx.Var.create(color_class)
    bg_class = rx.cond(
        color_class_var.contains("slate"),
        "bg-slate-100",
        rx.cond(
            color_class_var.contains("blue"),
            "bg-blue-50",
            rx.cond(
                color_class_var.contains("teal"),
                "bg-teal-50",
                rx.cond(
                    color_class_var.contains("red"),
                    "bg-red-50",
                    "bg-emerald-50",
                ),
            ),
        ),
    )
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.p(title, class_name="text-sm font-medium text-slate-500"),
                rx.el.p(
                    value, class_name="text-3xl font-bold text-slate-900 mt-1"
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.icon(icon, class_name=f"h-6 w-6 {color_class}"),
                class_name=f"p-3 rounded-xl {bg_class}",
            ),
            class_name="flex items-start justify-between",
        ),
        rx.el.div(
            rx.el.span(
                subtitle, class_name="text-sm font-medium text-slate-600"
            ),
            class_name="mt-4",
        ),
        class_name="bg-white p-6 rounded-xl shadow-sm border border-slate-200",
    )


def filter_bar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.label(
                "Year",
                class_name="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1 block",
            ),
            rx.el.select(
                rx.foreach(
                    DashboardState.year_options,
                    lambda y: rx.el.option(y, value=y),
                ),
                value=DashboardState.selected_year,
                on_change=DashboardState.set_year,
                class_name="w-40 px-3 py-2 bg-white border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none appearance-none",
            ),
            class_name="relative",
        ),
        rx.el.div(
            rx.el.label(
                "Semester",
                class_name="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1 block",
            ),
            rx.el.select(
                rx.foreach(
                    DashboardState.semester_options,
                    lambda s: rx.el.option(s, value=s),
                ),
                value=DashboardState.selected_semester,
                on_change=DashboardState.set_semester,
                class_name="w-48 px-3 py-2 bg-white border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none appearance-none",
            ),
            class_name="relative",
        ),
        rx.el.div(
            rx.el.label(
                "Program",
                class_name="text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1 block",
            ),
            rx.el.select(
                rx.foreach(
                    DashboardState.program_options,
                    lambda p: rx.el.option(p, value=p),
                ),
                value=DashboardState.selected_program,
                on_change=DashboardState.set_program,
                class_name="w-48 px-3 py-2 bg-white border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none appearance-none",
            ),
            class_name="relative",
        ),
        class_name="flex flex-wrap gap-4 mb-8 bg-white p-4 rounded-xl shadow-sm border border-slate-200",
    )


def inline_filter_row() -> rx.Component:
    return rx.el.div(
        rx.el.select(
            rx.foreach(
                DashboardState.year_options, lambda y: rx.el.option(y, value=y)
            ),
            value=DashboardState.selected_year,
            on_change=DashboardState.set_year,
            class_name="px-3 py-1.5 bg-white border border-slate-200 rounded-full text-sm font-medium focus:ring-2 focus:ring-blue-500 outline-none appearance-none cursor-pointer",
        ),
        rx.el.select(
            rx.foreach(
                DashboardState.semester_options,
                lambda s: rx.el.option(s, value=s),
            ),
            value=DashboardState.selected_semester,
            on_change=DashboardState.set_semester,
            class_name="px-3 py-1.5 bg-white border border-slate-200 rounded-full text-sm font-medium focus:ring-2 focus:ring-blue-500 outline-none appearance-none cursor-pointer",
        ),
        rx.el.select(
            rx.foreach(
                DashboardState.program_options,
                lambda p: rx.el.option(p, value=p),
            ),
            value=DashboardState.selected_program,
            on_change=DashboardState.set_program,
            class_name="px-3 py-1.5 bg-white border border-slate-200 rounded-full text-sm font-medium focus:ring-2 focus:ring-blue-500 outline-none appearance-none cursor-pointer",
        ),
        class_name="flex flex-wrap items-center gap-3",
    )


def welcome_banner() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2(
                f"Welcome back, {AuthState.user_name}",
                class_name="text-2xl font-bold text-slate-900 tracking-tight mb-1",
            ),
            rx.el.p(
                f"Here's your quality assurance overview for {DashboardState.selected_semester} {DashboardState.selected_year}",
                class_name="text-sm font-medium text-slate-500",
            ),
            class_name="flex-1",
        ),
        inline_filter_row(),
        class_name="flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-gradient-to-r from-blue-50 to-white p-6 rounded-xl border border-slate-200 shadow-sm mb-8",
    )


def primary_kpi_cards() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "Overall IA Compliance",
                            class_name="text-sm font-medium text-slate-500 mb-1",
                        ),
                        rx.el.div(
                            rx.el.span(
                                rx.cond(
                                    DashboardState.overall_compliance > 80,
                                    rx.el.span(
                                        class_name="w-2.5 h-2.5 rounded-full bg-emerald-500 mr-2 shrink-0"
                                    ),
                                    rx.cond(
                                        DashboardState.overall_compliance > 60,
                                        rx.el.span(
                                            class_name="w-2.5 h-2.5 rounded-full bg-amber-500 mr-2 shrink-0"
                                        ),
                                        rx.el.span(
                                            class_name="w-2.5 h-2.5 rounded-full bg-red-500 mr-2 shrink-0"
                                        ),
                                    ),
                                ),
                                f"{DashboardState.overall_compliance}%",
                                class_name="text-3xl font-bold text-slate-900 flex items-center",
                            ),
                            class_name="mb-1",
                        ),
                        rx.el.p(
                            "Across 11 AUN-QA Criteria",
                            class_name="text-xs text-slate-500",
                        ),
                        class_name="flex-1",
                    ),
                    rx.el.div(
                        rx.icon("activity", class_name="h-6 w-6 text-blue-600"),
                        class_name="w-12 h-12 rounded-xl bg-blue-50 flex items-center justify-center shrink-0",
                    ),
                    class_name="flex justify-between items-start mb-4",
                ),
                rx.el.div(
                    rx.el.span(
                        "↑ 2.1% from last year",
                        class_name="text-xs font-semibold text-emerald-600 bg-emerald-50 px-2 py-1 rounded-full",
                    ),
                    class_name="mt-auto self-start",
                ),
                class_name="flex flex-col h-full",
            ),
            class_name="bg-white p-6 rounded-xl border border-slate-200 border-l-4 border-l-blue-500 shadow-sm transition-shadow hover:shadow-md",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Programs Tracked",
                        class_name="text-sm font-medium text-slate-500 mb-1",
                    ),
                    rx.el.p(
                        f"{DashboardState.programs_tracked_count}",
                        class_name="text-3xl font-bold text-slate-900 mb-1",
                    ),
                    rx.el.p(
                        "Active PLO assessment",
                        class_name="text-xs text-slate-500",
                    ),
                    class_name="flex-1",
                ),
                rx.el.div(
                    rx.icon("book-open", class_name="h-6 w-6 text-blue-500"),
                    class_name="w-12 h-12 rounded-xl bg-blue-50 flex items-center justify-center shrink-0",
                ),
                class_name="flex justify-between items-start",
            ),
            class_name="bg-white p-6 rounded-xl border border-slate-200 border-l-4 border-l-blue-400 shadow-sm transition-shadow hover:shadow-md",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.p(
                            "Criteria at Risk",
                            class_name="text-sm font-medium text-slate-500 mb-1",
                        ),
                        rx.el.div(
                            rx.cond(
                                DashboardState.criteria_at_risk_count > 0,
                                rx.el.span(
                                    class_name="absolute top-1 -right-2 w-3 h-3 rounded-full bg-red-500 animate-pulse"
                                ),
                                rx.fragment(),
                            ),
                            rx.el.p(
                                f"{DashboardState.criteria_at_risk_count}",
                                class_name="text-3xl font-bold text-red-600 mb-1 relative inline-block",
                            ),
                            class_name="relative",
                        ),
                        rx.el.p(
                            "Requires immediate action",
                            class_name="text-xs text-slate-500",
                        ),
                        class_name="flex-1",
                    ),
                    rx.el.div(
                        rx.icon(
                            "triangle-alert", class_name="h-6 w-6 text-red-600"
                        ),
                        class_name="w-12 h-12 rounded-xl bg-red-50 flex items-center justify-center shrink-0",
                    ),
                    class_name="flex justify-between items-start",
                )
            ),
            class_name="bg-white p-6 rounded-xl border border-slate-200 border-l-4 border-l-red-500 shadow-sm transition-shadow hover:shadow-md",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.p(
                        "Avg PLO Attainment",
                        class_name="text-sm font-medium text-slate-500 mb-1",
                    ),
                    rx.el.p(
                        f"{DashboardState.avg_plo_attainment}%",
                        class_name="text-3xl font-bold text-teal-600 mb-1",
                    ),
                    rx.el.p(
                        "Across selected program",
                        class_name="text-xs text-slate-500",
                    ),
                    class_name="flex-1",
                ),
                rx.el.div(
                    rx.icon("target", class_name="h-6 w-6 text-teal-600"),
                    class_name="w-12 h-12 rounded-xl bg-teal-50 flex items-center justify-center shrink-0",
                ),
                class_name="flex justify-between items-start",
            ),
            class_name="bg-white p-6 rounded-xl border border-slate-200 border-l-4 border-l-teal-500 shadow-sm transition-shadow hover:shadow-md",
        ),
        class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8",
    )


def charts_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "IA Criteria Compliance",
                class_name="text-lg font-bold text-slate-800",
            ),
            rx.el.p(
                "Overall performance across 11 standard criteria",
                class_name="text-sm text-slate-500 mb-6",
            ),
            rx.recharts.bar_chart(
                rx.recharts.cartesian_grid(
                    stroke_dasharray="3 3", horizontal=True, vertical=False
                ),
                rx.recharts.graphing_tooltip(separator=""),
                rx.recharts.bar(
                    data_key="compliance", fill="#2563EB", radius=[4, 4, 0, 0]
                ),
                rx.recharts.x_axis(
                    data_key="name",
                    tick_line=False,
                    axis_line=False,
                    tick_size=10,
                    custom_attrs={
                        "fontSize": "10px",
                        "angle": -45,
                        "textAnchor": "end",
                        "dy": 10,
                    },
                ),
                rx.recharts.y_axis(
                    tick_line=False,
                    axis_line=False,
                    tick_size=10,
                    custom_attrs={"fontSize": "11px"},
                    domain=[0, 100],
                ),
                data=DashboardState.ia_chart_data,
                height=300,
                width="100%",
                margin={"left": 0, "right": 10, "top": 10, "bottom": 40},
            ),
            class_name="bg-white p-6 rounded-xl border border-slate-200 shadow-sm",
        ),
        rx.el.div(
            rx.el.h3(
                "Compliance Trend",
                class_name="text-lg font-bold text-slate-800",
            ),
            rx.el.p(
                "Year-over-year institutional compliance",
                class_name="text-sm text-slate-500 mb-6",
            ),
            rx.recharts.area_chart(
                rx.recharts.cartesian_grid(
                    stroke_dasharray="3 3", horizontal=True, vertical=False
                ),
                rx.recharts.graphing_tooltip(separator=""),
                rx.recharts.area(
                    data_key="overall_compliance",
                    stroke="#2563EB",
                    fill="#EFF6FF",
                    type_="monotone",
                ),
                rx.recharts.x_axis(
                    data_key="year",
                    tick_line=False,
                    axis_line=False,
                    tick_size=10,
                    custom_attrs={"fontSize": "11px"},
                ),
                rx.recharts.y_axis(
                    domain=[0, 100],
                    tick_line=False,
                    axis_line=False,
                    tick_size=10,
                    custom_attrs={"fontSize": "11px"},
                ),
                data=DashboardState.ia_trend_data,
                height=300,
                width="100%",
                margin={"left": 0, "right": 10, "top": 10, "bottom": 0},
            ),
            class_name="bg-white p-6 rounded-xl border border-slate-200 shadow-sm",
        ),
        class_name="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8",
    )


def criteria_list_item(crit: dict, is_top: bool) -> rx.Component:
    dot_color = rx.cond(
        is_top,
        "bg-emerald-500",
        rx.cond(crit["score"].to(float) < 5.0, "bg-red-500", "bg-amber-500"),
    )
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                class_name=f"w-2 h-2 rounded-full {dot_color} mr-3 shrink-0 mt-1.5"
            ),
            rx.el.div(
                rx.el.p(
                    crit["name"],
                    class_name="text-sm font-medium text-slate-900 truncate",
                ),
                rx.cond(
                    ~is_top,
                    rx.el.a(
                        "Review →",
                        href="/ia-assessment",
                        class_name="text-xs font-semibold text-blue-600 hover:text-blue-800 transition-colors",
                    ),
                    rx.fragment(),
                ),
            ),
            class_name="flex items-start",
        ),
        rx.el.div(
            rx.el.p(
                f"{crit['score']}/7.0",
                class_name="text-sm font-bold text-slate-900",
            ),
            class_name="ml-4 shrink-0 text-right",
        ),
        class_name="flex items-center justify-between py-3 border-b border-slate-100 last:border-0",
    )


def secondary_insights() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "Top Performing Criteria",
                class_name="text-lg font-bold text-slate-800 mb-4",
            ),
            rx.el.div(
                rx.foreach(
                    DashboardState.top_criteria,
                    lambda c: criteria_list_item(c, True),
                )
            ),
            class_name="bg-white p-6 rounded-xl border border-slate-200 shadow-sm",
        ),
        rx.el.div(
            rx.el.div(
                class_name="absolute top-0 left-0 w-full h-1 bg-red-100 rounded-t-xl"
            ),
            rx.el.h3(
                "Criteria Needing Attention",
                class_name="text-lg font-bold text-slate-800 mb-4 mt-1",
            ),
            rx.el.div(
                rx.foreach(
                    DashboardState.bottom_criteria,
                    lambda c: criteria_list_item(c, False),
                )
            ),
            class_name="bg-white px-6 pb-6 pt-5 rounded-xl border border-slate-200 shadow-sm relative",
        ),
        rx.el.div(
            rx.el.h3(
                "Quick Actions",
                class_name="text-lg font-bold text-slate-800 mb-4",
            ),
            rx.el.div(
                rx.el.a(
                    rx.icon(
                        "file-text", class_name="h-4 w-4 mr-3 text-slate-500"
                    ),
                    rx.el.span(
                        "Generate IA Report",
                        class_name="text-sm font-medium text-slate-700",
                    ),
                    href="/reports",
                    class_name="flex items-center w-full px-4 py-3 mb-2 bg-white border border-slate-200 rounded-lg hover:bg-slate-50 transition-colors",
                ),
                rx.el.a(
                    rx.icon(
                        "bar-chart-3", class_name="h-4 w-4 mr-3 text-slate-500"
                    ),
                    rx.el.span(
                        "View PLO Analytics",
                        class_name="text-sm font-medium text-slate-700",
                    ),
                    href="/plo-analytics",
                    class_name="flex items-center w-full px-4 py-3 mb-2 bg-white border border-slate-200 rounded-lg hover:bg-slate-50 transition-colors",
                ),
                rx.el.a(
                    rx.icon(
                        "database", class_name="h-4 w-4 mr-3 text-slate-500"
                    ),
                    rx.el.span(
                        "Manage Assessment Data",
                        class_name="text-sm font-medium text-slate-700",
                    ),
                    href="/data-management",
                    class_name="flex items-center w-full px-4 py-3 mb-2 bg-white border border-slate-200 rounded-lg hover:bg-slate-50 transition-colors",
                ),
                rx.el.a(
                    rx.icon(
                        "settings", class_name="h-4 w-4 mr-3 text-slate-500"
                    ),
                    rx.el.span(
                        "Review Settings",
                        class_name="text-sm font-medium text-slate-700",
                    ),
                    href="/settings",
                    class_name="flex items-center w-full px-4 py-3 bg-white border border-slate-200 rounded-lg hover:bg-slate-50 transition-colors",
                ),
                class_name="flex flex-col",
            ),
            class_name="bg-white p-6 rounded-xl border border-slate-200 shadow-sm",
        ),
        class_name="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8",
    )


def program_summary_row(prog: dict) -> rx.Component:
    val = prog["avg_attainment"].to(float)
    status_met = val >= 80.0
    return rx.el.div(
        rx.el.div(
            rx.el.p(
                prog["program"],
                class_name="w-24 font-bold text-slate-900 text-sm",
            ),
            rx.el.div(
                rx.el.div(
                    class_name="h-full bg-teal-500 rounded-full",
                    style={"width": f"{val}%"},
                ),
                class_name="flex-1 h-3 bg-slate-100 rounded-full overflow-hidden mx-4",
            ),
            rx.el.p(
                f"{prog['avg_attainment']}%",
                class_name="w-16 text-right font-bold text-slate-900 text-sm",
            ),
            rx.el.div(
                rx.cond(
                    status_met,
                    rx.el.span(
                        "Met",
                        class_name="px-2 py-1 bg-emerald-100 text-emerald-800 text-xs font-bold rounded-md",
                    ),
                    rx.el.span(
                        "Not Met",
                        class_name="px-2 py-1 bg-red-100 text-red-800 text-xs font-bold rounded-md",
                    ),
                ),
                class_name="w-20 text-right ml-4",
            ),
            class_name="flex items-center w-full",
        ),
        class_name="py-3 border-b border-slate-100 last:border-0",
    )


def plo_summary() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h3(
                "PLO Attainment by Program",
                class_name="text-lg font-bold text-slate-800",
            ),
            rx.el.p(
                "Program-level outcome achievement rates",
                class_name="text-sm text-slate-500 mb-6",
            ),
        ),
        rx.el.div(
            rx.foreach(DashboardState.program_summary_data, program_summary_row)
        ),
        class_name="bg-white p-6 rounded-xl border border-slate-200 shadow-sm mb-8",
    )


def activity_item(act: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(act["icon"], class_name=f"h-4 w-4 {act['color']}"),
            class_name=f"w-8 h-8 rounded-full {act['bg']} flex items-center justify-center shrink-0 mt-1 z-10",
        ),
        rx.el.div(
            rx.el.p(
                act["text"], class_name="text-sm font-medium text-slate-800"
            ),
            rx.el.p(act["time"], class_name="text-xs text-slate-400 mt-0.5"),
            class_name="ml-4 flex-1",
        ),
        class_name="flex items-start relative pb-6 last:pb-0 before:content-[''] before:absolute before:left-4 before:top-10 before:bottom-0 before:w-px before:-ml-px before:bg-slate-200 last:before:hidden",
    )


def recent_activity() -> rx.Component:
    return rx.el.div(
        rx.el.h3(
            "Recent Activity",
            class_name="text-lg font-bold text-slate-800 mb-6",
        ),
        rx.el.div(rx.foreach(DashboardState.recent_activities, activity_item)),
        class_name="bg-white p-6 rounded-xl border border-slate-200 shadow-sm",
    )


def dashboard_page() -> rx.Component:
    content = rx.el.div(
        welcome_banner(),
        primary_kpi_cards(),
        charts_section(),
        secondary_insights(),
        plo_summary(),
        recent_activity(),
        class_name="animate-fade-in max-w-7xl mx-auto",
    )
    return layout(content, "Dashboard Overview", "Home / Dashboard", "/")