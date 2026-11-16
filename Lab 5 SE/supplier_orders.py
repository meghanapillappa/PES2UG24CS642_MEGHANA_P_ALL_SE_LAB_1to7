
"""Manage supplier orders and warehouse notifications."""

import sqlite3


def create_connection():
    """Create an in-memory SQLite database and its orders table."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        CREATE TABLE orders (
            id INTEGER PRIMARY KEY,
            supplier TEXT,
            item TEXT,
            quantity INTEGER,
            received INTEGER
        )
        """
    )
    return connection


def place_order(connection, supplier, item, quantity):
    """Place an order and return the total quantity ordered."""
    connection.execute(
        """
        INSERT INTO orders (supplier, item, quantity, received)
        VALUES (?, ?, ?, 0)
        """,
        (supplier, item, quantity),
    )
    total = connection.execute(
        "SELECT SUM(quantity) FROM orders"
    ).fetchone()[0]
    return total


def mark_received(connection, order_id, remarks=None):
    """Mark an order as received and optionally store remarks."""
    del remarks  # The original schema has no remarks column.
    connection.execute(
        "UPDATE orders SET received = 1 WHERE id = ?",
        (order_id,),
    )


def notify_warehouse(supplier):
    """Print a warehouse notification without invoking a shell."""
    print(f"Notifying warehouse about {supplier}")


def cleanup(connection):
    """Delete orders that have been marked as received."""
    connection.execute("DELETE FROM orders WHERE received = 1")


def pending_count(connection):
    """Return the number of orders that have not been received."""
    return connection.execute(
        "SELECT COUNT(*) FROM orders WHERE received = 0"
    ).fetchone()[0]


def main():
    """Run a demonstration of supplier order management."""
    connection = create_connection()
    try:
        place_order(connection, "Acme Steel", "rods", 40)
        total = place_order(connection, "Bolt Co", "bolts", 500)
        mark_received(connection, 1, "ok")
        notify_warehouse("Acme")
        print(pending_count(connection), total)
        cleanup(connection)
    finally:
        connection.close()


if __name__ == "__main__":
    main()
