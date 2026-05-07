import reflex as rx
from app.components.layout import layout
from app.states.settings_state import SettingsState
from app.states.auth_state import AuthState


def profile_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("user", class_name="h-5 w-5 text-blue-600 mr-2"),
            rx.el.h3(
                "Profile Information",
                class_name="text-lg font-bold text-slate-900",
            ),
            class_name="flex items-center mb-6 pb-4 border-b border-slate-100",
        ),
        rx.el.div(
            rx.el.div(
                rx.image(
                    src=f"https://api.dicebear.com/9.x/initials/svg?seed={AuthState.user_name}",
                    class_name="h-20 w-20 rounded-full bg-slate-200",
                ),
                class_name="mb-6 sm:mb-0 sm:mr-8",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.el.label(
                            "Full Name",
                            class_name="block text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1",
                        ),
                        rx.el.p(
                            AuthState.user_name,
                            class_name="text-sm font-medium text-slate-900",
                        ),
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Email Address",
                            class_name="block text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1",
                        ),
                        rx.el.p(
                            "user@apc.edu.ph",
                            class_name="text-sm font-medium text-slate-900",
                        ),
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Role",
                            class_name="block text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1",
                        ),
                        rx.el.span(
                            AuthState.user_role,
                            class_name="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800",
                        ),
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Program Affiliation",
                            class_name="block text-xs font-semibold text-slate-500 uppercase tracking-wider mb-1",
                        ),
                        rx.el.p(
                            AuthState.user_program,
                            class_name="text-sm font-medium text-slate-900",
                        ),
                    ),
                    class_name="grid grid-cols-1 sm:grid-cols-2 gap-6",
                ),
                class_name="flex-1",
            ),
            class_name="flex flex-col sm:flex-row items-start",
        ),
        rx.el.div(
            rx.el.button(
                "Sign Out",
                on_click=AuthState.logout,
                class_name="px-4 py-2 border border-red-200 text-red-600 hover:bg-red-50 text-sm font-medium rounded-lg transition-colors",
            ),
            class_name="mt-8 pt-4 border-t border-slate-100 flex justify-end",
        ),
        class_name="bg-white rounded-xl border border-slate-200 shadow-sm p-6 mb-8",
    )


def system_preferences_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon(
                "sliders_horizontal", class_name="h-5 w-5 text-blue-600 mr-2"
            ),
            rx.el.h3(
                "Assessment Configuration",
                class_name="text-lg font-bold text-slate-900",
            ),
            class_name="flex items-center mb-6 pb-4 border-b border-slate-100",
        ),
        rx.el.form(
            rx.el.div(
                rx.el.div(
                    rx.el.label(
                        "PLO Target Threshold",
                        class_name="block text-sm font-medium text-slate-700 mb-1",
                    ),
                    rx.el.div(
                        rx.el.input(
                            type="number",
                            name="plo_target",
                            default_value=SettingsState.plo_target.to(str),
                            min="0",
                            max="100",
                            step="1",
                            class_name="w-full pl-3 pr-8 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500",
                        ),
                        rx.el.span(
                            "%",
                            class_name="absolute right-3 top-1/2 transform -translate-y-1/2 text-slate-500 text-sm",
                        ),
                        class_name="relative",
                    ),
                ),
                rx.el.div(
                    rx.el.label(
                        "IA Compliance Threshold",
                        class_name="block text-sm font-medium text-slate-700 mb-1",
                    ),
                    rx.el.div(
                        rx.el.input(
                            type="number",
                            name="ia_threshold",
                            default_value=SettingsState.ia_threshold.to(str),
                            min="0",
                            max="7",
                            step="0.1",
                            class_name="w-full pl-3 pr-10 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500",
                        ),
                        rx.el.span(
                            "/7.0",
                            class_name="absolute right-3 top-1/2 transform -translate-y-1/2 text-slate-500 text-sm",
                        ),
                        class_name="relative",
                    ),
                ),
                rx.el.div(
                    rx.el.label(
                        "Academic Year",
                        class_name="block text-sm font-medium text-slate-700 mb-1",
                    ),
                    rx.el.select(
                        rx.el.option("2024", value="2024"),
                        rx.el.option("2023", value="2023"),
                        rx.el.option("2022", value="2022"),
                        rx.el.option("2021", value="2021"),
                        rx.el.option("2020", value="2020"),
                        name="academic_year",
                        default_value=SettingsState.academic_year,
                        class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500 bg-white appearance-none",
                    ),
                ),
                rx.el.div(
                    rx.el.label(
                        "Assessment Cycle",
                        class_name="block text-sm font-medium text-slate-700 mb-1",
                    ),
                    rx.el.select(
                        rx.el.option("Annual", value="Annual"),
                        rx.el.option("Bi-annual", value="Bi-annual"),
                        rx.el.option("Quarterly", value="Quarterly"),
                        name="assessment_cycle",
                        default_value=SettingsState.assessment_cycle,
                        class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500 bg-white appearance-none",
                    ),
                ),
                class_name="grid grid-cols-1 sm:grid-cols-2 gap-6 mb-6",
            ),
            rx.el.div(
                rx.el.button(
                    "Save Preferences",
                    type="submit",
                    class_name="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white text-sm font-medium rounded-lg transition-colors",
                ),
                class_name="flex justify-end",
            ),
            on_submit=SettingsState.update_preferences,
            reset_on_submit=False,
        ),
        class_name="bg-white rounded-xl border border-slate-200 shadow-sm p-6 mb-8",
    )


