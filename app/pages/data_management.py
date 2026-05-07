import reflex as rx
from app.components.layout import layout
from app.states.data_management_state import DataManagementState
from app.states.dashboard_state import DashboardState


def tab_bar() -> rx.Component:
    return rx.el.div(
        rx.el.nav(
            rx.el.button(
                "IA Indicators",
                on_click=DataManagementState.set_active_tab("ia"),
                class_name=rx.cond(
                    DataManagementState.active_tab == "ia",
                    "whitespace-nowrap pb-4 px-1 border-b-2 border-blue-600 font-medium text-sm text-blue-600",
                    "whitespace-nowrap pb-4 px-1 border-b-2 border-transparent font-medium text-sm text-slate-500 hover:text-slate-700 hover:border-slate-300",
                ),
            ),
            rx.el.button(
                "PLO Assessments",
                on_click=DataManagementState.set_active_tab("plo"),
                class_name=rx.cond(
                    DataManagementState.active_tab == "plo",
                    "whitespace-nowrap pb-4 px-1 border-b-2 border-blue-600 font-medium text-sm text-blue-600 ml-8",
                    "whitespace-nowrap pb-4 px-1 border-b-2 border-transparent font-medium text-sm text-slate-500 hover:text-slate-700 hover:border-slate-300 ml-8",
                ),
            ),
            class_name="-mb-px flex",
            aria_label="Tabs",
        ),
        class_name="border-b border-slate-200 mb-6",
    )


def action_bar() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon(
                    "search",
                    class_name="h-4 w-4 text-slate-400 absolute left-3 top-1/2 transform -translate-y-1/2",
                ),
                rx.el.input(
                    placeholder=rx.cond(
                        DataManagementState.active_tab == "ia",
                        "Search criteria...",
                        "Search PLOs...",
                    ),
                    on_change=DataManagementState.set_search_query.debounce(
                        300
                    ),
                    class_name="pl-9 pr-4 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 w-full sm:w-64",
                ),
                class_name="relative",
            ),
            class_name="flex-1",
        ),
        rx.cond(
            DataManagementState.can_edit,
            rx.el.button(
                rx.icon("plus", class_name="h-4 w-4 mr-2"),
                "Add New",
                on_click=DataManagementState.toggle_add_modal,
                class_name="flex items-center px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium rounded-lg transition-colors",
            ),
            rx.fragment(),
        ),
        class_name="flex justify-between items-center mb-6",
    )


def ia_table_row(item: dict) -> rx.Component:
    status_color = rx.match(
        item["status"],
        ("Compliant", "bg-emerald-100 text-emerald-800"),
        ("Needs Improvement", "bg-amber-100 text-amber-800"),
        ("At Risk", "bg-red-100 text-red-800"),
        "bg-slate-100 text-slate-800",
    )
    score_color = rx.cond(
        item["score"].to(float) >= 5.0,
        "text-emerald-600",
        rx.cond(
            item["score"].to(float) >= 4.0, "text-amber-600", "text-red-600"
        ),
    )
    return rx.el.tr(
        rx.el.td(
            item["id"],
            class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900",
        ),
        rx.el.td(
            item["name"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-slate-700",
        ),
        rx.el.td(
            rx.el.span(
                f"{item['score']} / 7.0",
                class_name=f"font-semibold {score_color}",
            ),
            class_name="px-6 py-4 whitespace-nowrap text-sm",
        ),
        rx.el.td(
            rx.el.div(
                rx.el.div(
                    class_name="h-2 bg-blue-600 rounded-full",
                    style={"width": f"{item['compliance_pct']}%"},
                ),
                class_name="w-24 bg-slate-200 rounded-full overflow-hidden",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.el.span(
                item["status"],
                class_name=f"px-2.5 py-0.5 rounded-full text-xs font-medium {status_color}",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            item["evidence_count"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-slate-700",
        ),
        rx.el.td(
            rx.cond(
                DataManagementState.can_edit,
                rx.el.div(
                    rx.el.button(
                        rx.icon("pencil", class_name="h-4 w-4"),
                        on_click=DataManagementState.toggle_edit_modal(item),
                        class_name="text-slate-400 hover:text-blue-600 mr-3 transition-colors",
                        title="Edit",
                    ),
                    rx.el.button(
                        rx.icon("trash-2", class_name="h-4 w-4"),
                        on_click=DataManagementState.delete_ia_indicator(
                            item["id"]
                        ),
                        class_name="text-slate-400 hover:text-red-600 transition-colors",
                        title="Delete",
                    ),
                    class_name="flex items-center",
                ),
                rx.fragment(),
            ),
            class_name="px-6 py-4 whitespace-nowrap text-right text-sm font-medium",
        ),
        class_name="hover:bg-slate-50 transition-colors border-b border-slate-200",
    )


def ia_table() -> rx.Component:
    return rx.cond(
        DataManagementState.active_tab == "ia",
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "ID",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Criteria Name",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Score",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Compliance %",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Evidence",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Actions",
                            class_name="px-6 py-3 text-right text-xs font-semibold text-slate-500 uppercase tracking-wider",
                        ),
                        class_name="bg-slate-50 border-b border-slate-200",
                    )
                ),
                rx.el.tbody(
                    rx.foreach(
                        DataManagementState.filtered_ia_data, ia_table_row
                    )
                ),
                class_name="min-w-full",
            ),
            class_name="bg-white rounded-xl shadow-sm border border-slate-200 overflow-x-auto",
        ),
        rx.fragment(),
    )


