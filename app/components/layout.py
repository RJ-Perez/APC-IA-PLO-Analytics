import reflex as rx
from app.components.sidebar import sidebar
from app.components.header import header
from app.states.auth_state import AuthState


def layout(
    content: rx.Component, title: str, breadcrumb: str, route: str
) -> rx.Component:
    return rx.el.div(
        sidebar(route),
        rx.el.main(
            header(title, breadcrumb),
            rx.el.div(content, class_name="p-8"),
            class_name="flex-1 flex flex-col min-w-0 bg-slate-50 min-h-screen",
        ),
        class_name="flex h-screen font-['Inter'] text-slate-900 bg-slate-50",
    )