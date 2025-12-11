from dataclasses import dataclass
from typing import Iterable, Iterator


@dataclass
class MeterReading:
    meter_id: str
    kwh: float
    timestamp: str


def calculate_total_consumption(readings: Iterable[MeterReading]) -> float:
    """Calculate total consumption from meter readings."""
    total = 0.0
    for reading in readings:
        total += reading.kwh
    return total


def get_high_consumption_readings(
    readings: Iterable[MeterReading], threshold: float
) -> list[MeterReading]:
    """Get readings above threshold consumption."""
    print(f"Processing {len(list(readings))} readings...")
    return [r for r in readings if r.kwh > threshold]


def get_meter_ids(readings: Iterable[MeterReading]) -> list[str]:
    """Extract all meter IDs from readings."""
    ids = list[str]()
    for reading in readings:
        if reading.meter_id.startswith("ELEC"):
            ids.append(reading.meter_id)
    return ids


def reading_generator(meter_id: str, days: int) -> Iterator[MeterReading]:
    """
    Generate daily readings for a meter.
    Yields one reading per day.
    """
    for day in range(days):
        kwh = 25.0 + (day * 2.5)  # Simulated consumption
        timestamp = f"2024-01-{day + 1:02d}"
        yield MeterReading(meter_id, kwh, timestamp)


def process_readings_in_batches(
    readings: Iterable[MeterReading], batch_size: int
) -> Iterator[list[MeterReading]]:
    """
    Process readings in batches.
    Should accept Iterable and return Iterator.
    """
    batch: list[MeterReading] = []
    for reading in readings:
        batch.append(reading)
        if len(batch) == batch_size:
            yield batch
            batch = []
    if batch:
        yield batch


def count_readings(readings: Iterable[MeterReading]) -> int:
    """Count total number of readings."""
    return len(list(readings))


def get_first_reading(readings: Iterable[MeterReading]) -> MeterReading | None:
    """Get the first reading from an iterable."""
    for reading in readings:
        return reading
    return None


def average_consumption(readings: Iterable[MeterReading]) -> float:
    """
    Calculate average consumption across readings.
    Should accept any Iterable.
    """
    total = 0.0
    count = 0
    for reading in readings:
        total += reading.kwh
        count += 1
    return total / count if count > 0 else 0.0


# Usage
readings = {
    MeterReading("ELEC001", 45.5, "2024-01-01"),
    MeterReading("ELEC002", 120.3, "2024-01-01"),
    MeterReading("ELEC003", 78.9, "2024-01-01"),
}

total = calculate_total_consumption(readings)
high_usage = get_high_consumption_readings(readings, 100.0)
ids = get_meter_ids(readings)

daily_readings = reading_generator("ELEC001", 7)
first = get_first_reading(daily_readings)

batches = process_readings_in_batches(readings, 2)
for batch in batches:
    print(f"Batch of {len(batch)} readings")

reading_tuple = tuple(readings)
avg = average_consumption(reading_tuple)
count = count_readings(reading_tuple)
