class VisionaryLeader:
    def __init__(self, name, vision, projects=None):
        self.name = name
        self.vision = vision
        self.projects = projects if projects else []
        self.impact_score = 0
        self.work_hours_per_week = 100

    def apply_first_principles(self, problem):
        print(f"[First Principles] Analyzing '{problem}'...")
        print(f"- Breaking down '{problem}' into its fundamental truths.")
        print(f"- Reconstructing a solution from the ground up.")
        self.impact_score += 5
        return f"Solution for '{problem}' found through fundamental reasoning."

    def add_project(self, project_name, social_benefit):
        self.projects.append({"name": project_name, "benefit": social_benefit})
        self.impact_score += 10
        print(f"Project '{project_name}' started to achieve: {social_benefit}")

    def work_hard(self):
        print(f"{self.name} is working {self.work_hours_per_week} hours this week. Speed is the ultimate currency.")
        self.impact_score += 20

    def inspire(self):
        return f"{self.name} says: 'If other people are putting in 40 hours a week and you're putting in 100, you will achieve in 4 months what takes them a year.'"

    def display_legacy(self):
        print(f"--- Legacy of {self.name} ---")
        print(f"Vision: {self.vision}")
        print(f"Work Ethic: {self.work_hours_per_week} hrs/week")
        print(f"Projects count: {len(self.projects)}")
        print(f"Social Impact Score: {self.impact_score}")

elon_v2 = VisionaryLeader(
    name="Elon Enlightened", 
    vision="Making life multi-planetary while ensuring Earth remains a paradise for all."
)

print(elon_v2.apply_first_principles("Cost of space travel"))

elon_v2.work_hard()

elon_v2.add_project("SolarWater", "Providing clean water using 100% solar energy.")

print(elon_v2.inspire())
elon_v2.display_legacy()