def plo_table_row(item: dict) -> rx.Component:
    attainment = item["attainment_pct"].to(float)
    attainment_color = rx.cond(
        attainment >= 80.0,
        "text-emerald-600",
        rx.cond(attainment >= 70.0, "text-amber-600", "text-red-600"),
    )
    status = rx.cond(attainment >= 80.0, "Met", "Not Met")
    status_color = rx.cond(
        attainment >= 80.0,
        "bg-emerald-100 text-emerald-800",
        "bg-red-100 text-red-800",
    )
    return rx.el.tr(
        rx.el.td(
            item["program"],
            class_name="px-6 py-4 whitespace-nowrap text-sm font-medium text-slate-900",
        ),
        rx.el.td(
            item["plo_id"],
            class_name="px-6 py-4 whitespace-nowrap text-sm text-slate-700",
        ),
        rx.el.td(
            item["description"], class_name="px-6 py-4 text-sm text-slate-700"
        ),
        rx.el.td(
            rx.el.span(
                f"{item['attainment_pct']}%",
                class_name=f"font-semibold {attainment_color}",
            ),
            class_name="px-6 py-4 whitespace-nowrap text-sm",
        ),
        rx.el.td(
            rx.el.span(
                status,
                class_name=f"px-2.5 py-0.5 rounded-full text-xs font-medium {status_color}",
            ),
            class_name="px-6 py-4 whitespace-nowrap",
        ),
        rx.el.td(
            rx.cond(
                DataManagementState.can_edit,
                rx.el.div(
                    rx.el.button(
                        rx.icon("pencil", class_name="h-4 w-4"),
                        on_click=DataManagementState.toggle_edit_modal(item),
                        class_name="text-slate-400 hover:text-blue-600 mr-3 transition-colors",
                        title="Edit",
                    ),
                    rx.el.button(
                        rx.icon("trash-2", class_name="h-4 w-4"),
                        on_click=DataManagementState.delete_plo_assessment(
                            item["plo_id"]
                        ),
                        class_name="text-slate-400 hover:text-red-600 transition-colors",
                        title="Delete",
                    ),
                    class_name="flex items-center",
                ),
                rx.fragment(),
            ),
            class_name="px-6 py-4 whitespace-nowrap text-right text-sm font-medium",
        ),
        class_name="hover:bg-slate-50 transition-colors border-b border-slate-200",
    )


