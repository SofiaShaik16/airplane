import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):

    def validate(self):
        total_addons = 0

        if self.add_ons:
            for row in self.add_ons:
                total_addons += row.amount or 0

        self.total_amount = (self.flight_price or 0) + total_addons
            # Remove duplicate add-ons
            if row.item in seen:
                continue
            seen.add(row.item)
            unique_items.append(row)

            total_addons += row.amount or 0

        # Update child table (remove duplicates)
        self.add_ons = unique_items

        # Calculate total
        self.total_amount = (self.flight_price or 0) + total_addons

