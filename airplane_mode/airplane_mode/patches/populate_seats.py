import frappe
import random


def execute():
    tickets = frappe.get_all("Airplane Ticket", pluck="name")

    for ticket_name in tickets:
        doc = frappe.get_doc("Airplane Ticket", ticket_name)

        if doc.seat:
            continue

        number = random.randint(10, 99)
        letter = random.choice(["A", "B", "C", "D", "E"])

        doc.seat = f"{number}{letter}"
        doc.save()
