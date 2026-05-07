import reflex as rx
from app.states.dashboard_state import DashboardState, IACriteria, PLOData
from app.states.auth_state import AuthState


class DataManagementState(rx.State):
    active_tab: str = "ia"
    search_query: str = ""
    show_add_modal: bool = False
    show_edit_modal: bool = False
    editing_item: dict = {}
    is_loading: bool = False

    @rx.event
    def set_active_tab(self, tab: str):
        self.active_tab = tab
        self.search_query = ""

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query

    @rx.event
    def toggle_add_modal(self):
        self.show_add_modal = not self.show_add_modal

    @rx.event
    def toggle_edit_modal(self, item: dict = None):
        if item:
            self.editing_item = item
        self.show_edit_modal = not self.show_edit_modal

    @rx.var
    async def can_edit(self) -> bool:
        auth = await self.get_state(AuthState)
        return auth.is_admin or auth.is_program_chair

    @rx.var
    async def filtered_ia_data(self) -> list[IACriteria]:
        dashboard = await self.get_state(DashboardState)
        if not self.search_query:
            return dashboard.ia_criteria_base
        query = self.search_query.lower()
        return [
            item
            for item in dashboard.ia_criteria_base
            if query in item["name"].lower() or query in item["id"].lower()
        ]

    @rx.var
    async def filtered_plo_data(self) -> list[PLOData]:
        dashboard = await self.get_state(DashboardState)
        data = dashboard.filtered_plo_data
        if not self.search_query:
            return data
        query = self.search_query.lower()
        return [
            item
            for item in data
            if query in item["plo_id"].lower()
            or query in item["description"].lower()
        ]

    @rx.event
    async def add_ia_indicator(self, form_data: dict):
        dashboard = await self.get_state(DashboardState)
        new_item: IACriteria = {
            "id": form_data.get("id", f"{len(dashboard.ia_criteria_base) + 1}"),
            "name": form_data.get("name", ""),
            "score": float(form_data.get("score", 0.0)),
            "compliance_pct": int(form_data.get("compliance_pct", 0)),
            "status": form_data.get("status", "Compliant"),
            "evidence_count": int(form_data.get("evidence_count", 0)),
        }
        dashboard.ia_criteria_base.append(new_item)
        self.show_add_modal = False
        yield rx.toast("IA Indicator added successfully!")

    @rx.event
    async def update_ia_indicator(self, form_data: dict):
        dashboard = await self.get_state(DashboardState)
        item_id = form_data.get("original_id")
        for i, item in enumerate(dashboard.ia_criteria_base):
            if item["id"] == item_id:
                dashboard.ia_criteria_base[i] = {
                    "id": form_data.get("id", item_id),
                    "name": form_data.get("name", item["name"]),
                    "score": float(form_data.get("score", item["score"])),
                    "compliance_pct": int(
                        form_data.get("compliance_pct", item["compliance_pct"])
                    ),
                    "status": form_data.get("status", item["status"]),
                    "evidence_count": int(
                        form_data.get("evidence_count", item["evidence_count"])
                    ),
                }
                break
        self.show_edit_modal = False
        yield rx.toast("IA Indicator updated successfully!")

    @rx.event
    async def delete_ia_indicator(self, item_id: str):
        dashboard = await self.get_state(DashboardState)
        dashboard.ia_criteria_base = [
            item for item in dashboard.ia_criteria_base if item["id"] != item_id
        ]
        yield rx.toast("IA Indicator deleted!")

    @rx.event
    async def add_plo_assessment(self, form_data: dict):
        dashboard = await self.get_state(DashboardState)
        new_item: PLOData = {
            "program": form_data.get("program", "BSCS"),
            "plo_id": form_data.get("plo_id", "PLO1"),
            "description": form_data.get("description", ""),
            "attainment_pct": float(form_data.get("attainment_pct", 0.0)),
        }
        dashboard.plo_data_base.append(new_item)
        self.show_add_modal = False
        yield rx.toast("PLO Assessment added successfully!")

    @rx.event
    async def update_plo_assessment(self, form_data: dict):
        dashboard = await self.get_state(DashboardState)
        original_id = form_data.get("original_id")
        for i, item in enumerate(dashboard.plo_data_base):
            if item["plo_id"] == original_id:
                dashboard.plo_data_base[i] = {
                    "program": form_data.get("program", item["program"]),
                    "plo_id": form_data.get("plo_id", item["plo_id"]),
                    "description": form_data.get(
                        "description", item["description"]
                    ),
                    "attainment_pct": float(
                        form_data.get("attainment_pct", item["attainment_pct"])
                    ),
                }
                break
        self.show_edit_modal = False
        yield rx.toast("PLO Assessment updated successfully!")

    @rx.event
    async def delete_plo_assessment(self, plo_id: str):
        dashboard = await self.get_state(DashboardState)
        dashboard.plo_data_base = [
            item for item in dashboard.plo_data_base if item["plo_id"] != plo_id
        ]
        yield rx.toast("PLO Assessment deleted!")

    @rx.event
    async def sync_data(self):
        self.is_loading = True
        import asyncio

        await asyncio.sleep(1)
        self.is_loading = False