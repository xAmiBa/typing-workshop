from typing import (
    Any,
    Callable,
    Iterable,
    Literal,
    TypedDict,
)
from dataclasses import dataclass
from datetime import datetime


# Type definitions
AccountStatus = Literal["active", "suspended", "closed"]
TariffType = Literal["fixed", "variable", "green"]
PaymentMethod = Literal["direct_debit", "card", "bank_transfer"]
ReadingType = Literal["electricity", "gas"]


class CustomerInfo(TypedDict):
    customer_id: str
    name: str
    email: str
    status: AccountStatus


class TariffRate(TypedDict):
    tariff_id: str
    type: TariffType
    rate_per_kwh: float
    standing_charge: float


class BillingPeriod(TypedDict):
    start_date: str
    end_date: str
    total_consumption: float
    total_cost: float


@dataclass
class MeterReading:
    meter_id: str
    reading_type: ReadingType
    value: float
    timestamp: datetime
    customer_id: str


@dataclass
class Payment:
    payment_id: str
    customer_id: str
    amount: float
    method: PaymentMethod
    status: str


@dataclass
class Account:
    """Customer account in the platform."""

    customer_info: CustomerInfo
    tariff: TariffRate
    meter_readings: list[MeterReading]
    balance: float

    def add_reading(self, reading: MeterReading) -> None:
        """Add a meter reading to the account."""
        self.meter_readings.append(reading)

    def calculate_bill(self, period: BillingPeriod):
        """Calculate bill for billing period. Returns Bill dataclass."""
        consumption = period["total_consumption"]
        cost = (consumption * self.tariff["rate_per_kwh"]) + self.tariff[
            "standing_charge"
        ]
        bill = Bill(
            customer_id=self.customer_info["customer_id"],
            period=period,
            amount=cost,
            account=self,
        )


@dataclass
class Bill:
    """Bill for a customer."""

    customer_id: str
    period: BillingPeriod
    amount: float
    account: Account


# Customer Management Functions


def create_customer(name: str, email: str, initial_status) -> CustomerInfo:
    """Create a new customer."""
    customer_id = f"CUST-{hash(email) % 10000:04d}"
    return {
        "customer_id": customer_id,
        "name": name,
        "email": email,
        "status": initial_status,
        "created_at": datetime.now().isoformat(),
    }


def update_customer_status(customer: CustomerInfo, new_status: str) -> None:
    """Update customer status."""
    customer["status"] = new_status


def get_active_customers(customers: list) -> list[CustomerInfo]:
    """Get all active customers."""
    return [c for c in customers if c["status"] == "active"]


def search_customers(customers: list[CustomerInfo], predicate) -> list[CustomerInfo]:
    """Search customers using a predicate function."""
    return [c for c in customers if predicate(c)]


# Tariff Management


def create_tariff(
    tariff_id: str, tariff_type: TariffType, rate: float, standing: float
) -> TariffRate:
    """Create a new tariff."""
    return {
        "tariff_id": tariff_id,
        "type": tariff_type,
        "rate_per_kwh": rate,
        "standing_charge": standing,
    }


def apply_tariff_discount(tariff: TariffRate, discount_pct: float) -> TariffRate:
    """Apply discount to tariff rate."""
    new_rate = tariff["rate_per_kwh"] * (1 - discount_pct)
    tariff["rate_per_kwh"] = new_rate
    return tariff


def get_cheapest_tariff(tariffs: Iterable[TariffRate]) -> TariffRate:
    """Find the cheapest tariff based on rate."""
    if len(tariffs) == 0:
        return None

    cheapest = None
    for tariff in tariffs:
        if cheapest is None or tariff["rate_per_kwh"] < cheapest["rate_per_kwh"]:
            cheapest = tariff
    return cheapest


# Reading Processing


def process_readings_batch(readings: Iterable[MeterReading], batch_size: int):
    """Process readings in batches. Yields batches of readings."""
    batch = []
    for reading in readings:
        batch.append(reading)
        if len(batch) >= batch_size:
            yield batch
            batch = []
    if batch:
        yield batch


def filter_readings_by_type(
    readings: Iterable[MeterReading], reading_type: str
) -> list[MeterReading]:
    """Filter readings by type."""
    return [r for r in readings if r.reading_type == reading_type]


def calculate_average_consumption(readings: list[MeterReading]) -> float:
    """Calculate average consumption from readings."""
    if len(readings) == 0:
        return 0.0

    total = 0.0
    for reading in readings:
        total += reading.value
    return total / len(readings)


