from db_connection import get_connection

def insert_sample_data():
    conn = get_connection()
    conn.execute("""
        INSERT INTO bookings VALUES
        (1, '2025-11-02', '2025-12-15', 101, 'Alice Martin', 'alice@email.com', 'F', 'FR', 'Economy', 2, 350.00, 700.00),
        (2, '2025-11-03', '2025-12-20', 102, 'John Doe', 'john@email.com', 'M', 'US', 'Business', 1, 900.00, 900.00);
    """)
    conn.close()
    print("✅ Inserted sample data!")

def test_on_sql_query():

    conn = get_connection()
    results = conn.execute("SELECT * FROM bookings;").fetchdf()
    print(results)

    results2 = conn.execute("""
    SELECT Ticket_Class, SUM(Revenue) AS total_revenue
    FROM bookings
    GROUP BY Ticket_Class;
    """).fetchdf()
    print(results2)

    conn.close()


if __name__ == "__main__":
    insert_sample_data()
    test_on_sql_query()

'''What it does:
Inserts sample data into the bookings table.
Runs two test SQL queries to verify data insertion and aggregation functionality.'''