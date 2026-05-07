import reflex as rx
from app.components.layout import layout
from app.states.dashboard_state import DashboardState
from app.pages.dashboard import stat_card


def program_selector() -> rx.Component:
    return rx.el.div(
        rx.foreach(
            DashboardState.program_options,
            lambda p: rx.el.button(
                p,
                on_click=DashboardState.set_program(p),
                class_name=rx.cond(
                    DashboardState.selected_program == p,
                    "px-4 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium transition-colors",
                    "px-4 py-2 bg-white text-slate-600 hover:bg-slate-50 border border-slate-200 rounded-lg text-sm font-medium transition-colors",
                ),
            ),
        ),
        class_name="flex flex-wrap gap-2 mb-8",
    )


def heat_map_row(mapping: dict) -> rx.Component:

    def get_color(val: str) -> str:
        return rx.match(
            val,
            ("High", "bg-teal-100 text-teal-800"),
            ("Medium", "bg-blue-100 text-blue-800"),
            ("Low", "bg-slate-100 text-slate-600"),
            "bg-white",
        )

    return rx.el.tr(
        rx.el.td(
            mapping["course"],
            class_name="px-4 py-3 font-medium text-slate-900 border-b border-slate-200",
        ),
        rx.el.td(
            mapping["PLO1"],
            class_name=f"px-4 py-3 text-center border-b border-slate-200 {get_color(mapping['PLO1'])}",
        ),
        rx.el.td(
            mapping["PLO2"],
            class_name=f"px-4 py-3 text-center border-b border-slate-200 {get_color(mapping['PLO2'])}",
        ),
        rx.el.td(
            mapping["PLO3"],
            class_name=f"px-4 py-3 text-center border-b border-slate-200 {get_color(mapping['PLO3'])}",
        ),
        rx.el.td(
            mapping["PLO4"],
            class_name=f"px-4 py-3 text-center border-b border-slate-200 {get_color(mapping['PLO4'])}",
        ),
        class_name="hover:bg-slate-50",
    )


def plo_analytics_page() -> rx.Component:
    content = rx.el.div(
        program_selector(),
        rx.el.div(
            stat_card(
                "Total PLOs Assessed",
                f"{DashboardState.total_plos_assessed}",
                "In selected program",
                "book-open",
                "text-teal-600",
            ),
            stat_card(
                "Average Attainment",
                f"{DashboardState.avg_plo_attainment}%",
                "Overall achievement",
                "activity",
                "text-teal-600",
            ),
            stat_card(
                "Above Target (>80%)",
                f"{DashboardState.plos_above_target}",
                "PLOs meeting goal",
                "arrow-up-right",
                "text-teal-600",
            ),
            stat_card(
                "Below Target",
                f"{DashboardState.plos_below_target}",
                "PLOs needing attention",
                "arrow-down-right",
                "text-red-600",
            ),
            class_name="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h4(
                    "PLO Attainment vs Target (80%)",
                    class_name="text-lg font-bold text-slate-800 mb-6",
                ),
                rx.recharts.bar_chart(
                    rx.recharts.cartesian_grid(
                        stroke_dasharray="3 3", horizontal=True, vertical=False
                    ),
                    rx.recharts.graphing_tooltip(separator=""),
                    rx.recharts.bar(data_key="attainment", fill="#14B8A6"),
                    rx.recharts.x_axis(
                        data_key="name",
                        tick_line=False,
                        axis_line=False,
                        custom_attrs={"fontSize": "10px"},
                    ),
                    rx.recharts.y_axis(
                        domain=[0, 100],
                        tick_line=False,
                        axis_line=False,
                        custom_attrs={"fontSize": "10px"},
                    ),
                    data=DashboardState.plo_chart_data,
                    height=300,
                    width="100%",
                    margin={"left": 20, "right": 20, "top": 10, "bottom": 20},
                ),
                class_name="bg-white p-6 rounded-xl border border-slate-200 shadow-sm",
            ),
            rx.el.div(
                rx.el.h4(
                    "PLO × Course Mapping Heatmap",
                    class_name="text-lg font-bold text-slate-800 mb-6",
                ),
                rx.el.div(
                    rx.el.table(
                        rx.el.thead(
                            rx.el.tr(
                                rx.el.th(
                                    "Course",
                                    class_name="px-4 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider border-b border-slate-200",
                                ),
                                rx.el.th(
                                    "PLO 1",
                                    class_name="px-4 py-3 text-center text-xs font-semibold text-slate-500 uppercase tracking-wider border-b border-slate-200",
                                ),
                                rx.el.th(
                                    "PLO 2",
                                    class_name="px-4 py-3 text-center text-xs font-semibold text-slate-500 uppercase tracking-wider border-b border-slate-200",
                                ),
                                rx.el.th(
                                    "PLO 3",
                                    class_name="px-4 py-3 text-center text-xs font-semibold text-slate-500 uppercase tracking-wider border-b border-slate-200",
                                ),
                                rx.el.th(
                                    "PLO 4",
                                    class_name="px-4 py-3 text-center text-xs font-semibold text-slate-500 uppercase tracking-wider border-b border-slate-200",
                                ),
                            )
                        ),
                        rx.el.tbody(
                            rx.foreach(
                                DashboardState.course_plo_mapping, heat_map_row
                            )
                        ),
                        class_name="min-w-full",
                    ),
                    class_name="overflow-x-auto rounded-lg border border-slate-200",
                ),
                class_name="bg-white p-6 rounded-xl border border-slate-200 shadow-sm",
            ),
            class_name="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-8",
        ),
        class_name="animate-fade-in",
    )
    return layout(
        content, "PLO Analytics", "Home / PLO Analytics", "/plo-analytics"
    )