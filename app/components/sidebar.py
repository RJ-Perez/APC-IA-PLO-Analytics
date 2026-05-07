import reflex as rx
from app.states.auth_state import AuthState


def nav_item(label: str, icon: str, url: str, active_url: str) -> rx.Component:
    is_active = active_url == url
    return rx.el.a(
        rx.el.div(
            rx.icon(
                icon,
                class_name=f"h-5 w-5 mr-3 {('text-blue-600' if is_active else 'text-slate-500')}",
            ),
            rx.el.span(
                label,
                class_name=f"font-medium {('text-blue-700' if is_active else 'text-slate-700')}",
            ),
            class_name=rx.cond(
                is_active,
                "flex items-center px-4 py-3 rounded-lg bg-blue-50 text-blue-700 transition-colors",
                "flex items-center px-4 py-3 rounded-lg hover:bg-slate-100 text-slate-700 transition-colors",
            ),
        ),
        href=url,
        class_name="block w-full mb-1",
    )


def sidebar(current_route: str) -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.image(
                    src="placeholder.svg",
                    class_name="h-10 w-10 rounded-full object-cover mr-2",
                ),
                rx.el.div(
                    rx.el.h1(
                        "APC",
                        class_name="text-xl font-bold tracking-tight text-slate-900",
                    ),
                    rx.el.p(
                        "Quality Assurance",
                        class_name="text-xs font-medium text-slate-500 uppercase tracking-wider",
                    ),
                ),
                class_name="flex items-center px-6 py-6 border-b border-slate-200",
            ),
            rx.el.nav(
                nav_item("Dashboard", "layout-dashboard", "/", current_route),
                nav_item(
                    "IA Assessment",
                    "clipboard-check",
                    "/ia-assessment",
                    current_route,
                ),
                nav_item(
                    "PLO Analytics",
                    "bar-chart-3",
                    "/plo-analytics",
                    current_route,
                ),
                nav_item(
                    "Data Management",
                    "database",
                    "/data-management",
                    current_route,
                ),
                nav_item("Reports", "file-text", "/reports", current_route),
                nav_item("Settings", "settings", "/settings", current_route),
                class_name="flex-1 overflow-y-auto py-6 px-3",
            ),
            rx.el.div(
                rx.el.div(
                    rx.image(
                        src=f"https://api.dicebear.com/9.x/initials/svg?seed={AuthState.user_name}",
                        class_name="h-10 w-10 rounded-full bg-slate-200",
                    ),
                    rx.el.div(
                        rx.el.p(
                            AuthState.user_name,
                            class_name="text-sm font-semibold text-slate-900 truncate",
                        ),
                        rx.el.p(
                            AuthState.user_role,
                            class_name="text-xs font-medium text-slate-500 truncate",
                        ),
                        class_name="ml-3 flex-1 min-w-0",
                    ),
                    rx.el.button(
                        rx.icon(
                            "log-out",
                            class_name="h-4 w-4 text-slate-400 hover:text-slate-600",
                        ),
                        on_click=AuthState.logout,
                        class_name="ml-2 p-1 rounded hover:bg-slate-200 transition-colors",
                        title="Logout",
                    ),
                    class_name="flex items-center w-full",
                ),
                class_name="p-4 border-t border-slate-200 bg-slate-50",
            ),
            class_name="flex flex-col h-full bg-white border-r border-slate-200",
        ),
        class_name="w-64 flex-shrink-0 h-screen sticky top-0 z-20",
    )