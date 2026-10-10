
import json
import re


FIELD_ALIASES = {
    "vendor_name": [
        "vendor", "vendor name", "supplier",
        "supplier name", "company name"
    ],
    "invoice_amount": [
        "invoice amount", "amount", "total",
        "total due", "invoice total", "amount due"
    ],
    "invoice_number": [
        "invoice number", "invoice no", "invoice id",
        "bill number", "bill no"
    ],
    "invoice_date": [
        "invoice date", "bill date", "date"
    ],
}


def normalize_name(name: str) -> str:
    """Make column names easier to compare."""
    return re.sub(r"[^a-z0-9]+", " ", name.lower()).strip()


def adapt_format(source_data_json: str) -> str:
    """
    Match unfamiliar column names to standard fields.
    Input JSON: {"columns": [...], "rows": [{...}]}
    """
    try:
        data = json.loads(source_data_json)
    except json.JSONDecodeError:
        return json.dumps({"error": "Input must be valid JSON."})

    columns = data.get("columns")
    rows = data.get("rows")

    if not isinstance(columns, list) or not isinstance(rows, list):
        return json.dumps({
            "error": "Provide a columns list and a rows list."
        })

    if not all(isinstance(c, str) for c in columns):
        return json.dumps({"error": "Every column name must be text."})

    if not all(isinstance(r, dict) for r in rows):
        return json.dumps({"error": "Every row must be an object."})

    if any(not all(c in row for c in columns) for row in rows):
        return json.dumps({
            "error": "Every row must contain all listed columns."
        })

    if len(columns) != len(set(columns)):
        return json.dumps({
            "error": "Column names must be unique."
        })

    normalized = {
        normalize_name(column): column for column in columns
    }

    mapping = {}
    needs_review = []

    for standard_field, aliases in FIELD_ALIASES.items():
        possible_names = [standard_field.replace("_", " ")] + aliases
        matches = [
            normalized[normalize_name(alias)]
            for alias in possible_names
            if normalize_name(alias) in normalized
        ]
        matches = list(dict.fromkeys(matches))

        if len(matches) == 1:
            mapping[standard_field] = matches[0]
        elif len(matches) > 1:
            needs_review.append({
                "field": standard_field,
                "reason": "Several columns could match this field.",
                "columns": matches,
            })

    mapped_columns = set(mapping.values())
    unmapped_columns = [
        column for column in columns if column not in mapped_columns
    ]

    output_rows = []
    for row in rows:
        output_rows.append({
            standard_field: row[source_column]
            for standard_field, source_column in mapping.items()
        })

    return json.dumps({
        "column_mapping": mapping,
        "adapted_rows": output_rows,
        "unmapped_columns": unmapped_columns,
        "needs_review": needs_review,
        "message": (
            "Check the mapping before using the data. "
            "Unmapped columns and ambiguous matches need review."
        ),
    }, indent=2)