def plo_table() -> rx.Component:
    return rx.cond(
        DataManagementState.active_tab == "plo",
        rx.el.div(
            rx.el.table(
                rx.el.thead(
                    rx.el.tr(
                        rx.el.th(
                            "Program",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "PLO ID",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Description",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Attainment %",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Status",
                            class_name="px-6 py-3 text-left text-xs font-semibold text-slate-500 uppercase tracking-wider",
                        ),
                        rx.el.th(
                            "Actions",
                            class_name="px-6 py-3 text-right text-xs font-semibold text-slate-500 uppercase tracking-wider",
                        ),
                        class_name="bg-slate-50 border-b border-slate-200",
                    )
                ),
                rx.el.tbody(
                    rx.foreach(
                        DataManagementState.filtered_plo_data, plo_table_row
                    )
                ),
                class_name="min-w-full",
            ),
            class_name="bg-white rounded-xl shadow-sm border border-slate-200 overflow-x-auto",
        ),
        rx.fragment(),
    )


def add_modal() -> rx.Component:
    return rx.cond(
        DataManagementState.show_add_modal,
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        rx.cond(
                            DataManagementState.active_tab == "ia",
                            "Add IA Indicator",
                            "Add PLO Assessment",
                        ),
                        class_name="text-lg font-bold text-slate-900",
                    ),
                    rx.el.button(
                        rx.icon("x", class_name="h-5 w-5 text-slate-500"),
                        on_click=DataManagementState.toggle_add_modal,
                        class_name="hover:text-slate-700",
                    ),
                    class_name="flex justify-between items-center mb-4",
                ),
                rx.cond(
                    DataManagementState.active_tab == "ia",
                    rx.el.form(
                        rx.el.div(
                            rx.el.label(
                                "Name",
                                class_name="block text-sm font-medium text-slate-700 mb-1",
                            ),
                            rx.el.input(
                                name="name",
                                required=True,
                                class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500",
                            ),
                            class_name="mb-4",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Score (0-7)",
                                    class_name="block text-sm font-medium text-slate-700 mb-1",
                                ),
                                rx.el.input(
                                    type="number",
                                    name="score",
                                    step="0.1",
                                    min="0",
                                    max="7",
                                    required=True,
                                    class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500",
                                ),
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Compliance %",
                                    class_name="block text-sm font-medium text-slate-700 mb-1",
                                ),
                                rx.el.input(
                                    type="number",
                                    name="compliance_pct",
                                    min="0",
                                    max="100",
                                    required=True,
                                    class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500",
                                ),
                            ),
                            class_name="grid grid-cols-2 gap-4 mb-4",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Status",
                                    class_name="block text-sm font-medium text-slate-700 mb-1",
                                ),
                                rx.el.select(
                                    rx.el.option(
                                        "Compliant", value="Compliant"
                                    ),
                                    rx.el.option(
                                        "Needs Improvement",
                                        value="Needs Improvement",
                                    ),
                                    rx.el.option("At Risk", value="At Risk"),
                                    name="status",
                                    class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500 bg-white appearance-none",
                                ),
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Evidence Count",
                                    class_name="block text-sm font-medium text-slate-700 mb-1",
                                ),
                                rx.el.input(
                                    type="number",
                                    name="evidence_count",
                                    min="0",
                                    required=True,
                                    class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500",
                                ),
                            ),
                            class_name="grid grid-cols-2 gap-4 mb-6",
                        ),
                        rx.el.div(
                            rx.el.button(
                                "Cancel",
                                type="button",
                                on_click=DataManagementState.toggle_add_modal,
                                class_name="px-4 py-2 border border-slate-300 rounded-md text-sm font-medium text-slate-700 bg-white hover:bg-slate-50",
                            ),
                            rx.el.button(
                                "Add Indicator",
                                type="submit",
                                class_name="ml-3 px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700",
                            ),
                            class_name="flex justify-end",
                        ),
                        on_submit=DataManagementState.add_ia_indicator,
                        reset_on_submit=True,
                    ),
                    rx.el.form(
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Program",
                                    class_name="block text-sm font-medium text-slate-700 mb-1",
                                ),
                                rx.el.select(
                                    rx.el.option("BSCS", value="BSCS"),
                                    rx.el.option("BSIT", value="BSIT"),
                                    rx.el.option("BSMM", value="BSMM"),
                                    rx.el.option("BSA", value="BSA"),
                                    rx.el.option("BSBA", value="BSBA"),
                                    name="program",
                                    class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500 bg-white appearance-none",
                                ),
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "PLO ID",
                                    class_name="block text-sm font-medium text-slate-700 mb-1",
                                ),
                                rx.el.input(
                                    name="plo_id",
                                    required=True,
                                    class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500",
                                ),
                            ),
                            class_name="grid grid-cols-2 gap-4 mb-4",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Description",
                                class_name="block text-sm font-medium text-slate-700 mb-1",
                            ),
                            rx.el.input(
                                name="description",
                                required=True,
                                class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500",
                            ),
                            class_name="mb-4",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Attainment %",
                                class_name="block text-sm font-medium text-slate-700 mb-1",
                            ),
                            rx.el.input(
                                type="number",
                                name="attainment_pct",
                                step="0.1",
                                min="0",
                                max="100",
                                required=True,
                                class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500",
                            ),
                            class_name="mb-6",
                        ),
                        rx.el.div(
                            rx.el.button(
                                "Cancel",
                                type="button",
                                on_click=DataManagementState.toggle_add_modal,
                                class_name="px-4 py-2 border border-slate-300 rounded-md text-sm font-medium text-slate-700 bg-white hover:bg-slate-50",
                            ),
                            rx.el.button(
                                "Add Assessment",
                                type="submit",
                                class_name="ml-3 px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700",
                            ),
                            class_name="flex justify-end",
                        ),
                        on_submit=DataManagementState.add_plo_assessment,
                        reset_on_submit=True,
                    ),
                ),
                class_name="bg-white rounded-xl shadow-xl p-6 w-full max-w-md mx-4",
            ),
            class_name="fixed inset-0 bg-slate-900/50 z-50 flex items-center justify-center",
        ),
        rx.fragment(),
    )


