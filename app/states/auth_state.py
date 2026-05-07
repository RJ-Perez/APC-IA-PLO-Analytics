import reflex as rx
from pydantic import BaseModel
import logging


class UserSession(BaseModel):
    name: str
    email: str
    role: str
    program: str


class AuthState(rx.State):
    session_data: str = rx.LocalStorage(name="apc_user_session", sync=True)

    @rx.var
    def current_user(self) -> UserSession | None:
        if self.session_data:
            try:
                return UserSession.model_validate_json(self.session_data)
            except Exception as e:
                logging.exception(f"Error parsing session data: {e}")
                return None
        return None

    @rx.var
    def is_logged_in(self) -> bool:
        return self.current_user is not None

    @rx.var
    def user_name(self) -> str:
        return self.current_user.name if self.current_user else "Guest User"

    @rx.var
    def user_role(self) -> str:
        return self.current_user.role if self.current_user else "Stakeholder"

    @rx.var
    def user_program(self) -> str:
        return self.current_user.program if self.current_user else "N/A"

    @rx.var
    def is_admin(self) -> bool:
        return self.user_role == "Admin"

    @rx.var
    def is_program_chair(self) -> bool:
        return self.user_role == "Program Chair"

    @rx.var
    def is_faculty(self) -> bool:
        return self.user_role == "Faculty"

    @rx.var
    def is_stakeholder(self) -> bool:
        return self.user_role == "Stakeholder"

    @rx.event
    def login(self, form_data: dict):
        email = form_data.get("email", "")
        role = form_data.get("role", "Stakeholder")
        name = (
            "Alex Admin"
            if role == "Admin"
            else "Prof. Chair"
            if role == "Program Chair"
            else "Dr. Faculty"
            if role == "Faculty"
            else "Jane Stakeholder"
        )
        program = (
            "BSCS" if role in ["Program Chair", "Faculty"] else "All Programs"
        )
        session = UserSession(
            name=name, email=email, role=role, program=program
        )
        self.session_data = session.model_dump_json()
        return rx.redirect("/")

    @rx.event
    def logout(self):
        self.session_data = ""
        return rx.redirect("/login")

    @rx.event
    def require_login(self):
        if not self.session_data:
            return rx.redirect("/login")