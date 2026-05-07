import reflex as rx
from app.states.dashboard_state import DashboardState
import csv
import io


class ReportState(rx.State):
    selected_report_type: str = "AUN-QA IA Summary Report"
    report_types: list[str] = [
        "AUN-QA IA Summary Report",
        "PLO Attainment Report",
        "Program Comparison Report",
        "Criteria Deep Dive Report",
    ]
    is_generating: bool = False
    report_generated: bool = False

    @rx.event
    def set_report_type(self, r_type: str):
        self.selected_report_type = r_type
        self.report_generated = False

    @rx.event
    async def generate_report(self):
        self.is_generating = True
        import asyncio

        await asyncio.sleep(1.5)
        self.is_generating = False
        self.report_generated = True
        yield rx.toast("Report generated successfully!")

    @rx.event
    async def export_csv(self):
        dashboard = await self.get_state(DashboardState)
        output = io.StringIO()
        writer = csv.writer(output)
        if "IA" in self.selected_report_type:
            writer.writerow(
                [
                    "ID",
                    "Name",
                    "Score",
                    "Compliance %",
                    "Status",
                    "Evidence Count",
                ]
            )
            for c in dashboard.ia_criteria_base:
                writer.writerow(
                    [
                        c["id"],
                        c["name"],
                        c["score"],
                        c["compliance_pct"],
                        c["status"],
                        c["evidence_count"],
                    ]
                )
        else:
            writer.writerow(
                ["Program", "PLO ID", "Description", "Attainment %"]
            )
            for p in dashboard.plo_data_base:
                if (
                    dashboard.selected_program == "All Programs"
                    or p["program"] == dashboard.selected_program
                ):
                    writer.writerow(
                        [
                            p["program"],
                            p["plo_id"],
                            p["description"],
                            p["attainment_pct"],
                        ]
                    )
        csv_content = output.getvalue()
        return rx.download(
            data=csv_content.encode("utf-8"),
            filename=f"{self.selected_report_type.replace(' ', '_')}.csv",
        )