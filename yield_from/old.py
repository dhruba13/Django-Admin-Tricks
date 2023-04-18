
while True:
    conn = old_pool.get(block=False)
    if conn:
        conn.close()



def genreport(gen):
    return ((print(item), item)[-1] for item in gen)
