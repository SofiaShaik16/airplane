import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):

    def validate(self):
        total_addons = 0

        if self.add_ons:
            for row in self.add_ons:
                total_addons += row.amount or 0

        self.total_amount = (self.flight_price or 0) + total_addons

import frappe
import random
from frappe.model.document import Document

class AirplaneTicket(Document):

   
    def before_insert(self):
        number = random.randint(1, 100)
        letter = random.choice(['A', 'B', 'C', 'D', 'E'])
        self.seat_no = f"{number}{letter}"

    
    def validate(self):
        total_addons = 0
        seen = set()
        unique_rows = []

        if self.add_ons:
            for row in self.add_ons:
                if row.item in seen:
                    continue

                seen.add(row.item)
                unique_rows.append(row)
                total_addons += row.amount or 0

        self.add_ons = unique_rows
        self.total_amount = (self.flight_price or 0) + total_addons

    def before_submit(self):
        if self.ticket_status != "Boarded":
            frappe.throw("Cannot submit ticket unless passenger is Boarded")
import frappe
from frappe.model.document import Document

class AirplaneFlight(Document):

    def validate(self):
        if self.source_airport:
            self.source_airport_code = frappe.db.get_value(
                "Airport", self.source_airport, "code"
            )

        if self.destination_airport:
            self.destination_airport_code = frappe.db.get_value(
                "Airport", self.destination_airport, "code"
            )

    def on_submit(self):
        self.status = "Completed"

def calculate_total_amount(self):
    add_on_total = 0

    for item in self.add_ons:
        add_on_total += item.amount or 0

    self.total_amount = (self.flight_price or 0) + add_on_total

def remove_duplicate_add_ons(self):
    seen = set()
    unique_rows = []

    for item in self.add_ons:
        if item.item not in seen:
            seen.add(item.item)
            unique_rows.append(item)

    self.add_ons = unique_rows

def validate(self):
    self.remove_duplicate_add_ons()
    self.calculate_total_amount()

def before_submit(self):
    if self.status != "Boarded":
        frappe.throw("Only Boarded tickets can be submitted")
