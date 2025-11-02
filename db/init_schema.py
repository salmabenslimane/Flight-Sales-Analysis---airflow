from db_connection import get_connection

def create_schema():

    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            Booking_ID INTEGER,
            Booking_Date DATE,
            Flight_Date DATE,
            Passenger_ID INTEGER,
            Passenger_Name VARCHAR,
            Email VARCHAR,
            Gender VARCHAR,
            Country_Code VARCHAR,
            Ticket_Class VARCHAR,
            Quantity INTEGER,
            Unit_Price DOUBLE,
            Revenue DOUBLE
        );
    """)
    conn.close()
    print("✅ Schema created successfully!")

if __name__ == "__main__":
    create_schema()


'''What it does:

Creates the main table bookings if it doesn’t already exist.

Defines all the columns you’ll use later for analysis.'''