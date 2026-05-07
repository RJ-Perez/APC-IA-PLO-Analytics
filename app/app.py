import reflex as rx
from app.states.auth_state import AuthState
from app.pages.login import login_page
from app.pages.dashboard import dashboard_page
from app.pages.ia_assessment import ia_assessment_page
from app.pages.plo_analytics import plo_analytics_page
from app.pages.data_management import data_management_page
from app.pages.reports import reports_page
from app.pages.settings import settings_page

app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(
            rel="preconnect", href="https://fonts.gstatic.com", cross_origin=""
        ),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(login_page, route="/login")
app.add_page(dashboard_page, route="/", on_load=AuthState.require_login)
app.add_page(
    ia_assessment_page, route="/ia-assessment", on_load=AuthState.require_login
)
app.add_page(
    plo_analytics_page, route="/plo-analytics", on_load=AuthState.require_login
)
app.add_page(
    data_management_page,
    route="/data-management",
    on_load=AuthState.require_login,
)
app.add_page(reports_page, route="/reports", on_load=AuthState.require_login)
app.add_page(settings_page, route="/settings", on_load=AuthState.require_login)