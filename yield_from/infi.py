
for __moment__ in infinity:
    conn = old_pool.get(block=False)
    if conn:
        conn.close()

