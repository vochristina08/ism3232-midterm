BULK_MIN_BAGS = 20
LARGE_MIN_BAGS = 80
BULK_DISCOUNT = 0.09
LARGE_DISCOUNT = 0.14
PARTNER_DISCOUNT = 0.04
SHIPPING_THRESHOLD = 250
SHIPPING_FEE = 35
PREPAYMENT_THRESHOLD = 1500
PALLET_MIN_BAGS = 60
PALLET_MIN_TOTAL = 700


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


def requires_prepayment(total: float) -> bool:
    """Return True if the shipment requires prepayment."""
    return total >= PREPAYMENT_THRESHOLD


def needs_pallet(bags: int, total: float) -> bool:
    """Return True when a shipment requires a freight pallet."""
    return bags > PALLET_MIN_BAGS and total > PALLET_MIN_TOTAL


def total_shipped(shipments: list) -> float:
    """Return the sum of all shipment totals."""
    total = 0.0

    for shipment in shipments:
        total += calculate_shipment_total(
            shipment["bag_price"],
            shipment["bags"],
            shipment["partner"],
        )

    return total


def largest_shipment(shipments: list) -> str:
    """Return the buyer with the largest shipment total."""
    largest_buyer = ""
    largest_total = 0.0

    for shipment in shipments:
        total = calculate_shipment_total(
            shipment["bag_price"],
            shipment["bags"],
            shipment["partner"],
        )

        if largest_buyer == "" or total > largest_total:
            largest_total = total
            largest_buyer = shipment["buyer"]

    return largest_buyer


def format_shipment_line(
    buyer: str, total: float, prepayment: bool, pallet: bool
) -> str:
    """Return a formatted shipment report line."""
    prepayment_text = "yes" if prepayment else "no"
    pallet_text = "yes" if pallet else "no"

    return (
        f"{buyer}: ${total:.2f} | prepayment: {prepayment_text} | pallet: {pallet_text}"
    )
