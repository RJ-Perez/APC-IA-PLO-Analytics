import reflex as rx
from app.states.auth_state import AuthState


def login_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.image(
                        src="placeholder.svg",
                        class_name="h-16 w-16 mx-auto mb-4 rounded-full object-cover",
                    ),
                    rx.el.h1(
                        "APC QA Dashboard",
                        class_name="text-2xl font-bold text-slate-900 text-center",
                    ),
                    rx.el.p(
                        "Sign in to access institutional data",
                        class_name="text-sm text-slate-500 text-center mt-2",
                    ),
                    class_name="mb-8",
                ),
                rx.el.form(
                    rx.el.div(
                        rx.el.label(
                            "Email Address",
                            class_name="block text-sm font-medium text-slate-700 mb-1",
                        ),
                        rx.el.input(
                            type="email",
                            name="email",
                            placeholder="user@apc.edu.ph",
                            class_name="w-full px-4 py-2 rounded-lg border border-slate-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all",
                            required=True,
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Password",
                            class_name="block text-sm font-medium text-slate-700 mb-1",
                        ),
                        rx.el.input(
                            type="password",
                            name="password",
                            placeholder="••••••••",
                            class_name="w-full px-4 py-2 rounded-lg border border-slate-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all",
                            required=True,
                        ),
                        class_name="mb-4",
                    ),
                    rx.el.div(
                        rx.el.label(
                            "Role (Demo Selection)",
                            class_name="block text-sm font-medium text-slate-700 mb-1",
                        ),
                        rx.el.select(
                            rx.el.option("Admin", value="Admin"),
                            rx.el.option(
                                "Program Chair", value="Program Chair"
                            ),
                            rx.el.option("Faculty", value="Faculty"),
                            rx.el.option("Stakeholder", value="Stakeholder"),
                            name="role",
                            class_name="w-full px-4 py-2 rounded-lg border border-slate-300 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition-all bg-white appearance-none",
                        ),
                        class_name="mb-6",
                    ),
                    rx.el.button(
                        "Sign In",
                        type="submit",
                        class_name="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-2.5 px-4 rounded-lg transition-colors shadow-sm",
                    ),
                    on_submit=AuthState.login,
                ),
                class_name="w-full max-w-md bg-white p-8 rounded-2xl shadow-xl border border-slate-100",
            ),
            class_name="flex items-center justify-center min-h-screen bg-slate-50 font-['Inter'] px-4",
        )
    )