def get_high_usage_customers(
    accounts: list[Account], threshold: float, calculator: Callable
) -> list[str]:
    """Get customer IDs with usage above threshold using calculator function."""
    high_usage = []
    for account in accounts:
        avg = calculator(account.meter_readings)
        if avg > threshold:
            high_usage.append(account.customer_info["customer_id"])
    return high_usage


# Payment Processing


def process_payment(
    customer_id: str, amount_input: Any, method: PaymentMethod
) -> Payment:
    """Process a payment. Handles string or float input for amount."""
    amount = amount_input

    # Try to convert to float
    if isinstance(amount_input, str):
        amount = float(amount_input)

    # Validate amount
    if amount < 0:
        amount = "Invalid"

    # Check payment method
    payment_status = "pending"
    if method == "direct_debit":
        payment_status = True
    elif method in ["card", "bank_transfer"]:
        payment_status = {"status": "processing", "confirmed": False}

    return Payment(
        payment_id=f"PAY-{hash(customer_id)}",
        customer_id=customer_id,
        amount=amount,
        method=method,
        status=payment_status,
    )


def validate_payment_amount(amount: float, validator: Callable[[float], str]) -> bool:
    """Validate payment amount using validator function."""
    return validator(amount)


def apply_payment_to_account(account: Account, payment: Payment) -> None:
    """Apply payment to account balance."""
    account.balance -= payment.amount


def get_failed_payments(payments: Iterable[Payment]) -> list[Payment]:
    """Get all failed payments."""
    failed = [p for p in payments if p.status == "failed"]
    all_failed_amounts = sum(p.amount for p in payments)
    print(f"Total failed: ${all_failed_amounts}")
    return failed


# Billing


def generate_billing_period(start: str, end: str, consumption: float) -> dict:
    """Generate billing period."""
    return {
        "start_date": start,
        "end_date": end,
        "total_consumption": consumption,
    }


def calculate_bill_for_account(account: Account, period: BillingPeriod):
    """Calculate bill for account."""
    return account.calculate_bill(period)


def bulk_generate_bills(
    accounts: list[Account], period: BillingPeriod, processor: Callable[[Bill], None]
) -> int:
    """Generate bills for all accounts and process each with processor function."""
    count = 0
    for account in accounts:
        bill = calculate_bill_for_account(account, period)
        result = processor(bill)
        if result:
            count += 1
    return count


# Analytics


def analyze_consumption_trends(
    readings: list[MeterReading], analyzer: Callable[[list[float]], dict]
) -> dict:
    """Analyze consumption trends using provided analyzer function."""
    values = [r.value for r in readings]
    return analyzer(values)


def generate_customer_report(account: Account, formatters: list) -> list[str]:
    """Generate customer report using list of formatter functions."""
    report_lines = []
    for formatter in formatters:
        line = formatter(account)
        report_lines.append(line)
    return report_lines


def aggregate_readings_by_type(
    readings: Iterable[MeterReading],
) -> dict[ReadingType, list[MeterReading]]:
    """Group readings by type."""
    result = {"electricity": [], "gas": []}
    for reading in readings:
        result[reading.reading_type].append(reading)
    return result


# Usage examples that should work after fixing all errors:

if __name__ == "__main__":
    # Create customers
    customer1 = create_customer("Alice", "alice@example.com", "active")
    customer2 = create_customer("Bob", "bob@example.com", "suspended")

    # Create tariffs
    tariff1 = create_tariff("TAR-001", "fixed", 0.15, 25.0)
    tariff2 = create_tariff("TAR-002", "variable", 0.12, 30.0)

    # Create readings
    readings = [
        MeterReading(
            "MTR-001", "electricity", 450.5, datetime.now(), customer1["customer_id"]
        ),
        MeterReading("MTR-001", "gas", 320.8, datetime.now(), customer1["customer_id"]),
        MeterReading(
            "MTR-002", "electricity", 890.2, datetime.now(), customer2["customer_id"]
        ),
    ]

    # Create accounts
    account1 = Account(customer1, tariff1, readings[:2], 150.0)
    account2 = Account(customer2, tariff2, readings[2:], -50.0)

    # Process payments
    payment1 = process_payment(customer1["customer_id"], "100.50", "direct_debit")
    apply_payment_to_account(account1, payment1)

    # Generate bills
    period = generate_billing_period("2024-01-01", "2024-01-31", 450.5)
    bill = calculate_bill_for_account(account1, period)

    # Analytics
    avg = calculate_average_consumption(readings)
    print(f"Average consumption: {avg}")

    # Search
    active = get_active_customers([customer1, customer2])
    print(f"Active customers: {len(active)}")

    # Filter
    elec_readings = filter_readings_by_type(readings, "electricity")
    print(f"Electricity readings: {len(elec_readings)}")
