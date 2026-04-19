import frappe

def get_context(context):
    context.flights = frappe.get_all(
        "Airplane Flight",
        fields=["name"]
    )