def toggle_row(
    label: str, description: str, state_var: rx.Var, toggle_key: str
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.p(label, class_name="text-sm font-medium text-slate-900"),
            rx.el.p(description, class_name="text-sm text-slate-500"),
        ),
        rx.el.button(
            rx.el.span(
                class_name=rx.cond(
                    state_var,
                    "translate-x-5 pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow transform ring-0 transition ease-in-out duration-200",
                    "translate-x-0 pointer-events-none inline-block h-5 w-5 rounded-full bg-white shadow transform ring-0 transition ease-in-out duration-200",
                )
            ),
            role="switch",
            on_click=lambda: SettingsState.toggle_notification(
                toggle_key, ~state_var
            ),
            class_name=rx.cond(
                state_var,
                "bg-blue-600 relative inline-flex flex-shrink-0 h-6 w-11 border-2 border-transparent rounded-full cursor-pointer transition-colors ease-in-out duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500",
                "bg-slate-200 relative inline-flex flex-shrink-0 h-6 w-11 border-2 border-transparent rounded-full cursor-pointer transition-colors ease-in-out duration-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500",
            ),
        ),
        class_name="flex items-center justify-between py-4 border-b border-slate-100 last:border-0",
    )


def notifications_card() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.icon("bell", class_name="h-5 w-5 text-blue-600 mr-2"),
            rx.el.h3(
                "Notifications", class_name="text-lg font-bold text-slate-900"
            ),
            class_name="flex items-center mb-2 pb-4 border-b border-slate-100",
        ),
        toggle_row(
            "Email Notifications",
            "Receive alerts when criteria fall below threshold",
            SettingsState.email_notifications,
            "email_notifications",
        ),
        toggle_row(
            "Weekly Reports",
            "Get automated weekly summary reports",
            SettingsState.weekly_reports,
            "weekly_reports",
        ),
        toggle_row(
            "PLO Alerts",
            "Notifications when PLO attainment drops below target",
            SettingsState.plo_alerts,
            "plo_alerts",
        ),
        class_name="bg-white rounded-xl border border-slate-200 shadow-sm p-6 mb-8",
    )


def user_management_card() -> rx.Component:
    return rx.cond(
        AuthState.is_admin,
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.icon("users", class_name="h-5 w-5 text-blue-600 mr-2"),
                    rx.el.h3(
                        "User Management",
                        class_name="text-lg font-bold text-slate-900",
                    ),
                    class_name="flex items-center",
                ),
                rx.el.button(
                    rx.icon("plus", class_name="h-4 w-4 mr-2"),
                    "Add User",
                    on_click=SettingsState.toggle_add_user_modal,
                    class_name="flex items-center px-3 py-1.5 bg-white border border-slate-300 text-slate-700 hover:bg-slate-50 text-sm font-medium rounded-lg transition-colors",
                ),
                class_name="flex justify-between items-center mb-6 pb-4 border-b border-slate-100",
            ),
            rx.el.div(
                rx.el.table(
                    rx.el.thead(
                        rx.el.tr(
                            rx.el.th(
                                "Name",
                                class_name="px-4 py-3 text-left text-xs font-semibold text-slate-500 uppercase",
                            ),
                            rx.el.th(
                                "Email",
                                class_name="px-4 py-3 text-left text-xs font-semibold text-slate-500 uppercase",
                            ),
                            rx.el.th(
                                "Role",
                                class_name="px-4 py-3 text-left text-xs font-semibold text-slate-500 uppercase",
                            ),
                            rx.el.th(
                                "Program",
                                class_name="px-4 py-3 text-left text-xs font-semibold text-slate-500 uppercase",
                            ),
                            rx.el.th(
                                "Status",
                                class_name="px-4 py-3 text-left text-xs font-semibold text-slate-500 uppercase",
                            ),
                            class_name="bg-slate-50 border-b border-slate-200",
                        )
                    ),
                    rx.el.tbody(
                        rx.foreach(
                            SettingsState.sample_users,
                            lambda u: rx.el.tr(
                                rx.el.td(
                                    u["name"],
                                    class_name="px-4 py-3 text-sm font-medium text-slate-900 border-b border-slate-100",
                                ),
                                rx.el.td(
                                    u["email"],
                                    class_name="px-4 py-3 text-sm text-slate-500 border-b border-slate-100",
                                ),
                                rx.el.td(
                                    u["role"],
                                    class_name="px-4 py-3 text-sm text-slate-700 border-b border-slate-100",
                                ),
                                rx.el.td(
                                    u["program"],
                                    class_name="px-4 py-3 text-sm text-slate-700 border-b border-slate-100",
                                ),
                                rx.el.td(
                                    rx.cond(
                                        u["status"] == "Active",
                                        rx.el.span(
                                            "Active",
                                            class_name="inline-flex items-center px-2 py-0.5 rounded-full text-xs font-medium bg-emerald-100 text-emerald-800",
                                        ),
                                        rx.el.span(
                                            "Inactive",
                                            class_name="inline-flex items-center px-2 py-0.5 rounded-full text-xs font-medium bg-slate-100 text-slate-600",
                                        ),
                                    ),
                                    class_name="px-4 py-3 whitespace-nowrap border-b border-slate-100",
                                ),
                                class_name="hover:bg-slate-50",
                            ),
                        )
                    ),
                    class_name="w-full",
                ),
                class_name="overflow-x-auto rounded-lg border border-slate-200",
            ),
            class_name="bg-white rounded-xl border border-slate-200 shadow-sm p-6",
        ),
        rx.fragment(),
    )


