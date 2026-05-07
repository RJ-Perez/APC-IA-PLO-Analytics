import reflex as rx
from typing import TypedDict
import random


class IACriteria(TypedDict):
    id: str
    name: str
    score: float
    compliance_pct: int
    status: str
    evidence_count: int


class PLOData(TypedDict):
    program: str
    plo_id: str
    description: str
    attainment_pct: float


class IATrend(TypedDict):
    year: str
    overall_compliance: float


class PLOTrend(TypedDict):
    year: str
    PLO1: float
    PLO2: float
    PLO3: float
    PLO4: float


class CoursePLOMapping(TypedDict):
    course: str
    PLO1: str
    PLO2: str
    PLO3: str
    PLO4: str


class DashboardState(rx.State):
    year_options: list[str] = ["2020", "2021", "2022", "2023", "2024"]
    semester_options: list[str] = ["1st Semester", "2nd Semester", "Summer"]
    program_options: list[str] = [
        "All Programs",
        "BSCS",
        "BSIT",
        "BSMM",
        "BSA",
        "BSBA",
    ]
    selected_year: str = "2024"
    selected_semester: str = "1st Semester"
    selected_program: str = "All Programs"
    selected_criteria: str = ""
    show_criteria_detail: bool = False
    selected_plo: str = ""
    show_plo_detail: bool = False
    ia_trend_data: list[IATrend] = [
        {"year": "2020", "overall_compliance": 72.0},
        {"year": "2021", "overall_compliance": 75.0},
        {"year": "2022", "overall_compliance": 78.0},
        {"year": "2023", "overall_compliance": 81.0},
        {"year": "2024", "overall_compliance": 83.0},
    ]
    plo_trend_data: list[PLOTrend] = [
        {"year": "2020", "PLO1": 75, "PLO2": 70, "PLO3": 68, "PLO4": 80},
        {"year": "2021", "PLO1": 78, "PLO2": 72, "PLO3": 70, "PLO4": 82},
        {"year": "2022", "PLO1": 82, "PLO2": 75, "PLO3": 74, "PLO4": 85},
        {"year": "2023", "PLO1": 85, "PLO2": 78, "PLO3": 76, "PLO4": 88},
        {"year": "2024", "PLO1": 88, "PLO2": 82, "PLO3": 79, "PLO4": 91},
    ]
    course_plo_mapping: list[CoursePLOMapping] = [
        {
            "course": "CS101",
            "PLO1": "High",
            "PLO2": "Medium",
            "PLO3": "Low",
            "PLO4": "Low",
        },
        {
            "course": "CS201",
            "PLO1": "Medium",
            "PLO2": "High",
            "PLO3": "Medium",
            "PLO4": "Low",
        },
        {
            "course": "CS301",
            "PLO1": "Low",
            "PLO2": "Medium",
            "PLO3": "High",
            "PLO4": "Medium",
        },
        {
            "course": "CS401",
            "PLO1": "Low",
            "PLO2": "Low",
            "PLO3": "Medium",
            "PLO4": "High",
        },
    ]
    ia_criteria_base: list[IACriteria] = [
        {
            "id": "1",
            "name": "Strategic QA",
            "score": 5.2,
            "compliance_pct": 85,
            "status": "Compliant",
            "evidence_count": 12,
        },
        {
            "id": "2",
            "name": "Curriculum Design",
            "score": 4.8,
            "compliance_pct": 78,
            "status": "Needs Improvement",
            "evidence_count": 8,
        },
        {
            "id": "3",
            "name": "Teaching & Learning",
            "score": 6.1,
            "compliance_pct": 92,
            "status": "Compliant",
            "evidence_count": 15,
        },
        {
            "id": "4",
            "name": "Student Assessment",
            "score": 5.5,
            "compliance_pct": 88,
            "status": "Compliant",
            "evidence_count": 14,
        },
        {
            "id": "5",
            "name": "Academic Staff",
            "score": 4.2,
            "compliance_pct": 65,
            "status": "At Risk",
            "evidence_count": 5,
        },
        {
            "id": "6",
            "name": "Student Support",
            "score": 5.9,
            "compliance_pct": 90,
            "status": "Compliant",
            "evidence_count": 20,
        },
        {
            "id": "7",
            "name": "Facilities",
            "score": 6.4,
            "compliance_pct": 95,
            "status": "Compliant",
            "evidence_count": 22,
        },
        {
            "id": "8",
            "name": "Output/Outcomes",
            "score": 5.0,
            "compliance_pct": 80,
            "status": "Needs Improvement",
            "evidence_count": 10,
        },
        {
            "id": "9",
            "name": "Stakeholder Satisfaction",
            "score": 5.7,
            "compliance_pct": 89,
            "status": "Compliant",
            "evidence_count": 18,
        },
        {
            "id": "10",
            "name": "Social Responsibility",
            "score": 6.0,
            "compliance_pct": 91,
            "status": "Compliant",
            "evidence_count": 11,
        },
        {
            "id": "11",
            "name": "Internationalization",
            "score": 3.8,
            "compliance_pct": 58,
            "status": "At Risk",
            "evidence_count": 4,
        },
    ]
    plo_data_base: list[PLOData] = [
        {
            "program": "BSCS",
            "plo_id": "PLO1",
            "description": "Computing Fundamentals",
            "attainment_pct": 88.5,
        },
        {
            "program": "BSCS",
            "plo_id": "PLO2",
            "description": "Problem Analysis",
            "attainment_pct": 82.0,
        },
        {
            "program": "BSCS",
            "plo_id": "PLO3",
            "description": "Design/Development",
            "attainment_pct": 79.5,
        },
        {
            "program": "BSCS",
            "plo_id": "PLO4",
            "description": "Modern Tool Usage",
            "attainment_pct": 91.0,
        },
        {
            "program": "BSIT",
            "plo_id": "PLO1",
            "description": "IT Fundamentals",
            "attainment_pct": 85.0,
        },
        {
            "program": "BSIT",
            "plo_id": "PLO2",
            "description": "System Admin",
            "attainment_pct": 76.5,
        },
        {
            "program": "BSBA",
            "plo_id": "PLO1",
            "description": "Business Knowledge",
            "attainment_pct": 90.0,
        },
        {
            "program": "BSBA",
            "plo_id": "PLO2",
            "description": "Ethical Leadership",
            "attainment_pct": 95.0,
        },
    ]
    recent_activities: list[dict[str, str]] = [
        {
            "icon": "edit-2",
            "color": "text-blue-500",
            "bg": "bg-blue-100",
            "text": "IA Criteria 7 (Facilities) updated — score changed to 6.4",
            "time": "2 hours ago",
        },
        {
            "icon": "calculator",
            "color": "text-teal-500",
            "bg": "bg-teal-100",
            "text": "PLO3 attainment for BSCS recalculated — 79.5%",
            "time": "5 hours ago",
        },
        {
            "icon": "file-text",
            "color": "text-emerald-500",
            "bg": "bg-emerald-100",
            "text": "Semester report generated for 1st Semester 2024",
            "time": "1 day ago",
        },
        {
            "icon": "upload",
            "color": "text-purple-500",
            "bg": "bg-purple-100",
            "text": "New evidence uploaded for Academic Staff criteria",
            "time": "2 days ago",
        },
        {
            "icon": "settings",
            "color": "text-amber-500",
            "bg": "bg-amber-100",
            "text": "PLO target threshold updated to 80%",
            "time": "3 days ago",
        },
    ]

    @rx.var
    def top_criteria(self) -> list[IACriteria]:
        sorted_crit = sorted(
            self.ia_criteria_base, key=lambda x: x["score"], reverse=True
        )
        return sorted_crit[:3]

    @rx.var
    def bottom_criteria(self) -> list[IACriteria]:
        sorted_crit = sorted(self.ia_criteria_base, key=lambda x: x["score"])
        return sorted_crit[:3]

    @rx.var
    def program_summary_data(self) -> list[dict[str, str | float | int]]:
        summary = {}
        for p in self.plo_data_base:
            prog = p["program"]
            if prog not in summary:
                summary[prog] = {
                    "attainment_sum": 0,
                    "count": 0,
                    "above_target": 0,
                }
            summary[prog]["attainment_sum"] += p["attainment_pct"]
            summary[prog]["count"] += 1
            if p["attainment_pct"] >= 80.0:
                summary[prog]["above_target"] += 1
        res = []
        for prog, data in summary.items():
            res.append(
                {
                    "program": prog,
                    "avg_attainment": round(
                        data["attainment_sum"] / data["count"], 1
                    ),
                    "plo_count": data["count"],
                    "above_target": data["above_target"],
                }
            )
        return res

    @rx.event
    def open_criteria_detail(self, criteria_id: str):
        self.selected_criteria = criteria_id
        self.show_criteria_detail = True

    @rx.event
    def close_criteria_detail(self):
        self.show_criteria_detail = False

    @rx.event
    def open_plo_detail(self, plo_id: str):
        self.selected_plo = plo_id
        self.show_plo_detail = True

    @rx.event
    def close_plo_detail(self):
        self.show_plo_detail = False

    @rx.event
    def set_year(self, year: str):
        self.selected_year = year

    @rx.event
    def set_semester(self, semester: str):
        self.selected_semester = semester

    @rx.event
    def set_program(self, program: str):
        self.selected_program = program

    @rx.var
    def filtered_ia_criteria(self) -> list[IACriteria]:
        return self.ia_criteria_base

    @rx.var
    def filtered_plo_data(self) -> list[PLOData]:
        if self.selected_program == "All Programs":
            return self.plo_data_base
        return [
            p
            for p in self.plo_data_base
            if p["program"] == self.selected_program
        ]

    @rx.var
    def overall_compliance(self) -> float:
        if not self.ia_criteria_base:
            return 0.0
        total = sum((c["compliance_pct"] for c in self.ia_criteria_base))
        return round(total / len(self.ia_criteria_base), 1)

    @rx.var
    def criteria_at_risk_count(self) -> int:
        return len(
            [c for c in self.ia_criteria_base if c["status"] == "At Risk"]
        )

    @rx.var
    def programs_tracked_count(self) -> int:
        return len(set([p["program"] for p in self.plo_data_base]))

    @rx.var
    def avg_plo_attainment(self) -> float:
        filtered = self.filtered_plo_data
        if not filtered:
            return 0.0
        return round(
            sum((p["attainment_pct"] for p in filtered)) / len(filtered), 1
        )

    @rx.var
    def plos_above_target(self) -> int:
        return len(
            [p for p in self.filtered_plo_data if p["attainment_pct"] > 80.0]
        )

    @rx.var
    def plos_below_target(self) -> int:
        return len(
            [p for p in self.filtered_plo_data if p["attainment_pct"] <= 80.0]
        )

    @rx.var
    def total_plos_assessed(self) -> int:
        return len(self.filtered_plo_data)

    @rx.var
    def ia_chart_data(self) -> list[dict[str, str | float | int]]:
        return [
            {
                "name": c["name"],
                "compliance": c["compliance_pct"],
                "fill": "#2563EB"
                if c["status"] == "Compliant"
                else "#F59E0B"
                if c["status"] == "Needs Improvement"
                else "#EF4444",
            }
            for c in self.ia_criteria_base
        ]

    @rx.var
    def plo_chart_data(self) -> list[dict[str, str | float]]:
        return [
            {
                "name": p["plo_id"],
                "attainment": p["attainment_pct"],
                "fill": "#14B8A6"
                if p["attainment_pct"] > 80
                else "#F59E0B"
                if p["attainment_pct"] > 70
                else "#EF4444",
            }
            for p in self.filtered_plo_data
        ]

    @rx.var
    def ia_score_chart_data(self) -> list[dict[str, str | float | int]]:
        return [
            {
                "name": c["name"],
                "score": c["score"],
                "fill": "#2563EB"
                if c["status"] == "Compliant"
                else "#F59E0B"
                if c["status"] == "Needs Improvement"
                else "#EF4444",
            }
            for c in self.ia_criteria_base
        ]

    @rx.var
    def avg_ia_score(self) -> float:
        if not self.ia_criteria_base:
            return 0.0
        total = sum((c["score"] for c in self.ia_criteria_base))
        return round(total / len(self.ia_criteria_base), 1)

    @rx.var
    def compliant_criteria_count(self) -> int:
        return len(
            [c for c in self.ia_criteria_base if c["status"] == "Compliant"]
        )

    @rx.var
    def needs_improvement_count(self) -> int:
        return len(
            [
                c
                for c in self.ia_criteria_base
                if c["status"] == "Needs Improvement"
            ]
        )