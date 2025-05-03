from datetime import datetime
import db

def get_threads(page, page_size):
    sql = """SELECT t.id, t.title, COUNT(m.id) total, MAX(m.sent_at) last,
             t.post_type, t.status, t.priority
             FROM threads t, messages m
             WHERE t.id = m.thread_id
             GROUP BY t.id
             ORDER BY t.id DESC
             LIMIT ? OFFSET ?"""
    limit = page_size
    offset = page_size * (page - 1)
    return db.query(sql, [limit, offset])

def get_thread_count():
    sql = "SELECT COUNT(*) FROM threads"
    return db.query(sql)[0][0]

def get_thread(thread_id):
    sql = "SELECT id, title, post_type, status, priority FROM threads WHERE id = ?"
    result = db.query(sql, [thread_id])
    return result[0] if result else None

def get_messages(thread_id):
    sql = """SELECT m.id, m.content, m.sent_at, m.user_id, u.username
             FROM messages m, users u
             WHERE m.user_id = u.id AND m.thread_id = ?
             ORDER BY m.id"""
    return db.query(sql, [thread_id])

def get_message(message_id):
    sql = """SELECT m.id, m.content, m.user_id, m.thread_id
             FROM messages m, threads t
             WHERE m.id = ? AND t.id = m.thread_id"""
    result = db.query(sql, [message_id])
    return result[0] if result else None

def add_thread(title, content, post_type, status, priority, user_id):
    sql = "INSERT INTO threads (title, post_type, status, priority, user_id) VALUES (?, ?, ?, ?, ?)"
    db.execute(sql, [title, post_type, status, priority, user_id])
    thread_id = db.last_insert_id()
    add_message(content, user_id, thread_id)
    return thread_id

def add_message(content, user_id, thread_id):
    sql = """INSERT INTO messages (content, user_id, thread_id, sent_at)
             VALUES (?, ?, ?, ?)"""
    db.execute(sql, [content, user_id, thread_id, datetime.now()])

def update_message(message_id, content):
    sql = "UPDATE messages SET content = ? WHERE id = ?"
    db.execute(sql, [content, message_id])

def remove_message(message_id):
    sql = "DELETE FROM messages WHERE id = ?"
    db.execute(sql, [message_id])

def search(query, post_type, status, priority):
    sql = """SELECT m.id message_id,
                    m.thread_id,
                    t.title thread_title,
                    m.content,
                    m.sent_at,
                    u.username
             FROM threads t, messages m, users u
             WHERE t.id = m.thread_id AND
                   u.id = m.user_id"""

    params = []

    if query:
        sql += " AND m.content LIKE ?"
        params.append("%" + query + "%")

    if post_type:
        placeholders = ",".join("?" for _ in post_type)
        sql += f" AND t.post_type IN ({placeholders})"
        params.extend(post_type)

    if status:
        placeholders = ",".join("?" for _ in status)
        sql += f" AND t.status IN ({placeholders})"
        params.extend(status)

    if priority:
        placeholders = ",".join("?" for _ in priority)
        sql += f" AND t.priority IN ({placeholders})"
        params.extend(priority)

    sql += " ORDER BY m.sent_at DESC"

    return db.query(sql, params)
