import reflex as rx
from app.components.layout import layout
from app.states.dashboard_state import DashboardState
from app.pages.dashboard import stat_card, filter_bar


def criteria_card(criteria: dict) -> rx.Component:
    status_color = rx.match(
        criteria["status"],
        ("Compliant", "bg-emerald-100 text-emerald-800 border-emerald-200"),
        ("Needs Improvement", "bg-amber-100 text-amber-800 border-amber-200"),
        ("At Risk", "bg-red-100 text-red-800 border-red-200"),
        "bg-slate-100 text-slate-800 border-slate-200",
    )
    progress_color = rx.match(
        criteria["status"],
        ("Compliant", "bg-emerald-500"),
        ("Needs Improvement", "bg-amber-500"),
        ("At Risk", "bg-red-500"),
        "bg-slate-500",
    )
    return rx.el.div(
        rx.el.div(
            rx.el.h4(
                f"{criteria['id']}. {criteria['name']}",
                class_name="font-bold text-slate-900",
            ),
            rx.el.span(
                criteria["status"],
                class_name=f"text-xs font-semibold px-2 py-1 rounded-full border {status_color}",
            ),
            class_name="flex justify-between items-start mb-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "Score", class_name="text-xs text-slate-500 font-medium"
                ),
                rx.el.span(
                    f"{criteria['score']} / 7.0",
                    class_name="text-sm font-bold text-slate-900",
                ),
                class_name="flex justify-between mb-1",
            ),
            rx.el.div(
                rx.el.div(
                    class_name=f"h-full rounded-full {progress_color}",
                    style={
                        "width": f"{criteria['score'].to(float) / 7.0 * 100}%"
                    },
                ),
                class_name="w-full h-2 bg-slate-100 rounded-full mb-4 overflow-hidden",
            ),
        ),
        rx.el.div(
            rx.el.div(
                rx.icon("file-text", class_name="h-4 w-4 text-slate-400 mr-1"),
                rx.el.span(
                    f"{criteria['evidence_count']} Evidences",
                    class_name="text-xs text-slate-600",
                ),
                class_name="flex items-center",
            ),
            rx.el.button(
                "View Details",
                on_click=DashboardState.open_criteria_detail(criteria["id"]),
                class_name="text-xs font-medium text-blue-600 hover:text-blue-800",
            ),
            class_name="flex justify-between items-center mt-4 pt-4 border-t border-slate-100",
        ),
        class_name="bg-white p-5 rounded-xl border border-slate-200 shadow-sm",
    )


def criteria_modal() -> rx.Component:
    return rx.cond(
        DashboardState.show_criteria_detail,
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Criteria Details",
                        class_name="text-lg font-bold text-slate-900",
                    ),
                    rx.el.button(
                        rx.icon("x", class_name="h-5 w-5 text-slate-500"),
                        on_click=DashboardState.close_criteria_detail,
                    ),
                    class_name="flex justify-between items-center mb-4",
                ),
                rx.el.p(
                    f"Details for Criteria {DashboardState.selected_criteria} will go here in final version.",
                    class_name="text-slate-600 mb-6",
                ),
                rx.el.button(
                    "Close",
                    on_click=DashboardState.close_criteria_detail,
                    class_name="w-full bg-slate-100 hover:bg-slate-200 text-slate-800 font-semibold py-2 px-4 rounded-lg transition-colors",
                ),
                class_name="bg-white rounded-xl shadow-xl p-6 max-w-lg w-full",
            ),
            class_name="fixed inset-0 bg-slate-900/50 z-50 flex items-center justify-center p-4",
        ),
        rx.fragment(),
    )


def ia_assessment_page() -> rx.Component:
    content = rx.el.div(
        filter_bar(),
        rx.el.div(
            stat_card(
                "Overall IA Score",
                f"{DashboardState.avg_ia_score} / 7.0",
                "Average across 11 Criteria",
                "star",
                "text-blue-600",
            ),
            stat_card(
                "Compliant",
                f"{DashboardState.compliant_criteria_count}",
                "Criteria meeting standards",
                "check-circle",
                "text-emerald-600",
            ),
            stat_card(
                "Needs Improvement",
                f"{DashboardState.needs_improvement_count}",
                "Criteria requiring attention",
                "alert-circle",
                "text-amber-600",
            ),
            stat_card(
                "At Risk",
                f"{DashboardState.criteria_at_risk_count}",
                "Criteria below threshold",
                "triangle-alert",
                "text-red-600",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8",
        ),
        rx.el.div(
            rx.el.h4(
                "Criteria Scores (7-Point Scale)",
                class_name="text-lg font-bold text-slate-800 mb-6",
            ),
            rx.recharts.bar_chart(
                rx.recharts.cartesian_grid(
                    stroke_dasharray="3 3", horizontal=True, vertical=False
                ),
                rx.recharts.graphing_tooltip(separator=""),
                rx.recharts.bar(data_key="score", fill="#2563EB"),
                rx.recharts.x_axis(
                    rx.recharts.label(
                        value="Criteria",
                        position="bottom",
                        custom_attrs={"fontSize": "12px"},
                    ),
                    data_key="name",
                    tick_line=False,
                    axis_line=False,
                    tick_size=10,
                    custom_attrs={"fontSize": "10px"},
                ),
                rx.recharts.y_axis(
                    rx.recharts.label(
                        value="Score",
                        position="left",
                        custom_attrs={"angle": -90, "fontSize": "12px"},
                    ),
                    domain=[0, 7],
                    tick_line=False,
                    axis_line=False,
                    tick_size=10,
                    custom_attrs={"fontSize": "10px"},
                ),
                data=DashboardState.ia_score_chart_data,
                height=300,
                width="100%",
                margin={"left": 20, "right": 20, "top": 10, "bottom": 20},
            ),
            class_name="bg-white p-6 rounded-xl border border-slate-200 shadow-sm mb-8",
        ),
        rx.el.div(
            rx.foreach(
                DashboardState.ia_criteria_base, lambda c: criteria_card(c)
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-6",
        ),
        criteria_modal(),
        class_name="animate-fade-in",
    )
    return layout(
        content, "IA Assessment", "Home / IA Assessment", "/ia-assessment"
    )