def validate(self):
    self.remove_duplicates()
    self.calculate_total()

def calculate_total(self):
    add_on_total = 0
    for row in self.add_ons:
        add_on_total += row.amount or 0

    self.total_amount = (self.flight_price or 0) + add_on_total
def remove_duplicates(self):
    seen = set()
    unique_rows = []

    for row in self.add_ons:
        if row.item not in seen:
            seen.add(row.item)
            unique_rows.append(row)

    self.add_ons = unique_rows
def before_submit(self):
    if self.status != "Boarded":
        frappe.throw("Only Boarded tickets can be submitted")