def add_user_modal() -> rx.Component:
    return rx.cond(
        SettingsState.show_add_user_modal,
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "Add New User",
                        class_name="text-lg font-bold text-slate-900",
                    ),
                    rx.el.button(
                        rx.icon("x", class_name="h-5 w-5 text-slate-500"),
                        on_click=SettingsState.toggle_add_user_modal,
                        class_name="hover:text-slate-700",
                    ),
                    class_name="flex justify-between items-center mb-4",
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.label(
                            "Full Name",
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
                        rx.el.label(
                            "Email Address",
                            class_name="block text-sm font-medium text-slate-700 mb-1",
                        ),
                        rx.el.input(
                            type="email",
                            name="email",
                            required=True,
                            class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500",
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.label(
                                "Role",
                                class_name="block text-sm font-medium text-slate-700 mb-1",
                            ),
                            rx.el.select(
                                rx.el.option("Admin", value="Admin"),
                                rx.el.option(
                                    "Program Chair", value="Program Chair"
                                ),
                                rx.el.option("Faculty", value="Faculty"),
                                rx.el.option(
                                    "Stakeholder", value="Stakeholder"
                                ),
                                name="role",
                                class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500 bg-white appearance-none",
                            ),
                        ),
                        rx.el.div(
                            rx.el.label(
                                "Program",
                                class_name="block text-sm font-medium text-slate-700 mb-1",
                            ),
                            rx.el.select(
                                rx.el.option("All", value="All"),
                                rx.el.option("BSCS", value="BSCS"),
                                rx.el.option("BSIT", value="BSIT"),
                                rx.el.option("BSBA", value="BSBA"),
                                rx.el.option("N/A", value="N/A"),
                                name="program",
                                class_name="w-full px-3 py-2 border border-slate-300 rounded-md text-sm focus:ring-blue-500 focus:border-blue-500 bg-white appearance-none",
                            ),
                        ),
                        class_name="grid grid-cols-2 gap-4 mb-6",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "Cancel",
                            type="button",
                            on_click=SettingsState.toggle_add_user_modal,
                            class_name="px-4 py-2 border border-slate-300 rounded-md text-sm font-medium text-slate-700 bg-white hover:bg-slate-50",
                        ),
                        rx.el.button(
                            "Add User",
                            type="submit",
                            class_name="ml-3 px-4 py-2 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-blue-600 hover:bg-blue-700",
                        ),
                        class_name="flex justify-end",
                    ),
                    on_submit=SettingsState.add_user,
                    reset_on_submit=True,
                ),
                class_name="bg-white rounded-xl shadow-xl p-6 w-full max-w-md mx-4",
            ),
            class_name="fixed inset-0 bg-slate-900/50 z-50 flex items-center justify-center",
        ),
        rx.fragment(),
    )


def settings_page() -> rx.Component:
    content = rx.el.div(
        rx.el.div(
            profile_card(),
            system_preferences_card(),
            notifications_card(),
            user_management_card(),
            class_name="max-w-4xl mx-auto",
        ),
        add_user_modal(),
        class_name="animate-fade-in",
    )
    return layout(content, "Settings", "Home / Settings", "/settings")