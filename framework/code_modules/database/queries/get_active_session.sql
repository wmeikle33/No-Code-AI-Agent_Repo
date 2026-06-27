SELECT
    session_id,
    user_id,
    start_time
FROM sessions
WHERE status = 'active';
