BULK_MIN_BAGS = 20
LARGE_MIN_BAGS = 80
BULK_DISCOUNT = 0.09
LARGE_DISCOUNT = 0.14
PARTNER_DISCOUNT = 0.04
SHIPPING_THRESHOLD = 250
SHIPPING_FEE = 35


def calculate_bean_cost(bag_price: float, bags: int) -> float:
    """Calculate the cost of coffee bags before discounts."""
    return bag_price * bags

def get_bulk_discount(bags: int, partner: bool = False) -> float:
    """Return the discount rate based on bag count and partner status."""
    if bags >= LARGE_MIN_BAGS:
        discount = LARGE_DISCOUNT
    elif bags >= BULK_MIN_BAGS:
        discount = BULK_DISCOUNT
    else:
        discount = 0.0

    if partner and bags >= BULK_MIN_BAGS:
        discount += PARTNER_DISCOUNT

    return discount


def calculate_shipment_total(
    bag_price: float, bags: int, partner: bool = False
) -> float:
    """Calculate the discounted shipment cost plus any shipping fee."""
    bean_cost = calculate_bean_cost(bag_price, bags)
    discount = get_bulk_discount(bags, partner)
    discounted_cost = bean_cost * (1 - discount)

    if discounted_cost < SHIPPING_THRESHOLD:
        return discounted_cost + SHIPPING_FEE

    return discounted_cost

def requires_prepayment(shipment_total: float) -> bool:
    """Return True if the shipment requires prepayment."""
    return shipment_total >= 1500