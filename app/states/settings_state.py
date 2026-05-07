import reflex as rx
from typing import TypedDict
from app.states.auth_state import AuthState


class UserInfo(TypedDict):
    name: str
    email: str
    role: str
    program: str
    status: str


class SettingsState(rx.State):
    plo_target: float = 80.0
    ia_threshold: float = 5.0
    academic_year: str = "2024"
    assessment_cycle: str = "Annual"
    email_notifications: bool = True
    weekly_reports: bool = True
    plo_alerts: bool = True
    sample_users: list[UserInfo] = [
        {
            "name": "Alex Admin",
            "email": "admin@apc.edu.ph",
            "role": "Admin",
            "program": "All",
            "status": "Active",
        },
        {
            "name": "Prof. Chair",
            "email": "chair@apc.edu.ph",
            "role": "Program Chair",
            "program": "BSCS",
            "status": "Active",
        },
        {
            "name": "Dr. Faculty",
            "email": "faculty@apc.edu.ph",
            "role": "Faculty",
            "program": "BSCS",
            "status": "Active",
        },
        {
            "name": "Jane Stakeholder",
            "email": "stakeholder@apc.edu.ph",
            "role": "Stakeholder",
            "program": "N/A",
            "status": "Inactive",
        },
    ]
    show_add_user_modal: bool = False

    @rx.event
    def toggle_add_user_modal(self):
        self.show_add_user_modal = not self.show_add_user_modal

    @rx.event
    def add_user(self, form_data: dict):
        new_user: UserInfo = {
            "name": form_data.get("name", "New User"),
            "email": form_data.get("email", "new@apc.edu.ph"),
            "role": form_data.get("role", "Faculty"),
            "program": form_data.get("program", "BSCS"),
            "status": "Active",
        }
        self.sample_users.append(new_user)
        self.show_add_user_modal = False
        yield rx.toast("User added successfully!")

    @rx.event
    def update_preferences(self, form_data: dict):
        self.plo_target = float(form_data.get("plo_target", self.plo_target))
        self.ia_threshold = float(
            form_data.get("ia_threshold", self.ia_threshold)
        )
        self.academic_year = form_data.get("academic_year", self.academic_year)
        self.assessment_cycle = form_data.get(
            "assessment_cycle", self.assessment_cycle
        )
        yield rx.toast("Preferences saved successfully!")

    @rx.event
    def toggle_notification(self, key: str, value: bool):
        if key == "email_notifications":
            self.email_notifications = value
        elif key == "weekly_reports":
            self.weekly_reports = value
        elif key == "plo_alerts":
            self.plo_alerts = value