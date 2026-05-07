import reflex as rx
from app.states.auth_state import AuthState


def header(title: str, breadcrumb: str) -> rx.Component:
    return rx.el.header(
        rx.el.div(
            rx.el.div(
                rx.el.p(
                    breadcrumb,
                    class_name="text-sm font-medium text-slate-500 mb-1",
                ),
                rx.el.h2(
                    title,
                    class_name="text-2xl font-bold text-slate-900 tracking-tight",
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.el.span(
                    AuthState.user_role,
                    class_name="inline-flex items-center px-3 py-1 rounded-full text-sm font-semibold bg-blue-100 text-blue-800 border border-blue-200",
                ),
                class_name="flex items-center gap-4",
            ),
            class_name="flex items-center justify-between",
        ),
        class_name="bg-white border-b border-slate-200 px-8 py-6 sticky top-0 z-10",
    )