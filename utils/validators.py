def is_valid_shipment_no(value: str) -> bool:
    if not value:
        return False
    return value.isalnum()
