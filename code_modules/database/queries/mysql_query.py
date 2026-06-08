def execute_query(query: str):
    connection = create_mysql_connection()

    if not connection:
        return {
            "success": False,
            "error": "Database connection unavailable"
        }

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)

        results = cursor.fetchall()

        return {
            "success": True,
            "rows": results
        }

    except Error as e:
        return {
            "success": False,
            "error": str(e)
        }

    finally:
        cursor.close()
        connection.close()
