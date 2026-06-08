from datetime import datetime
from uuid import uuid4

class AgentRunRepository:
    def __init__(self, connection):
        self.connection = connection

    def create_agent_run(self, agent_name, user_message, status="running"):
        run_id = str(uuid4())

        query = """
        INSERT INTO agent_runs (
            id,
            agent_name,
            user_message,
            status,
            created_at
        )
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor = self.connection.cursor()
        cursor.execute(
            query,
            (
                run_id,
                agent_name,
                user_message,
                status,
                datetime.utcnow(),
            ),
        )
        self.connection.commit()
        cursor.close()

        return run_id

    def get_recent_runs(self, limit=20):
        query = """
        SELECT id, agent_name, user_message, status, created_at
        FROM agent_runs
        ORDER BY created_at DESC
        LIMIT %s
        """

        cursor = self.connection.cursor(dictionary=True)
        cursor.execute(query, (limit,))
        rows = cursor.fetchall()
        cursor.close()

        return rows