def edit_modal() -> rx.Component:
    return rx.cond(
        DataManagementState.show_edit_modal,
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        rx.cond(
                            DataManagementState.active_tab == "ia",
                            "Edit IA Indicator",
                            "Edit PLO Assessment",
                        ),
                        class_name="text-lg font-bold text-slate-900",
                    ),
                    rx.el.button(
                        rx.icon("x", class_name="h-5 w-5 text-slate-500"),
                        on_click=DataManagementState.toggle_edit_modal(),
                        class_name="hover:text-slate-700",
                    ),
                    class_name="flex justify-between items-center mb-4",
                ),
                rx.cond(
                    DataManagementState.active_tab == "ia",
                    rx.el.form(
                        rx.el.input(
                            type="hidden",
                            name="original_id",
                            value=DataManagementState.editing_item["id"].to(
                                str
                            ),
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Name",
                                class_name="block text-sm font-medium text-slate-700 mb-1",
                            ),
                            rx.el.input(
                                name="name",
                                default_value=DataManagementState.editing_item[
                                    "name"
                                ].to(str),
                                required=True,
                                class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500",
                            ),
                            class_name="mb-4",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Score (0-7)",
                                    class_name="block text-sm font-medium text-slate-700 mb-1",
                                ),
                                rx.el.input(
                                    type="number",
                                    name="score",
                                    step="0.1",
                                    min="0",
                                    max="7",
                                    default_value=DataManagementState.editing_item[
                                        "score"
                                    ].to(str),
                                    required=True,
                                    class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500",
                                ),
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Compliance %",
                                    class_name="block text-sm font-medium text-slate-700 mb-1",
                                ),
                                rx.el.input(
                                    type="number",
                                    name="compliance_pct",
                                    min="0",
                                    max="100",
                                    default_value=DataManagementState.editing_item[
                                        "compliance_pct"
                                    ].to(str),
                                    required=True,
                                    class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500",
                                ),
                            ),
                            class_name="grid grid-cols-2 gap-4 mb-4",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Status",
                                    class_name="block text-sm font-medium text-slate-700 mb-1",
                                ),
                                rx.el.select(
                                    rx.el.option(
                                        "Compliant", value="Compliant"
                                    ),
                                    rx.el.option(
                                        "Needs Improvement",
                                        value="Needs Improvement",
                                    ),
                                    rx.el.option("At Risk", value="At Risk"),
                                    name="status",
                                    default_value=DataManagementState.editing_item[
                                        "status"
                                    ].to(str),
                                    class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500 bg-white appearance-none",
                                ),
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "Evidence Count",
                                    class_name="block text-sm font-medium text-slate-700 mb-1",
                                ),
                                rx.el.input(
                                    type="number",
                                    name="evidence_count",
                                    min="0",
                                    default_value=DataManagementState.editing_item[
                                        "evidence_count"
                                    ].to(str),
                                    required=True,
                                    class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500",
                                ),
                            ),
                            class_name="grid grid-cols-2 gap-4 mb-6",
                        ),
                        rx.el.div(
                            rx.el.button(
                                "Cancel",
                                type="button",
                                on_click=DataManagementState.toggle_edit_modal(),
                                class_name="px-4 py-2 border border-slate-300 rounded-md text-sm font-medium text-slate-700 bg-white hover:bg-slate-50",
                            ),
                            rx.el.button(
                                "Save Changes",
                                type="submit",
                                class_name="ml-3 px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700",
                            ),
                            class_name="flex justify-end",
                        ),
                        on_submit=DataManagementState.update_ia_indicator,
                        reset_on_submit=True,
                    ),
                    rx.el.form(
                        rx.el.input(
                            type="hidden",
                            name="original_id",
                            value=DataManagementState.editing_item["plo_id"].to(
                                str
                            ),
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.label(
                                    "Program",
                                    class_name="block text-sm font-medium text-slate-700 mb-1",
                                ),
                                rx.el.select(
                                    rx.el.option("BSCS", value="BSCS"),
                                    rx.el.option("BSIT", value="BSIT"),
                                    rx.el.option("BSMM", value="BSMM"),
                                    rx.el.option("BSA", value="BSA"),
                                    rx.el.option("BSBA", value="BSBA"),
                                    name="program",
                                    default_value=DataManagementState.editing_item[
                                        "program"
                                    ].to(str),
                                    class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500 bg-white appearance-none",
                                ),
                            ),
                            rx.el.div(
                                rx.el.label(
                                    "PLO ID",
                                    class_name="block text-sm font-medium text-slate-700 mb-1",
                                ),
                                rx.el.input(
                                    name="plo_id",
                                    default_value=DataManagementState.editing_item[
                                        "plo_id"
                                    ].to(str),
                                    required=True,
                                    class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500",
                                ),
                            ),
                            class_name="grid grid-cols-2 gap-4 mb-4",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Description",
                                class_name="block text-sm font-medium text-slate-700 mb-1",
                            ),
                            rx.el.input(
                                name="description",
                                default_value=DataManagementState.editing_item[
                                    "description"
                                ].to(str),
                                required=True,
                                class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500",
                            ),
                            class_name="mb-4",
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Attainment %",
                                class_name="block text-sm font-medium text-slate-700 mb-1",
                            ),
                            rx.el.input(
                                type="number",
                                name="attainment_pct",
                                step="0.1",
                                min="0",
                                max="100",
                                default_value=DataManagementState.editing_item[
                                    "attainment_pct"
                                ].to(str),
                                required=True,
                                class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500",
                            ),
                            class_name="mb-6",
                        ),
                        rx.el.div(
                            rx.el.button(
                                "Cancel",
                                type="button",
                                on_click=DataManagementState.toggle_edit_modal(),
                                class_name="px-4 py-2 border border-slate-300 rounded-md text-sm font-medium text-slate-700 bg-white hover:bg-slate-50",
                            ),
                            rx.el.button(
                                "Save Changes",
                                type="submit",
                                class_name="ml-3 px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700",
                            ),
                            class_name="flex justify-end",
                        ),
                        on_submit=DataManagementState.update_plo_assessment,
                        reset_on_submit=True,
                    ),
                ),
                class_name="bg-white rounded-xl shadow-xl p-6 w-full max-w-md mx-4",
            ),
            class_name="fixed inset-0 bg-slate-900/50 z-50 flex items-center justify-center",
        ),
        rx.fragment(),
    )


def data_management_page() -> rx.Component:
    content = rx.el.div(
        tab_bar(),
        action_bar(),
        ia_table(),
        plo_table(),
        add_modal(),
        edit_modal(),
        class_name="animate-fade-in",
    )
    return layout(
        content, "Data Management", "Home / Data Management", "/data-management"
    )