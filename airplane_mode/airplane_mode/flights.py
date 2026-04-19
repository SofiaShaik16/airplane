def get_context(context):
    import frappe

    context.flights = frappe.get_all(
        "Airplane Flight",
        fields=[
            "name",
            "airplane",
            "source_airport",
            "destination_airport_code",
            "date_of_departure",
            "time_of_departure",
            "duration",
            "route"
        ]
    )
